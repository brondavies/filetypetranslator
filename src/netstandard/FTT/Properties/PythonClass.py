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
    
    return []

def getFileCategory(fileName):
    """
    Returns a file category for the given file name
    :param str fileName A file name, file extension or file path specification
    """
    extension = __getExt(fileName)
    if extension in (_7z, "7zip", ace, air, apk, appxbundle, arc, arj, "asec", "bar", bz2, "bzip", cab, cso, deb, "dlc", dmg, gz, "gzip", hqx, "inv", "ipa", iso, "isz", jar, msu, "nbh", pak, rar, rpm, sis, sisx, sit, "sitd", sitx, tar, targz, tgz, "webarchive", xap, z, zip):
        return FileCategory.Archive

    if extension in (_3ga, aac, aiff, amr, ape, "arf", asf, asx, "cda", "dvf", flac, "gp4", "gp5", gpx, "logic", m4a, m4b, m4p, midi, mp3, ogg, "pcm", "rec", snd, "sng", "uax", wav, wma, wpl, "zab"):
        return FileCategory.Audio

    if extension in (_as, asm, asp, "aspx", bat, c, "cp", cpp, cs, css, gradle, htm, "inc", jad, java, js, json, "jsp", lib, m, "matlab", ml, o, perl, php, pl, ps1, py, rb, "rc", rss, "scpt", sh, sql, src, "swift", vb, vbs, ws, xaml, "xcodeproj", xml, xsd, xsl, xslt, yml):
        return FileCategory.Code

    if extension in (abw, "aww", azw, azw3, "azw4", cbr, cbz, chm, "cnt", "dbx", djvu, doc, docm, docx, dot, dotm, dotx, epub, fb2, "iba", "ibooks", "ind", "indd", "lit", mht, mobi, mpp, odf, odt, ott, pages, pmd, "prn", "prproj", ps, pub, "pwi", rep, rtf, sdd, sdw, "shs", "snp", sxw, tpl, vsd, "wlmp", wpd, wps, wri):
        return FileCategory.Document

    if extension in (bmp, cpt, dds, dib, dng, "dt2", emf, gif, ico, "icon", icns, jpeg, jpg, pcx, pic, png, psd, "psdx", raw, tga, "thm", tif, tiff, wbmp, wdp, webp):
        return FileCategory.Image

    if extension in (oxps, pdf, xps):
        return FileCategory.PDF

    if extension in (key, "keynote", pot, potx, pps, ppsx, ppt, pptm, pptx):
        return FileCategory.Presentation

    if extension in (ods, numbers, sdc, xls, xlsx, xlsb):
        return FileCategory.Spreadsheet

    if extension in ("alx", application, csv, "eng", html, log, "lrc", "lst", nfo, opml, "plist", reg, srt, sub, "tbl", text, txt):
        return FileCategory.Text

    if extension in ("264", _3g2, _3gp, avi, bik, "dash", "dat", "dvr", flv, h264, m2t, m2ts, m4v, mkv, mod, mov, mp4, mpeg, mpg, "mswmm", mts, ogv, rmvb, swf, "tod", "tp", ts, vob, webm, wmv):
        return FileCategory.Video

    return FileCategory.Binary

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