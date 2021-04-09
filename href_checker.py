from bs4 import BeautifulSoup
import glob
import os
import requests
import sys

def get_all_html():
    corvette_htmls = glob.glob("dist/assets/**/*.html", recursive=True)
    return [g for g in glob.glob("dist/**/*.html", recursive=True) if g not in corvette_htmls]

def get_all_assets():
    return [g for g in glob.glob("dist/assets/**/*", recursive=True) if "." in g]

def soup_up(page):
    f = open(page, "r")
    html = f.read()
    f.close()
    return BeautifulSoup(html, 'html.parser')

def is_internal(h):
    if not h:
        return False
    if h[0] == "/":
        return True
    return False

def is_external(h):
    if h[:4] == "http":
        return True
    return False

def clean_internal(h):
    if "?" in h:
        h = h.split("?")[0]
    if h[-5:] == ".html":
        pass 
    elif h[-4:] == ".pdf":
        pass
    elif h[-1] == "/":
        h = h + "index.html"
    else:
        h = h + "/index.html"
    return "dist" + h

def check_internal_hrefs():
    print("---Checking Internal Links---")
    pages = get_all_html()
    assets = get_all_assets()
    for page in pages:
        soup = soup_up(page)
        links = [clean_internal(h.get("href")) for h in soup.find_all('a') if is_internal(h.get("href"))]
        for link in links:
            if link not in pages and link not in assets:
                print("{} IN {}".format(link, page))
    print("---Done---")
    
def check_external_hrefs():
    print("---Checking External Links---")
    pages = get_all_html()
    checked = []
    for page in pages:
        soup = soup_up(page)
        links = [h.get("href") for h in soup.find_all("a") if is_external(h.get("href")) and "mailto" not in h.get("href")]
        for link in links:
            if link not in checked:
                try:
                    resp = requests.head(link)
                    if int(resp.status_code) == 404:
                        resp = requests.get(link)
                    if int(resp.status_code) == 404: # Could check other codes but complicates scraper vs browser for permissions
                        print("NOT FOUND: {} IN {}".format(link, page))
                except:
                    print("ERROR DURING {} IN {}".format(link, page))
                checked.append(link)
    print("---Done---")

def check_asset_srcs():
    print("---Checking Asset Links---")
    pages = get_all_html()
    assets = get_all_assets()
    all_links = []
    for page in pages:
        soup = soup_up(page)
        images = ["dist" + s.get("src") for s in soup.find_all("img") if is_internal(s.get("src"))]
        styles = ["dist" + s.get("src") for s in soup.find_all("script") if is_internal(s.get("src"))]
        scripts = ["dist" + s.get("href") for s in soup.find_all("link") if is_internal(s.get("href"))]
        for link in images + styles + scripts:
            all_links.append(link)
            if link not in assets:
                print("{} IN {}".format(link, page))
    print("---Done---")
    print("---Checking Asset Usage---")
    for asset in assets:
        if asset not in all_links:
            print("UNUSED: {}".format(asset))
    print("---Done---")

if __name__=="__main__":
    if len(sys.argv) == 2:
        if sys.argv[1] == "--internal":
            check_internal_hrefs()
        elif sys.argv[1] == "--external":
            check_external_hrefs()
        elif sys.argv[1] == "--assets":
            check_asset_srcs()
        else:
            print("Unrecognized flag")
    else:
        check_internal_hrefs()
        check_external_hrefs()
        check_asset_srcs()
