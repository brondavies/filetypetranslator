# ![FTT Logo](https://raw.githubusercontent.com/brondavies/filetypetranslator/master/ftt-icon.png) File Type Translator (FTT)

A library of helper methods for your Python project to get [mime types](https://en.wikipedia.org/wiki/Media_type) and general file category

# Releases
Available as a [pypi package](https://pypi.org/packages/fttlib)
#### 1.1.2 - Initial python release

# Examples

#### Import the library

```python
from fttlib import FTT
```

####  When you need to know the mime type of a file based on its extension.

```python
mimeType = FTT.getMimeType("Path/To/My/File.doc")
print(mimeType)

mimeType = FTT.getMimeType("Path/To/My/File.docx")
print(mimeType)

>  application/msword
>  application/vnd.openxmlformats-officedocument.wordprocessingml.document
```

####  When you need to know the file type category of a file based on its extension.

```python
FileCategory category = FTT.getFileCategory("Path/To/My/File.docx")
print(category)

category = FTT.getFileCategory("Path/To/My/File.jpg")
print(category)

>  Document
>  Image
```

####  When you need to know the preferred file extension for a file based on its mime type.

```python
string[] extensions = FTT.getMimeTypeFileExtension("text/csv")
print(extensions[0])

>  csv
```

# Design

This library is designed along the following tenets:

* No external dependencies
* No file system access
* Small memory footprint
* Simple static methods (no extension methods and no instantiatable classes)
* Case-insensitive
* Portable - works in applications targeting any runtime

# File Categories

File media types are broken down into relatively few categories.  Sub-categories may be considered in a future release according to information on [Wikipedia](https://en.wikipedia.org/wiki/List_of_file_formats)  Here are the guidelines that determine a file's category

* Archive: any file that can be extracted into several files
* Audio: any file that can only contain an audio stream
* Binary: any file that is unclassified or does not have a text representation
* Code: any file that contains instructions that are compilable or machine-readable
* Document: any file that is designed for conveying structured information between people
* Image: any file that can only contain a single image or series of images
* PDF: any file that is considered a document archive format
* Presentation: any file that is designed for electronic presentations consisting of a series of separate pages or slides
* Spreadsheet: any file in which data is arranged in rows and columns and can be manipulated and used in calculations
* Text: any file that is not classified under another category and is not binary
* Video: any file that is designed to be a container for a video stream

# Known Limitations

* Even though a mime type to file extension mapping is not necessarily one-to-one, the most common should be returned by the library
* This library does not provide file sniffing capabilities - in other words, if you have a file and you want to verify the contents are of a specific type, look elsewhere. FTT only uses the file name with an extension.  That capability may be added in a future release.
* The only file categories presently considered are Archive, Audio, Binary, Code, Document, Image, PDF, Presentation, Spreadsheet, Text, and Video.  Binary is the default if there is no match in the database.

# Sources

While it is unrealistic to expect this library to provide a comprehensive list with *all* the file types the world has to offer, it would be nice if we could get close.  Generally, if the file type is even remotely common, it is listed in one of the sources.  You can [submit a bug report](https://github.com/brondavies/filetypetranslator/issues/new) for a file type that is missing or that you think should be added.  You will have to include a reputable source as well.

### Information sources for this library are provided through the following and in order of preference:

1. http://www.iana.org/assignments/media-types/media-types.xhtml
1. https://gitlab.freedesktop.org/xdg/shared-mime-info
1. https://cdn.rawgit.com/jshttp/mime-db/master/db.json
1. http://www.file-extensions.org/
