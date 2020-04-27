import os
from enum import Enum, unique, auto

#constants

def __getExt(fileName):
    if '.' in fileName: return os.path.splitext(fileName)[1].replace('.', '')
    else: return fileName

"""
Methods for translating between mime-types and file extensions
"""
def getMimeType(fileName):
    """
    Returns the mime type for the given file name
    :param str fileName A file name, file extension or file path specification
    """
    extension = __getExt(fileName)
    #getMimeType body

def getMimeTypeFileExtensions(mimeType):
    """
    Returns a list of possible file extensions for the given mime type
    :param str mimeType A mime Type
    """
    #getMimeTypeFileExtensions body

def getFileCategory(fileName):
    """
    Returns a file category for the given file name
    :param str fileName A file name, file extension or file path specification
    """
    #getFileCategory body

@unique
class FileCategory(Enum):
    """
    Any file that can be extracted into several files
    """
    Archive = auto()
    """
    Any file that can only contain an audio stream
    """
    Audio = auto()
    """
    Any file that is unclassified or does not have a text representation
    """
    Binary = auto()
    """
    Any file that contains instructions that are compilable or machine-readable
    """
    Code = auto()
    """
    Any file that is designed for conveying structured information between people
    """
    Document = auto()
    """
    Any file that can only contain a single image or series of images
    """
    Image = auto()
    """
    Any file that is considered a document archive format
    """
    PDF = auto()
    """
    Any file that is designed for electronic presentations consisting of a series of separate pages or slides
    """
    Presentation = auto()
    """
    Any file in which data is arranged in rows and columns and can be manipulated and used in calculations
    """
    Spreadsheet = auto()
    """
    Any file that is not classified under another category and is not binary
    """
    Text = auto()
    """
    Any file that is designed to be a container for a video stream
    """
    Video = auto()