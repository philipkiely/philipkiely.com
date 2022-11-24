Title: How to Download Files and Folders from Google Colab
Date: 2022-11-23
Modified: 2022-11-23
Slug: colab_download
Authors: Philip Kiely
Summary: Google Colab's UI has a file browser, but there is no option in the UI to download files. Instead, you have to use code. The following only works on Chrome.

Google Colab's UI has a file browser, but there is no option in the UI to download files. Instead, you have to use code. The following only works on Chrome.

### How to download a file

For any file in your working directory, you can download it with:

```python
google.colab import files

files.download("filename.txt")
```

### How to download a folder

The `files.download()` function only supports individual files, not folders. So to download a folder, you'll first have to zip it up, then download it:

```python
google.colab import files
import shutil

shutil.make_archive("my_folder", 'zip', "my_folder")
files.download("my_folder.zip")
```

You can unzip the downloaded folder locally.

#### What is the working directory on Colab?

In Colab, your working directory is `/content`. You can access all of the Linux directories by navigating through the file tree in the UI, as well as in code. But your working directory is the default file path and everything should be relative to `/content`.

For more on working with local files in Colab, see [this notebook by Google](https://colab.research.google.com/notebooks/io.ipynb#scrollTo=p2E4EKhCWEC5).