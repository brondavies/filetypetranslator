"""
Methods for translating between mime-types and file extensions
"""
def getMimeType(fileName):
    """
    Returns the mime type for the given file name
    :param str fileName A file name, file extension or file path specification
    """
    return "text/plain"

def getMimeTypeFileExtensions(mimeType):
    """
    Returns a list of possible file extensions for the given mime type
    :param str mimeType A mime Type
    """
    return "txt"

def getFileCategory(fileName):
    """
    Returns a file category for the given file name
    :param str fileName A file name, file extension or file path specification
    """
    return FileCategory.Unknown