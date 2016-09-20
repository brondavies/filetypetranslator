﻿namespace FTTLib
{
    public partial class FTT
    {
        private static FileCategory GetFileCategoryInternal(string extension)
        {
            switch (extension)
            {
                case _7z:
                case "7zip":
                case ace:
                case air:
                case apk:
                case "appxbundle":
                case "arc":
                case arj:
                case "asec":
                case "bar":
                case bz2:
                case "bzip":
                case cab:
                case "cso":
                case deb:
                case "dlc":
                case dmg:
                case gz:
                case "gzip":
                case hqx:
                case "inv":
                case "ipa":
                case iso:
                case "isz":
                case jar:
                case "msu":
                case "nbh":
                case pak:
                case rar:
                case rpm:
                case sis:
                case sisx:
                case sit:
                case "sitd":
                case sitx:
                case tar:
                case targz:
                case tgz:
                case "webarchive":
                case xap:
                case z:
                case zip:
                    return FileCategory.Archive;

                case _3ga:
                case aac:
                case aiff:
                case amr:
                case ape:
                case "arf":
                case asf:
                case asx:
                case "cda":
                case "dvf":
                case flac:
                case "gp4":
                case "gp5":
                case gpx:
                case "logic":
                case m4a:
                case m4b:
                case "m4p":
                case midi:
                case mp3:
                case ogg:
                case "pcm":
                case "rec":
                case snd:
                case "sng":
                case "uax":
                case wav:
                case wma:
                case wpl:
                case "zab":
                    return FileCategory.Audio;

                case _as:
                case asm:
                case asp:
                case "aspx":
                case bat:
                case c:
                case "cp":
                case cpp:
                case cs:
                case css:
                case "gradle":
                case htm:
                case "inc":
                case jad:
                case java:
                case js:
                case json:
                case "jsp":
                case "lib":
                case m:
                case "matlab":
                case ml:
                case o:
                case perl:
                case php:
                case pl:
                case "ps1":
                case py:
                case rb:
                case "rc":
                case rss:
                case "scpt":
                case sh:
                case sql:
                case src:
                case "swift":
                case "vb":
                case "vbs":
                case "ws":
                case "xaml":
                case "xcodeproj":
                case xml:
                case xsd:
                case xsl:
                case xslt:
                case yml:
                    return FileCategory.Code;

                case abw:
                case "aww":
                case azw:
                case "azw3":
                case "azw4":
                case cbr:
                case cbz:
                case chm:
                case "cnt":
                case "dbx":
                case djvu:
                case doc:
                case docm:
                case docx:
                case dot:
                case dotm:
                case dotx:
                case epub:
                case fb2:
                case "iba":
                case "ibooks":
                case "ind":
                case "indd":
                case key:
                case "keynote":
                case "lit":
                case mht:
                case mobi:
                case mpp:
                case odf:
                case ods:
                case odt:
                case ott:
                case oxps:
                case "pages":
                case pdf:
                case pmd:
                case pot:
                case potx:
                case pps:
                case ppsx:
                case ppt:
                case pptm:
                case pptx:
                case "prn":
                case "prproj":
                case ps:
                case pub:
                case "pwi":
                case rep:
                case rtf:
                case sdd:
                case sdw:
                case "shs":
                case "snp":
                case sxw:
                case tpl:
                case vsd:
                case "wlmp":
                case wpd:
                case wps:
                case wri:
                case xps:
                    return FileCategory.Document;

                case bmp:
                case cpt:
                case dds:
                case dib:
                case dng:
                case "dt2":
                case emf:
                case gif:
                case ico:
                case "icon":
                case icns:
                case jpeg:
                case jpg:
                case pcx:
                case pic:
                case png:
                case psd:
                case "psdx":
                case raw:
                case tga:
                case "thm":
                case tif:
                case tiff:
                case wbmp:
                case "wdp":
                case webp:
                    return FileCategory.Image;
                    
                case "alx":
                case application:
                case csv:
                case "eng":
                case html:
                case log:
                case "lrc":
                case "lst":
                case nfo:
                case opml:
                case "plist":
                case reg:
                case srt:
                case sub:
                case "tbl":
                case text:
                case txt:
                    return FileCategory.Text;

                case "264":
                case _3g2:
                case _3gp:
                case avi:
                case "bik":
                case "dash":
                case "dat":
                case "dvr":
                case flv:
                case h264:
                case m2t:
                case m2ts:
                case m4v:
                case mkv:
                case mod:
                case mov:
                case mp4:
                case mpeg:
                case mpg:
                case "mswmm":
                case mts:
                case ogv:
                case rmvb:
                case swf:
                case "tod":
                case "tp":
                case ts:
                case vob:
                case webm:
                case wmv:
                    return FileCategory.Video;

                default:
                    return FileCategory.Binary;
            }
        }
    }
}