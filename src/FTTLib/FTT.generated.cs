namespace FTT
{
    public partial class FTT
    {
        private static string GetMimeTypeInternal(string extension)
        {
            switch (extension)
            {
                // backup file
                case "~":
                case "%":
                case "bak":
                case "old":
                case "sik":
                    return "application/x-trash";
                // Lotus 1-2-3 spreadsheet
                case "123":
                case "wk1":
                case "wk3":
                case "wk4":
                case "wks":
                    return "application/vnd.lotus-1-2-3";
                // Genesis 32X ROM
                case "32x":
                case "mdx":
                    return "application/x-genesis-32x-rom";
                case "3dml":
                    return "text/vnd.in3d.3dml";
                // 3D Studio image
                case "3ds":
                    return "image/x-3ds";
                // 3GPP2 multimedia file
                case "3g2":
                case "3gp2":
                case "3gpp2":
                    return "video/3gpp2";
                // 3GPP multimedia file
                case "3gp":
                case "3gpp":
                case "3ga":
                    return "video/3gpp";
                // T602 document
                case "602":
                    return "application/x-t602";
                // 7-zip archive
                case "7z":
                    return "application/x-7z-compressed";
                // AR archive
                case "a":
                case "ar":
                    return "application/x-archive";
                // Atari 2600
                case "a26":
                    return "application/x-atari-2600-rom";
                // Atari 7800
                case "a78":
                    return "application/x-atari-7800-rom";
                case "aab":
                case "u32":
                case "vox":
                case "x32":
                    return "application/x-authorware-bin";
                // AAC audio
                case "aac":
                    return "audio/aac";
                case "aam":
                    return "application/x-authorware-map";
                case "aas":
                    return "application/x-authorware-seg";
                // AbiWord document
                case "abw":
                case "abwcrashed":
                case "abwgz":
                case "zabw":
                    return "application/x-abiword";
                // Dolby Digital audio
                case "ac3":
                    return "audio/ac3";
                case "acc":
                    return "application/vnd.americandynamics.acc";
                // ACE archive
                case "ace":
                    return "application/x-ace";
                case "acu":
                    return "application/vnd.acucobol";
                case "acutc":
                case "atc":
                    return "application/vnd.acucorp";
                // Ada source code
                case "adb":
                case "ads":
                    return "text/x-adasrc";
                // Amiga disk image
                case "adf":
                    return "application/x-amiga-disk-format";
                case "adp":
                    return "audio/adpcm";
                case "aep":
                    return "application/vnd.audiograph";
                // Adobe font metrics
                case "afm":
                    return "application/x-font-afm";
                case "afp":
                case "list3820":
                case "listafp":
                    return "application/vnd.ibm.modcap";
                // Applix Graphics image
                case "ag":
                    return "image/x-applix-graphics";
                // Adobe Illustrator document
                case "ai":
                    return "application/illustrator";
                // AIFC audio
                case "aifc":
                case "aiffc":
                    return "audio/x-aifc";
                // AIFF/Amiga/Mac audio
                case "aiff":
                case "aif":
                    return "audio/x-aiff";
                case "air":
                    return "application/vnd.adobe.air-application-installer-package+zip";
                // Alzip archive
                case "alz":
                    return "application/x-alz";
                case "ami":
                    return "application/vnd.amiga.ami";
                // AMR audio
                case "amr":
                    return "audio/amr";
                // AmazonMP3 download file
                case "amz":
                    return "audio/x-amzxml";
                // Windows animated cursor
                case "ani":
                    return "application/x-navi-animation";
                // ANIM animation
                case "anim[1-9j]":
                    return "video/x-anim";
                // Annodex exchange format
                case "anx":
                    return "application/annodex";
                // Monkey's audio
                case "ape":
                    return "audio/x-ape";
                // Android package
                case "apk":
                    return "application/vnd.android.package-archive";
                // AppImage application bundle
                case "appimage":
                    return "application/x-iso9660-appimage";
                case "application":
                    return "application/x-ms-application";
                case "apr":
                    return "application/vnd.lotus-approach";
                // ARJ archive
                case "arj":
                    return "application/x-arj";
                // Sony ARW raw image
                case "arw":
                    return "image/x-sony-arw";
                // Applix Spreadsheets spreadsheet
                case "as":
                    return "application/x-applix-spreadsheet";
                // ASF video
                case "asf":
                    return "application/vnd.ms-asf";
                case "asm":
                case "s":
                    return "text/x-asm";
                case "aso":
                    return "application/vnd.accpac.simply.aso";
                // ASP page
                case "asp":
                    return "application/x-asp";
                // Microsoft ASX playlist
                case "asx":
                case "wax":
                case "wvx":
                case "wmx":
                    return "audio/x-ms-asx";
                // Atom syndication feed
                case "atom":
                    return "application/atom+xml";
                case "atomcat":
                    return "application/atomcat+xml";
                case "atomsvc":
                    return "application/atomsvc+xml";
                case "atx":
                    return "application/vnd.antix.game-component";
                // ULAW (Sun) audio
                case "au":
                case "snd":
                    return "audio/basic";
                // author list
                case "authors":
                    return "text/x-authors";
                // AVI video
                case "avi":
                case "avf":
                case "divx":
                    return "video/x-msvideo";
                // Applix Words document
                case "aw":
                    return "application/x-applix-word";
                // AMR-WB audio
                case "awb":
                    return "audio/amr-wb";
                // AWK script
                case "awk":
                    return "application/x-awk";
                // Annodex Audio
                case "axa":
                    return "audio/annodex";
                // Annodex Video
                case "axv":
                    return "video/annodex";
                case "azf":
                    return "application/vnd.airzip.filesecure.azf";
                case "azs":
                    return "application/vnd.airzip.filesecure.azs";
                case "azw":
                    return "application/vnd.amazon.ebook";
                case "bat":
                case "com":
                case "dll":
                    return "application/x-msdownload";
                // BCPIO document
                case "bcpio":
                    return "application/x-bcpio";
                // BDF font
                case "bdf":
                    return "application/x-font-bdf";
                case "bh2":
                    return "application/vnd.fujitsu.oasysprs";
                // BibTeX document
                case "bib":
                    return "text/x-bibtex";
                // unknown
                case "bin":
                case "bpk":
                case "deploy":
                case "dist":
                case "distz":
                case "dms":
                case "dump":
                case "elc":
                case "lrf":
                    return "application/octet-stream";
                // Blender scene
                case "blender":
                case "blend":
                    return "application/x-blender";
                case "bmi":
                    return "application/vnd.bmi";
                // Windows BMP image
                case "bmp":
                case "dib":
                    return "image/bmp";
                case "box":
                    return "application/vnd.previewsystems.box";
                case "boz":
                    return "application/x-bzip2";
                // binary differences between files
                case "bsdiff":
                    return "application/x-bsdiff";
                case "btif":
                    return "image/prs.btif";
                // Bzip archive
                case "bz2":
                case "bz":
                    return "application/x-bzip";
                case "c4d":
                case "c4f":
                case "c4g":
                case "c4p":
                case "c4u":
                    return "application/vnd.clonk.c4group";
                // Microsoft Cabinet archive
                case "cab":
                    return "application/vnd.ms-cab-compressed";
                case "car":
                    return "application/vnd.curl.car";
                case "cat":
                    return "application/vnd.ms-pki.seccat";
                // comic book archive
                case "cb7":
                    return "application/x-cb7";
                // COBOL source file
                case "cbl":
                case "cob":
                    return "text/x-cobol";
                // comic book archive
                case "cbr":
                    return "application/x-cbr";
                // comic book archive
                case "cbt":
                    return "application/x-cbt";
                // comic book archive
                case "cbz":
                    return "application/vnd.comicbook+zip";
                // CCMX color correction file
                case "ccmx":
                    return "application/x-ccmx";
                case "cct":
                case "cst":
                case "cxt":
                case "dir":
                case "dxr":
                case "fgd":
                case "swa":
                case "w3d":
                    return "application/x-director";
                case "ccxml":
                    return "application/ccxml+xml";
                case "cdbcmsg":
                    return "application/vnd.contact.cmsg";
                // Unidata NetCDF document
                case "cdf":
                case "nc":
                    return "application/x-netcdf";
                case "cdkey":
                    return "application/vnd.mediastation.cdkey";
                // Corel Draw drawing
                case "cdr":
                    return "application/vnd.corel-draw";
                case "cdx":
                    return "chemical/x-cdx";
                case "cdxml":
                    return "application/vnd.chemdraw+xml";
                case "cdy":
                    return "application/vnd.cinderella";
                // X.509 certificate
                case "cer":
                    return "application/pkix-cert";
                // Computer Graphics Metafile
                case "cgm":
                    return "image/cgm";
                // ChangeLog document
                case "changelog":
                    return "text/x-changelog";
                case "chat":
                    return "application/x-chat";
                // CHM document
                case "chm":
                    return "application/vnd.ms-htmlhelp";
                // KChart chart
                case "chrt":
                    return "application/x-kchart";
                case "cif":
                    return "chemical/x-cif";
                case "cii":
                    return "application/vnd.anser-web-certificate-issue-initiation";
                case "cil":
                    return "application/vnd.ms-artgalry";
                case "cla":
                    return "application/vnd.claymore";
                // Java class
                case "class":
                    return "application/x-java";
                case "clkk":
                    return "application/vnd.crick.clicker.keyboard";
                case "clkp":
                    return "application/vnd.crick.clicker.palette";
                case "clkt":
                    return "application/vnd.crick.clicker.template";
                case "clkw":
                    return "application/vnd.crick.clicker.wordbank";
                case "clkx":
                    return "application/vnd.crick.clicker";
                case "clp":
                    return "application/x-msclip";
                // CMake source code
                case "cmake":
                case "cmakeliststxt":
                    return "text/x-cmake";
                case "cmc":
                    return "application/vnd.cosmocaller";
                case "cmdf":
                    return "chemical/x-cmdf";
                case "cml":
                    return "chemical/x-cml";
                case "cmp":
                    return "application/vnd.yellowriver-custom-menu";
                case "cmx":
                    return "image/x-cmx";
                case "cod":
                    return "application/vnd.rim.cod";
                // CoffeeScript document
                case "coffee":
                    return "application/vnd.coffeescript";
                // license terms
                case "copying":
                    return "text/x-copying";
                // program crash data
                case "core":
                    return "application/x-core";
                // CPIO archive
                case "cpio":
                    return "application/x-cpio";
                // CPIO archive (gzip-compressed)
                case "cpiogz":
                    return "application/x-cpio-compressed";
                // C++ source code
                case "cpp":
                case "cxx":
                case "cc":
                case "c":
                case "c++":
                    return "text/x-c++src";
                case "cpt":
                    return "application/mac-compactpro";
                // Canon CR2 raw image
                case "cr2":
                    return "image/x-canon-cr2";
                case "crd":
                    return "application/x-mscardfile";
                // author credits
                case "credits":
                    return "text/x-credits";
                // Certificate revocation list
                case "crl":
                    return "application/pkix-crl";
                // Canon CRW raw image
                case "crw":
                    return "image/x-canon-crw";
                // C# source code
                case "cs":
                    return "text/x-csharp";
                // C shell script
                case "csh":
                    return "application/x-csh";
                case "csml":
                    return "chemical/x-csml";
                case "csp":
                    return "application/vnd.commonspace";
                // CSS stylesheet
                case "css":
                    return "text/css";
                // CSV document
                case "csv":
                    return "text/csv";
                // CSV Schema document
                case "csvs":
                    return "text/csv-schema";
                case "cu":
                    return "application/cu-seeme";
                // CD image cuesheet
                case "cue":
                    return "application/x-cue";
                // Windows cursor
                case "cur":
                    return "image/x-win-bitmap";
                case "curl":
                    return "text/vnd.curl";
                case "cww":
                    return "application/prs.cww";
                // D source code
                case "d":
                case "di":
                    return "text/x-dsrc";
                case "daf":
                    return "application/vnd.mobius.daf";
                // DAR archive
                case "dar":
                    return "application/x-dar";
                case "dataless":
                case "seed":
                    return "application/vnd.fdsn.seed";
                case "davmount":
                    return "application/davmount+xml";
                // Xbase document
                case "dbf":
                    return "application/x-dbf";
                // DocBook document
                case "dbk":
                case "docbook":
                    return "application/x-docbook+xml";
                // Dreamcast GD-ROM
                case "dc":
                    return "application/x-dc-rom";
                // DCL script
                case "dcl":
                    return "text/x-dcl";
                // Kodak DCR raw image
                case "dcr":
                    return "image/x-kodak-dcr";
                case "dcurl":
                    return "text/vnd.curl.dcurl";
                case "dd2":
                    return "application/vnd.oma.dd2+xml";
                case "ddd":
                    return "application/vnd.fujixerox.ddd";
                // DirectDraw surface
                case "dds":
                    return "image/x-dds";
                // Debian package
                case "deb":
                case "udeb":
                    return "application/vnd.debian.binary-package";
                // DER/PEM/Netscape-encoded X.509 certificate
                case "der":
                case "crt":
                case "cert":
                case "pem":
                    return "application/x-x509-ca-cert";
                // desktop configuration file
                case "desktop":
                case "kdelnk":
                    return "application/x-desktop";
                case "dfac":
                    return "application/vnd.dreamfactory";
                // Dia diagram
                case "dia":
                    return "application/x-dia-diagram";
                case "dic":
                    return "text/x-c";
                // DICOM image
                case "dicomdir":
                case "dcm":
                    return "application/dicom";
                // differences between files
                case "diff":
                case "patch":
                    return "text/x-patch";
                case "dis":
                    return "application/vnd.mobius.dis";
                // DjVu image
                case "djvu":
                case "djv":
                    return "image/vnd.djvu";
                // Apple disk image
                case "dmg":
                    return "application/x-apple-diskimage";
                case "dna":
                    return "application/vnd.dna";
                // Adobe DNG negative
                case "dng":
                    return "image/x-adobe-dng";
                // Word document
                case "doc":
                case "wiz":
                    return "application/msword";
                // Word document
                case "docm":
                    return "application/vnd.ms-word.document.macroenabled.12";
                // Word 2007 document
                case "docx":
                    return "application/vnd.openxmlformats-officedocument.wordprocessingml.document";
                // Word template
                case "dot":
                    return "application/msword-template";
                // Word document template
                case "dotm":
                    return "application/vnd.ms-word.template.macroenabled.12";
                // Word 2007 document template
                case "dotx":
                    return "application/vnd.openxmlformats-officedocument.wordprocessingml.template";
                case "dp":
                    return "application/vnd.osgi.dp";
                case "dpg":
                    return "application/vnd.dpgraph";
                case "dsc":
                    return "text/prs.lines.tag";
                // DSSSL document
                case "dsl":
                    return "text/x-dsl";
                case "dtb":
                    return "application/x-dtbook+xml";
                // DTD file
                case "dtd":
                    return "application/xml-dtd";
                // DTS audio
                case "dts":
                    return "audio/vnd.dts";
                // DTSHD audio
                case "dtshd":
                    return "audio/vnd.dts.hd";
                // DV video
                case "dv":
                    return "video/dv";
                // TeX DVI document
                case "dvi":
                    return "application/x-dvi";
                // TeX DVI document (bzip-compressed)
                case "dvibz2":
                    return "application/x-bzdvi";
                // TeX DVI document (gzip-compressed)
                case "dvigz":
                    return "application/x-gzdvi";
                case "dwf":
                    return "model/vnd.dwf";
                // AutoCAD image
                case "dwg":
                    return "image/vnd.dwg";
                // DXF vector image
                case "dxf":
                    return "image/vnd.dxf";
                case "dxp":
                    return "application/vnd.spotfire.dxp";
                // Eiffel source code
                case "e":
                case "eif":
                    return "text/x-eiffel";
                case "ecelp4800":
                    return "audio/vnd.nuera.ecelp4800";
                case "ecelp7470":
                    return "audio/vnd.nuera.ecelp7470";
                case "ecelp9600":
                    return "audio/vnd.nuera.ecelp9600";
                case "edm":
                    return "application/vnd.novadigm.edm";
                case "edx":
                    return "application/vnd.novadigm.edx";
                case "efif":
                    return "application/vnd.picsel";
                // Egon Animator animation
                case "egon":
                    return "application/x-egon";
                case "ei6":
                    return "application/vnd.pg.osasli";
                // Emacs Lisp source code
                case "el":
                    return "text/x-emacs-lisp";
                // EMF image
                case "emf":
                    return "image/emf";
                // email message
                case "eml":
                case "mime":
                case "nws":
                    return "message/rfc822";
                case "emma":
                    return "application/emma+xml";
                // eMusic download package
                case "emp":
                    return "application/vnd.emusic-emusic_package";
                // XML entities document
                case "ent":
                    return "application/xml-external-parsed-entity";
                case "eol":
                    return "audio/vnd.digital-winds";
                case "eot":
                    return "application/vnd.ms-fontobject";
                // EPS image
                case "eps":
                case "epsi":
                case "epsf":
                    return "image/x-eps";
                // EPS image (bzip-compressed)
                case "epsbz2":
                case "epsibz2":
                case "epsfbz2":
                    return "image/x-bzeps";
                // EPS image (gzip-compressed)
                case "epsgz":
                case "epsigz":
                case "epsfgz":
                    return "image/x-gzeps";
                // electronic book document
                case "epub":
                    return "application/epub+zip";
                // Erlang source code
                case "erl":
                    return "text/x-erlang";
                // ECMAScript program
                case "es":
                case "ecma":
                    return "application/ecmascript";
                case "es3":
                case "et3":
                    return "application/vnd.eszigno3+xml";
                case "esf":
                    return "application/vnd.epson.esf";
                // Enlightenment theme
                case "etheme":
                    return "application/x-e-theme";
                // Setext document
                case "etx":
                    return "text/x-setext";
                // DOS/Windows executable
                case "exe":
                    return "application/x-ms-dos-executable";
                // EXR image
                case "exr":
                    return "image/x-exr";
                case "ext":
                    return "application/vnd.novadigm.ext";
                // ATK inset
                case "ez":
                    return "application/andrew-inset";
                case "ez2":
                    return "application/vnd.ezpix-album";
                case "ez3":
                    return "application/vnd.ezpix-package";
                // Fortran source code
                case "f":
                case "f90":
                case "f95":
                case "for":
                case "f77":
                    return "text/x-fortran";
                // FictionBook document
                case "fb2":
                    return "application/x-fictionbook+xml";
                // Compressed FictionBook document
                case "fb2zip":
                    return "application/x-zip-compressed-fb2";
                case "fbs":
                    return "image/vnd.fastbidsheet";
                case "fdf":
                    return "application/vnd.fdf";
                case "fe_launch":
                    return "application/vnd.denovo.fcselayout-link";
                // feature specification in Gherkin format
                case "feature":
                    return "text/x-gherkin";
                case "fg5":
                    return "application/vnd.fujitsu.oasysgp";
                case "fh":
                case "fh4":
                case "fh5":
                case "fh7":
                case "fhc":
                    return "image/x-freehand";
                // XFig image
                case "fig":
                    return "image/x-xfig";
                // FITS document
                case "fits":
                    return "image/fits";
                // FLTK Fluid file
                case "fl":
                    return "application/x-fluid";
                // FLAC audio
                case "flac":
                    return "audio/flac";
                // Flatpak application bundle
                case "flatpak":
                case "xdgapp":
                    return "application/vnd.flatpak";
                // Flatpak repository reference
                case "flatpakref":
                    return "application/vnd.flatpak.ref";
                // Flatpak repository description
                case "flatpakrepo":
                    return "application/vnd.flatpak.repo";
                // FLIC animation
                case "fli":
                case "flc":
                    return "video/x-flic";
                case "flo":
                    return "application/vnd.micrografx.flo";
                // Flash video
                case "flv":
                    return "video/x-flv";
                // Kivio flowchart
                case "flw":
                    return "application/x-kivio";
                case "flx":
                    return "text/vnd.fmi.flexstor";
                case "fly":
                    return "text/vnd.fly";
                // Adobe FrameMaker document
                case "fm":
                case "book":
                case "frame":
                case "maker":
                    return "application/vnd.framemaker";
                case "fnc":
                    return "application/vnd.frogans.fnc";
                // XSL FO file
                case "fo":
                case "xslfo":
                    return "text/x-xslfo";
                // ODG drawing (Flat XML)
                case "fodg":
                    return "application/vnd.oasis.opendocument.graphics-flat-xml";
                // ODP presentation (Flat XML)
                case "fodp":
                    return "application/vnd.oasis.opendocument.presentation-flat-xml";
                // ODS spreadsheet (Flat XML)
                case "fods":
                    return "application/vnd.oasis.opendocument.spreadsheet-flat-xml";
                // ODT document (Flat XML)
                case "fodt":
                    return "application/vnd.oasis.opendocument.text-flat-xml";
                case "fpx":
                    return "image/vnd.fpx";
                case "fsc":
                    return "application/vnd.fsc.weblaunch";
                case "fst":
                    return "image/vnd.fst";
                case "ftc":
                    return "application/vnd.fluxtime.clip";
                case "fti":
                    return "application/vnd.anser-web-funds-transfer-initiation";
                case "fvt":
                    return "video/vnd.fvt";
                // JavaFX video
                case "fxm":
                    return "video/x-javafx";
                case "fzs":
                    return "application/vnd.fuzzysheet";
                // CCITT G3 fax
                case "g3":
                    return "image/fax-g3";
                case "gac":
                    return "application/vnd.groove-account";
                // Game Boy ROM
                case "gb":
                case "sgb":
                    return "application/x-gameboy-rom";
                // Game Boy Advance ROM
                case "gba":
                case "agb":
                    return "application/x-gba-rom";
                // Game Boy Color ROM
                case "gbc":
                case "cgb":
                    return "application/x-gameboy-color-rom";
                case "gdl":
                    return "model/vnd.gdl";
                // GEDCOM family history
                case "ged":
                case "gedcom":
                    return "application/x-gedcom";
                // Genesis ROM
                case "gen":
                    return "application/x-genesis-rom";
                case "geo":
                    return "application/vnd.dynageo";
                // GeoJSON geospatial data
                case "geojson":
                    return "application/geo+json";
                case "gex":
                case "gre":
                    return "application/vnd.geometry-explorer";
                // generic font file
                case "gf":
                    return "application/x-tex-gf";
                // Game Gear ROM
                case "gg":
                    return "application/x-gamegear-rom";
                case "ggb":
                    return "application/vnd.geogebra.file";
                case "ggt":
                    return "application/vnd.geogebra.tool";
                case "ghf":
                    return "application/vnd.groove-help";
                // GIF image
                case "gif":
                    return "image/gif";
                case "gim":
                    return "application/vnd.groove-identity-message";
                // Glade project
                case "glade":
                    return "application/x-glade";
                // GML document
                case "gml":
                    return "application/gml+xml";
                // translated messages (machine-readable)
                case "gmo":
                case "mo":
                    return "application/x-gettext-translation";
                // profiler results
                case "gmonout":
                    return "application/x-profile";
                case "gmx":
                    return "application/vnd.gmx";
                // GNUnet search file
                case "gnd":
                    return "application/gnunet-directory";
                // GnuCash financial data
                case "gnucash":
                case "gnc":
                case "xac":
                    return "application/x-gnucash";
                // Gnumeric spreadsheet
                case "gnumeric":
                    return "application/x-gnumeric";
                // Go source code
                case "go":
                    return "text/x-go";
                // Gnuplot document
                case "gp":
                case "gplt":
                case "gnuplot":
                    return "application/x-gnuplot";
                case "gph":
                    return "application/vnd.flographit";
                // GPX geographic data
                case "gpx":
                    return "application/gpx+xml";
                case "gqf":
                case "gqs":
                    return "application/vnd.grafeq";
                // Graphite scientific graph
                case "gra":
                    return "application/x-graphite";
                case "gram":
                    return "application/srgs";
                case "grv":
                    return "application/vnd.groove-injector";
                case "grxml":
                    return "application/srgs+xml";
                // Genie source code
                case "gs":
                    return "text/x-genie";
                // GSM 06.10 audio
                case "gsm":
                    return "audio/x-gsm";
                case "gtm":
                    return "application/vnd.groove-tool-message";
                case "gtw":
                    return "model/vnd.gtw";
                // Graphviz DOT graph
                case "gv":
                    return "text/vnd.graphviz";
                // Google Video Pointer
                case "gvp":
                    return "text/x-google-video-pointer";
                // Gzip archive
                case "gz":
                    return "application/gzip";
                // C header
                case "h":
                    return "text/x-chdr";
                case "h261":
                    return "video/h261";
                case "h263":
                    return "video/h263";
                case "h264":
                    return "video/h264";
                case "hbci":
                    return "application/vnd.hbci";
                // HDF document
                case "hdf":
                case "hdf4":
                case "h4":
                case "hdf5":
                case "h5":
                    return "application/x-hdf";
                // C++ header
                case "hh":
                case "hp":
                case "hpp":
                case "h++":
                case "hxx":
                    return "text/x-c++hdr";
                // WinHelp help file
                case "hlp":
                    return "application/winhlp";
                // HPGL file
                case "hpgl":
                    return "application/vnd.hp-hpgl";
                case "hpid":
                    return "application/vnd.hp-hpid";
                case "hps":
                    return "application/vnd.hp-hps";
                case "hqx":
                    return "application/mac-binhex40";
                // Haskell source code
                case "hs":
                    return "text/x-haskell";
                case "htke":
                    return "application/vnd.kenameaapp";
                // HTML document
                case "html":
                case "htm":
                    return "text/html";
                case "hvd":
                    return "application/vnd.yamaha.hv-dic";
                case "hvp":
                    return "application/vnd.yamaha.hv-voice";
                case "hvs":
                    return "application/vnd.yamaha.hv-script";
                // Haansoft Hangul document
                case "hwp":
                    return "application/x-hwp";
                // Haansoft Hangul document template
                case "hwt":
                    return "application/x-hwt";
                // Citrix ICA settings file
                case "ica":
                    return "application/x-ica";
                // TGA image
                case "icb":
                case "tga":
                case "tpic":
                case "vda":
                    return "image/x-tga";
                // ICC profile
                case "icc":
                case "icm":
                    return "application/vnd.iccprofile";
                case "ice":
                    return "x-conference/x-cooltalk";
                // MacOS X icon
                case "icns":
                    return "image/x-icns";
                // Windows icon
                case "ico":
                    return "image/vnd.microsoft.icon";
                // IDL document
                case "idl":
                    return "text/x-idl";
                // IEF image
                case "ief":
                    return "image/ief";
                // ILBM image
                case "iff":
                case "ilbm":
                case "lbm":
                    return "image/x-ilbm";
                case "ifm":
                    return "application/vnd.shana.informed.formdata";
                case "igl":
                    return "application/vnd.igloader";
                // IGES document
                case "igs":
                case "iges":
                    return "model/iges";
                case "igx":
                    return "application/vnd.micrografx.igx";
                case "iif":
                    return "application/vnd.shana.informed.interchange";
                case "imp":
                    return "application/vnd.accpac.simply.imp";
                case "ims":
                    return "application/vnd.ms-ims";
                // iMelody ringtone
                case "imy":
                case "ime":
                    return "text/x-imelody";
                // installation instructions
                case "install":
                    return "text/x-install";
                case "ipk":
                    return "application/vnd.shana.informed.package";
                // iptables configuration file
                case "iptables":
                    return "text/x-iptables";
                // Jupyter Notebook
                case "ipynb":
                    return "application/x-ipynb+json";
                case "irm":
                    return "application/vnd.ibm.rights-management";
                case "irp":
                    return "application/vnd.irepository.package+xml";
                // raw CD image
                case "iso":
                case "iso9660":
                    return "application/x-cd-image";
                // Impulse Tracker audio
                case "it":
                    return "audio/x-it";
                // IT 8.7 color calibration file
                case "it87":
                    return "application/x-it87";
                case "itp":
                    return "application/vnd.shana.informed.formtemplate";
                case "ivp":
                    return "application/vnd.immervision-ivp";
                case "ivu":
                    return "application/vnd.immervision-ivu";
                // JAD document
                case "jad":
                    return "text/vnd.sun.j2me.app-descriptor";
                case "jam":
                    return "application/vnd.jam";
                // Java archive
                case "jar":
                    return "application/x-java-archive";
                // Java source code
                case "java":
                    return "text/x-java";
                // Java JCE keystore
                case "jceks":
                    return "application/x-java-jce-keystore";
                case "jisp":
                    return "application/vnd.jisp";
                // Java keystore
                case "jks":
                case "ks":
                case "cacerts":
                    return "application/x-java-keystore";
                case "jlt":
                    return "application/vnd.hp-jlyt";
                // JNG image
                case "jng":
                    return "image/x-jng";
                // JNLP file
                case "jnlp":
                    return "application/x-java-jnlp-file";
                case "joda":
                    return "application/vnd.joost.joda-archive";
                // JPEG-2000 image
                case "jp2":
                case "jpf":
                    return "image/jp2";
                // JPEG image
                case "jpeg":
                case "jpg":
                case "jpe":
                    return "image/jpeg";
                case "jpgm":
                case "jpm":
                    return "video/jpm";
                case "jpgv":
                    return "video/jpeg";
                // JBuilder project
                case "jpr":
                case "jpx":
                    return "application/x-jbuilder-project";
                // JRD document
                case "jrd":
                    return "application/jrd+json";
                // JavaScript program
                case "js":
                case "jsm":
                    return "application/javascript";
                // JSON document
                case "json":
                    return "application/json";
                // JSON-LD document
                case "jsonld":
                    return "application/ld+json";
                // JSON patch
                case "json-patch":
                    return "application/json-patch+json";
                // Kodak K25 raw image
                case "k25":
                    return "image/x-kodak-k25";
                // Karbon14 drawing
                case "karbon":
                    return "application/x-karbon";
                // Kodak KDC raw image
                case "kdc":
                    return "image/x-kodak-kdc";
                // Kexi database file-based project
                case "kexi":
                    return "application/x-kexiproject-sqlite2";
                // Kexi settings for database server connection
                case "kexic":
                    return "application/x-kexi-connectiondata";
                // shortcut to Kexi project on database server
                case "kexis":
                    return "application/x-kexiproject-shortcut";
                // Apple Keynote 5 presentation
                case "key":
                    return "application/x-iwork-keynote-sffkey";
                // KFormula formula
                case "kfo":
                    return "application/x-kformula";
                case "kia":
                    return "application/vnd.kidspiration";
                // KIllustrator drawing
                case "kil":
                    return "application/x-killustrator";
                // KML geographic data
                case "kml":
                    return "application/vnd.google-earth.kml+xml";
                // KML geographic compressed data
                case "kmz":
                    return "application/vnd.google-earth.kmz";
                case "kne":
                case "knp":
                    return "application/vnd.kinar";
                // Kontour drawing
                case "kon":
                    return "application/x-kontour";
                // KPovModeler scene
                case "kpm":
                    return "application/x-kpovmodeler";
                // KPresenter presentation
                case "kpr":
                case "kpt":
                    return "application/x-kpresenter";
                // Krita document
                case "kra":
                    return "application/x-krita";
                // KSpread spreadsheet
                case "ksp":
                    return "application/x-kspread";
                case "ktr":
                case "ktz":
                    return "application/vnd.kahootz";
                // Kugar document
                case "kud":
                    return "application/x-kugar";
                // KWord document
                case "kwd":
                case "kwt":
                    return "application/x-kword";
                // libtool shared library
                case "la":
                    return "application/x-shared-library-la";
                case "lbd":
                    return "application/vnd.llamagraphics.life-balance.desktop";
                case "lbe":
                    return "application/vnd.llamagraphics.life-balance.exchange+xml";
                // LDIF address book
                case "ldif":
                    return "text/x-ldif";
                case "les":
                    return "application/vnd.hhe.lesson-player";
                // LHA archive
                case "lha":
                case "lzh":
                    return "application/x-lha";
                // LHS source code
                case "lhs":
                    return "text/x-literate-haskell";
                // LHZ archive
                case "lhz":
                    return "application/x-lhz";
                case "link66":
                    return "application/vnd.route66.link66+xml";
                // application log
                case "log":
                    return "text/x-log";
                case "lostxml":
                    return "application/lost+xml";
                case "lrm":
                    return "application/vnd.ms-lrm";
                // Lrzip archive
                case "lrz":
                    return "application/x-lrzip";
                case "ltf":
                    return "application/vnd.frogans.ltf";
                // Lua script
                case "lua":
                    return "text/x-lua";
                case "lvp":
                    return "audio/vnd.lucent.voice";
                // LightWave object
                case "lwo":
                case "lwob":
                    return "image/x-lwo";
                // Lotus Word Pro
                case "lwp":
                    return "application/vnd.lotus-wordpro";
                // LightWave scene
                case "lws":
                    return "image/x-lws";
                // Lilypond music sheet
                case "ly":
                    return "text/x-lilypond";
                // LyX document
                case "lyx":
                    return "application/x-lyx";
                // Lzip archive
                case "lz":
                    return "application/x-lzip";
                // LZ4 archive
                case "lz4":
                    return "application/x-lz4";
                // LZMA archive
                case "lzma":
                    return "application/x-lzma";
                // LZO archive
                case "lzo":
                    return "application/x-lzop";
                // Objective-C source code
                case "m":
                    return "text/x-objcsrc";
                case "m13":
                case "m14":
                case "mvb":
                    return "application/x-msmediaview";
                // MPEG video (streamed)
                case "m1u":
                case "m4u":
                case "mxu":
                    return "video/vnd.mpegurl";
                // MPEG-2 transport stream
                case "m2t":
                case "m2ts":
                case "mts":
                case "cpi":
                case "clpi":
                case "mpl":
                case "mpls":
                case "bdm":
                case "bdmv":
                    return "video/mp2t";
                // MP3 audio (streamed)
                case "m3u":
                case "m3u8":
                case "vlc":
                    return "audio/x-mpegurl";
                // M4 macro
                case "m4":
                    return "application/x-m4";
                // MPEG-4 audio
                case "m4a":
                case "f4a":
                case "mp4a":
                    return "audio/mp4";
                // MPEG-4 audio book
                case "m4b":
                case "f4b":
                    return "audio/x-m4b";
                // Markaby script
                case "mab":
                    return "application/x-markaby";
                case "mag":
                    return "application/vnd.ecowin.chart";
                // Makefile
                case "makefile":
                case "gnumakefile":
                case "mk":
                case "mak":
                    return "text/x-makefile";
                // Manpage manual document
                case "man":
                    return "application/x-troff-man";
                // Web application cache manifest
                case "manifest":
                    return "text/cache-manifest";
                case "mbk":
                    return "application/vnd.mobius.mbk";
                // mailbox file
                case "mbox":
                    return "application/mbox";
                case "mc1":
                    return "application/vnd.medcalcdata";
                case "mcd":
                    return "application/vnd.mcd";
                case "mcurl":
                    return "text/vnd.curl.mcurl";
                // Markdown document
                case "md":
                case "mkd":
                case "markdown":
                    return "text/markdown";
                // JET database
                case "mdb":
                    return "application/vnd.ms-access";
                // Microsoft Document Imaging format
                case "mdi":
                    return "image/vnd.ms-modi";
                // Troff ME input document
                case "me":
                    return "text/x-troff-me";
                case "mesh":
                case "msh":
                case "silo":
                    return "model/mesh";
                // Meson source code
                case "mesonbuild":
                case "meson_optionstxt":
                    return "text/x-meson";
                // Metalink file
                case "meta4":
                    return "application/metalink4+xml";
                // Metalink file
                case "metalink":
                    return "application/metalink+xml";
                case "mfm":
                    return "application/vnd.mfmp";
                // MagicPoint presentation
                case "mgp":
                    return "application/x-magicpoint";
                case "mgz":
                    return "application/vnd.proteus.magazine";
                // MHTML web archive
                case "mhtml":
                case "mht":
                    return "application/x-mimearchive";
                // MIDI audio
                case "mid":
                case "midi":
                case "kar":
                case "rmi":
                    return "audio/midi";
                // Adobe FrameMaker MIF document
                case "mif":
                    return "application/x-mif";
                // MiniPSF audio
                case "minipsf":
                    return "audio/x-minipsf";
                case "mj2":
                case "mjp2":
                    return "video/mj2";
                // Matroska 3D video
                case "mk3d":
                    return "video/x-matroska-3d";
                // Matroska audio
                case "mka":
                    return "audio/x-matroska";
                // Matroska video
                case "mkv":
                    return "video/x-matroska";
                // OCaml source code
                case "ml":
                case "mli":
                    return "text/x-ocaml";
                case "mlp":
                    return "application/vnd.dolby.mlp";
                // Troff MM input document
                case "mm":
                    return "text/x-troff-mm";
                case "mmd":
                    return "application/vnd.chipnuts.karaoke-mmd";
                // SMAF audio
                case "mmf":
                case "smaf":
                    return "application/x-smaf";
                // MathML document
                case "mml":
                case "mathml":
                    return "application/mathml+xml";
                case "mmr":
                    return "image/vnd.fujixerox.edmics-mmr";
                // MNG animation
                case "mng":
                    return "video/x-mng";
                case "mny":
                    return "application/x-msmoney";
                // compressed Tracker audio
                case "mo3":
                    return "audio/x-mo3";
                // Mobipocket e-book
                case "mobi":
                case "prc":
                    return "application/x-mobipocket-ebook";
                // Qt MOC file
                case "moc":
                    return "text/x-moc";
                // Amiga SoundTracker audio
                case "mod":
                case "ult":
                case "uni":
                case "m15":
                case "mtm":
                case "669":
                case "med":
                    return "audio/x-mod";
                // Managed Object Format
                case "mof":
                    return "text/x-mof";
                // SGI video
                case "movie":
                    return "video/x-sgi-movie";
                // MP2 audio
                case "mp2":
                    return "audio/mp2";
                // MP3 audio
                case "mp3":
                case "mpga":
                case "m2a":
                case "m3a":
                case "mp2a":
                    return "audio/mpeg";
                // MPEG-4 video
                case "mp4":
                case "m4v":
                case "f4v":
                case "lrv":
                case "mp4v":
                case "mpg4":
                    return "video/mp4";
                case "mp4s":
                    return "application/mp4";
                // Musepack audio
                case "mpc":
                case "mpp":
                case "mp+":
                    return "audio/x-musepack";
                // MPEG video
                case "mpeg":
                case "mpg":
                case "mpe":
                case "vob":
                case "[0-9][0-9][0-9]vdr":
                case "m1v":
                case "m2v":
                case "mpa":
                    return "video/mpeg";
                case "mpkg":
                    return "application/vnd.apple.installer+xml";
                case "mpm":
                    return "application/vnd.blueice.multipass";
                case "mpn":
                    return "application/vnd.mophun.application";
                case "mpt":
                    return "application/vnd.ms-project";
                case "mpy":
                    return "application/vnd.ibm.minipay";
                case "mqy":
                    return "application/vnd.mobius.mqy";
                case "mrc":
                    return "application/marc";
                // MRML playlist
                case "mrml":
                case "mrl":
                    return "text/x-mrml";
                // Minolta MRW raw image
                case "mrw":
                    return "image/x-minolta-mrw";
                // Troff MS input document
                case "ms":
                    return "text/x-troff-ms";
                case "mscml":
                    return "application/mediaservercontrol+xml";
                case "mseed":
                    return "application/vnd.fdsn.mseed";
                case "mseq":
                    return "application/vnd.mseq";
                case "msf":
                    return "application/vnd.epson.msf";
                // Windows Installer package
                case "msi":
                    return "application/x-msi";
                case "msl":
                    return "application/vnd.mobius.msl";
                // Office drawing
                case "msod":
                    return "image/x-msod";
                case "msty":
                    return "application/vnd.muvee.style";
                // MSX ROM
                case "msx":
                    return "application/x-msx-rom";
                // Mup publication
                case "mup":
                case "not":
                    return "text/x-mup";
                case "mus":
                    return "application/vnd.musician";
                case "musicxml":
                    return "application/vnd.recordare.musicxml+xml";
                case "mwf":
                    return "application/vnd.mfer";
                // MXF video
                case "mxf":
                    return "application/mxf";
                case "mxl":
                    return "application/vnd.recordare.musicxml";
                case "mxml":
                case "xhvml":
                case "xvm":
                case "xvml":
                    return "application/xv+xml";
                case "mxs":
                    return "application/vnd.triscape.mxs";
                // Nintendo64 ROM
                case "n64":
                case "z64":
                case "v64":
                    return "application/x-n64-rom";
                // Mathematica Notebook
                case "nb":
                case "ma":
                case "mb":
                    return "application/mathematica";
                case "ncx":
                    return "application/x-dtbncx+xml";
                // Nintendo DS ROM
                case "nds":
                    return "application/x-nintendo-ds-rom";
                // Nikon NEF raw image
                case "nef":
                    return "image/x-nikon-nef";
                // NES ROM
                case "nes":
                case "nez":
                case "unf":
                case "unif":
                    return "application/x-nes-rom";
                // NFO document
                case "nfo":
                    return "text/x-nfo";
                case "n-gage":
                    return "application/vnd.nokia.n-gage.symbian.install";
                case "ngdat":
                    return "application/vnd.nokia.n-gage.data";
                // Neo-Geo Pocket ROM
                case "ngp":
                    return "application/x-neo-geo-pocket-rom";
                case "nlu":
                    return "application/vnd.neurolanguage.nlu";
                case "nml":
                    return "application/vnd.enliven";
                case "nnd":
                    return "application/vnd.noblenet-directory";
                case "nns":
                    return "application/vnd.noblenet-sealer";
                case "nnw":
                    return "application/vnd.noblenet-web";
                case "npx":
                    return "image/vnd.net-fpx";
                // Windows Media Station file
                case "nsc":
                    return "application/x-netshow-channel";
                case "nsf":
                    return "application/vnd.lotus-notes";
                // NullSoft video
                case "nsv":
                    return "video/x-nsv";
                // NewzBin usenet index
                case "nzb":
                    return "application/x-nzb";
                // object code
                case "o":
                    return "application/x-object";
                case "oa2":
                    return "application/vnd.fujitsu.oasys2";
                case "oa3":
                    return "application/vnd.fujitsu.oasys3";
                case "oas":
                    return "application/vnd.fujitsu.oasys";
                case "obd":
                    return "application/x-msbinder";
                // TGIF document
                case "obj":
                    return "application/x-tgif";
                // OCL file
                case "ocl":
                    return "text/x-ocl";
                // ODA document
                case "oda":
                    return "application/oda";
                // ODB database
                case "odb":
                    return "application/vnd.oasis.opendocument.database";
                // ODC chart
                case "odc":
                    return "application/vnd.oasis.opendocument.chart";
                // ODF formula
                case "odf":
                    return "application/vnd.oasis.opendocument.formula";
                // ODG drawing
                case "odg":
                    return "application/vnd.oasis.opendocument.graphics";
                // ODI image
                case "odi":
                    return "application/vnd.oasis.opendocument.image";
                // ODM document
                case "odm":
                case "otm":
                    return "application/vnd.oasis.opendocument.text-master";
                // ODP presentation
                case "odp":
                    return "application/vnd.oasis.opendocument.presentation";
                // ODS spreadsheet
                case "ods":
                    return "application/vnd.oasis.opendocument.spreadsheet";
                // ODT document
                case "odt":
                    return "application/vnd.oasis.opendocument.text";
                // Ogg Audio
                case "oga":
                case "ogg":
                case "opus":
                    return "audio/ogg";
                // OGM video
                case "ogm":
                    return "video/x-ogm+ogg";
                // Ogg Video
                case "ogv":
                    return "video/ogg";
                // Ogg multimedia file
                case "ogx":
                    return "application/ogg";
                // GNU Oleo spreadsheet
                case "oleo":
                    return "application/x-oleo";
                case "onepkg":
                case "onetmp":
                case "onetoc":
                case "onetoc2":
                    return "application/onenote";
                // OOC source code
                case "ooc":
                    return "text/x-ooc";
                case "opf":
                    return "application/oebps-package+xml";
                // OPML syndication feed
                case "opml":
                    return "text/x-opml+xml";
                // OpenRaster archiving image
                case "ora":
                    return "image/openraster";
                // Olympus ORF raw image
                case "orf":
                    return "image/x-olympus-orf";
                case "org":
                    return "application/vnd.lotus-organizer";
                case "osf":
                    return "application/vnd.yamaha.openscoreformat";
                case "osfpvg":
                    return "application/vnd.yamaha.openscoreformat.osfpvg+xml";
                // ODC template
                case "otc":
                    return "application/vnd.oasis.opendocument.chart-template";
                // ODF template
                case "otf":
                case "odft":
                    return "application/vnd.oasis.opendocument.formula-template";
                // ODG template
                case "otg":
                    return "application/vnd.oasis.opendocument.graphics-template";
                // OTH template
                case "oth":
                    return "application/vnd.oasis.opendocument.text-web";
                case "oti":
                    return "application/vnd.oasis.opendocument.image-template";
                // ODP template
                case "otp":
                    return "application/vnd.oasis.opendocument.presentation-template";
                // ODS template
                case "ots":
                    return "application/vnd.oasis.opendocument.spreadsheet-template";
                // ODT template
                case "ott":
                    return "application/vnd.oasis.opendocument.text-template";
                // OWL XML file
                case "owx":
                    return "application/owl+xml";
                // XPS document
                case "oxps":
                case "xps":
                    return "application/oxps";
                // OpenOffice.org extension
                case "oxt":
                    return "application/vnd.openofficeorg.extension";
                // Pascal source code
                case "p":
                case "pas":
                    return "text/x-pascal";
                // PKCS#10 certification request
                case "p10":
                    return "application/pkcs10";
                // PKCS#12 certificate bundle
                case "p12":
                case "pfx":
                    return "application/pkcs12";
                // Adobe PageMaker
                case "p65":
                case "pm6":
                case "pmd":
                    return "application/x-pagemaker";
                // PKCS#7 certificate bundle
                case "p7b":
                case "spc":
                    return "application/x-pkcs7-certificates";
                // PKCS#7 Message or Certificate
                case "p7c":
                case "p7m":
                    return "application/pkcs7-mime";
                case "p7r":
                    return "application/x-pkcs7-certreqresp";
                // detached S/MIME signature
                case "p7s":
                    return "application/pkcs7-signature";
                // PKCS#8 private key
                case "p8":
                    return "application/pkcs8";
                // Pack200 Java archive
                case "pack":
                    return "application/x-java-pack200";
                // PAK archive
                case "pak":
                    return "application/x-pak";
                // Parchive archive
                case "par2":
                    return "application/x-par2";
                case "pbd":
                    return "application/vnd.powerbuilder6";
                // PBM image
                case "pbm":
                    return "image/x-portable-bitmap";
                // Network Packet Capture
                case "pcap":
                case "cap":
                case "dmp":
                    return "application/vnd.tcpdump.pcap";
                // PCD image
                case "pcd":
                    return "image/x-photo-cd";
                // PC Engine ROM
                case "pce":
                    return "application/x-pc-engine-rom";
                // PCF font
                case "pcf":
                case "pcfz":
                case "pcfgz":
                    return "application/x-font-pcf";
                // PCL file
                case "pcl":
                    return "application/vnd.hp-pcl";
                case "pclxl":
                    return "application/vnd.hp-pclxl";
                // Macintosh Quickdraw/PICT drawing
                case "pct":
                case "pict":
                case "pict1":
                case "pict2":
                case "pic":
                    return "image/x-pict";
                case "pcurl":
                    return "application/vnd.curl.pcurl";
                // PCX image
                case "pcx":
                    return "image/vnd.zbrush.pcx";
                // AportisDoc document
                case "pdb":
                case "pdc":
                    return "application/x-aportisdoc";
                // PDF document
                case "pdf":
                    return "application/pdf";
                // PDF document (bzip-compressed)
                case "pdfbz2":
                    return "application/x-bzpdf";
                // PDF document (gzip-compressed)
                case "pdfgz":
                    return "application/x-gzpdf";
                // PDF document (XZ-compressed)
                case "pdfxz":
                    return "application/x-xzpdf";
                // Pentax PEF raw image
                case "pef":
                    return "image/x-pentax-pef";
                // Postscript type-1 font
                case "pfa":
                case "pfb":
                case "gsf":
                case "pfm":
                    return "application/x-font-type1";
                case "pfr":
                    return "application/font-tdpfr";
                // PGM image
                case "pgm":
                    return "image/x-portable-graymap";
                // PGN chess game notation
                case "pgn":
                    return "application/vnd.chess-pgn";
                // PGP/MIME-encrypted message header
                case "pgp":
                case "gpg":
                case "asc":
                    return "application/pgp-encrypted";
                // PHP script
                case "php":
                case "php3":
                case "php4":
                case "php5":
                case "phps":
                    return "application/x-php";
                // packed font file
                case "pk":
                    return "application/x-tex-pk";
                case "pki":
                    return "application/pkixcmp";
                // PkiPath certification path
                case "pkipath":
                    return "application/pkix-pkipath";
                // Perl script
                case "pl":
                case "pm":
                case "al":
                case "perl":
                case "pod":
                case "t":
                    return "application/x-perl";
                // iRiver Playlist
                case "pla":
                    return "audio/x-iriver-pla";
                case "plb":
                    return "application/vnd.3gpp.pic-bw-large";
                case "plc":
                    return "application/vnd.mobius.plc";
                case "plf":
                    return "application/vnd.pocketlearn";
                // PlanPerfect spreadsheet
                case "pln":
                    return "application/x-planperfect";
                // MP3 ShoutCast playlist
                case "pls":
                    return "audio/x-scpls";
                case "pml":
                    return "application/vnd.ctc-posml";
                // PNG image
                case "png":
                    return "image/png";
                // PNM image
                case "pnm":
                    return "image/x-portable-anymap";
                // MacPaint Bitmap image
                case "pntg":
                    return "image/x-macpaint";
                // translation file
                case "po":
                    return "text/x-gettext-translation";
                // SPSS Portable Data File
                case "por":
                    return "application/x-spss-por";
                case "portpkg":
                    return "application/vnd.macports.portpkg";
                // PowerPoint presentation template
                case "potm":
                    return "application/vnd.ms-powerpoint.template.macroenabled.12";
                // PowerPoint 2007 presentation template
                case "potx":
                    return "application/vnd.openxmlformats-officedocument.presentationml.template";
                // PowerPoint add-in
                case "ppam":
                    return "application/vnd.ms-powerpoint.addin.macroenabled.12";
                case "ppd":
                    return "application/vnd.cups-ppd";
                // PPM image
                case "ppm":
                    return "image/x-portable-pixmap";
                // PowerPoint presentation
                case "ppsm":
                    return "application/vnd.ms-powerpoint.slideshow.macroenabled.12";
                // PowerPoint 2007 show
                case "ppsx":
                    return "application/vnd.openxmlformats-officedocument.presentationml.slideshow";
                // PowerPoint presentation
                case "pptm":
                    return "application/vnd.ms-powerpoint.presentation.macroenabled.12";
                // PowerPoint 2007 presentation
                case "pptx":
                    return "application/vnd.openxmlformats-officedocument.presentationml.presentation";
                // PowerPoint presentation
                case "ppz":
                case "ppt":
                case "pps":
                case "pot":
                case "ppa":
                case "pwz":
                    return "application/vnd.ms-powerpoint";
                // Palm OS database
                case "pqa":
                case "oprc":
                    return "application/vnd.palm";
                case "pre":
                    return "application/vnd.lotus-freelance";
                case "prf":
                    return "application/pics-rules";
                // PS document
                case "ps":
                    return "application/postscript";
                case "psb":
                    return "application/vnd.3gpp.pic-bw-small";
                // PostScript document (bzip-compressed)
                case "psbz2":
                    return "application/x-bzpostscript";
                // Photoshop image
                case "psd":
                    return "image/vnd.adobe.photoshop";
                // Linux PSF console font
                case "psf":
                    return "application/x-font-linux-psf";
                // Linux PSF console font (gzip-compressed)
                case "psfgz":
                    return "application/x-gz-font-linux-psf";
                // PSFlib audio library
                case "psflib":
                    return "audio/x-psflib";
                // PostScript document (gzip-compressed)
                case "psgz":
                    return "application/x-gzpostscript";
                // Pocket Word document
                case "psw":
                    return "application/x-pocket-word";
                case "ptid":
                    return "application/vnd.pvi.ptid1";
                // Microsoft Publisher document
                case "pub":
                    return "application/vnd.ms-publisher";
                case "pvb":
                    return "application/vnd.3gpp.pic-bw-var";
                // Pathetic Writer document
                case "pw":
                    return "application/x-pw";
                case "pwn":
                    return "application/vnd.3m.post-it-notes";
                // Python script
                case "py":
                case "pyx":
                case "wsgi":
                    return "text/x-python";
                case "pya":
                    return "audio/vnd.ms-playready.media.pya";
                // Python bytecode
                case "pyc":
                case "pyo":
                    return "application/x-python-bytecode";
                case "pyv":
                    return "video/vnd.ms-playready.media.pyv";
                case "qam":
                    return "application/vnd.epson.quickanime";
                case "qbo":
                    return "application/vnd.intu.qbo";
                case "qfx":
                    return "application/vnd.intu.qfx";
                // Quicken document
                case "qif":
                    return "application/x-qw";
                // Qt Markup Language file
                case "qml":
                case "qmltypes":
                case "qmlproject":
                    return "text/x-qml";
                // Qpress archive
                case "qp":
                    return "application/x-qpress";
                case "qps":
                    return "application/vnd.publishare-delta-tree";
                // QuickTime video
                case "qt":
                case "mov":
                case "moov":
                case "qtvr":
                    return "video/quicktime";
                // QtiPlot document
                case "qti":
                case "qtigz":
                    return "application/x-qtiplot";
                // QuickTime image
                case "qtif":
                    return "image/x-quicktime";
                // QuickTime metalink playlist
                case "qtl":
                    return "application/x-quicktime-media-link";
                case "qwd":
                case "qwt":
                case "qxb":
                case "qxd":
                case "qxl":
                case "qxt":
                    return "application/vnd.quark.quarkxpress";
                // RealAudio document
                case "ra":
                case "rax":
                    return "audio/vnd.rn-realaudio";
                // Fuji RAF raw image
                case "raf":
                    return "image/x-fuji-raf";
                // RealMedia Metafile
                case "ram":
                    return "application/ram";
                // RAML document
                case "raml":
                    return "application/raml+yaml";
                // RAR archive
                case "rar":
                    return "application/vnd.rar";
                // CMU raster image
                case "ras":
                    return "image/x-cmu-raster";
                // Panasonic raw image
                case "raw":
                    return "image/x-panasonic-raw";
                // Raw disk image
                case "raw-disk-image":
                case "img":
                    return "application/x-raw-disk-image";
                // Raw disk image (XZ-compressed)
                case "raw-disk-imagexz":
                case "imgxz":
                    return "application/x-raw-disk-image-xz-compressed";
                // Ruby script
                case "rb":
                    return "application/x-ruby";
                case "rcprofile":
                    return "application/vnd.ipunplugged.rcprofile";
                // RDF file
                case "rdf":
                case "rdfs":
                case "owl":
                    return "application/rdf+xml";
                case "rdz":
                    return "application/vnd.data-vision.rdz";
                // README document
                case "readme":
                    return "text/x-readme";
                // Windows Registry extract
                case "reg":
                    return "text/x-ms-regedit";
                // rejected patch
                case "rej":
                    return "text/x-reject";
                case "rep":
                    return "application/vnd.businessobjects";
                case "res":
                    return "application/x-dtbresource+xml";
                // RGB image
                case "rgb":
                    return "image/x-rgb";
                case "rif":
                    return "application/reginfo+xml";
                case "rl":
                    return "application/resource-lists+xml";
                case "rlc":
                    return "image/vnd.fujixerox.edmics-rlc";
                case "rld":
                    return "application/resource-lists-diff+xml";
                // Run Length Encoded bitmap image
                case "rle":
                    return "image/rle";
                // RealMedia document
                case "rm":
                case "rmj":
                case "rmm":
                case "rms":
                case "rmx":
                case "rmvb":
                    return "application/vnd.rn-realmedia";
                // GNU mail message
                case "rmail":
                    return "message/x-gnu-rmail";
                case "rmp":
                    return "audio/x-pn-realaudio-plugin";
                // RELAX NG XML schema
                case "rnc":
                    return "application/relax-ng-compact-syntax";
                // RealPix document
                case "rp":
                    return "image/vnd.rn-realpix";
                // RPM package
                case "rpm":
                    return "application/x-rpm";
                case "rpss":
                    return "application/vnd.nokia.radio-presets";
                case "rpst":
                    return "application/vnd.nokia.radio-preset";
                case "rq":
                    return "application/sparql-query";
                // Rust source code
                case "rs":
                    return "text/rust";
                case "rsd":
                    return "application/rsd+xml";
                // RSS summary
                case "rss":
                    return "application/rss+xml";
                // RealText document
                case "rt":
                    return "text/vnd.rn-realtext";
                // RTF document
                case "rtf":
                    return "application/rtf";
                // rich text document
                case "rtx":
                    return "text/richtext";
                // RealVideo document
                case "rv":
                case "rvx":
                    return "video/vnd.rn-realvideo";
                // Panasonic raw2 image
                case "rw2":
                    return "image/x-panasonic-raw2";
                // Scream Tracker 3 audio
                case "s3m":
                    return "audio/x-s3m";
                case "saf":
                    return "application/vnd.yamaha.smaf-audio";
                // Lotus AmiPro document
                case "sam":
                    return "application/x-amipro";
                // SAMI subtitles
                case "sami":
                    return "application/x-sami";
                // Sass CSS pre-processor file
                case "sass":
                    return "text/x-sass";
                // SPSS Data File
                case "sav":
                case "zsav":
                    return "application/x-spss-sav";
                case "sbml":
                    return "application/sbml+xml";
                case "sc":
                    return "application/vnd.ibm.secure-container";
                // Scala source code
                case "scala":
                    return "text/x-scala";
                case "scd":
                    return "application/x-msschedule";
                // Scheme source code
                case "scm":
                case "ss":
                    return "text/x-scheme";
                // SCons configuration file
                case "sconstruct":
                case "sconscript":
                    return "text/x-scons";
                case "scq":
                    return "application/scvp-cv-request";
                case "scs":
                    return "application/scvp-cv-response";
                // Sass CSS pre-processor file
                case "scss":
                    return "text/x-scss";
                case "scurl":
                    return "text/vnd.curl.scurl";
                // StarDraw drawing
                case "sda":
                    return "application/vnd.stardivision.draw";
                // StarCalc spreadsheet
                case "sdc":
                    return "application/vnd.stardivision.calc";
                // StarImpress presentation
                case "sdd":
                case "sdp":
                    return "application/vnd.stardivision.impress";
                case "sdkd":
                case "sdkm":
                    return "application/vnd.solent.sdkm+xml";
                // StarChart chart
                case "sds":
                    return "application/vnd.stardivision.chart";
                // StarWriter document
                case "sdw":
                case "vor":
                case "sgl":
                    return "application/vnd.stardivision.writer";
                case "see":
                    return "application/vnd.seemail";
                case "sema":
                    return "application/vnd.sema";
                case "semd":
                    return "application/vnd.semd";
                case "semf":
                    return "application/vnd.semf";
                case "ser":
                    return "application/java-serialized-object";
                case "setpay":
                    return "application/set-payment-initiation";
                case "setreg":
                    return "application/set-registration-initiation";
                // Super NES ROM
                case "sfc":
                case "smc":
                    return "application/vnd.nintendo.snes.rom";
                case "sfd-hdstx":
                    return "application/vnd.hydrostatix.sof-data";
                case "sfs":
                    return "application/vnd.spotfire.sfs";
                // SG-1000 ROM
                case "sg":
                    return "application/x-sg1000-rom";
                // SGF record
                case "sgf":
                    return "application/x-go-sgf";
                // SGI image
                case "sgi":
                    return "image/x-sgi";
                // SGML document
                case "sgml":
                case "sgm":
                    return "text/sgml";
                // shell script
                case "sh":
                    return "application/x-shellscript";
                // Dia shape
                case "shape":
                    return "application/x-dia-shape";
                // shell archive
                case "shar":
                    return "application/x-shar";
                case "shf":
                    return "application/shf+xml";
                // Shorten audio
                case "shn":
                    return "application/x-shorten";
                case "si":
                    return "text/vnd.wap.si";
                // Siag spreadsheet
                case "siag":
                    return "application/x-siag";
                case "sic":
                    return "application/vnd.wap.sic";
                // Commodore 64 audio
                case "sid":
                case "psid":
                    return "audio/prs.sid";
                // detached OpenPGP signature
                case "sig":
                    return "application/pgp-signature";
                // SIS package
                case "sis":
                    return "application/vnd.symbian.install";
                // SISX package
                case "sisx":
                    return "x-epoc/x-sisx-app";
                // StuffIt archive
                case "sit":
                    return "application/x-stuffit";
                case "sitx":
                    return "application/x-stuffitx";
                // Sieve mail filter script
                case "siv":
                    return "application/sieve";
                // Skencil document
                case "sk":
                case "sk1":
                    return "image/x-skencil";
                case "skd":
                case "skm":
                case "skp":
                case "skt":
                    return "application/vnd.koan";
                // PGP keys
                case "skr":
                case "pkr":
                    return "application/pgp-keys";
                case "sl":
                    return "text/vnd.wap.sl";
                case "slc":
                    return "application/vnd.wap.slc";
                // PowerPoint slide
                case "sldm":
                    return "application/vnd.ms-powerpoint.slide.macroenabled.12";
                // PowerPoint 2007 slide
                case "sldx":
                    return "application/vnd.openxmlformats-officedocument.presentationml.slide";
                case "slt":
                    return "application/vnd.epson.salt";
                // StarMail email
                case "smd":
                    return "application/vnd.stardivision.mail";
                // StarMath formula
                case "smf":
                    return "application/vnd.stardivision.math";
                // SMIL document
                case "smil":
                case "smi":
                case "sml":
                case "kino":
                    return "application/smil+xml";
                // Master System ROM
                case "sms":
                    return "application/x-sms-rom";
                // Snap package
                case "snap":
                    return "application/vnd.snap";
                case "snf":
                    return "application/x-font-snf";
                // shared library
                case "so":
                    return "application/x-sharedlib";
                // Speedo font
                case "spd":
                    return "application/x-font-speedo";
                // RPM spec file
                case "spec":
                    return "text/x-rpm-spec";
                case "spf":
                    return "application/vnd.yamaha.smaf-phrase";
                case "spot":
                    return "text/vnd.in3d.spot";
                case "spp":
                    return "application/scvp-vp-response";
                case "spq":
                    return "application/scvp-vp-request";
                // Speex audio
                case "spx":
                    return "audio/x-speex";
                // SQL code
                case "sql":
                    return "application/sql";
                // Squashfs filesystem
                case "sqsh":
                    return "application/vnd.squashfs";
                // Sony SR2 raw image
                case "sr2":
                    return "image/x-sony-sr2";
                // WAIS source code
                case "src":
                    return "application/x-wais-source";
                // Source RPM package
                case "srcrpm":
                case "spm":
                    return "application/x-source-rpm";
                // Sony SRF raw image
                case "srf":
                    return "image/x-sony-srf";
                // SubRip subtitles
                case "srt":
                    return "application/x-subrip";
                case "srx":
                    return "application/sparql-results+xml";
                // SSA subtitles
                case "ssa":
                case "ass":
                    return "text/x-ssa";
                case "sse":
                    return "application/vnd.kodak-descriptor";
                case "ssf":
                    return "application/vnd.epson.ssf";
                case "ssml":
                    return "application/ssml+xml";
                // OpenOffice Calc template
                case "stc":
                    return "application/vnd.sun.xml.calc.template";
                // OpenOffice Draw template
                case "std":
                    return "application/vnd.sun.xml.draw.template";
                case "stf":
                    return "application/vnd.wt.stf";
                // OpenOffice Impress template
                case "sti":
                    return "application/vnd.sun.xml.impress.template";
                case "stk":
                    return "application/hyperstudio";
                case "stl":
                    return "application/vnd.ms-pki.stl";
                // Scream Tracker audio
                case "stm":
                    return "audio/x-stm";
                case "str":
                    return "application/vnd.pg.format";
                // OpenOffice Writer template
                case "stw":
                    return "application/vnd.sun.xml.writer.template";
                // MicroDVD subtitles
                case "sub":
                    return "text/x-microdvd";
                // Sun raster image
                case "sun":
                    return "image/x-sun-raster";
                case "sus":
                case "susp":
                    return "application/vnd.sus-calendar";
                // SystemVerilog source code
                case "sv":
                    return "text/x-svsrc";
                // SV4 CPIO archive
                case "sv4cpio":
                    return "application/x-sv4cpio";
                // SV4 CPIO archive (with CRC)
                case "sv4crc":
                    return "application/x-sv4crc";
                case "svd":
                    return "application/vnd.svd";
                // SVG image
                case "svg":
                    return "image/svg+xml";
                // compressed SVG image
                case "svgz":
                    return "image/svg+xml-compressed";
                // SystemVerilog header
                case "svh":
                    return "text/x-svhdr";
                // Shockwave Flash file
                case "swf":
                case "spl":
                    return "application/vnd.adobe.flash.movie";
                case "swi":
                    return "application/vnd.arastra.swi";
                // OpenOffice Calc spreadsheet
                case "sxc":
                    return "application/vnd.sun.xml.calc";
                // OpenOffice Draw drawing
                case "sxd":
                    return "application/vnd.sun.xml.draw";
                // OpenOffice Writer global document
                case "sxg":
                    return "application/vnd.sun.xml.writer.global";
                // OpenOffice Impress presentation
                case "sxi":
                    return "application/vnd.sun.xml.impress";
                // OpenOffice Math formula
                case "sxm":
                    return "application/vnd.sun.xml.math";
                // OpenOffice Writer document
                case "sxw":
                    return "application/vnd.sun.xml.writer";
                // spreadsheet interchange document
                case "sylk":
                case "slk":
                    return "text/spreadsheet";
                // txt2tags document
                case "t2t":
                    return "text/x-txt2tags";
                case "tao":
                    return "application/vnd.tao.intent-module-archive";
                // Tar archive
                case "tar":
                case "gtar":
                case "gem":
                    return "application/x-tar";
                // Tar archive (bzip-compressed)
                case "tarbz2":
                case "tarbz":
                case "tbz2":
                case "tbz":
                case "tb2":
                    return "application/x-bzip-compressed-tar";
                // Tar archive (gzip-compressed)
                case "targz":
                case "tgz":
                    return "application/x-compressed-tar";
                // Tar archive (lrzip-compressed)
                case "tarlrz":
                case "tlrz":
                    return "application/x-lrzip-compressed-tar";
                // Tar archive (lzip-compressed)
                case "tarlz":
                    return "application/x-lzip-compressed-tar";
                // Tar archive (LZ4-compressed)
                case "tarlz4":
                    return "application/x-lz4-compressed-tar";
                // Tar archive (LZMA-compressed)
                case "tarlzma":
                case "tlz":
                    return "application/x-lzma-compressed-tar";
                // Tar archive (LZO-compressed)
                case "tarlzo":
                case "tzo":
                    return "application/x-tzo";
                // Tar archive (XZ-compressed)
                case "tarxz":
                case "txz":
                    return "application/x-xz-compressed-tar";
                // Tar archive (compressed)
                case "tarz":
                case "taz":
                    return "application/x-tarz";
                case "tcap":
                    return "application/vnd.3gpp2.tcap";
                // Tcl script
                case "tcl":
                case "tk":
                    return "text/x-tcl";
                case "teacher":
                    return "application/vnd.smart.teacher";
                // TeX document
                case "tex":
                case "ltx":
                case "sty":
                case "cls":
                case "dtx":
                case "ins":
                case "latex":
                    return "text/x-tex";
                // TeXInfo document
                case "texi":
                case "texinfo":
                    return "text/x-texinfo";
                case "tfm":
                    return "application/x-tex-tfm";
                // theme
                case "theme":
                    return "application/x-theme";
                // Microsoft Windows theme pack
                case "themepack":
                    return "application/x-windows-themepack";
                // TIFF image
                case "tif":
                case "tiff":
                    return "image/tiff";
                case "tmo":
                    return "application/vnd.tmobile-livetv";
                // TNEF message
                case "tnef":
                case "tnf":
                case "winmaildat":
                    return "application/vnd.ms-tnef";
                // CD Table Of Contents
                case "toc":
                    return "application/x-cdrdao-toc";
                // BitTorrent seed file
                case "torrent":
                    return "application/x-bittorrent";
                case "tpl":
                    return "application/vnd.groove-tool-template";
                case "tpt":
                    return "application/vnd.trid.tpt";
                // Troff document
                case "tr":
                case "roff":
                    return "text/troff";
                case "tra":
                    return "application/vnd.trueapp";
                // TriG RDF document
                case "trig":
                    return "application/x-trig";
                case "trm":
                    return "application/x-msterminal";
                // message catalog
                case "ts":
                    return "text/vnd.trolltech.linguist";
                // TSV document
                case "tsv":
                    return "text/tab-separated-values";
                // TrueAudio audio
                case "tta":
                    return "audio/x-tta";
                // TrueType font
                case "ttf":
                case "ttc":
                    return "application/x-font-ttf";
                // Turtle document
                case "ttl":
                    return "text/turtle";
                // TrueType XML font
                case "ttx":
                    return "application/x-font-ttx";
                case "twd":
                case "twds":
                    return "application/vnd.simtech-mindmapper";
                // Twig template
                case "twig":
                    return "text/x-twig";
                case "txd":
                    return "application/vnd.genomatix.tuxedo";
                case "txf":
                    return "application/vnd.mobius.txf";
                // plain text document
                case "txt":
                case ",v":
                case "conf":
                case "def":
                case "in":
                case "ksh":
                case "list":
                case "text":
                    return "text/plain";
                case "ufd":
                case "ufdl":
                    return "application/vnd.ufdl";
                // UFRaw ID image
                case "ufraw":
                    return "application/x-ufraw";
                // Qt Designer file
                case "ui":
                    return "application/x-designer";
                // X-Motif UIL table
                case "uil":
                    return "text/x-uil";
                case "umj":
                    return "application/vnd.umajin";
                case "unityweb":
                    return "application/vnd.unity";
                case "uoml":
                    return "application/vnd.uoml+xml";
                case "uri":
                case "uris":
                case "urls":
                    return "text/uri-list";
                // Internet shortcut
                case "url":
                    return "application/x-mswinurl";
                // Ustar archive
                case "ustar":
                    return "application/x-ustar";
                case "utz":
                    return "application/vnd.uiq.theme";
                // uuencoded file
                case "uue":
                case "uu":
                    return "text/x-uuencode";
                // Verilog source code
                case "v":
                    return "text/x-verilog";
                // Vala source code
                case "vala":
                case "vapi":
                    return "text/x-vala";
                // electronic business card
                case "vcard":
                case "vcf":
                case "vct":
                case "gcrd":
                    return "text/vcard";
                case "vcd":
                    return "application/x-cdlink";
                case "vcg":
                    return "application/vnd.groove-vcard";
                // VCS/ICS calendar
                case "vcs":
                case "ics":
                case "ifb":
                    return "text/calendar";
                case "vcx":
                    return "application/vnd.vcx";
                // VHDL source code
                case "vhd":
                case "vhdl":
                    return "text/x-vhdl";
                case "vis":
                    return "application/vnd.visionary";
                // Vivo video
                case "viv":
                case "vivo":
                    return "video/vnd.vivo";
                // VOC audio
                case "voc":
                    return "audio/x-voc";
                // VRML document
                case "vrm":
                case "vrml":
                case "wrl":
                    return "model/vrml";
                // Microsoft Visio document
                case "vsd":
                case "vst":
                case "vsw":
                case "vss":
                    return "application/vnd.visio";
                // Office Open XML Visio Drawing
                case "vsdm":
                    return "application/vnd.ms-visio.drawing.macroenabled.main+xml";
                // Office Open XML Visio Drawing
                case "vsdx":
                    return "application/vnd.ms-visio.drawing.main+xml";
                case "vsf":
                    return "application/vnd.vsf";
                // Office Open XML Visio Stencil
                case "vssm":
                    return "application/vnd.ms-visio.stencil.macroenabled.main+xml";
                // Office Open XML Visio Stencil
                case "vssx":
                    return "application/vnd.ms-visio.stencil.main+xml";
                // Office Open XML Visio Template
                case "vstm":
                    return "application/vnd.ms-visio.template.macroenabled.main+xml";
                // Office Open XML Visio Template
                case "vstx":
                    return "application/vnd.ms-visio.template.main+xml";
                // WebVTT subtitles
                case "vtt":
                    return "text/vtt";
                case "vtu":
                    return "model/vnd.vtu";
                case "vxml":
                    return "application/voicexml+xml";
                // WiiWare bundle
                case "wad":
                    return "application/x-wii-wad";
                // WAV audio
                case "wav":
                    return "audio/x-wav";
                // Quattro Pro spreadsheet
                case "wb1":
                case "wb2":
                case "wb3":
                    return "application/x-quattropro";
                // WBMP image
                case "wbmp":
                    return "image/vnd.wap.wbmp";
                case "wbs":
                    return "application/vnd.criticaltools.wbs+xml";
                case "wbxml":
                    return "application/vnd.wap.wbxml";
                // Microsoft Works document
                case "wcm":
                case "wdb":
                case "wps":
                case "xlr":
                    return "application/vnd.ms-works";
                // WebM video
                case "webm":
                    return "video/webm";
                // WebP image
                case "webp":
                    return "image/webp";
                // WIM disk Image
                case "wim":
                case "swm":
                    return "application/x-ms-wim";
                // Partially downloaded file
                case "wkdownload":
                case "crdownload":
                case "part":
                    return "application/x-partial-download";
                case "wm":
                    return "video/x-ms-wm";
                // Windows Media audio
                case "wma":
                    return "audio/x-ms-wma";
                case "wmd":
                    return "application/x-ms-wmd";
                // WMF image
                case "wmf":
                    return "image/wmf";
                // WML document
                case "wml":
                    return "text/vnd.wap.wml";
                case "wmlc":
                    return "application/vnd.wap.wmlc";
                // WMLScript program
                case "wmls":
                    return "text/vnd.wap.wmlscript";
                case "wmlsc":
                    return "application/vnd.wap.wmlscriptc";
                // Windows Media video
                case "wmv":
                    return "video/x-ms-wmv";
                case "wmz":
                    return "application/x-ms-wmz";
                // WOFF font
                case "woff":
                    return "application/font-woff";
                // WordPerfect document
                case "wp":
                case "wp4":
                case "wp5":
                case "wp6":
                case "wpd":
                case "wpp":
                    return "application/vnd.wordperfect";
                // WordPerfect/Drawperfect image
                case "wpg":
                    return "application/x-wpg";
                // WPL playlist
                case "wpl":
                    return "application/vnd.ms-wpl";
                case "wqd":
                    return "application/vnd.wqd";
                // WRI document
                case "wri":
                    return "application/x-mswrite";
                case "wsdl":
                    return "application/wsdl+xml";
                case "wspolicy":
                    return "application/wspolicy+xml";
                case "wtb":
                    return "application/vnd.webturbo";
                // WavPack audio
                case "wv":
                case "wvp":
                    return "audio/x-wavpack";
                // WavPack audio correction file
                case "wvc":
                    return "audio/x-wavpack-correction";
                // WWF document
                case "wwf":
                    return "application/x-wwf";
                case "x3d":
                    return "application/vnd.hzn-3d-crossword";
                // Sigma X3F raw image
                case "x3f":
                    return "image/x-sigma-x3f";
                case "xap":
                    return "application/x-silverlight-app";
                // XAR archive
                case "xar":
                case "pkg":
                    return "application/x-xar";
                case "xbap":
                    return "application/x-ms-xbap";
                case "xbd":
                    return "application/vnd.fujixerox.docuworks.binder";
                // XBEL bookmarks
                case "xbel":
                    return "application/x-xbel";
                // XBM image
                case "xbm":
                    return "image/x-xbitmap";
                // GIMP image
                case "xcf":
                    return "image/x-xcf";
                // compressed GIMP image
                case "xcfgz":
                case "xcfbz2":
                    return "image/x-compressed-xcf";
                case "xdm":
                    return "application/vnd.syncml.dm+xml";
                case "xdp":
                    return "application/vnd.adobe.xdp+xml";
                case "xdw":
                    return "application/vnd.fujixerox.docuworks";
                case "xenc":
                    return "application/xenc+xml";
                case "xer":
                    return "application/patch-ops-error+xml";
                case "xfdf":
                    return "application/vnd.adobe.xfdf";
                case "xfdl":
                    return "application/vnd.xfdl";
                // XHTML page
                case "xhtml":
                case "xht":
                    return "application/xhtml+xml";
                // Scream Tracker instrument
                case "xi":
                    return "audio/x-xi";
                case "xif":
                    return "image/vnd.xiff";
                // Excel add-in
                case "xlam":
                    return "application/vnd.ms-excel.addin.macroenabled.12";
                // XLIFF translation file
                case "xlf":
                case "xliff":
                    return "application/x-xliff";
                // Excel spreadsheet
                case "xls":
                case "xlc":
                case "xll":
                case "xlm":
                case "xlw":
                case "xla":
                case "xlt":
                case "xld":
                case "xlb":
                    return "application/vnd.ms-excel";
                // Excel 2007 binary spreadsheet
                case "xlsb":
                    return "application/vnd.ms-excel.sheet.binary.macroenabled.12";
                // Excel spreadsheet
                case "xlsm":
                    return "application/vnd.ms-excel.sheet.macroenabled.12";
                // Excel 2007 spreadsheet
                case "xlsx":
                    return "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet";
                // Excel spreadsheet template
                case "xltm":
                    return "application/vnd.ms-excel.template.macroenabled.12";
                // Excel 2007 spreadsheet template
                case "xltx":
                    return "application/vnd.openxmlformats-officedocument.spreadsheetml.template";
                // FastTracker II audio
                case "xm":
                    return "audio/x-xm";
                // XMF audio
                case "xmf":
                    return "audio/x-xmf";
                // XMI file
                case "xmi":
                    return "text/x-xmi";
                // XML document
                case "xml":
                case "xbl":
                case "xsd":
                case "rng":
                case "xpdl":
                    return "application/xml";
                case "xo":
                    return "application/vnd.olpc-sugar";
                case "xop":
                    return "application/xop+xml";
                // XPInstall installer module
                case "xpi":
                    return "application/x-xpinstall";
                // XPM image
                case "xpm":
                    return "image/x-xpixmap";
                case "xpr":
                    return "application/vnd.is-xpr";
                case "xpw":
                case "xpx":
                    return "application/vnd.intercon.formnet";
                // XSLT stylesheet
                case "xsl":
                case "xslt":
                    return "application/xslt+xml";
                case "xsm":
                    return "application/vnd.syncml+xml";
                // XSPF playlist
                case "xspf":
                    return "application/xspf+xml";
                // XUL interface document
                case "xul":
                    return "application/vnd.mozilla.xul+xml";
                // X window image
                case "xwd":
                    return "image/x-xwindowdump";
                case "xyz":
                    return "chemical/x-xyz";
                // XZ archive
                case "xz":
                    return "application/x-xz";
                // YAML document
                case "yaml":
                case "yml":
                    return "application/x-yaml";
                // UNIX-compressed file
                case "z":
                    return "application/x-compress";
                case "zaz":
                    return "application/vnd.zzazz.deck+xml";
                // Zip archive
                case "zip":
                    return "application/zip";
                case "zir":
                case "zirz":
                    return "application/vnd.zul";
                case "zmm":
                    return "application/vnd.handheld-entertainment+xml";
                // Zoo archive
                case "zoo":
                    return "application/x-zoo";
                // Zlib archive
                case "zz":
                    return "application/zlib";
            }
            return "";
        }
    }
}