# File Type Translator (FTT)
A library of helper methods for your .Net project to get [mime types]() and general file category

# Examples

####  When you need to know the mime type of a file based on its extension.

```csharp
string mimeType = FTT.GetMimeType(@"Path\To\My\File.doc");
Console.WriteLine(mimeType);

mimeType = FTT.GetMimeType(@"Path\To\My\File.docx");
Console.WriteLine(mimeType);

>  application/msword
>  application/vnd.openxmlformats-officedocument.wordprocessingml.document
```

####  When you need to know the file type category of a file based on its extension.

```csharp
FileCategory category = FTT.GetFileCategory(@"Path\To\My\File.docx");
Console.WriteLine(category);

category = FTT.GetFileCategory(@"Path\To\My\File.xls");
Console.WriteLine(category);

>  Document
>  Spreadsheet
```

####  When you need to know the prefferred file extension for a file based on its mime type.

```csharp
string extension = FTT.GetMimeTypeFileExtension("text/csv");
Console.WriteLine(extension);

>  .csv
```

# Design

This library is designed along the following tenets:

* No external dependencies
* No file system access
* Small memory footprint
* Simple static methods (no extension methods and no instantiatable classes)
* Case-insensitive
* Portable - works in applications targeting any CLR

# File Categories

File media types are broken down into relatively few categories.  Here are the guidelines that determine a file's category

* Archive: any file that can be extracted into several files
* Audio: any file that can only contain an audio stream
* Binary: any file that is unclassified or does not have a text representation
* Code: any file that contains instructions that are compilable or machine-readable
* Document: any file that is designed for conveying structured information between people
* Image: any file that can only contain a single image or series of images
* Text: any file that is not classified under another category and is not binary
* Video: any file that is designed to be a container for a video stream

# Known Limitations

* Even though a mime type to file extension mapping is not necessarily one-to-one, the most common should be returned by the library
* This library does not provide file sniffing capabilities - in other words, if you have a file and you want to verify the contents are of a specific type, look elsewhere. FTT only uses the file name with an extension.  That capability may be added in a future release.
* The only file categories presently considered are Archive, Audio, Binary, Code, Document, Image, Text, and Video.  Binary is the default if there is no match in the database.

# Sources

While it is unrealistic to expect this library to provide a comprehensive list with *all* the file types the world has to offer, it would be nice if we could get close.  Generally, if the file type is even remotely common, it is listed in one of the sources.  You can [submit a bug report](https://github.com/brondavies/filetypetranslator/issues/new) for a file type that is missing or that you think should be added.  You will have to include a reputable source as well.

### Information sources for this library are provided through the following and in order of preference:

1. http://www.iana.org/assignments/media-types/media-types.xhtml
1. https://cgit.freedesktop.org/xdg/shared-mime-info/plain/freedesktop.org.xml.in
1. http://www.stdicon.com/mimetypes
1. http://www.file-extensions.org/
