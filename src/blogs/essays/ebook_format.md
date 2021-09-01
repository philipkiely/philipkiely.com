Title: How to Format a PK&C Ebook for Publication
Date: 2021-09-01
Modified: 2021-09-01
Slug: ebook_format
Authors: Philip Kiely
Summary:

After publishing several ebooks, I have a process

## Stage 1: Writing in Markdown

* Good to write in
* Matches the level of syntax my brain thinks with
* Automatic headers, links, footnotes, etc

## Intermediary: Pandoc Markdown to Word Conversion

Turn markdown into a microsoft word doc

## Stage 2: Formatting in Microsoft Word

A little different for each book but let's do a dangerous guide because I have to make a bunch of them.

* Use styles pane not WYSIWYG
  * Body Styles - Why font
  * Header Styles - Why font & color
* A5 paper, margins
* Page numbering
* Footnotes vs Endnotes
* Images
* Making a TOC
* Exporting to PDF (embed fonts)

## Intermediary: Microsoft Word to PDF Export

## Stage 3: Final Assembly in Preview

* Making the cover
* Attaching cover and other full-width images
* Testing Links

## Bonus: Making an EPUB in Apple Pages

An EPUB is an open-source format that is supported by a wide variety of e-reader applications. For an independent author publishing digital books, making your book available as an EPUB as well as a PDF is a great way to increase readership by giving people the format they prefer. PK&C books like *Writing for Software Developers* and parts of *Cold Email for Interesting People* are available in EPUB and are popular in that format.

However, EPUB is something called a "reflowable layout" format. Unlike PDFs &mdash; which have fixed fonts, page sizes, and image positions &mdash; EPUBs let readers set their own font and font size and then automatically position images and break pages according to the screen size the file is being displayed on. Accordingly, the EPUB format is awesome for text-heavy books but for an entry in the *Dangerous Guides* series, with its emphasis on images and hybrid comic-book layout, it is not a good format.

While the Dangerous Guides are not available in EPUB, making the format outside the scope of this guide, I can offer a brief description of how I generate an EPUB.

Perhaps surprisingly, Microsoft Word does not have a native EPUB export option, but Apple Pages offers an excellent one. I follow the following steps:

* Open the Microsoft Word doc in Apple Pages and save it as a native pages file.
* Delete the page numbers and table of contents as the EPUB generation process will create those from the headers.
* Go through the EPUB export options, adding my name in the Author metadata field and using the PNG version of the cover from the earlier step as the book's cover.

Unfortunately, now whenever I make changes to the final text in the Microsoft Word version, which had become the single source of truth, I now have to change it in the Apple Pages version as well to update the EPUB. So, if fixing typos after publication, I need to fix them twice, adding a moment to the process. However, it is worth the extra effort because it is much less work than turning the Microsoft Word document or PDF into a nice-looking EPUB directly.
