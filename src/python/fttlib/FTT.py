import os
from enum import Enum, unique, auto

#constants
applicationvndlotus123 = "application/vnd.lotus-1-2-3"
_123 = "123"
wk1 = "wk1"
wk3 = "wk3"
wk4 = "wk4"
wks = "wks"
applicationvnd1000mindsdecisionmodelxml = "application/vnd.1000minds.decision-model+xml"
_1km = "1km"
applicationxgenesis32xrom = "application/x-genesis-32x-rom"
_32x = "32x"
mdx = "mdx"
textvndin3d3dml = "text/vnd.in3d.3dml"
_3dml = "3dml"
imagex3ds = "image/x-3ds"
_3ds = "3ds"
video3gpp2 = "video/3gpp2"
_3g2 = "3g2"
_3gp2 = "3gp2"
_3gpp2 = "3gpp2"
video3gpp = "video/3gpp"
_3gp = "3gp"
_3gpp = "3gpp"
_3ga = "3ga"
model3mf = "model/3mf"
_3mf = "3mf"
applicationxt602 = "application/x-t602"
_602 = "602"
applicationx7zcompressed = "application/x-7z-compressed"
_7z = "7z"
applicationxarchive = "application/x-archive"
a = "a"
ar = "ar"
applicationxatari2600rom = "application/x-atari-2600-rom"
a26 = "a26"
applicationxatari7800rom = "application/x-atari-7800-rom"
a78 = "a78"
audioxpnaudibleaudio = "audio/x-pn-audibleaudio"
aa = "aa"
aax = "aax"
applicationxauthorwarebin = "application/x-authorware-bin"
aab = "aab"
x32 = "x32"
u32 = "u32"
vox = "vox"
audioaac = "audio/aac"
aac = "aac"
adts = "adts"
applicationxauthorwaremap = "application/x-authorware-map"
aam = "aam"
applicationxauthorwareseg = "application/x-authorware-seg"
aas = "aas"
applicationxabiword = "application/x-abiword"
abw = "abw"
abwcrashed = "abwcrashed"
abwgz = "abwgz"
zabw = "zabw"
applicationpkixattrcert = "application/pkix-attr-cert"
ac = "ac"
audioac3 = "audio/ac3"
ac3 = "ac3"
applicationvndamericandynamicsacc = "application/vnd.americandynamics.acc"
acc = "acc"
applicationxace = "application/x-ace"
ace = "ace"
applicationvndacucobol = "application/vnd.acucobol"
acu = "acu"
textxadasrc = "text/x-adasrc"
adb = "adb"
ads = "ads"
applicationxamigadiskformat = "application/x-amiga-disk-format"
adf = "adf"
audioadpcm = "audio/adpcm"
adp = "adp"
applicationvndaudiograph = "application/vnd.audiograph"
aep = "aep"
applicationxfontafm = "application/x-font-afm"
afm = "afm"
applicationvndibmmodcap = "application/vnd.ibm.modcap"
afp = "afp"
listafp = "listafp"
list3820 = "list3820"
imagexapplixgraphics = "image/x-applix-graphics"
ag = "ag"
applicationvndaheadspace = "application/vnd.ahead.space"
ahead = "ahead"
applicationillustrator = "application/illustrator"
ai = "ai"
audioxaifc = "audio/x-aifc"
aifc = "aifc"
aiffc = "aiffc"
audioxaiff = "audio/x-aiff"
aiff = "aiff"
aif = "aif"
applicationvndadobeairapplicationinstallerpackagezip = "application/vnd.adobe.air-application-installer-package+zip"
air = "air"
applicationvnddvbait = "application/vnd.dvb.ait"
ait = "ait"
applicationxalz = "application/x-alz"
alz = "alz"
applicationvndamigaami = "application/vnd.amiga.ami"
ami = "ami"
audioamr = "audio/amr"
amr = "amr"
audioxamzxml = "audio/x-amzxml"
amz = "amz"
applicationxnavianimation = "application/x-navi-animation"
ani = "ani"
videoxanim = "video/x-anim"
anim19j = "anim19j"
applicationannodex = "application/annodex"
anx = "anx"
audioxape = "audio/x-ape"
ape = "ape"
applicationvndandroidpackagearchive = "application/vnd.android.package-archive"
apk = "apk"
imageapng = "image/apng"
apng = "apng"
applicationxiso9660appimage = "application/x-iso9660-appimage"
appimage = "appimage"
applicationxmsapplication = "application/x-ms-application"
application = "application"
applicationvndlotusapproach = "application/vnd.lotus-approach"
apr = "apr"
applicationxfreearc = "application/x-freearc"
arc = "arc"
applicationxarj = "application/x-arj"
arj = "arj"
imagexsonyarw = "image/x-sony-arw"
arw = "arw"
applicationxapplixspreadsheet = "application/x-applix-spreadsheet"
_as = "as"
textxcommonlisp = "text/x-common-lisp"
asd = "asd"
fasl = "fasl"
lisp = "lisp"
ros = "ros"
applicationvndmsasf = "application/vnd.ms-asf"
asf = "asf"
applicationvndaccpacsimplyaso = "application/vnd.accpac.simply.aso"
aso = "aso"
applicationxasp = "application/x-asp"
asp = "asp"
audioxmsasx = "audio/x-ms-asx"
asx = "asx"
wax = "wax"
wvx = "wvx"
wmx = "wmx"
applicationvndacucorp = "application/vnd.acucorp"
atc = "atc"
acutc = "acutc"
applicationatomxml = "application/atom+xml"
atom = "atom"
applicationatomcatxml = "application/atomcat+xml"
atomcat = "atomcat"
applicationatomdeletedxml = "application/atomdeleted+xml"
atomdeleted = "atomdeleted"
applicationatomsvcxml = "application/atomsvc+xml"
atomsvc = "atomsvc"
applicationvndantixgamecomponent = "application/vnd.antix.game-component"
atx = "atx"
audiobasic = "audio/basic"
au = "au"
snd = "snd"
textxauthors = "text/x-authors"
authors = "authors"
textxsystemdunit = "text/x-systemd-unit"
automount = "automount"
device = "device"
mount = "mount"
path = "path"
scope = "scope"
slice = "slice"
socket = "socket"
swap = "swap"
target = "target"
timer = "timer"
videoxmsvideo = "video/x-msvideo"
avi = "avi"
avf = "avf"
divx = "divx"
imageavif = "image/avif"
avif = "avif"
imageavifsequence = "image/avif-sequence"
avifs = "avifs"
applicationxapplixword = "application/x-applix-word"
aw = "aw"
audioamrwb = "audio/amr-wb"
awb = "awb"
applicationxawk = "application/x-awk"
awk = "awk"
audioannodex = "audio/annodex"
axa = "axa"
videoannodex = "video/annodex"
axv = "axv"
applicationvndairzipfilesecureazf = "application/vnd.airzip.filesecure.azf"
azf = "azf"
applicationvndairzipfilesecureazs = "application/vnd.airzip.filesecure.azs"
azs = "azs"
imagevndairzipacceleratorazv = "image/vnd.airzip.accelerator.azv"
azv = "azv"
applicationvndamazonebook = "application/vnd.amazon.ebook"
azw = "azw"
applicationvndamazonmobi8ebook = "application/vnd.amazon.mobi8-ebook"
azw3 = "azw3"
kfx = "kfx"
applicationxtrash = "application/x-trash"
bak = "bak"
old = "old"
sik = "sik"
applicationxbcpio = "application/x-bcpio"
bcpio = "bcpio"
applicationxfontbdf = "application/x-font-bdf"
bdf = "bdf"
applicationbdoc = "application/bdoc"
bdoc = "bdoc"
applicationvndrealvncbed = "application/vnd.realvnc.bed"
bed = "bed"
applicationvndfujitsuoasysprs = "application/vnd.fujitsu.oasysprs"
bh2 = "bh2"
textxbibtex = "text/x-bibtex"
bib = "bib"
applicationoctetstream = "application/octet-stream"
bin = "bin"
dms = "dms"
lrf = "lrf"
mar = "mar"
dist = "dist"
distz = "distz"
bpk = "bpk"
dump = "dump"
elc = "elc"
deploy = "deploy"
dll = "dll"
msp = "msp"
msm = "msm"
buffer = "buffer"
applicationxblorb = "application/x-blorb"
blb = "blb"
blorb = "blorb"
applicationxblender = "application/x-blender"
blender = "blender"
blend = "blend"
applicationvndbmi = "application/vnd.bmi"
bmi = "bmi"
applicationvndbalsamiqbmmlxml = "application/vnd.balsamiq.bmml+xml"
bmml = "bmml"
imagebmp = "image/bmp"
bmp = "bmp"
dib = "dib"
applicationvndpreviewsystemsbox = "application/vnd.previewsystems.box"
box = "box"
applicationxbzip2 = "application/x-bzip2"
boz = "boz"
applicationxbpspatch = "application/x-bps-patch"
bps = "bps"
applicationxbsdiff = "application/x-bsdiff"
bsdiff = "bsdiff"
modelvndvalvesourcecompiledmap = "model/vnd.valve.source.compiled-map"
bsp = "bsp"
imageprsbtif = "image/prs.btif"
btif = "btif"
applicationxbzip = "application/x-bzip"
bz2 = "bz2"
bz = "bz"
applicationvndcluetrustcartomobileconfig = "application/vnd.cluetrust.cartomobile-config"
c11amc = "c11amc"
applicationvndcluetrustcartomobileconfigpkg = "application/vnd.cluetrust.cartomobile-config-pkg"
c11amz = "c11amz"
applicationvndclonkc4group = "application/vnd.clonk.c4group"
c4g = "c4g"
c4d = "c4d"
c4f = "c4f"
c4p = "c4p"
c4u = "c4u"
applicationvndmscabcompressed = "application/vnd.ms-cab-compressed"
cab = "cab"
audioxcaf = "audio/x-caf"
caf = "caf"
applicationvndcurlcar = "application/vnd.curl.car"
car = "car"
applicationvndmspkiseccat = "application/vnd.ms-pki.seccat"
cat = "cat"
applicationxcb7 = "application/x-cb7"
cb7 = "cb7"
applicationxcbr = "application/x-cbr"
cba = "cba"
textxcobol = "text/x-cobol"
cbl = "cbl"
cob = "cob"
applicationvndcomicbookrar = "application/vnd.comicbook-rar"
cbr = "cbr"
applicationxcbt = "application/x-cbt"
cbt = "cbt"
applicationvndcomicbookzip = "application/vnd.comicbook+zip"
cbz = "cbz"
applicationxccmx = "application/x-ccmx"
ccmx = "ccmx"
applicationxcocoa = "application/x-cocoa"
cco = "cco"
applicationccxmlxml = "application/ccxml+xml"
ccxml = "ccxml"
applicationvndcontactcmsg = "application/vnd.contact.cmsg"
cdbcmsg = "cdbcmsg"
applicationxnetcdf = "application/x-netcdf"
cdf = "cdf"
nc = "nc"
applicationcdfxxml = "application/cdfx+xml"
cdfx = "cdfx"
applicationvndmediastationcdkey = "application/vnd.mediastation.cdkey"
cdkey = "cdkey"
applicationcdmicapability = "application/cdmi-capability"
cdmia = "cdmia"
applicationcdmicontainer = "application/cdmi-container"
cdmic = "cdmic"
applicationcdmidomain = "application/cdmi-domain"
cdmid = "cdmid"
applicationcdmiobject = "application/cdmi-object"
cdmio = "cdmio"
applicationcdmiqueue = "application/cdmi-queue"
cdmiq = "cdmiq"
applicationvndcoreldraw = "application/vnd.corel-draw"
cdr = "cdr"
chemicalxcdx = "chemical/x-cdx"
cdx = "cdx"
applicationvndchemdrawxml = "application/vnd.chemdraw+xml"
cdxml = "cdxml"
applicationvndcinderella = "application/vnd.cinderella"
cdy = "cdy"
applicationpkixcert = "application/pkix-cert"
cer = "cer"
applicationxcfscompressed = "application/x-cfs-compressed"
cfs = "cfs"
imagecgm = "image/cgm"
cgm = "cgm"
textxchangelog = "text/x-changelog"
changelog = "changelog"
applicationxchat = "application/x-chat"
chat = "chat"
applicationvndmshtmlhelp = "application/vnd.ms-htmlhelp"
chm = "chm"
applicationxkchart = "application/x-kchart"
chrt = "chrt"
chemicalxcif = "chemical/x-cif"
cif = "cif"
applicationvndanserwebcertificateissueinitiation = "application/vnd.anser-web-certificate-issue-initiation"
cii = "cii"
applicationvndmsartgalry = "application/vnd.ms-artgalry"
cil = "cil"
applicationnode = "application/node"
cjs = "cjs"
textxopenclsrc = "text/x-opencl-src"
cl = "cl"
applicationvndclaymore = "application/vnd.claymore"
cla = "cla"
applicationxjava = "application/x-java"
_class = "class"
applicationvndcrickclickerkeyboard = "application/vnd.crick.clicker.keyboard"
clkk = "clkk"
applicationvndcrickclickerpalette = "application/vnd.crick.clicker.palette"
clkp = "clkp"
applicationvndcrickclickertemplate = "application/vnd.crick.clicker.template"
clkt = "clkt"
applicationvndcrickclickerwordbank = "application/vnd.crick.clicker.wordbank"
clkw = "clkw"
applicationvndcrickclicker = "application/vnd.crick.clicker"
clkx = "clkx"
applicationxmsclip = "application/x-msclip"
clp = "clp"
textxcmake = "text/x-cmake"
cmake = "cmake"
cmakeliststxt = "cmakeliststxt"
applicationvndcosmocaller = "application/vnd.cosmocaller"
cmc = "cmc"
chemicalxcmdf = "chemical/x-cmdf"
cmdf = "cmdf"
chemicalxcml = "chemical/x-cml"
cml = "cml"
applicationvndyellowrivercustommenu = "application/vnd.yellowriver-custom-menu"
cmp = "cmp"
imagexcmx = "image/x-cmx"
cmx = "cmx"
applicationvndrimcod = "application/vnd.rim.cod"
cod = "cod"
applicationvndcoffeescript = "application/vnd.coffeescript"
coffee = "coffee"
applicationxmsdownload = "application/x-msdownload"
com = "com"
bat = "bat"
textxcopying = "text/x-copying"
copying = "copying"
applicationxcore = "application/x-core"
core = "core"
applicationxcpio = "application/x-cpio"
cpio = "cpio"
applicationxcpiocompressed = "application/x-cpio-compressed"
cpiogz = "cpiogz"
textxcsrc = "text/x-c++src"
cpp = "cpp"
cxx = "cxx"
cc = "cc"
c = "c"
applicationmaccompactpro = "application/mac-compactpro"
cpt = "cpt"
imagexcanoncr2 = "image/x-canon-cr2"
cr2 = "cr2"
applicationxmscardfile = "application/x-mscardfile"
crd = "crd"
textxcredits = "text/x-credits"
credits = "credits"
applicationpkixcrl = "application/pkix-crl"
crl = "crl"
imagexcanoncrw = "image/x-canon-crw"
crw = "crw"
applicationxchromeextension = "application/x-chrome-extension"
crx = "crx"
applicationvndrigcryptonote = "application/vnd.rig.cryptonote"
cryptonote = "cryptonote"
textxcsharp = "text/x-csharp"
cs = "cs"
applicationxcsh = "application/x-csh"
csh = "csh"
applicationvndcitationstylesstylexml = "application/vnd.citationstyles.style+xml"
csl = "csl"
chemicalxcsml = "chemical/x-csml"
csml = "csml"
applicationvndcommonspace = "application/vnd.commonspace"
csp = "csp"
textcss = "text/css"
css = "css"
textcsv = "text/csv"
csv = "csv"
textcsvschema = "text/csv-schema"
csvs = "csvs"
applicationcuseeme = "application/cu-seeme"
cu = "cu"
applicationxcue = "application/x-cue"
cue = "cue"
imagexwinbitmap = "image/x-win-bitmap"
cur = "cur"
textvndcurl = "text/vnd.curl"
curl = "curl"
applicationxappleworksdocument = "application/x-appleworks-document"
cwk = "cwk"
applicationprscww = "application/prs.cww"
cww = "cww"
textxdsrc = "text/x-dsrc"
d = "d"
di = "di"
modelvndcolladaxml = "model/vnd.collada+xml"
dae = "dae"
applicationvndmobiusdaf = "application/vnd.mobius.daf"
daf = "daf"
applicationxdar = "application/x-dar"
dar = "dar"
applicationvnddart = "application/vnd.dart"
dart = "dart"
applicationdavmountxml = "application/davmount+xml"
davmount = "davmount"
applicationxdbf = "application/x-dbf"
dbf = "dbf"
applicationxdocbookxml = "application/x-docbook+xml"
dbk = "dbk"
docbook = "docbook"
applicationxdcrom = "application/x-dc-rom"
dc = "dc"
textxdcl = "text/x-dcl"
dcl = "dcl"
imagexkodakdcr = "image/x-kodak-dcr"
dcr = "dcr"
textvndcurldcurl = "text/vnd.curl.dcurl"
dcurl = "dcurl"
applicationvndomadd2xml = "application/vnd.oma.dd2+xml"
dd2 = "dd2"
applicationvndfujixeroxddd = "application/vnd.fujixerox.ddd"
ddd = "ddd"
applicationvndsyncmldmddfxml = "application/vnd.syncml.dmddf+xml"
ddf = "ddf"
imagexdds = "image/x-dds"
dds = "dds"
applicationvnddebianbinarypackage = "application/vnd.debian.binary-package"
deb = "deb"
udeb = "udeb"
applicationxx509cacert = "application/x-x509-ca-cert"
der = "der"
crt = "crt"
cert = "cert"
pem = "pem"
applicationxdesktop = "application/x-desktop"
desktop = "desktop"
kdelnk = "kdelnk"
applicationvnddreamfactory = "application/vnd.dreamfactory"
dfac = "dfac"
applicationxdgccompressed = "application/x-dgc-compressed"
dgc = "dgc"
applicationxdiadiagram = "application/x-dia-diagram"
dia = "dia"
textxc = "text/x-c"
dic = "dic"
applicationdicom = "application/dicom"
dicomdir = "dicomdir"
dcm = "dcm"
textxpatch = "text/x-patch"
diff = "diff"
patch = "patch"
applicationxdirector = "application/x-director"
dir = "dir"
dxr = "dxr"
cst = "cst"
cct = "cct"
cxt = "cxt"
w3d = "w3d"
fgd = "fgd"
swa = "swa"
applicationvndmobiusdis = "application/vnd.mobius.dis"
dis = "dis"
messagedispositionnotification = "message/disposition-notification"
dispositionnotification = "disposition-notification"
imagevnddjvu = "image/vnd.djvu"
djvu = "djvu"
djv = "djv"
applicationxapplediskimage = "application/x-apple-diskimage"
dmg = "dmg"
applicationvnddna = "application/vnd.dna"
dna = "dna"
imagexadobedng = "image/x-adobe-dng"
dng = "dng"
applicationmsword = "application/msword"
doc = "doc"
applicationvndmsworddocumentmacroenabled12 = "application/vnd.ms-word.document.macroenabled.12"
docm = "docm"
applicationvndopenxmlformatsofficedocumentwordprocessingmldocument = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
docx = "docx"
applicationmswordtemplate = "application/msword-template"
dot = "dot"
applicationvndmswordtemplatemacroenabled12 = "application/vnd.ms-word.template.macroenabled.12"
dotm = "dotm"
applicationvndopenxmlformatsofficedocumentwordprocessingmltemplate = "application/vnd.openxmlformats-officedocument.wordprocessingml.template"
dotx = "dotx"
applicationvndosgidp = "application/vnd.osgi.dp"
dp = "dp"
applicationvnddpgraph = "application/vnd.dpgraph"
dpg = "dpg"
audiovnddra = "audio/vnd.dra"
dra = "dra"
imagedicomrle = "image/dicom-rle"
drle = "drle"
textprslinestag = "text/prs.lines.tag"
dsc = "dsc"
textxdsl = "text/x-dsl"
dsl = "dsl"
applicationdsscder = "application/dssc+der"
dssc = "dssc"
applicationxdtbookxml = "application/x-dtbook+xml"
dtb = "dtb"
applicationxmldtd = "application/xml-dtd"
dtd = "dtd"
audiovnddts = "audio/vnd.dts"
dts = "dts"
audiovnddtshd = "audio/vnd.dts.hd"
dtshd = "dtshd"
videodv = "video/dv"
dv = "dv"
videovnddvbfile = "video/vnd.dvb.file"
dvb = "dvb"
applicationxdvi = "application/x-dvi"
dvi = "dvi"
applicationxbzdvi = "application/x-bzdvi"
dvibz2 = "dvibz2"
applicationxgzdvi = "application/x-gzdvi"
dvigz = "dvigz"
applicationatscdwdxml = "application/atsc-dwd+xml"
dwd = "dwd"
modelvnddwf = "model/vnd.dwf"
dwf = "dwf"
imagevnddwg = "image/vnd.dwg"
dwg = "dwg"
imagevnddxf = "image/vnd.dxf"
dxf = "dxf"
applicationvndspotfiredxp = "application/vnd.spotfire.dxp"
dxp = "dxp"
textxeiffel = "text/x-eiffel"
e = "e"
eif = "eif"
audiovndnueraecelp4800 = "audio/vnd.nuera.ecelp4800"
ecelp4800 = "ecelp4800"
audiovndnueraecelp7470 = "audio/vnd.nuera.ecelp7470"
ecelp7470 = "ecelp7470"
audiovndnueraecelp9600 = "audio/vnd.nuera.ecelp9600"
ecelp9600 = "ecelp9600"
applicationvndnovadigmedm = "application/vnd.novadigm.edm"
edm = "edm"
applicationvndnovadigmedx = "application/vnd.novadigm.edx"
edx = "edx"
applicationvndpicsel = "application/vnd.picsel"
efif = "efif"
applicationxegon = "application/x-egon"
egon = "egon"
applicationvndpgosasli = "application/vnd.pg.osasli"
ei6 = "ei6"
textxemacslisp = "text/x-emacs-lisp"
el = "el"
imageemf = "image/emf"
emf = "emf"
messagerfc822 = "message/rfc822"
eml = "eml"
mime = "mime"
applicationemmaxml = "application/emma+xml"
emma = "emma"
applicationemotionmlxml = "application/emotionml+xml"
emotionml = "emotionml"
applicationvndemusicemusicpackage = "application/vnd.emusic-emusic_package"
emp = "emp"
applicationxmsmetafile = "application/x-msmetafile"
emz = "emz"
applicationxmlexternalparsedentity = "application/xml-external-parsed-entity"
ent = "ent"
audiovnddigitalwinds = "audio/vnd.digital-winds"
eol = "eol"
applicationvndmsfontobject = "application/vnd.ms-fontobject"
eot = "eot"
imagexeps = "image/x-eps"
eps = "eps"
epsi = "epsi"
epsf = "epsf"
imagexbzeps = "image/x-bzeps"
epsbz2 = "epsbz2"
epsibz2 = "epsibz2"
epsfbz2 = "epsfbz2"
imagexgzeps = "image/x-gzeps"
epsgz = "epsgz"
epsigz = "epsigz"
epsfgz = "epsfgz"
applicationepubzip = "application/epub+zip"
epub = "epub"
textxerlang = "text/x-erlang"
erl = "erl"
applicationecmascript = "application/ecmascript"
es = "es"
ecma = "ecma"
applicationvndeszigno3xml = "application/vnd.eszigno3+xml"
es3 = "es3"
et3 = "et3"
applicationvndosgisubsystem = "application/vnd.osgi.subsystem"
esa = "esa"
applicationvndepsonesf = "application/vnd.epson.esf"
esf = "esf"
applicationxetheme = "application/x-e-theme"
etheme = "etheme"
textxsetext = "text/x-setext"
etx = "etx"
applicationxeva = "application/x-eva"
eva = "eva"
applicationxenvoy = "application/x-envoy"
evy = "evy"
applicationxmsdosexecutable = "application/x-ms-dos-executable"
exe = "exe"
applicationexi = "application/exi"
exi = "exi"
imagexexr = "image/x-exr"
exr = "exr"
applicationvndnovadigmext = "application/vnd.novadigm.ext"
ext = "ext"
applicationandrewinset = "application/andrew-inset"
ez = "ez"
applicationvndezpixalbum = "application/vnd.ezpix-album"
ez2 = "ez2"
applicationvndezpixpackage = "application/vnd.ezpix-package"
ez3 = "ez3"
textxfortran = "text/x-fortran"
f = "f"
f90 = "f90"
f95 = "f95"
_for = "for"
f77 = "f77"
applicationxfictionbookxml = "application/x-fictionbook+xml"
fb2 = "fb2"
applicationxzipcompressedfb2 = "application/x-zip-compressed-fb2"
fb2zip = "fb2zip"
imagevndfastbidsheet = "image/vnd.fastbidsheet"
fbs = "fbs"
applicationvndadobeformscentralfcdt = "application/vnd.adobe.formscentral.fcdt"
fcdt = "fcdt"
applicationvndisacfcs = "application/vnd.isac.fcs"
fcs = "fcs"
applicationxrawfloppydiskimage = "application/x-raw-floppy-disk-image"
fd = "fd"
qd = "qd"
applicationvndfdf = "application/vnd.fdf"
fdf = "fdf"
applicationxfdsdisk = "application/x-fds-disk"
fds = "fds"
applicationfdtxml = "application/fdt+xml"
fdt = "fdt"
applicationvnddenovofcselayoutlink = "application/vnd.denovo.fcselayout-link"
felaunch = "fe_launch"
textxgherkin = "text/x-gherkin"
feature = "feature"
applicationvndfujitsuoasysgp = "application/vnd.fujitsu.oasysgp"
fg5 = "fg5"
imagexfreehand = "image/x-freehand"
fh = "fh"
fhc = "fhc"
fh4 = "fh4"
fh5 = "fh5"
fh7 = "fh7"
imagexxfig = "image/x-xfig"
fig = "fig"
imagefits = "image/fits"
fits = "fits"
applicationxfluid = "application/x-fluid"
fl = "fl"
audioflac = "audio/flac"
flac = "flac"
applicationvndflatpak = "application/vnd.flatpak"
flatpak = "flatpak"
xdgapp = "xdgapp"
applicationvndflatpakref = "application/vnd.flatpak.ref"
flatpakref = "flatpakref"
applicationvndflatpakrepo = "application/vnd.flatpak.repo"
flatpakrepo = "flatpakrepo"
videoxflic = "video/x-flic"
fli = "fli"
flc = "flc"
applicationvndmicrografxflo = "application/vnd.micrografx.flo"
flo = "flo"
videoxflv = "video/x-flv"
flv = "flv"
applicationxkivio = "application/x-kivio"
flw = "flw"
textvndfmiflexstor = "text/vnd.fmi.flexstor"
flx = "flx"
textvndfly = "text/vnd.fly"
fly = "fly"
applicationvndframemaker = "application/vnd.framemaker"
fm = "fm"
frame = "frame"
maker = "maker"
book = "book"
applicationvndfrogansfnc = "application/vnd.frogans.fnc"
fnc = "fnc"
textxxslfo = "text/x-xslfo"
fo = "fo"
xslfo = "xslfo"
applicationvndoasisopendocumentgraphicsflatxml = "application/vnd.oasis.opendocument.graphics-flat-xml"
fodg = "fodg"
applicationvndoasisopendocumentpresentationflatxml = "application/vnd.oasis.opendocument.presentation-flat-xml"
fodp = "fodp"
applicationvndoasisopendocumentspreadsheetflatxml = "application/vnd.oasis.opendocument.spreadsheet-flat-xml"
fods = "fods"
applicationvndoasisopendocumenttextflatxml = "application/vnd.oasis.opendocument.text-flat-xml"
fodt = "fodt"
imagevndfpx = "image/vnd.fpx"
fpx = "fpx"
applicationvndfscweblaunch = "application/vnd.fsc.weblaunch"
fsc = "fsc"
imagevndfst = "image/vnd.fst"
fst = "fst"
applicationvndfluxtimeclip = "application/vnd.fluxtime.clip"
ftc = "ftc"
applicationvndanserwebfundstransferinitiation = "application/vnd.anser-web-funds-transfer-initiation"
fti = "fti"
videovndfvt = "video/vnd.fvt"
fvt = "fvt"
videoxjavafx = "video/x-javafx"
fxm = "fxm"
applicationvndadobefxp = "application/vnd.adobe.fxp"
fxp = "fxp"
fxpl = "fxpl"
applicationvndfuzzysheet = "application/vnd.fuzzysheet"
fzs = "fzs"
applicationvndgeoplan = "application/vnd.geoplan"
g2w = "g2w"
imagefaxg3 = "image/fax-g3"
g3 = "g3"
applicationvndgeospace = "application/vnd.geospace"
g3w = "g3w"
applicationvndgrooveaccount = "application/vnd.groove-account"
gac = "gac"
applicationxtads = "application/x-tads"
gam = "gam"
applicationxgameboyrom = "application/x-gameboy-rom"
gb = "gb"
sgb = "sgb"
applicationxgbarom = "application/x-gba-rom"
gba = "gba"
agb = "agb"
applicationxgameboycolorrom = "application/x-gameboy-color-rom"
gbc = "gbc"
cgb = "cgb"
imagexgimpgbr = "image/x-gimp-gbr"
gbr = "gbr"
applicationxgcacompressed = "application/x-gca-compressed"
gca = "gca"
textxgcode = "text/x.gcode"
gcode = "gcode"
modelvndgdl = "model/vnd.gdl"
gdl = "gdl"
applicationvndgoogleappsdocument = "application/vnd.google-apps.document"
gdoc = "gdoc"
applicationxgedcom = "application/x-gedcom"
ged = "ged"
gedcom = "gedcom"
applicationxgenesisrom = "application/x-genesis-rom"
gen = "gen"
sgd = "sgd"
applicationvnddynageo = "application/vnd.dynageo"
geo = "geo"
applicationgeojson = "application/geo+json"
geojson = "geojson"
applicationvndgeometryexplorer = "application/vnd.geometry-explorer"
gex = "gex"
gre = "gre"
applicationxtexgf = "application/x-tex-gf"
gf = "gf"
applicationxgamegearrom = "application/x-gamegear-rom"
gg = "gg"
applicationvndgeogebrafile = "application/vnd.geogebra.file"
ggb = "ggb"
applicationvndgeogebratool = "application/vnd.geogebra.tool"
ggt = "ggt"
applicationvndgroovehelp = "application/vnd.groove-help"
ghf = "ghf"
imagegif = "image/gif"
gif = "gif"
imagexgimpgih = "image/x-gimp-gih"
gih = "gih"
applicationvndgrooveidentitymessage = "application/vnd.groove-identity-message"
gim = "gim"
applicationxglade = "application/x-glade"
glade = "glade"
modelgltfbinary = "model/gltf-binary"
glb = "glb"
modelgltfjson = "model/gltf+json"
gltf = "gltf"
applicationgmlxml = "application/gml+xml"
gml = "gml"
applicationxgettexttranslation = "application/x-gettext-translation"
gmo = "gmo"
mo = "mo"
applicationxprofile = "application/x-profile"
gmonout = "gmonout"
applicationvndgmx = "application/vnd.gmx"
gmx = "gmx"
applicationgnunetdirectory = "application/gnunet-directory"
gnd = "gnd"
applicationxgnucash = "application/x-gnucash"
gnucash = "gnucash"
gnc = "gnc"
xac = "xac"
applicationxgnumeric = "application/x-gnumeric"
gnumeric = "gnumeric"
textxgo = "text/x-go"
go = "go"
applicationxgnuplot = "application/x-gnuplot"
gp = "gp"
gplt = "gplt"
gnuplot = "gnuplot"
applicationvndflographit = "application/vnd.flographit"
gph = "gph"
applicationgpxxml = "application/gpx+xml"
gpx = "gpx"
applicationvndgrafeq = "application/vnd.grafeq"
gqf = "gqf"
gqs = "gqs"
applicationxgraphite = "application/x-graphite"
gra = "gra"
textxgradle = "text/x-gradle"
gradle = "gradle"
applicationsrgs = "application/srgs"
gram = "gram"
applicationxgrampsxml = "application/x-gramps-xml"
gramps = "gramps"
textxgroovy = "text/x-groovy"
groovy = "groovy"
gvy = "gvy"
gy = "gy"
gsh = "gsh"
applicationvndgrooveinjector = "application/vnd.groove-injector"
grv = "grv"
applicationsrgsxml = "application/srgs+xml"
grxml = "grxml"
textxgenie = "text/x-genie"
gs = "gs"
applicationvndgoogleappsspreadsheet = "application/vnd.google-apps.spreadsheet"
gsheet = "gsheet"
applicationvndgoogleappspresentation = "application/vnd.google-apps.presentation"
gslides = "gslides"
audioxgsm = "audio/x-gsm"
gsm = "gsm"
applicationvndgroovetoolmessage = "application/vnd.groove-tool-message"
gtm = "gtm"
modelvndgtw = "model/vnd.gtw"
gtw = "gtw"
textvndgraphviz = "text/vnd.graphviz"
gv = "gv"
textxgooglevideopointer = "text/x-google-video-pointer"
gvp = "gvp"
applicationgxf = "application/gxf"
gxf = "gxf"
applicationvndgeonext = "application/vnd.geonext"
gxt = "gxt"
applicationgzip = "application/gzip"
gz = "gz"
videoh261 = "video/h261"
h261 = "h261"
videoh263 = "video/h263"
h263 = "h263"
videoh264 = "video/h264"
h264 = "h264"
applicationvndhalxml = "application/vnd.hal+xml"
hal = "hal"
applicationvndhbci = "application/vnd.hbci"
hbci = "hbci"
textxhandlebarstemplate = "text/x-handlebars-template"
hbs = "hbs"
applicationxvirtualboxhdd = "application/x-virtualbox-hdd"
hdd = "hdd"
applicationxhdf = "application/x-hdf"
hdf = "hdf"
hdf4 = "hdf4"
h4 = "h4"
hdf5 = "hdf5"
h5 = "h5"
imageheif = "image/heif"
heic = "heic"
heif = "heif"
imageheicsequence = "image/heic-sequence"
heics = "heics"
imageheifsequence = "image/heif-sequence"
heifs = "heifs"
imagehej2k = "image/hej2k"
hej2 = "hej2"
applicationatscheldxml = "application/atsc-held+xml"
held = "held"
applicationxhfefloppyimage = "application/x-hfe-floppy-image"
hfe = "hfe"
textxchdr = "text/x-c++hdr"
hh = "hh"
hp = "hp"
hpp = "hpp"
h = "h"
hxx = "hxx"
applicationhjson = "application/hjson"
hjson = "hjson"
applicationwinhlp = "application/winhlp"
hlp = "hlp"
applicationvndhphpgl = "application/vnd.hp-hpgl"
hpgl = "hpgl"
applicationvndhphpid = "application/vnd.hp-hpid"
hpid = "hpid"
applicationvndhphps = "application/vnd.hp-hps"
hps = "hps"
applicationmacbinhex40 = "application/mac-binhex40"
hqx = "hqx"
textxhaskell = "text/x-haskell"
hs = "hs"
imagehsj2 = "image/hsj2"
hsj2 = "hsj2"
textxcomponent = "text/x-component"
htc = "htc"
applicationvndkenameaapp = "application/vnd.kenameaapp"
htke = "htke"
applicationvndyamahahvdic = "application/vnd.yamaha.hv-dic"
hvd = "hvd"
applicationvndyamahahvvoice = "application/vnd.yamaha.hv-voice"
hvp = "hvp"
applicationvndyamahahvscript = "application/vnd.yamaha.hv-script"
hvs = "hvs"
applicationxhwp = "application/x-hwp"
hwp = "hwp"
applicationxhwt = "application/x-hwt"
hwt = "hwt"
applicationvndintergeo = "application/vnd.intergeo"
i2g = "i2g"
applicationxica = "application/x-ica"
ica = "ica"
applicationvndiccprofile = "application/vnd.iccprofile"
icc = "icc"
icm = "icm"
xconferencexcooltalk = "x-conference/x-cooltalk"
ice = "ice"
imagexicns = "image/x-icns"
icns = "icns"
imagevndmicrosofticon = "image/vnd.microsoft.icon"
ico = "ico"
textxidl = "text/x-idl"
idl = "idl"
imageief = "image/ief"
ief = "ief"
imagexilbm = "image/x-ilbm"
iff = "iff"
ilbm = "ilbm"
lbm = "lbm"
applicationvndshanainformedformdata = "application/vnd.shana.informed.formdata"
ifm = "ifm"
applicationvndigloader = "application/vnd.igloader"
igl = "igl"
applicationvndinsorsigm = "application/vnd.insors.igm"
igm = "igm"
modeliges = "model/iges"
igs = "igs"
iges = "iges"
applicationvndmicrografxigx = "application/vnd.micrografx.igx"
igx = "igx"
applicationvndshanainformedinterchange = "application/vnd.shana.informed.interchange"
iif = "iif"
applicationvndaccpacsimplyimp = "application/vnd.accpac.simply.imp"
imp = "imp"
applicationvndmsims = "application/vnd.ms-ims"
ims = "ims"
textximelody = "text/x-imelody"
imy = "imy"
ime = "ime"
applicationinkmlxml = "application/inkml+xml"
ink = "ink"
inkml = "inkml"
textxinstall = "text/x-install"
install = "install"
applicationvndastraeasoftwareiota = "application/vnd.astraea-software.iota"
iota = "iota"
applicationipfix = "application/ipfix"
ipfix = "ipfix"
applicationvndshanainformedpackage = "application/vnd.shana.informed.package"
ipk = "ipk"
applicationxipspatch = "application/x-ips-patch"
ips = "ips"
textxiptables = "text/x-iptables"
iptables = "iptables"
applicationxipynbjson = "application/x-ipynb+json"
ipynb = "ipynb"
applicationvndibmrightsmanagement = "application/vnd.ibm.rights-management"
irm = "irm"
applicationvndirepositorypackagexml = "application/vnd.irepository.package+xml"
irp = "irp"
applicationxcdimage = "application/x-cd-image"
iso = "iso"
iso9660 = "iso9660"
audioxit = "audio/x-it"
it = "it"
applicationxit87 = "application/x-it87"
it87 = "it87"
applicationvndshanainformedformtemplate = "application/vnd.shana.informed.formtemplate"
itp = "itp"
applicationitsxml = "application/its+xml"
its = "its"
applicationvndimmervisionivp = "application/vnd.immervision-ivp"
ivp = "ivp"
applicationvndimmervisionivu = "application/vnd.immervision-ivu"
ivu = "ivu"
imagexjp2codestream = "image/x-jp2-codestream"
j2c = "j2c"
j2k = "j2k"
jpc = "jpc"
textvndsunj2meappdescriptor = "text/vnd.sun.j2me.app-descriptor"
jad = "jad"
textjade = "text/jade"
jade = "jade"
applicationvndjam = "application/vnd.jam"
jam = "jam"
applicationxjavaarchive = "application/x-java-archive"
jar = "jar"
applicationxjavaarchivediff = "application/x-java-archive-diff"
jardiff = "jardiff"
textxjava = "text/x-java"
java = "java"
applicationxjavajcekeystore = "application/x-java-jce-keystore"
jceks = "jceks"
imagejphc = "image/jphc"
jhc = "jhc"
applicationvndjisp = "application/vnd.jisp"
jisp = "jisp"
applicationxjavakeystore = "application/x-java-keystore"
jks = "jks"
ks = "ks"
cacerts = "cacerts"
imagejls = "image/jls"
jls = "jls"
applicationvndhpjlyt = "application/vnd.hp-jlyt"
jlt = "jlt"
imagexjng = "image/x-jng"
jng = "jng"
applicationxjavajnlpfile = "application/x-java-jnlp-file"
jnlp = "jnlp"
applicationvndjoostjodaarchive = "application/vnd.joost.joda-archive"
joda = "joda"
imagejp2 = "image/jp2"
jp2 = "jp2"
jpg2 = "jpg2"
imagejpx = "image/jpx"
jpf = "jpf"
imagejpeg = "image/jpeg"
jpg = "jpg"
jpeg = "jpeg"
jpe = "jpe"
videojpeg = "video/jpeg"
jpgv = "jpgv"
imagejph = "image/jph"
jph = "jph"
imagejpm = "image/jpm"
jpm = "jpm"
jpgm = "jpgm"
applicationxjbuilderproject = "application/x-jbuilder-project"
jpr = "jpr"
jpx = "jpx"
applicationjrdjson = "application/jrd+json"
jrd = "jrd"
applicationjavascript = "application/javascript"
js = "js"
jsm = "jsm"
mjs = "mjs"
applicationjson = "application/json"
json = "json"
map = "map"
applicationjson5 = "application/json5"
json5 = "json5"
applicationldjson = "application/ld+json"
jsonld = "jsonld"
applicationjsonmljson = "application/jsonml+json"
jsonml = "jsonml"
applicationjsonpatchjson = "application/json-patch+json"
jsonpatch = "jsonpatch"
textjsx = "text/jsx"
jsx = "jsx"
imagejxr = "image/jxr"
jxr = "jxr"
imagejxra = "image/jxra"
jxra = "jxra"
imagejxrs = "image/jxrs"
jxrs = "jxrs"
imagejxs = "image/jxs"
jxs = "jxs"
imagejxsc = "image/jxsc"
jxsc = "jxsc"
imagejxsi = "image/jxsi"
jxsi = "jxsi"
imagejxss = "image/jxss"
jxss = "jxss"
imagexkodakk25 = "image/x-kodak-k25"
k25 = "k25"
applicationxthomsoncassette = "application/x-thomson-cassette"
k7 = "k7"
applicationxkarbon = "application/x-karbon"
karbon = "karbon"
applicationxkeepass2 = "application/x-keepass2"
kdbx = "kdbx"
imagexkodakkdc = "image/x-kodak-kdc"
kdc = "kdc"
applicationxkexiprojectsqlite2 = "application/x-kexiproject-sqlite2"
kexi = "kexi"
applicationxkexiconnectiondata = "application/x-kexi-connectiondata"
kexic = "kexic"
applicationxkexiprojectshortcut = "application/x-kexiproject-shortcut"
kexis = "kexis"
applicationvndapplekeynote = "application/vnd.apple.keynote"
keynote = "keynote"
applicationxkformula = "application/x-kformula"
kfo = "kfo"
applicationvndkidspiration = "application/vnd.kidspiration"
kia = "kia"
applicationxkillustrator = "application/x-killustrator"
kil = "kil"
applicationvndgoogleearthkmlxml = "application/vnd.google-earth.kml+xml"
kml = "kml"
applicationvndgoogleearthkmz = "application/vnd.google-earth.kmz"
kmz = "kmz"
applicationvndkinar = "application/vnd.kinar"
kne = "kne"
knp = "knp"
applicationxkontour = "application/x-kontour"
kon = "kon"
applicationxkpovmodeler = "application/x-kpovmodeler"
kpm = "kpm"
applicationxkpresenter = "application/x-kpresenter"
kpr = "kpr"
kpt = "kpt"
applicationvnddskeypoint = "application/vnd.ds-keypoint"
kpxx = "kpxx"
applicationxkrita = "application/x-krita"
kra = "kra"
applicationxkspread = "application/x-kspread"
ksp = "ksp"
textxkotlin = "text/x-kotlin"
kt = "kt"
imagektx = "image/ktx"
ktx = "ktx"
applicationvndkahootz = "application/vnd.kahootz"
ktz = "ktz"
ktr = "ktr"
applicationxkugar = "application/x-kugar"
kud = "kud"
applicationxkword = "application/x-kword"
kwd = "kwd"
kwt = "kwt"
applicationxsharedlibraryla = "application/x-shared-library-la"
la = "la"
applicationvndlaslasxml = "application/vnd.las.las+xml"
lasxml = "lasxml"
applicationvndllamagraphicslifebalancedesktop = "application/vnd.llamagraphics.life-balance.desktop"
lbd = "lbd"
applicationvndllamagraphicslifebalanceexchangexml = "application/vnd.llamagraphics.life-balance.exchange+xml"
lbe = "lbe"
textxldif = "text/x-ldif"
ldif = "ldif"
applicationvndhhelessonplayer = "application/vnd.hhe.lesson-player"
les = "les"
textless = "text/less"
less = "less"
applicationlgrxml = "application/lgr+xml"
lgr = "lgr"
applicationxlha = "application/x-lha"
lha = "lha"
lzh = "lzh"
textxliteratehaskell = "text/x-literate-haskell"
lhs = "lhs"
applicationxlhz = "application/x-lhz"
lhz = "lhz"
applicationvndroute66link66xml = "application/vnd.route66.link66+xml"
link66 = "link66"
textcoffeescript = "text/coffeescript"
litcoffee = "litcoffee"
applicationxmsshortcut = "application/x-ms-shortcut"
lnk = "lnk"
applicationxatarilynxrom = "application/x-atari-lynx-rom"
lnx = "lnx"
audiousac = "audio/usac"
loas = "loas"
xhe = "xhe"
textxlog = "text/x-log"
log = "log"
applicationlostxml = "application/lost+xml"
lostxml = "lostxml"
applicationvndmslrm = "application/vnd.ms-lrm"
lrm = "lrm"
applicationxlrzip = "application/x-lrzip"
lrz = "lrz"
applicationvndfrogansltf = "application/vnd.frogans.ltf"
ltf = "ltf"
textxlua = "text/x-lua"
lua = "lua"
applicationxluabytecode = "application/x-lua-bytecode"
luac = "luac"
audiovndlucentvoice = "audio/vnd.lucent.voice"
lvp = "lvp"
imagexlwo = "image/x-lwo"
lwo = "lwo"
lwob = "lwob"
applicationvndlotuswordpro = "application/vnd.lotus-wordpro"
lwp = "lwp"
imagexlws = "image/x-lws"
lws = "lws"
textxlilypond = "text/x-lilypond"
ly = "ly"
applicationxlyx = "application/x-lyx"
lyx = "lyx"
applicationxlzip = "application/x-lzip"
lz = "lz"
applicationxlz4 = "application/x-lz4"
lz4 = "lz4"
applicationxlzma = "application/x-lzma"
lzma = "lzma"
applicationxlzop = "application/x-lzop"
lzo = "lzo"
textxobjcsrc = "text/x-objcsrc"
m = "m"
videovndmpegurl = "video/vnd.mpegurl"
m1u = "m1u"
m4u = "m4u"
mxu = "mxu"
applicationmp21 = "application/mp21"
m21 = "m21"
mp21 = "mp21"
videomp2t = "video/mp2t"
m2t = "m2t"
m2ts = "m2ts"
mts = "mts"
cpi = "cpi"
clpi = "clpi"
mpl = "mpl"
mpls = "mpls"
bdm = "bdm"
bdmv = "bdmv"
audioxmpegurl = "audio/x-mpegurl"
m3u = "m3u"
m3u8 = "m3u8"
vlc = "vlc"
applicationxm4 = "application/x-m4"
m4 = "m4"
audiomp4 = "audio/mp4"
m4a = "m4a"
f4a = "f4a"
mp4a = "mp4a"
audioxm4b = "audio/x-m4b"
m4b = "m4b"
f4b = "f4b"
audioxm4r = "audio/x-m4r"
m4r = "m4r"
applicationxthomsoncartridgememo7 = "application/x-thomson-cartridge-memo7"
m7 = "m7"
applicationxmarkaby = "application/x-markaby"
mab = "mab"
applicationmadsxml = "application/mads+xml"
mads = "mads"
applicationmmtaeixml = "application/mmt-aei+xml"
maei = "maei"
applicationvndecowinchart = "application/vnd.ecowin.chart"
mag = "mag"
textxmakefile = "text/x-makefile"
makefile = "makefile"
gnumakefile = "gnumakefile"
mk = "mk"
mak = "mak"
applicationxtroffman = "application/x-troff-man"
man = "man"
textcachemanifest = "text/cache-manifest"
manifest = "manifest"
appcache = "appcache"
applicationvndmobiusmbk = "application/vnd.mobius.mbk"
mbk = "mbk"
applicationmbox = "application/mbox"
mbox = "mbox"
applicationvndmedcalcdata = "application/vnd.medcalcdata"
mc1 = "mc1"
textvndsenxwarpscript = "text/vnd.senx.warpscript"
mc2 = "mc2"
applicationvndmcd = "application/vnd.mcd"
mcd = "mcd"
textvndcurlmcurl = "text/vnd.curl.mcurl"
mcurl = "mcurl"
textmarkdown = "text/markdown"
md = "md"
mkd = "mkd"
markdown = "markdown"
applicationvndmsaccess = "application/vnd.ms-access"
mdb = "mdb"
imagevndmsmodi = "image/vnd.ms-modi"
mdi = "mdi"
textxtroffme = "text/x-troff-me"
me = "me"
textxmeson = "text/x-meson"
mesonbuild = "mesonbuild"
mesonoptionstxt = "mesonoptionstxt"
applicationmetalink4xml = "application/metalink4+xml"
meta4 = "meta4"
applicationmetalinkxml = "application/metalink+xml"
metalink = "metalink"
applicationmetsxml = "application/mets+xml"
mets = "mets"
applicationvndmfmp = "application/vnd.mfmp"
mfm = "mfm"
applicationrpkimanifest = "application/rpki-manifest"
mft = "mft"
applicationxmagicpoint = "application/x-magicpoint"
mgp = "mgp"
applicationvndproteusmagazine = "application/vnd.proteus.magazine"
mgz = "mgz"
applicationxmimearchive = "application/x-mimearchive"
mhtml = "mhtml"
mht = "mht"
audiomidi = "audio/midi"
mid = "mid"
midi = "midi"
kar = "kar"
rmi = "rmi"
applicationxmie = "application/x-mie"
mie = "mie"
applicationxmif = "application/x-mif"
mif = "mif"
audioxminipsf = "audio/x-minipsf"
minipsf = "minipsf"
videomj2 = "video/mj2"
mj2 = "mj2"
mjp2 = "mjp2"
videoxmjpeg = "video/x-mjpeg"
mjpeg = "mjpeg"
mjpg = "mjpg"
videoxmatroska3d = "video/x-matroska-3d"
mk3d = "mk3d"
audioxmatroska = "audio/x-matroska"
mka = "mka"
videoxmatroska = "video/x-matroska"
mkv = "mkv"
mks = "mks"
textxocaml = "text/x-ocaml"
ml = "ml"
mli = "mli"
applicationvnddolbymlp = "application/vnd.dolby.mlp"
mlp = "mlp"
textxtroffmm = "text/x-troff-mm"
mm = "mm"
applicationvndchipnutskaraokemmd = "application/vnd.chipnuts.karaoke-mmd"
mmd = "mmd"
applicationxsmaf = "application/x-smaf"
mmf = "mmf"
smaf = "smaf"
applicationmathmlxml = "application/mathml+xml"
mml = "mml"
mathml = "mathml"
imagevndfujixeroxedmicsmmr = "image/vnd.fujixerox.edmics-mmr"
mmr = "mmr"
videoxmng = "video/x-mng"
mng = "mng"
applicationxmsmoney = "application/x-msmoney"
mny = "mny"
audioxmo3 = "audio/x-mo3"
mo3 = "mo3"
applicationxmobipocketebook = "application/x-mobipocket-ebook"
mobi = "mobi"
prc = "prc"
textxmoc = "text/x-moc"
moc = "moc"
audioxmod = "audio/x-mod"
mod = "mod"
ult = "ult"
uni = "uni"
m15 = "m15"
mtm = "mtm"
_669 = "669"
med = "med"
applicationmodsxml = "application/mods+xml"
mods = "mods"
textxmof = "text/x-mof"
mof = "mof"
videoxsgimovie = "video/x-sgi-movie"
movie = "movie"
audiomp2 = "audio/mp2"
mp2 = "mp2"
audiompeg = "audio/mpeg"
mp3 = "mp3"
mpga = "mpga"
mp2a = "mp2a"
m2a = "m2a"
m3a = "m3a"
videomp4 = "video/mp4"
mp4 = "mp4"
m4v = "m4v"
f4v = "f4v"
lrv = "lrv"
mp4v = "mp4v"
mpg4 = "mpg4"
applicationmp4 = "application/mp4"
mp4s = "mp4s"
m4p = "m4p"
audioxmusepack = "audio/x-musepack"
mpc = "mpc"
mpp = "mpp"
mp = "mp"
applicationdashxml = "application/dash+xml"
mpd = "mpd"
videompeg = "video/mpeg"
mpeg = "mpeg"
mpg = "mpg"
mpe = "mpe"
vob = "vob"
_090909vdr = "090909vdr"
m1v = "m1v"
m2v = "m2v"
applicationvndappleinstallerxml = "application/vnd.apple.installer+xml"
mpkg = "mpkg"
applicationvndblueicemultipass = "application/vnd.blueice.multipass"
mpm = "mpm"
applicationvndmophunapplication = "application/vnd.mophun.application"
mpn = "mpn"
applicationvndmsproject = "application/vnd.ms-project"
mpt = "mpt"
applicationvndibmminipay = "application/vnd.ibm.minipay"
mpy = "mpy"
applicationvndmobiusmqy = "application/vnd.mobius.mqy"
mqy = "mqy"
applicationmarc = "application/marc"
mrc = "mrc"
applicationmarcxmlxml = "application/marcxml+xml"
mrcx = "mrcx"
textxmrml = "text/x-mrml"
mrml = "mrml"
mrl = "mrl"
imagexminoltamrw = "image/x-minolta-mrw"
mrw = "mrw"
textxtroffms = "text/x-troff-ms"
ms = "ms"
applicationmediaservercontrolxml = "application/mediaservercontrol+xml"
mscml = "mscml"
applicationvndfdsnmseed = "application/vnd.fdsn.mseed"
mseed = "mseed"
applicationvndmseq = "application/vnd.mseq"
mseq = "mseq"
applicationvndepsonmsf = "application/vnd.epson.msf"
msf = "msf"
applicationvndmsoutlook = "application/vnd.ms-outlook"
msg = "msg"
modelmesh = "model/mesh"
msh = "msh"
mesh = "mesh"
silo = "silo"
applicationxmsi = "application/x-msi"
msi = "msi"
applicationvndmobiusmsl = "application/vnd.mobius.msl"
msl = "msl"
imagexmsod = "image/x-msod"
msod = "msod"
applicationvndmuveestyle = "application/vnd.muvee.style"
msty = "msty"
applicationxmsxrom = "application/x-msx-rom"
msx = "msx"
modelmtl = "model/mtl"
mtl = "mtl"
textxmup = "text/x-mup"
mup = "mup"
_not = "not"
applicationvndmusician = "application/vnd.musician"
mus = "mus"
applicationmmtusdxml = "application/mmt-usd+xml"
musd = "musd"
applicationvndrecordaremusicxmlxml = "application/vnd.recordare.musicxml+xml"
musicxml = "musicxml"
applicationxmsmediaview = "application/x-msmediaview"
mvb = "mvb"
m13 = "m13"
m14 = "m14"
applicationvndmfer = "application/vnd.mfer"
mwf = "mwf"
applicationmxf = "application/mxf"
mxf = "mxf"
applicationvndrecordaremusicxml = "application/vnd.recordare.musicxml"
mxl = "mxl"
audiomobilexmf = "audio/mobile-xmf"
mxmf = "mxmf"
applicationxvxml = "application/xv+xml"
mxml = "mxml"
xhvml = "xhvml"
xvml = "xvml"
xvm = "xvm"
applicationvndtriscapemxs = "application/vnd.triscape.mxs"
mxs = "mxs"
textn3 = "text/n3"
n3 = "n3"
applicationxn64rom = "application/x-n64-rom"
n64 = "n64"
z64 = "z64"
v64 = "v64"
applicationmathematica = "application/mathematica"
nb = "nb"
ma = "ma"
mb = "mb"
applicationvndwolframplayer = "application/vnd.wolfram.player"
nbp = "nbp"
applicationxdtbncxxml = "application/x-dtbncx+xml"
ncx = "ncx"
applicationxnintendodsrom = "application/x-nintendo-ds-rom"
nds = "nds"
imagexnikonnef = "image/x-nikon-nef"
nef = "nef"
applicationxnesrom = "application/x-nes-rom"
nes = "nes"
nez = "nez"
unf = "unf"
unif = "unif"
textxnfo = "text/x-nfo"
nfo = "nfo"
applicationvndnokiangagesymbianinstall = "application/vnd.nokia.n-gage.symbian.install"
ngage = "n-gage"
applicationxneogeopocketcolorrom = "application/x-neo-geo-pocket-color-rom"
ngc = "ngc"
applicationvndnokiangagedata = "application/vnd.nokia.n-gage.data"
ngdat = "ngdat"
applicationxneogeopocketrom = "application/x-neo-geo-pocket-rom"
ngp = "ngp"
applicationvndneurolanguagenlu = "application/vnd.neurolanguage.nlu"
nlu = "nlu"
applicationvndenliven = "application/vnd.enliven"
nml = "nml"
applicationvndnoblenetdirectory = "application/vnd.noblenet-directory"
nnd = "nnd"
applicationvndnoblenetsealer = "application/vnd.noblenet-sealer"
nns = "nns"
applicationvndnoblenetweb = "application/vnd.noblenet-web"
nnw = "nnw"
imagevndnetfpx = "image/vnd.net-fpx"
npx = "npx"
applicationnquads = "application/n-quads"
nq = "nq"
applicationxnetshowchannel = "application/x-netshow-channel"
nsc = "nsc"
applicationvndlotusnotes = "application/vnd.lotus-notes"
nsf = "nsf"
videoxnsv = "video/x-nsv"
nsv = "nsv"
applicationntriples = "application/n-triples"
nt = "nt"
applicationvndnitf = "application/vnd.nitf"
ntf = "ntf"
nitf = "nitf"
applicationvndapplenumbers = "application/vnd.apple.numbers"
numbers = "numbers"
applicationxnzb = "application/x-nzb"
nzb = "nzb"
applicationxobject = "application/x-object"
o = "o"
applicationvndfujitsuoasys2 = "application/vnd.fujitsu.oasys2"
oa2 = "oa2"
applicationvndfujitsuoasys3 = "application/vnd.fujitsu.oasys3"
oa3 = "oa3"
applicationvndfujitsuoasys = "application/vnd.fujitsu.oasys"
oas = "oas"
applicationxmsbinder = "application/x-msbinder"
obd = "obd"
applicationvndopenbloxgamexml = "application/vnd.openblox.game+xml"
obgx = "obgx"
applicationxtgif = "application/x-tgif"
obj = "obj"
textxocl = "text/x-ocl"
ocl = "ocl"
applicationoda = "application/oda"
oda = "oda"
applicationvndoasisopendocumentdatabase = "application/vnd.oasis.opendocument.database"
odb = "odb"
applicationvndoasisopendocumentchart = "application/vnd.oasis.opendocument.chart"
odc = "odc"
applicationvndoasisopendocumentformula = "application/vnd.oasis.opendocument.formula"
odf = "odf"
applicationvndoasisopendocumentgraphics = "application/vnd.oasis.opendocument.graphics"
odg = "odg"
applicationvndoasisopendocumentimage = "application/vnd.oasis.opendocument.image"
odi = "odi"
applicationvndoasisopendocumenttextmaster = "application/vnd.oasis.opendocument.text-master"
odm = "odm"
applicationvndoasisopendocumentpresentation = "application/vnd.oasis.opendocument.presentation"
odp = "odp"
applicationvndoasisopendocumentspreadsheet = "application/vnd.oasis.opendocument.spreadsheet"
ods = "ods"
applicationvndoasisopendocumenttext = "application/vnd.oasis.opendocument.text"
odt = "odt"
audioogg = "audio/ogg"
oga = "oga"
ogg = "ogg"
opus = "opus"
modelvndopengex = "model/vnd.opengex"
ogex = "ogex"
videoxogmogg = "video/x-ogm+ogg"
ogm = "ogm"
videoogg = "video/ogg"
ogv = "ogv"
applicationogg = "application/ogg"
ogx = "ogx"
applicationxoleo = "application/x-oleo"
oleo = "oleo"
applicationomdocxml = "application/omdoc+xml"
omdoc = "omdoc"
applicationonenote = "application/onenote"
onetoc = "onetoc"
onetoc2 = "onetoc2"
onetmp = "onetmp"
onepkg = "onepkg"
textxooc = "text/x-ooc"
ooc = "ooc"
applicationoebpspackagexml = "application/oebps-package+xml"
opf = "opf"
textxopmlxml = "text/x-opml+xml"
opml = "opml"
imageopenraster = "image/openraster"
ora = "ora"
imagexolympusorf = "image/x-olympus-orf"
orf = "orf"
applicationvndlotusorganizer = "application/vnd.lotus-organizer"
org = "org"
applicationvndyamahaopenscoreformat = "application/vnd.yamaha.openscoreformat"
osf = "osf"
applicationvndyamahaopenscoreformatosfpvgxml = "application/vnd.yamaha.openscoreformat.osfpvg+xml"
osfpvg = "osfpvg"
applicationvndopenstreetmapdataxml = "application/vnd.openstreetmap.data+xml"
osm = "osm"
applicationvndoasisopendocumentcharttemplate = "application/vnd.oasis.opendocument.chart-template"
otc = "otc"
applicationvndoasisopendocumentformulatemplate = "application/vnd.oasis.opendocument.formula-template"
otf = "otf"
odft = "odft"
applicationvndoasisopendocumentgraphicstemplate = "application/vnd.oasis.opendocument.graphics-template"
otg = "otg"
applicationvndoasisopendocumenttextweb = "application/vnd.oasis.opendocument.text-web"
oth = "oth"
applicationvndoasisopendocumentimagetemplate = "application/vnd.oasis.opendocument.image-template"
oti = "oti"
applicationvndoasisopendocumentpresentationtemplate = "application/vnd.oasis.opendocument.presentation-template"
otp = "otp"
applicationvndoasisopendocumentspreadsheettemplate = "application/vnd.oasis.opendocument.spreadsheet-template"
ots = "ots"
applicationvndoasisopendocumenttexttemplate = "application/vnd.oasis.opendocument.text-template"
ott = "ott"
applicationxvirtualboxova = "application/x-virtualbox-ova"
ova = "ova"
applicationxvirtualboxovf = "application/x-virtualbox-ovf"
ovf = "ovf"
applicationowlxml = "application/owl+xml"
owx = "owx"
applicationoxps = "application/oxps"
oxps = "oxps"
xps = "xps"
applicationvndopenofficeorgextension = "application/vnd.openofficeorg.extension"
oxt = "oxt"
textxpascal = "text/x-pascal"
p = "p"
pas = "pas"
applicationpkcs10 = "application/pkcs10"
p10 = "p10"
applicationpkcs12 = "application/pkcs12"
p12 = "p12"
pfx = "pfx"
applicationxpagemaker = "application/x-pagemaker"
p65 = "p65"
pm6 = "pm6"
pmd = "pmd"
applicationxpkcs7certificates = "application/x-pkcs7-certificates"
p7b = "p7b"
spc = "spc"
applicationpkcs7mime = "application/pkcs7-mime"
p7c = "p7c"
p7m = "p7m"
applicationxpkcs7certreqresp = "application/x-pkcs7-certreqresp"
p7r = "p7r"
applicationpkcs7signature = "application/pkcs7-signature"
p7s = "p7s"
applicationpkcs8 = "application/pkcs8"
p8 = "p8"
applicationpkcs8encrypted = "application/pkcs8-encrypted"
p8e = "p8e"
applicationxnsproxyautoconfig = "application/x-ns-proxy-autoconfig"
pac = "pac"
applicationxjavapack200 = "application/x-java-pack200"
pack = "pack"
applicationvndapplepages = "application/vnd.apple.pages"
pages = "pages"
applicationxpak = "application/x-pak"
pak = "pak"
applicationxpar2 = "application/x-par2"
par2 = "par2"
imagexgimppat = "image/x-gimp-pat"
pat = "pat"
applicationvndpawaafile = "application/vnd.pawaafile"
paw = "paw"
applicationvndpowerbuilder6 = "application/vnd.powerbuilder6"
pbd = "pbd"
imagexportablebitmap = "image/x-portable-bitmap"
pbm = "pbm"
applicationvndtcpdumppcap = "application/vnd.tcpdump.pcap"
pcap = "pcap"
cap = "cap"
dmp = "dmp"
imagexphotocd = "image/x-photo-cd"
pcd = "pcd"
applicationxpcenginerom = "application/x-pc-engine-rom"
pce = "pce"
applicationxfontpcf = "application/x-font-pcf"
pcf = "pcf"
pcfz = "pcfz"
pcfgz = "pcfgz"
applicationvndhppcl = "application/vnd.hp-pcl"
pcl = "pcl"
applicationvndhppclxl = "application/vnd.hp-pclxl"
pclxl = "pclxl"
imagexpict = "image/x-pict"
pct = "pct"
pict = "pict"
pict1 = "pict1"
pict2 = "pict2"
pic = "pic"
applicationvndcurlpcurl = "application/vnd.curl.pcurl"
pcurl = "pcurl"
imagevndzbrushpcx = "image/vnd.zbrush.pcx"
pcx = "pcx"
applicationxaportisdoc = "application/x-aportisdoc"
pdb = "pdb"
pdc = "pdc"
textxprocessing = "text/x-processing"
pde = "pde"
applicationpdf = "application/pdf"
pdf = "pdf"
applicationxbzpdf = "application/x-bzpdf"
pdfbz2 = "pdfbz2"
applicationxgzpdf = "application/x-gzpdf"
pdfgz = "pdfgz"
applicationxlzpdf = "application/x-lzpdf"
pdflz = "pdflz"
applicationxxzpdf = "application/x-xzpdf"
pdfxz = "pdfxz"
imagexpentaxpef = "image/x-pentax-pef"
pef = "pef"
applicationxfonttype1 = "application/x-font-type1"
pfa = "pfa"
pfb = "pfb"
gsf = "gsf"
pfm = "pfm"
applicationfonttdpfr = "application/font-tdpfr"
pfr = "pfr"
imagexportablegraymap = "image/x-portable-graymap"
pgm = "pgm"
applicationvndchesspgn = "application/vnd.chess-pgn"
pgn = "pgn"
applicationpgpencrypted = "application/pgp-encrypted"
pgp = "pgp"
gpg = "gpg"
asc = "asc"
applicationxphp = "application/x-php"
php = "php"
php3 = "php3"
php4 = "php4"
php5 = "php5"
phps = "phps"
applicationxtexpk = "application/x-tex-pk"
pk = "pk"
applicationpkixcmp = "application/pkixcmp"
pki = "pki"
applicationpkixpkipath = "application/pkix-pkipath"
pkipath = "pkipath"
applicationvndapplepkpass = "application/vnd.apple.pkpass"
pkpass = "pkpass"
applicationxperl = "application/x-perl"
pl = "pl"
pm = "pm"
al = "al"
perl = "perl"
pod = "pod"
t = "t"
audioxiriverpla = "audio/x-iriver-pla"
pla = "pla"
applicationvnd3gpppicbwlarge = "application/vnd.3gpp.pic-bw-large"
plb = "plb"
applicationvndmobiusplc = "application/vnd.mobius.plc"
plc = "plc"
applicationvndpocketlearn = "application/vnd.pocketlearn"
plf = "plf"
applicationxplanperfect = "application/x-planperfect"
pln = "pln"
audioxscpls = "audio/x-scpls"
pls = "pls"
applicationvndctcposml = "application/vnd.ctc-posml"
pml = "pml"
imagepng = "image/png"
png = "png"
imagexportableanymap = "image/x-portable-anymap"
pnm = "pnm"
imagexmacpaint = "image/x-macpaint"
pntg = "pntg"
textxgettexttranslation = "text/x-gettext-translation"
po = "po"
textxmavenxml = "text/x-maven+xml"
pomxml = "pomxml"
settingsxml = "settingsxml"
applicationxspsspor = "application/x-spss-por"
por = "por"
applicationvndmacportsportpkg = "application/vnd.macports.portpkg"
portpkg = "portpkg"
applicationvndmspowerpointtemplatemacroenabled12 = "application/vnd.ms-powerpoint.template.macroenabled.12"
potm = "potm"
applicationvndopenxmlformatsofficedocumentpresentationmltemplate = "application/vnd.openxmlformats-officedocument.presentationml.template"
potx = "potx"
applicationvndmspowerpointaddinmacroenabled12 = "application/vnd.ms-powerpoint.addin.macroenabled.12"
ppam = "ppam"
applicationvndcupsppd = "application/vnd.cups-ppd"
ppd = "ppd"
imagexportablepixmap = "image/x-portable-pixmap"
ppm = "ppm"
applicationvndmspowerpointslideshowmacroenabled12 = "application/vnd.ms-powerpoint.slideshow.macroenabled.12"
ppsm = "ppsm"
applicationvndopenxmlformatsofficedocumentpresentationmlslideshow = "application/vnd.openxmlformats-officedocument.presentationml.slideshow"
ppsx = "ppsx"
applicationvndmspowerpointpresentationmacroenabled12 = "application/vnd.ms-powerpoint.presentation.macroenabled.12"
pptm = "pptm"
applicationvndopenxmlformatsofficedocumentpresentationmlpresentation = "application/vnd.openxmlformats-officedocument.presentationml.presentation"
pptx = "pptx"
applicationvndmspowerpoint = "application/vnd.ms-powerpoint"
ppz = "ppz"
ppt = "ppt"
pps = "pps"
pot = "pot"
applicationvndpalm = "application/vnd.palm"
pqa = "pqa"
oprc = "oprc"
applicationvndlotusfreelance = "application/vnd.lotus-freelance"
pre = "pre"
applicationpicsrules = "application/pics-rules"
prf = "prf"
applicationprovenancexml = "application/provenance+xml"
provx = "provx"
applicationpostscript = "application/postscript"
ps = "ps"
applicationvnd3gpppicbwsmall = "application/vnd.3gpp.pic-bw-small"
psb = "psb"
applicationxbzpostscript = "application/x-bzpostscript"
psbz2 = "psbz2"
imagevndadobephotoshop = "image/vnd.adobe.photoshop"
psd = "psd"
applicationxfontlinuxpsf = "application/x-font-linux-psf"
psf = "psf"
applicationxgzfontlinuxpsf = "application/x-gz-font-linux-psf"
psfgz = "psfgz"
audioxpsflib = "audio/x-psflib"
psflib = "psflib"
applicationxgzpostscript = "application/x-gzpostscript"
psgz = "psgz"
applicationpskcxml = "application/pskc+xml"
pskcxml = "pskcxml"
applicationxpocketword = "application/x-pocket-word"
psw = "psw"
imageprspti = "image/prs.pti"
pti = "pti"
applicationvndpviptid1 = "application/vnd.pvi.ptid1"
ptid = "ptid"
applicationvndmspublisher = "application/vnd.ms-publisher"
pub = "pub"
applicationvnd3gpppicbwvar = "application/vnd.3gpp.pic-bw-var"
pvb = "pvb"
applicationxpw = "application/x-pw"
pw = "pw"
applicationvnd3mpostitnotes = "application/vnd.3m.post-it-notes"
pwn = "pwn"
textxpython3 = "text/x-python3"
py = "py"
py3 = "py3"
py3x = "py3x"
audiovndmsplayreadymediapya = "audio/vnd.ms-playready.media.pya"
pya = "pya"
applicationxpythonbytecode = "application/x-python-bytecode"
pyc = "pyc"
pyo = "pyo"
applicationxpyspreadbzspreadsheet = "application/x-pyspread-bz-spreadsheet"
pys = "pys"
applicationxpyspreadspreadsheet = "application/x-pyspread-spreadsheet"
pysu = "pysu"
videovndmsplayreadymediapyv = "video/vnd.ms-playready.media.pyv"
pyv = "pyv"
textxpython = "text/x-python"
pyx = "pyx"
wsgi = "wsgi"
applicationvndepsonquickanime = "application/vnd.epson.quickanime"
qam = "qam"
applicationvndintuqbo = "application/vnd.intu.qbo"
qbo = "qbo"
applicationxqemudisk = "application/x-qemu-disk"
qcow2 = "qcow2"
qcow = "qcow"
applicationvndintuqfx = "application/vnd.intu.qfx"
qfx = "qfx"
applicationxqw = "application/x-qw"
qif = "qif"
textxqml = "text/x-qml"
qml = "qml"
qmltypes = "qmltypes"
qmlproject = "qmlproject"
applicationxqpress = "application/x-qpress"
qp = "qp"
applicationvndpublisharedeltatree = "application/vnd.publishare-delta-tree"
qps = "qps"
videoquicktime = "video/quicktime"
qt = "qt"
mov = "mov"
moov = "moov"
qtvr = "qtvr"
applicationxqtiplot = "application/x-qtiplot"
qti = "qti"
qtigz = "qtigz"
imagexquicktime = "image/x-quicktime"
qtif = "qtif"
applicationxquicktimemedialink = "application/x-quicktime-media-link"
qtl = "qtl"
applicationvndquarkquarkxpress = "application/vnd.quark.quarkxpress"
qxd = "qxd"
qxt = "qxt"
qwd = "qwd"
qwt = "qwt"
qxl = "qxl"
qxb = "qxb"
audiovndrnrealaudio = "audio/vnd.rn-realaudio"
ra = "ra"
rax = "rax"
imagexfujiraf = "image/x-fuji-raf"
raf = "raf"
applicationram = "application/ram"
ram = "ram"
applicationramlyaml = "application/raml+yaml"
raml = "raml"
applicationrouteapdxml = "application/route-apd+xml"
rapd = "rapd"
applicationvndrar = "application/vnd.rar"
rar = "rar"
imagexcmuraster = "image/x-cmu-raster"
ras = "ras"
imagexpanasonicrw = "image/x-panasonic-rw"
raw = "raw"
applicationxrawdiskimage = "application/x-raw-disk-image"
rawdiskimage = "rawdiskimage"
img = "img"
applicationxrawdiskimagexzcompressed = "application/x-raw-disk-image-xz-compressed"
rawdiskimagexz = "rawdiskimagexz"
imgxz = "imgxz"
applicationxruby = "application/x-ruby"
rb = "rb"
applicationvndipunpluggedrcprofile = "application/vnd.ipunplugged.rcprofile"
rcprofile = "rcprofile"
applicationrdfxml = "application/rdf+xml"
rdf = "rdf"
rdfs = "rdfs"
owl = "owl"
applicationvnddatavisionrdz = "application/vnd.data-vision.rdz"
rdz = "rdz"
textxreadme = "text/x-readme"
readme = "readme"
textxmsregedit = "text/x-ms-regedit"
reg = "reg"
textxreject = "text/x-reject"
rej = "rej"
applicationp2poverlayxml = "application/p2p-overlay+xml"
relo = "relo"
applicationvndbusinessobjects = "application/vnd.businessobjects"
rep = "rep"
applicationxdtbresourcexml = "application/x-dtbresource+xml"
res = "res"
imagexrgb = "image/x-rgb"
rgb = "rgb"
applicationreginfoxml = "application/reginfo+xml"
rif = "rif"
audiovndrip = "audio/vnd.rip"
rip = "rip"
applicationxresearchinfosystems = "application/x-research-info-systems"
ris = "ris"
applicationresourcelistsxml = "application/resource-lists+xml"
rl = "rl"
imagevndfujixeroxedmicsrlc = "image/vnd.fujixerox.edmics-rlc"
rlc = "rlc"
applicationresourcelistsdiffxml = "application/resource-lists-diff+xml"
rld = "rld"
imagerle = "image/rle"
rle = "rle"
applicationvndrnrealmedia = "application/vnd.rn-realmedia"
rm = "rm"
rmj = "rmj"
rmm = "rmm"
rms = "rms"
rmx = "rmx"
rmvb = "rmvb"
messagexgnurmail = "message/x-gnu-rmail"
rmail = "rmail"
audioxpnrealaudioplugin = "audio/x-pn-realaudio-plugin"
rmp = "rmp"
applicationrelaxngcompactsyntax = "application/relax-ng-compact-syntax"
rnc = "rnc"
applicationrpkiroa = "application/rpki-roa"
roa = "roa"
imagevndrnrealpix = "image/vnd.rn-realpix"
rp = "rp"
applicationvndcloantorp9 = "application/vnd.cloanto.rp9"
rp9 = "rp9"
applicationxrpm = "application/x-rpm"
rpm = "rpm"
applicationvndnokiaradiopresets = "application/vnd.nokia.radio-presets"
rpss = "rpss"
applicationvndnokiaradiopreset = "application/vnd.nokia.radio-preset"
rpst = "rpst"
applicationsparqlquery = "application/sparql-query"
rq = "rq"
textrust = "text/rust"
rs = "rs"
applicationatscrsatxml = "application/atsc-rsat+xml"
rsat = "rsat"
applicationrsdxml = "application/rsd+xml"
rsd = "rsd"
applicationurcressheetxml = "application/urc-ressheet+xml"
rsheet = "rsheet"
applicationrssxml = "application/rss+xml"
rss = "rss"
textxrst = "text/x-rst"
rst = "rst"
textvndrnrealtext = "text/vnd.rn-realtext"
rt = "rt"
applicationrtf = "application/rtf"
rtf = "rtf"
textrichtext = "text/richtext"
rtx = "rtx"
applicationxmakeself = "application/x-makeself"
run = "run"
applicationrouteusdxml = "application/route-usd+xml"
rusd = "rusd"
videovndrnrealvideo = "video/vnd.rn-realvideo"
rv = "rv"
rvx = "rvx"
imagexpanasonicrw2 = "image/x-panasonic-rw2"
rw2 = "rw2"
textxasm = "text/x-asm"
s = "s"
asm = "asm"
audioxs3m = "audio/x-s3m"
s3m = "s3m"
applicationvndyamahasmafaudio = "application/vnd.yamaha.smaf-audio"
saf = "saf"
applicationxamipro = "application/x-amipro"
sam = "sam"
applicationxsami = "application/x-sami"
sami = "sami"
applicationxthomsonsapimage = "application/x-thomson-sap-image"
sap = "sap"
textxsass = "text/x-sass"
sass = "sass"
applicationxspsssav = "application/x-spss-sav"
sav = "sav"
zsav = "zsav"
applicationsbmlxml = "application/sbml+xml"
sbml = "sbml"
applicationvndibmsecurecontainer = "application/vnd.ibm.secure-container"
sc = "sc"
textxscala = "text/x-scala"
scala = "scala"
applicationxmsschedule = "application/x-msschedule"
scd = "scd"
textxscheme = "text/x-scheme"
scm = "scm"
ss = "ss"
textxscons = "text/x-scons"
sconstruct = "sconstruct"
sconscript = "sconscript"
applicationscvpcvrequest = "application/scvp-cv-request"
scq = "scq"
applicationscvpcvresponse = "application/scvp-cv-response"
scs = "scs"
textxscss = "text/x-scss"
scss = "scss"
textvndcurlscurl = "text/vnd.curl.scurl"
scurl = "scurl"
applicationvndstardivisiondraw = "application/vnd.stardivision.draw"
sda = "sda"
applicationvndstardivisioncalc = "application/vnd.stardivision.calc"
sdc = "sdc"
applicationvndstardivisionimpress = "application/vnd.stardivision.impress"
sdd = "sdd"
sdp = "sdp"
applicationvndsolentsdkmxml = "application/vnd.solent.sdkm+xml"
sdkm = "sdkm"
sdkd = "sdkd"
applicationvndstardivisionchart = "application/vnd.stardivision.chart"
sds = "sds"
applicationvndstardivisionwriter = "application/vnd.stardivision.writer"
sdw = "sdw"
vor = "vor"
sgl = "sgl"
applicationxsea = "application/x-sea"
sea = "sea"
applicationvndseemail = "application/vnd.seemail"
see = "see"
applicationvndfdsnseed = "application/vnd.fdsn.seed"
seed = "seed"
dataless = "dataless"
applicationvndsema = "application/vnd.sema"
sema = "sema"
applicationvndsemd = "application/vnd.semd"
semd = "semd"
applicationvndsemf = "application/vnd.semf"
semf = "semf"
applicationsenmlxml = "application/senml+xml"
senmlx = "senmlx"
applicationsensmlxml = "application/sensml+xml"
sensmlx = "sensmlx"
applicationjavaserializedobject = "application/java-serialized-object"
ser = "ser"
textxdbusservice = "text/x-dbus-service"
service = "service"
applicationsetpaymentinitiation = "application/set-payment-initiation"
setpay = "setpay"
applicationsetregistrationinitiation = "application/set-registration-initiation"
setreg = "setreg"
applicationvndnintendosnesrom = "application/vnd.nintendo.snes.rom"
sfc = "sfc"
smc = "smc"
applicationvndhydrostatixsofdata = "application/vnd.hydrostatix.sof-data"
sfdhdstx = "sfd-hdstx"
applicationvndspotfiresfs = "application/vnd.spotfire.sfs"
sfs = "sfs"
textxsfv = "text/x-sfv"
sfv = "sfv"
applicationxsg1000rom = "application/x-sg1000-rom"
sg = "sg"
applicationxgosgf = "application/x-go-sgf"
sgf = "sgf"
imagexsgi = "image/x-sgi"
sgi = "sgi"
textsgml = "text/sgml"
sgml = "sgml"
sgm = "sgm"
applicationxshellscript = "application/x-shellscript"
sh = "sh"
applicationxdiashape = "application/x-dia-shape"
shape = "shape"
applicationxshar = "application/x-shar"
shar = "shar"
textshex = "text/shex"
shex = "shex"
applicationshfxml = "application/shf+xml"
shf = "shf"
applicationxshorten = "application/x-shorten"
shn = "shn"
texthtml = "text/html"
shtml = "shtml"
applicationxsiag = "application/x-siag"
siag = "siag"
audioprssid = "audio/prs.sid"
sid = "sid"
psid = "psid"
applicationpgpsignature = "application/pgp-signature"
sig = "sig"
audiosilk = "audio/silk"
sil = "sil"
applicationvndsymbianinstall = "application/vnd.symbian.install"
sis = "sis"
xepocxsisxapp = "x-epoc/x-sisx-app"
sisx = "sisx"
applicationxstuffit = "application/x-stuffit"
sit = "sit"
applicationxstuffitx = "application/x-stuffitx"
sitx = "sitx"
applicationsieve = "application/sieve"
siv = "siv"
sieve = "sieve"
imagexskencil = "image/x-skencil"
sk = "sk"
sk1 = "sk1"
applicationvndkoan = "application/vnd.koan"
skp = "skp"
skd = "skd"
skt = "skt"
skm = "skm"
applicationpgpkeys = "application/pgp-keys"
skr = "skr"
pkr = "pkr"
key = "key"
applicationvndmspowerpointslidemacroenabled12 = "application/vnd.ms-powerpoint.slide.macroenabled.12"
sldm = "sldm"
applicationvndopenxmlformatsofficedocumentpresentationmlslide = "application/vnd.openxmlformats-officedocument.presentationml.slide"
sldx = "sldx"
textslim = "text/slim"
slim = "slim"
slm = "slm"
applicationroutestsidxml = "application/route-s-tsid+xml"
sls = "sls"
applicationvndepsonsalt = "application/vnd.epson.salt"
slt = "slt"
applicationvndstepmaniastepchart = "application/vnd.stepmania.stepchart"
sm = "sm"
applicationvndstardivisionmail = "application/vnd.stardivision.mail"
smd = "smd"
applicationvndstardivisionmath = "application/vnd.stardivision.math"
smf = "smf"
applicationsmilxml = "application/smil+xml"
smil = "smil"
smi = "smi"
sml = "sml"
kino = "kino"
applicationxsmsrom = "application/x-sms-rom"
sms = "sms"
videoxsmv = "video/x-smv"
smv = "smv"
applicationvndstepmaniapackage = "application/vnd.stepmania.package"
smzip = "smzip"
applicationvndsnap = "application/vnd.snap"
snap = "snap"
applicationxfontsnf = "application/x-font-snf"
snf = "snf"
applicationxsharedlib = "application/x-sharedlib"
so = "so"
applicationxfontspeedo = "application/x-font-speedo"
spd = "spd"
textxrpmspec = "text/x-rpm-spec"
spec = "spec"
applicationvndyamahasmafphrase = "application/vnd.yamaha.smaf-phrase"
spf = "spf"
textvndin3dspot = "text/vnd.in3d.spot"
spot = "spot"
applicationscvpvpresponse = "application/scvp-vp-response"
spp = "spp"
applicationscvpvprequest = "application/scvp-vp-request"
spq = "spq"
audioxspeex = "audio/x-speex"
spx = "spx"
applicationsql = "application/sql"
sql = "sql"
applicationxsqlite2 = "application/x-sqlite2"
sqlite2 = "sqlite2"
applicationvndsqlite3 = "application/vnd.sqlite3"
sqlite3 = "sqlite3"
applicationvndsquashfs = "application/vnd.squashfs"
sqsh = "sqsh"
imagexsonysr2 = "image/x-sony-sr2"
sr2 = "sr2"
applicationxwaissource = "application/x-wais-source"
src = "src"
applicationxsourcerpm = "application/x-source-rpm"
srcrpm = "srcrpm"
spm = "spm"
imagexsonysrf = "image/x-sony-srf"
srf = "srf"
applicationxsubrip = "application/x-subrip"
srt = "srt"
applicationsruxml = "application/sru+xml"
sru = "sru"
applicationsparqlresultsxml = "application/sparql-results+xml"
srx = "srx"
textxssa = "text/x-ssa"
ssa = "ssa"
ass = "ass"
applicationssdlxml = "application/ssdl+xml"
ssdl = "ssdl"
applicationvndkodakdescriptor = "application/vnd.kodak-descriptor"
sse = "sse"
applicationvndepsonssf = "application/vnd.epson.ssf"
ssf = "ssf"
applicationssmlxml = "application/ssml+xml"
ssml = "ssml"
applicationvndsailingtrackertrack = "application/vnd.sailingtracker.track"
st = "st"
applicationvndsunxmlcalctemplate = "application/vnd.sun.xml.calc.template"
stc = "stc"
applicationvndsunxmldrawtemplate = "application/vnd.sun.xml.draw.template"
std = "std"
applicationvndwtstf = "application/vnd.wt.stf"
stf = "stf"
applicationvndsunxmlimpresstemplate = "application/vnd.sun.xml.impress.template"
sti = "sti"
applicationhyperstudio = "application/hyperstudio"
stk = "stk"
modelstl = "model/stl"
stl = "stl"
audioxstm = "audio/x-stm"
stm = "stm"
applicationvndpgformat = "application/vnd.pg.format"
str = "str"
applicationvndsunxmlwritertemplate = "application/vnd.sun.xml.writer.template"
stw = "stw"
textstylus = "text/stylus"
stylus = "stylus"
styl = "styl"
textxmicrodvd = "text/x-microdvd"
sub = "sub"
imagexsunraster = "image/x-sun-raster"
sun = "sun"
applicationvndsuscalendar = "application/vnd.sus-calendar"
sus = "sus"
susp = "susp"
textxsvsrc = "text/x-svsrc"
sv = "sv"
applicationxsv4cpio = "application/x-sv4cpio"
sv4cpio = "sv4cpio"
applicationxsv4crc = "application/x-sv4crc"
sv4crc = "sv4crc"
applicationvnddvbservice = "application/vnd.dvb.service"
svc = "svc"
applicationvndsvd = "application/vnd.svd"
svd = "svd"
imagesvgxml = "image/svg+xml"
svg = "svg"
imagesvgxmlcompressed = "image/svg+xml-compressed"
svgz = "svgz"
textxsvhdr = "text/x-svhdr"
svh = "svh"
applicationvndadobeflashmovie = "application/vnd.adobe.flash.movie"
swf = "swf"
spl = "spl"
applicationvndaristanetworksswi = "application/vnd.aristanetworks.swi"
swi = "swi"
applicationswidxml = "application/swid+xml"
swidtag = "swidtag"
applicationvndsunxmlcalc = "application/vnd.sun.xml.calc"
sxc = "sxc"
applicationvndsunxmldraw = "application/vnd.sun.xml.draw"
sxd = "sxd"
applicationvndsunxmlwriterglobal = "application/vnd.sun.xml.writer.global"
sxg = "sxg"
applicationvndsunxmlimpress = "application/vnd.sun.xml.impress"
sxi = "sxi"
applicationvndsunxmlmath = "application/vnd.sun.xml.math"
sxm = "sxm"
applicationvndsunxmlwriter = "application/vnd.sun.xml.writer"
sxw = "sxw"
textspreadsheet = "text/spreadsheet"
sylk = "sylk"
slk = "slk"
textxtxt2tags = "text/x-txt2tags"
t2t = "t2t"
applicationxt3vmimage = "application/x-t3vm-image"
t3 = "t3"
imaget38 = "image/t38"
t38 = "t38"
applicationvndmynfc = "application/vnd.mynfc"
taglet = "taglet"
applicationvndtaointentmodulearchive = "application/vnd.tao.intent-module-archive"
tao = "tao"
imagevndtencenttap = "image/vnd.tencent.tap"
tap = "tap"
applicationxtar = "application/x-tar"
tar = "tar"
gtar = "gtar"
gem = "gem"
applicationxbzipcompressedtar = "application/x-bzip-compressed-tar"
tarbz2 = "tarbz2"
tarbz = "tarbz"
tbz2 = "tbz2"
tbz = "tbz"
tb2 = "tb2"
applicationxcompressedtar = "application/x-compressed-tar"
targz = "targz"
tgz = "tgz"
applicationxlrzipcompressedtar = "application/x-lrzip-compressed-tar"
tarlrz = "tarlrz"
tlrz = "tlrz"
applicationxlzipcompressedtar = "application/x-lzip-compressed-tar"
tarlz = "tarlz"
applicationxlz4compressedtar = "application/x-lz4-compressed-tar"
tarlz4 = "tarlz4"
applicationxlzmacompressedtar = "application/x-lzma-compressed-tar"
tarlzma = "tarlzma"
tlz = "tlz"
applicationxtzo = "application/x-tzo"
tarlzo = "tarlzo"
tzo = "tzo"
applicationxxzcompressedtar = "application/x-xz-compressed-tar"
tarxz = "tarxz"
txz = "txz"
applicationxtarz = "application/x-tarz"
tarz = "tarz"
taz = "taz"
applicationxzstdcompressedtar = "application/x-zstd-compressed-tar"
tarzst = "tarzst"
tzst = "tzst"
applicationvnd3gpp2tcap = "application/vnd.3gpp2.tcap"
tcap = "tcap"
texttcl = "text/tcl"
tcl = "tcl"
tk = "tk"
applicationvndsmartteacher = "application/vnd.smart.teacher"
teacher = "teacher"
applicationteixml = "application/tei+xml"
tei = "tei"
teicorpus = "teicorpus"
textxtex = "text/x-tex"
tex = "tex"
ltx = "ltx"
sty = "sty"
cls = "cls"
dtx = "dtx"
ins = "ins"
latex = "latex"
textxtexinfo = "text/x-texinfo"
texi = "texi"
texinfo = "texinfo"
applicationthraudxml = "application/thraud+xml"
tfi = "tfi"
applicationxtextfm = "application/x-tex-tfm"
tfm = "tfm"
imagetifffx = "image/tiff-fx"
tfx = "tfx"
imagextga = "image/x-tga"
tga = "tga"
icb = "icb"
tpic = "tpic"
vda = "vda"
applicationxtheme = "application/x-theme"
theme = "theme"
applicationxwindowsthemepack = "application/x-windows-themepack"
themepack = "themepack"
applicationvndmsofficetheme = "application/vnd.ms-officetheme"
thmx = "thmx"
imagetiff = "image/tiff"
tif = "tif"
tiff = "tiff"
applicationvndtmobilelivetv = "application/vnd.tmobile-livetv"
tmo = "tmo"
applicationvndmstnef = "application/vnd.ms-tnef"
tnef = "tnef"
tnf = "tnf"
winmaildat = "winmaildat"
applicationxcdrdaotoc = "application/x-cdrdao-toc"
toc = "toc"
applicationtoml = "application/toml"
toml = "toml"
applicationxbittorrent = "application/x-bittorrent"
torrent = "torrent"
applicationvndgroovetooltemplate = "application/vnd.groove-tool-template"
tpl = "tpl"
applicationvndtridtpt = "application/vnd.trid.tpt"
tpt = "tpt"
texttroff = "text/troff"
tr = "tr"
roff = "roff"
applicationvndtrueapp = "application/vnd.trueapp"
tra = "tra"
applicationtrig = "application/trig"
trig = "trig"
applicationxmsterminal = "application/x-msterminal"
trm = "trm"
textvndqtlinguist = "text/vnd.qt.linguist"
ts = "ts"
applicationtimestampeddata = "application/timestamped-data"
tsd = "tsd"
texttabseparatedvalues = "text/tab-separated-values"
tsv = "tsv"
audioxtta = "audio/x-tta"
tta = "tta"
fontcollection = "font/collection"
ttc = "ttc"
fontttf = "font/ttf"
ttf = "ttf"
textturtle = "text/turtle"
ttl = "ttl"
applicationttmlxml = "application/ttml+xml"
ttml = "ttml"
applicationxfontttx = "application/x-font-ttx"
ttx = "ttx"
applicationvndsimtechmindmapper = "application/vnd.simtech-mindmapper"
twd = "twd"
twds = "twds"
textxtwig = "text/x-twig"
twig = "twig"
applicationvndgenomatixtuxedo = "application/vnd.genomatix.tuxedo"
txd = "txd"
applicationvndmobiustxf = "application/vnd.mobius.txf"
txf = "txf"
textplain = "text/plain"
txt = "txt"
text = "text"
conf = "conf"
_def = "def"
list = "list"
_in = "in"
ini = "ini"
messageglobaldeliverystatus = "message/global-delivery-status"
u8dsn = "u8dsn"
messageglobalheaders = "message/global-headers"
u8hdr = "u8hdr"
messageglobaldispositionnotification = "message/global-disposition-notification"
u8mdn = "u8mdn"
messageglobal = "message/global"
u8msg = "u8msg"
applicationvndufdl = "application/vnd.ufdl"
ufd = "ufd"
ufdl = "ufdl"
applicationxufraw = "application/x-ufraw"
ufraw = "ufraw"
applicationxdesigner = "application/x-designer"
ui = "ui"
textxuil = "text/x-uil"
uil = "uil"
applicationxglulx = "application/x-glulx"
ulx = "ulx"
applicationvndumajin = "application/vnd.umajin"
umj = "umj"
applicationvndunity = "application/vnd.unity"
unityweb = "unityweb"
applicationvnduomlxml = "application/vnd.uoml+xml"
uoml = "uoml"
texturilist = "text/uri-list"
uri = "uri"
uris = "uris"
urls = "urls"
applicationxmswinurl = "application/x-mswinurl"
url = "url"
modelvndusdzzip = "model/vnd.usdz+zip"
usdz = "usdz"
applicationxustar = "application/x-ustar"
ustar = "ustar"
applicationvnduiqtheme = "application/vnd.uiq.theme"
utz = "utz"
textxuuencode = "text/x-uuencode"
uue = "uue"
uu = "uu"
audiovnddeceaudio = "audio/vnd.dece.audio"
uva = "uva"
uvva = "uvva"
applicationvnddecedata = "application/vnd.dece.data"
uvf = "uvf"
uvvf = "uvvf"
uvd = "uvd"
uvvd = "uvvd"
videovnddecehd = "video/vnd.dece.hd"
uvh = "uvh"
uvvh = "uvvh"
imagevnddecegraphic = "image/vnd.dece.graphic"
uvi = "uvi"
uvvi = "uvvi"
uvg = "uvg"
uvvg = "uvvg"
videovnddecemobile = "video/vnd.dece.mobile"
uvm = "uvm"
uvvm = "uvvm"
videovnddecepd = "video/vnd.dece.pd"
uvp = "uvp"
uvvp = "uvvp"
videovnddecesd = "video/vnd.dece.sd"
uvs = "uvs"
uvvs = "uvvs"
applicationvnddecettmlxml = "application/vnd.dece.ttml+xml"
uvt = "uvt"
uvvt = "uvvt"
videovnduvvump4 = "video/vnd.uvvu.mp4"
uvu = "uvu"
uvvu = "uvvu"
videovnddecevideo = "video/vnd.dece.video"
uvv = "uvv"
uvvv = "uvvv"
applicationvnddeceunspecified = "application/vnd.dece.unspecified"
uvx = "uvx"
uvvx = "uvvx"
applicationvnddecezip = "application/vnd.dece.zip"
uvz = "uvz"
uvvz = "uvvz"
textxverilog = "text/x-verilog"
v = "v"
textxvala = "text/x-vala"
vala = "vala"
vapi = "vapi"
applicationxvirtualboyrom = "application/x-virtual-boy-rom"
vb = "vb"
applicationxvirtualboxvbox = "application/x-virtualbox-vbox"
vbox = "vbox"
applicationxvirtualboxvboxextpack = "application/x-virtualbox-vbox-extpack"
vboxextpack = "vbox-extpack"
textvbscript = "text/vbscript"
vbs = "vbs"
textvcard = "text/vcard"
vcard = "vcard"
vcf = "vcf"
vct = "vct"
gcrd = "gcrd"
applicationxcdlink = "application/x-cdlink"
vcd = "vcd"
applicationvndgroovevcard = "application/vnd.groove-vcard"
vcg = "vcg"
textcalendar = "text/calendar"
vcs = "vcs"
ics = "ics"
ifb = "ifb"
applicationvndvcx = "application/vnd.vcx"
vcx = "vcx"
applicationxvirtualboxvdi = "application/x-virtualbox-vdi"
vdi = "vdi"
textxvhdl = "text/x-vhdl"
vhd = "vhd"
vhdl = "vhdl"
applicationvndvisionary = "application/vnd.visionary"
vis = "vis"
videovndvivo = "video/vnd.vivo"
viv = "viv"
vivo = "vivo"
applicationxvirtualboxvmdk = "application/x-virtualbox-vmdk"
vmdk = "vmdk"
audioxvoc = "audio/x-voc"
voc = "voc"
modelvrml = "model/vrml"
vrm = "vrm"
vrml = "vrml"
wrl = "wrl"
applicationvndvisio = "application/vnd.visio"
vsd = "vsd"
vst = "vst"
vsw = "vsw"
vss = "vss"
applicationvndmsvisiodrawingmacroenabledmainxml = "application/vnd.ms-visio.drawing.macroenabled.main+xml"
vsdm = "vsdm"
applicationvndmsvisiodrawingmainxml = "application/vnd.ms-visio.drawing.main+xml"
vsdx = "vsdx"
applicationvndvsf = "application/vnd.vsf"
vsf = "vsf"
applicationvndmsvisiostencilmacroenabledmainxml = "application/vnd.ms-visio.stencil.macroenabled.main+xml"
vssm = "vssm"
applicationvndmsvisiostencilmainxml = "application/vnd.ms-visio.stencil.main+xml"
vssx = "vssx"
applicationvndmsvisiotemplatemacroenabledmainxml = "application/vnd.ms-visio.template.macroenabled.main+xml"
vstm = "vstm"
applicationvndmsvisiotemplatemainxml = "application/vnd.ms-visio.template.main+xml"
vstx = "vstx"
imagevndvalvesourcetexture = "image/vnd.valve.source.texture"
vtf = "vtf"
textvtt = "text/vtt"
vtt = "vtt"
modelvndvtu = "model/vnd.vtu"
vtu = "vtu"
applicationvoicexmlxml = "application/voicexml+xml"
vxml = "vxml"
applicationxwiiwad = "application/x-wii-wad"
wad = "wad"
applicationvndsunwadlxml = "application/vnd.sun.wadl+xml"
wadl = "wadl"
applicationjavaarchive = "application/java-archive"
war = "war"
ear = "ear"
applicationwasm = "application/wasm"
wasm = "wasm"
audioxwav = "audio/x-wav"
wav = "wav"
applicationxquattropro = "application/x-quattropro"
wb1 = "wb1"
wb2 = "wb2"
wb3 = "wb3"
imagevndwapwbmp = "image/vnd.wap.wbmp"
wbmp = "wbmp"
applicationvndcriticaltoolswbsxml = "application/vnd.criticaltools.wbs+xml"
wbs = "wbs"
applicationvndwapwbxml = "application/vnd.wap.wbxml"
wbxml = "wbxml"
applicationvndmsworks = "application/vnd.ms-works"
wcm = "wcm"
wdb = "wdb"
wps = "wps"
xlr = "xlr"
imagevndmsphoto = "image/vnd.ms-photo"
wdp = "wdp"
audiowebm = "audio/webm"
weba = "weba"
applicationxwebappmanifestjson = "application/x-web-app-manifest+json"
webapp = "webapp"
videowebm = "video/webm"
webm = "webm"
applicationmanifestjson = "application/manifest+json"
webmanifest = "webmanifest"
imagewebp = "image/webp"
webp = "webp"
applicationvndpmiwidget = "application/vnd.pmi.widget"
wg = "wg"
applicationwidget = "application/widget"
wgt = "wgt"
applicationxmswim = "application/x-ms-wim"
wim = "wim"
swm = "swm"
applicationxpartialdownload = "application/x-partial-download"
wkdownload = "wkdownload"
crdownload = "crdownload"
part = "part"
videoxmswm = "video/x-ms-wm"
wm = "wm"
audioxmswma = "audio/x-ms-wma"
wma = "wma"
applicationxmswmd = "application/x-ms-wmd"
wmd = "wmd"
imagewmf = "image/wmf"
wmf = "wmf"
textvndwapwml = "text/vnd.wap.wml"
wml = "wml"
applicationvndwapwmlc = "application/vnd.wap.wmlc"
wmlc = "wmlc"
textvndwapwmlscript = "text/vnd.wap.wmlscript"
wmls = "wmls"
applicationvndwapwmlscriptc = "application/vnd.wap.wmlscriptc"
wmlsc = "wmlsc"
videoxmswmv = "video/x-ms-wmv"
wmv = "wmv"
applicationxmswmz = "application/x-ms-wmz"
wmz = "wmz"
fontwoff = "font/woff"
woff = "woff"
fontwoff2 = "font/woff2"
woff2 = "woff2"
applicationvndwordperfect = "application/vnd.wordperfect"
wp = "wp"
wp4 = "wp4"
wp5 = "wp5"
wp6 = "wp6"
wpd = "wpd"
wpp = "wpp"
applicationxwpg = "application/x-wpg"
wpg = "wpg"
applicationvndmswpl = "application/vnd.ms-wpl"
wpl = "wpl"
applicationvndwqd = "application/vnd.wqd"
wqd = "wqd"
applicationxmswrite = "application/x-mswrite"
wri = "wri"
applicationxwonderswanrom = "application/x-wonderswan-rom"
ws = "ws"
applicationxwonderswancolorrom = "application/x-wonderswan-color-rom"
wsc = "wsc"
applicationwsdlxml = "application/wsdl+xml"
wsdl = "wsdl"
applicationwspolicyxml = "application/wspolicy+xml"
wspolicy = "wspolicy"
applicationvndwebturbo = "application/vnd.webturbo"
wtb = "wtb"
audioxwavpack = "audio/x-wavpack"
wv = "wv"
wvp = "wvp"
audioxwavpackcorrection = "audio/x-wavpack-correction"
wvc = "wvc"
applicationxwwf = "application/x-wwf"
wwf = "wwf"
modelvndparasolidtransmitbinary = "model/vnd.parasolid.transmit.binary"
xb = "x_b"
modelvndparasolidtransmittext = "model/vnd.parasolid.transmit.text"
xt = "x_t"
modelx3dxml = "model/x3d+xml"
x3d = "x3d"
x3dz = "x3dz"
modelx3dbinary = "model/x3d+binary"
x3db = "x3db"
x3dbz = "x3dbz"
modelx3dvrml = "model/x3d+vrml"
x3dv = "x3dv"
x3dvz = "x3dvz"
imagexsigmax3f = "image/x-sigma-x3f"
x3f = "x3f"
applicationxamlxml = "application/xaml+xml"
xaml = "xaml"
applicationxsilverlightapp = "application/x-silverlight-app"
xap = "xap"
applicationxxar = "application/x-xar"
xar = "xar"
pkg = "pkg"
applicationxcapattxml = "application/xcap-att+xml"
xav = "xav"
applicationxmsxbap = "application/x-ms-xbap"
xbap = "xbap"
applicationvndfujixeroxdocuworksbinder = "application/vnd.fujixerox.docuworks.binder"
xbd = "xbd"
applicationxxbel = "application/x-xbel"
xbel = "xbel"
imagexxbitmap = "image/x-xbitmap"
xbm = "xbm"
applicationxcapcapsxml = "application/xcap-caps+xml"
xca = "xca"
imagexxcf = "image/x-xcf"
xcf = "xcf"
imagexcompressedxcf = "image/x-compressed-xcf"
xcfgz = "xcfgz"
xcfbz2 = "xcfbz2"
applicationcalendarxml = "application/calendar+xml"
xcs = "xcs"
applicationmrbconsumerxml = "application/mrb-consumer+xml"
xdf = "xdf"
applicationvndsyncmldmxml = "application/vnd.syncml.dm+xml"
xdm = "xdm"
applicationvndadobexdpxml = "application/vnd.adobe.xdp+xml"
xdp = "xdp"
applicationdsscxml = "application/dssc+xml"
xdssc = "xdssc"
applicationvndfujixeroxdocuworks = "application/vnd.fujixerox.docuworks"
xdw = "xdw"
applicationxcapelxml = "application/xcap-el+xml"
xel = "xel"
applicationxencxml = "application/xenc+xml"
xenc = "xenc"
applicationpatchopserrorxml = "application/patch-ops-error+xml"
xer = "xer"
applicationvndadobexfdf = "application/vnd.adobe.xfdf"
xfdf = "xfdf"
applicationvndxfdl = "application/vnd.xfdl"
xfdl = "xfdl"
applicationxhtmlxml = "application/xhtml+xml"
xhtml = "xhtml"
xht = "xht"
html = "html"
htm = "htm"
audioxxi = "audio/x-xi"
xi = "xi"
imagevndxiff = "image/vnd.xiff"
xif = "xif"
applicationvndmsexceladdinmacroenabled12 = "application/vnd.ms-excel.addin.macroenabled.12"
xlam = "xlam"
applicationxliffxml = "application/xliff+xml"
xlf = "xlf"
xliff = "xliff"
applicationvndmsexcel = "application/vnd.ms-excel"
xls = "xls"
xlc = "xlc"
xll = "xll"
xlm = "xlm"
xlw = "xlw"
xla = "xla"
xlt = "xlt"
xld = "xld"
applicationvndmsexcelsheetbinarymacroenabled12 = "application/vnd.ms-excel.sheet.binary.macroenabled.12"
xlsb = "xlsb"
applicationvndmsexcelsheetmacroenabled12 = "application/vnd.ms-excel.sheet.macroenabled.12"
xlsm = "xlsm"
applicationvndopenxmlformatsofficedocumentspreadsheetmlsheet = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
xlsx = "xlsx"
applicationvndmsexceltemplatemacroenabled12 = "application/vnd.ms-excel.template.macroenabled.12"
xltm = "xltm"
applicationvndopenxmlformatsofficedocumentspreadsheetmltemplate = "application/vnd.openxmlformats-officedocument.spreadsheetml.template"
xltx = "xltx"
audioxxm = "audio/x-xm"
xm = "xm"
audioxxmf = "audio/x-xmf"
xmf = "xmf"
textxxmi = "text/x-xmi"
xmi = "xmi"
applicationxml = "application/xml"
xml = "xml"
xbl = "xbl"
xsd = "xsd"
rng = "rng"
applicationxcapnsxml = "application/xcap-ns+xml"
xns = "xns"
applicationvndolpcsugar = "application/vnd.olpc-sugar"
xo = "xo"
applicationxopxml = "application/xop+xml"
xop = "xop"
applicationxxpinstall = "application/x-xpinstall"
xpi = "xpi"
applicationxprocxml = "application/xproc+xml"
xpl = "xpl"
imagexxpixmap = "image/x-xpixmap"
xpm = "xpm"
applicationvndisxpr = "application/vnd.is-xpr"
xpr = "xpr"
applicationvndinterconformnet = "application/vnd.intercon.formnet"
xpw = "xpw"
xpx = "xpx"
applicationxsltxml = "application/xslt+xml"
xsl = "xsl"
xslt = "xslt"
applicationvndsyncmlxml = "application/vnd.syncml+xml"
xsm = "xsm"
applicationxspfxml = "application/xspf+xml"
xspf = "xspf"
applicationvndmozillaxulxml = "application/vnd.mozilla.xul+xml"
xul = "xul"
imagexxwindowdump = "image/x-xwindowdump"
xwd = "xwd"
chemicalxxyz = "chemical/x-xyz"
xyz = "xyz"
applicationxxz = "application/x-xz"
xz = "xz"
applicationxyaml = "application/x-yaml"
yaml = "yaml"
yml = "yml"
applicationyang = "application/yang"
yang = "yang"
applicationyinxml = "application/yin+xml"
yin = "yin"
textxsuseymp = "text/x-suse-ymp"
ymp = "ymp"
applicationvndyoutubeyt = "application/vnd.youtube.yt"
yt = "yt"
applicationxcompress = "application/x-compress"
z = "z"
applicationxzmachine = "application/x-zmachine"
z1 = "z1"
z2 = "z2"
z3 = "z3"
z4 = "z4"
z5 = "z5"
z6 = "z6"
z7 = "z7"
z8 = "z8"
applicationvndzzazzdeckxml = "application/vnd.zzazz.deck+xml"
zaz = "zaz"
applicationzip = "application/zip"
zip = "zip"
applicationvndzul = "application/vnd.zul"
zir = "zir"
zirz = "zirz"
applicationvndhandheldentertainmentxml = "application/vnd.handheld-entertainment+xml"
zmm = "zmm"
applicationxzoo = "application/x-zoo"
zoo = "zoo"
applicationzstd = "application/zstd"
zst = "zst"
applicationzlib = "application/zlib"
zz = "zz"


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

    if extension == zz:
        return applicationzlib

    if extension == zst:
        return applicationzstd

    if extension == zoo:
        return applicationxzoo

    # iana
    if extension == zmm:
        return applicationvndhandheldentertainmentxml

    # iana
    if extension in (zir, zirz):
        return applicationvndzul

    if extension == zip:
        return applicationzip

    # iana
    if extension == zaz:
        return applicationvndzzazzdeckxml

    # apache
    if extension in (z1, z2, z3, z4, z5, z6, z7, z8):
        return applicationxzmachine

    if extension == z:
        return applicationxcompress

    if extension == yt:
        return applicationvndyoutubeyt

    if extension == ymp:
        return textxsuseymp

    # iana
    if extension == yin:
        return applicationyinxml

    # iana
    if extension == yang:
        return applicationyang

    if extension in (yaml, yml):
        return applicationxyaml

    if extension == xz:
        return applicationxxz

    # apache
    if extension == xyz:
        return chemicalxxyz

    if extension == xwd:
        return imagexxwindowdump

    if extension == xul:
        return applicationvndmozillaxulxml

    if extension == xspf:
        return applicationxspfxml

    # iana
    if extension == xsm:
        return applicationvndsyncmlxml

    if extension in (xsl, xslt):
        return applicationxsltxml

    # iana
    if extension in (xpw, xpx):
        return applicationvndinterconformnet

    # iana
    if extension == xpr:
        return applicationvndisxpr

    if extension == xpm:
        return imagexxpixmap

    # apache
    if extension == xpl:
        return applicationxprocxml

    if extension == xpi:
        return applicationxxpinstall

    # iana
    if extension == xop:
        return applicationxopxml

    # iana
    if extension == xo:
        return applicationvndolpcsugar

    # iana
    if extension == xns:
        return applicationxcapnsxml

    if extension in (xml, xbl, xsd, rng):
        return applicationxml

    if extension == xmi:
        return textxxmi

    if extension == xmf:
        return audioxxmf

    if extension == xm:
        return audioxxm

    if extension == xltx:
        return applicationvndopenxmlformatsofficedocumentspreadsheetmltemplate

    if extension == xltm:
        return applicationvndmsexceltemplatemacroenabled12

    if extension == xlsx:
        return applicationvndopenxmlformatsofficedocumentspreadsheetmlsheet

    if extension == xlsm:
        return applicationvndmsexcelsheetmacroenabled12

    if extension == xlsb:
        return applicationvndmsexcelsheetbinarymacroenabled12

    if extension in (xls, xlc, xll, xlm, xlw, xla, xlt, xld):
        return applicationvndmsexcel

    if extension in (xlf, xliff):
        return applicationxliffxml

    if extension == xlam:
        return applicationvndmsexceladdinmacroenabled12

    # iana
    if extension == xif:
        return imagevndxiff

    if extension == xi:
        return audioxxi

    if extension in (xhtml, xht, html, htm):
        return applicationxhtmlxml

    # iana
    if extension == xfdl:
        return applicationvndxfdl

    # iana
    if extension == xfdf:
        return applicationvndadobexfdf

    # iana
    if extension == xer:
        return applicationpatchopserrorxml

    # iana
    if extension == xenc:
        return applicationxencxml

    # iana
    if extension == xel:
        return applicationxcapelxml

    # iana
    if extension == xdw:
        return applicationvndfujixeroxdocuworks

    # iana
    if extension == xdssc:
        return applicationdsscxml

    # iana
    if extension == xdp:
        return applicationvndadobexdpxml

    # iana
    if extension == xdm:
        return applicationvndsyncmldmxml

    # iana
    if extension == xdf:
        return applicationmrbconsumerxml

    # iana
    if extension == xcs:
        return applicationcalendarxml

    if extension in (xcfgz, xcfbz2):
        return imagexcompressedxcf

    if extension == xcf:
        return imagexxcf

    # iana
    if extension == xca:
        return applicationxcapcapsxml

    if extension == xbm:
        return imagexxbitmap

    if extension == xbel:
        return applicationxxbel

    # iana
    if extension == xbd:
        return applicationvndfujixeroxdocuworksbinder

    # apache
    if extension == xbap:
        return applicationxmsxbap

    # iana
    if extension == xav:
        return applicationxcapattxml

    if extension in (xar, pkg):
        return applicationxxar

    # apache
    if extension == xap:
        return applicationxsilverlightapp

    # apache
    if extension == xaml:
        return applicationxamlxml

    if extension == x3f:
        return imagexsigmax3f

    # apache
    if extension in (x3dv, x3dvz):
        return modelx3dvrml

    # apache
    if extension in (x3db, x3dbz):
        return modelx3dbinary

    # iana
    if extension in (x3d, x3dz):
        return modelx3dxml

    # iana
    if extension == xt:
        return modelvndparasolidtransmittext

    # iana
    if extension == xb:
        return modelvndparasolidtransmitbinary

    if extension == wwf:
        return applicationxwwf

    if extension == wvc:
        return audioxwavpackcorrection

    if extension in (wv, wvp):
        return audioxwavpack

    # iana
    if extension == wtb:
        return applicationvndwebturbo

    # iana
    if extension == wspolicy:
        return applicationwspolicyxml

    # iana
    if extension == wsdl:
        return applicationwsdlxml

    if extension == wsc:
        return applicationxwonderswancolorrom

    if extension == ws:
        return applicationxwonderswanrom

    if extension == wri:
        return applicationxmswrite

    # iana
    if extension == wqd:
        return applicationvndwqd

    if extension == wpl:
        return applicationvndmswpl

    if extension == wpg:
        return applicationxwpg

    if extension in (wp, wp4, wp5, wp6, wpd, wpp):
        return applicationvndwordperfect

    if extension == woff2:
        return fontwoff2

    if extension == woff:
        return fontwoff

    # apache
    if extension == wmz:
        return applicationxmswmz

    if extension == wmv:
        return videoxmswmv

    # iana
    if extension == wmlsc:
        return applicationvndwapwmlscriptc

    if extension == wmls:
        return textvndwapwmlscript

    # iana
    if extension == wmlc:
        return applicationvndwapwmlc

    if extension == wml:
        return textvndwapwml

    if extension == wmf:
        return imagewmf

    # apache
    if extension == wmd:
        return applicationxmswmd

    if extension == wma:
        return audioxmswma

    # apache
    if extension == wm:
        return videoxmswm

    if extension in (wkdownload, crdownload, part):
        return applicationxpartialdownload

    if extension in (wim, swm):
        return applicationxmswim

    # iana
    if extension == wgt:
        return applicationwidget

    # iana
    if extension == wg:
        return applicationvndpmiwidget

    if extension == webp:
        return imagewebp

    if extension == webmanifest:
        return applicationmanifestjson

    if extension == webm:
        return videowebm

    if extension == webapp:
        return applicationxwebappmanifestjson

    # apache
    if extension == weba:
        return audiowebm

    # apache
    if extension == wdp:
        return imagevndmsphoto

    if extension in (wcm, wdb, wps, xlr):
        return applicationvndmsworks

    # iana
    if extension == wbxml:
        return applicationvndwapwbxml

    # iana
    if extension == wbs:
        return applicationvndcriticaltoolswbsxml

    if extension == wbmp:
        return imagevndwapwbmp

    if extension in (wb1, wb2, wb3):
        return applicationxquattropro

    if extension == wav:
        return audioxwav

    if extension == wasm:
        return applicationwasm

    # apache
    if extension in (war, ear):
        return applicationjavaarchive

    # iana
    if extension == wadl:
        return applicationvndsunwadlxml

    if extension == wad:
        return applicationxwiiwad

    # iana
    if extension == vxml:
        return applicationvoicexmlxml

    # iana
    if extension == vtu:
        return modelvndvtu

    if extension == vtt:
        return textvtt

    # iana
    if extension == vtf:
        return imagevndvalvesourcetexture

    if extension == vstx:
        return applicationvndmsvisiotemplatemainxml

    if extension == vstm:
        return applicationvndmsvisiotemplatemacroenabledmainxml

    if extension == vssx:
        return applicationvndmsvisiostencilmainxml

    if extension == vssm:
        return applicationvndmsvisiostencilmacroenabledmainxml

    # iana
    if extension == vsf:
        return applicationvndvsf

    if extension == vsdx:
        return applicationvndmsvisiodrawingmainxml

    if extension == vsdm:
        return applicationvndmsvisiodrawingmacroenabledmainxml

    if extension in (vsd, vst, vsw, vss):
        return applicationvndvisio

    if extension in (vrm, vrml, wrl):
        return modelvrml

    if extension == voc:
        return audioxvoc

    if extension == vmdk:
        return applicationxvirtualboxvmdk

    if extension in (viv, vivo):
        return videovndvivo

    # iana
    if extension == vis:
        return applicationvndvisionary

    if extension in (vhd, vhdl):
        return textxvhdl

    if extension == vdi:
        return applicationxvirtualboxvdi

    # iana
    if extension == vcx:
        return applicationvndvcx

    if extension in (vcs, ics, ifb):
        return textcalendar

    # iana
    if extension == vcg:
        return applicationvndgroovevcard

    # apache
    if extension == vcd:
        return applicationxcdlink

    if extension in (vcard, vcf, vct, gcrd):
        return textvcard

    if extension == vbs:
        return textvbscript

    if extension == vboxextpack:
        return applicationxvirtualboxvboxextpack

    if extension == vbox:
        return applicationxvirtualboxvbox

    if extension == vb:
        return applicationxvirtualboyrom

    if extension in (vala, vapi):
        return textxvala

    if extension == v:
        return textxverilog

    # iana
    if extension in (uvz, uvvz):
        return applicationvnddecezip

    # iana
    if extension in (uvx, uvvx):
        return applicationvnddeceunspecified

    # iana
    if extension in (uvv, uvvv):
        return videovnddecevideo

    # iana
    if extension in (uvu, uvvu):
        return videovnduvvump4

    # iana
    if extension in (uvt, uvvt):
        return applicationvnddecettmlxml

    # iana
    if extension in (uvs, uvvs):
        return videovnddecesd

    # iana
    if extension in (uvp, uvvp):
        return videovnddecepd

    # iana
    if extension in (uvm, uvvm):
        return videovnddecemobile

    # iana
    if extension in (uvi, uvvi, uvg, uvvg):
        return imagevnddecegraphic

    # iana
    if extension in (uvh, uvvh):
        return videovnddecehd

    # iana
    if extension in (uvf, uvvf, uvd, uvvd):
        return applicationvnddecedata

    # iana
    if extension in (uva, uvva):
        return audiovnddeceaudio

    if extension in (uue, uu):
        return textxuuencode

    # iana
    if extension == utz:
        return applicationvnduiqtheme

    if extension == ustar:
        return applicationxustar

    # iana
    if extension == usdz:
        return modelvndusdzzip

    if extension == url:
        return applicationxmswinurl

    # iana
    if extension in (uri, uris, urls):
        return texturilist

    # iana
    if extension == uoml:
        return applicationvnduomlxml

    # iana
    if extension == unityweb:
        return applicationvndunity

    # iana
    if extension == umj:
        return applicationvndumajin

    # apache
    if extension == ulx:
        return applicationxglulx

    if extension == uil:
        return textxuil

    if extension == ui:
        return applicationxdesigner

    if extension == ufraw:
        return applicationxufraw

    # iana
    if extension in (ufd, ufdl):
        return applicationvndufdl

    # iana
    if extension == u8msg:
        return messageglobal

    # iana
    if extension == u8mdn:
        return messageglobaldispositionnotification

    # iana
    if extension == u8hdr:
        return messageglobalheaders

    # iana
    if extension == u8dsn:
        return messageglobaldeliverystatus

    if extension in (txt, text, conf, _def, list, _in, ini):
        return textplain

    # iana
    if extension == txf:
        return applicationvndmobiustxf

    # iana
    if extension == txd:
        return applicationvndgenomatixtuxedo

    if extension == twig:
        return textxtwig

    # iana
    if extension in (twd, twds):
        return applicationvndsimtechmindmapper

    if extension == ttx:
        return applicationxfontttx

    # iana
    if extension == ttml:
        return applicationttmlxml

    if extension == ttl:
        return textturtle

    if extension == ttf:
        return fontttf

    if extension == ttc:
        return fontcollection

    if extension == tta:
        return audioxtta

    if extension == tsv:
        return texttabseparatedvalues

    # iana
    if extension == tsd:
        return applicationtimestampeddata

    if extension == ts:
        return textvndqtlinguist

    # apache
    if extension == trm:
        return applicationxmsterminal

    if extension == trig:
        return applicationtrig

    # iana
    if extension == tra:
        return applicationvndtrueapp

    if extension in (tr, roff):
        return texttroff

    # iana
    if extension == tpt:
        return applicationvndtridtpt

    # iana
    if extension == tpl:
        return applicationvndgroovetooltemplate

    if extension == torrent:
        return applicationxbittorrent

    if extension == toml:
        return applicationtoml

    if extension == toc:
        return applicationxcdrdaotoc

    if extension in (tnef, tnf, winmaildat):
        return applicationvndmstnef

    # iana
    if extension == tmo:
        return applicationvndtmobilelivetv

    if extension in (tif, tiff):
        return imagetiff

    # iana
    if extension == thmx:
        return applicationvndmsofficetheme

    if extension == themepack:
        return applicationxwindowsthemepack

    if extension == theme:
        return applicationxtheme

    if extension in (tga, icb, tpic, vda):
        return imagextga

    # iana
    if extension == tfx:
        return imagetifffx

    # apache
    if extension == tfm:
        return applicationxtextfm

    # iana
    if extension == tfi:
        return applicationthraudxml

    if extension in (texi, texinfo):
        return textxtexinfo

    if extension in (tex, ltx, sty, cls, dtx, ins, latex):
        return textxtex

    # iana
    if extension in (tei, teicorpus):
        return applicationteixml

    # iana
    if extension == teacher:
        return applicationvndsmartteacher

    if extension in (tcl, tk):
        return texttcl

    # iana
    if extension == tcap:
        return applicationvnd3gpp2tcap

    if extension in (tarzst, tzst):
        return applicationxzstdcompressedtar

    if extension in (tarz, taz):
        return applicationxtarz

    if extension in (tarxz, txz):
        return applicationxxzcompressedtar

    if extension in (tarlzo, tzo):
        return applicationxtzo

    if extension in (tarlzma, tlz):
        return applicationxlzmacompressedtar

    if extension == tarlz4:
        return applicationxlz4compressedtar

    if extension == tarlz:
        return applicationxlzipcompressedtar

    if extension in (tarlrz, tlrz):
        return applicationxlrzipcompressedtar

    if extension in (targz, tgz):
        return applicationxcompressedtar

    if extension in (tarbz2, tarbz, tbz2, tbz, tb2):
        return applicationxbzipcompressedtar

    if extension in (tar, gtar, gem):
        return applicationxtar

    # iana
    if extension == tap:
        return imagevndtencenttap

    # iana
    if extension == tao:
        return applicationvndtaointentmodulearchive

    # iana
    if extension == taglet:
        return applicationvndmynfc

    # iana
    if extension == t38:
        return imaget38

    # apache
    if extension == t3:
        return applicationxt3vmimage

    if extension == t2t:
        return textxtxt2tags

    if extension in (sylk, slk):
        return textspreadsheet

    if extension == sxw:
        return applicationvndsunxmlwriter

    if extension == sxm:
        return applicationvndsunxmlmath

    if extension == sxi:
        return applicationvndsunxmlimpress

    if extension == sxg:
        return applicationvndsunxmlwriterglobal

    if extension == sxd:
        return applicationvndsunxmldraw

    if extension == sxc:
        return applicationvndsunxmlcalc

    # iana
    if extension == swidtag:
        return applicationswidxml

    # iana
    if extension == swi:
        return applicationvndaristanetworksswi

    if extension in (swf, spl):
        return applicationvndadobeflashmovie

    if extension == svh:
        return textxsvhdr

    if extension == svgz:
        return imagesvgxmlcompressed

    if extension == svg:
        return imagesvgxml

    # iana
    if extension == svd:
        return applicationvndsvd

    # iana
    if extension == svc:
        return applicationvnddvbservice

    if extension == sv4crc:
        return applicationxsv4crc

    if extension == sv4cpio:
        return applicationxsv4cpio

    if extension == sv:
        return textxsvsrc

    # iana
    if extension in (sus, susp):
        return applicationvndsuscalendar

    if extension == sun:
        return imagexsunraster

    if extension == sub:
        return textxmicrodvd

    if extension in (stylus, styl):
        return textstylus

    if extension == stw:
        return applicationvndsunxmlwritertemplate

    # iana
    if extension == str:
        return applicationvndpgformat

    if extension == stm:
        return audioxstm

    if extension == stl:
        return modelstl

    # iana
    if extension == stk:
        return applicationhyperstudio

    if extension == sti:
        return applicationvndsunxmlimpresstemplate

    # iana
    if extension == stf:
        return applicationvndwtstf

    if extension == std:
        return applicationvndsunxmldrawtemplate

    if extension == stc:
        return applicationvndsunxmlcalctemplate

    # iana
    if extension == st:
        return applicationvndsailingtrackertrack

    # iana
    if extension == ssml:
        return applicationssmlxml

    # iana
    if extension == ssf:
        return applicationvndepsonssf

    # iana
    if extension == sse:
        return applicationvndkodakdescriptor

    # apache
    if extension == ssdl:
        return applicationssdlxml

    if extension in (ssa, ass):
        return textxssa

    # iana
    if extension == srx:
        return applicationsparqlresultsxml

    # iana
    if extension == sru:
        return applicationsruxml

    if extension == srt:
        return applicationxsubrip

    if extension == srf:
        return imagexsonysrf

    if extension in (srcrpm, spm):
        return applicationxsourcerpm

    if extension == src:
        return applicationxwaissource

    if extension == sr2:
        return imagexsonysr2

    if extension == sqsh:
        return applicationvndsquashfs

    if extension == sqlite3:
        return applicationvndsqlite3

    if extension == sqlite2:
        return applicationxsqlite2

    if extension == sql:
        return applicationsql

    if extension == spx:
        return audioxspeex

    # iana
    if extension == spq:
        return applicationscvpvprequest

    # iana
    if extension == spp:
        return applicationscvpvpresponse

    # iana
    if extension == spot:
        return textvndin3dspot

    # iana
    if extension == spf:
        return applicationvndyamahasmafphrase

    if extension == spec:
        return textxrpmspec

    if extension == spd:
        return applicationxfontspeedo

    if extension == so:
        return applicationxsharedlib

    # apache
    if extension == snf:
        return applicationxfontsnf

    if extension == snap:
        return applicationvndsnap

    # iana
    if extension == smzip:
        return applicationvndstepmaniapackage

    # apache
    if extension == smv:
        return videoxsmv

    if extension == sms:
        return applicationxsmsrom

    if extension in (smil, smi, sml, kino):
        return applicationsmilxml

    if extension == smf:
        return applicationvndstardivisionmath

    if extension == smd:
        return applicationvndstardivisionmail

    # iana
    if extension == sm:
        return applicationvndstepmaniastepchart

    # iana
    if extension == slt:
        return applicationvndepsonsalt

    # iana
    if extension == sls:
        return applicationroutestsidxml

    if extension in (slim, slm):
        return textslim

    if extension == sldx:
        return applicationvndopenxmlformatsofficedocumentpresentationmlslide

    if extension == sldm:
        return applicationvndmspowerpointslidemacroenabled12

    if extension in (skr, pkr, key):
        return applicationpgpkeys

    # iana
    if extension in (skp, skd, skt, skm):
        return applicationvndkoan

    if extension in (sk, sk1):
        return imagexskencil

    if extension in (siv, sieve):
        return applicationsieve

    # apache
    if extension == sitx:
        return applicationxstuffitx

    if extension == sit:
        return applicationxstuffit

    if extension == sisx:
        return xepocxsisxapp

    if extension == sis:
        return applicationvndsymbianinstall

    # apache
    if extension == sil:
        return audiosilk

    if extension == sig:
        return applicationpgpsignature

    if extension in (sid, psid):
        return audioprssid

    if extension == siag:
        return applicationxsiag

    # iana
    if extension == shtml:
        return texthtml

    if extension == shn:
        return applicationxshorten

    # iana
    if extension == shf:
        return applicationshfxml

    if extension == shex:
        return textshex

    if extension == shar:
        return applicationxshar

    if extension == shape:
        return applicationxdiashape

    if extension == sh:
        return applicationxshellscript

    if extension in (sgml, sgm):
        return textsgml

    if extension == sgi:
        return imagexsgi

    if extension == sgf:
        return applicationxgosgf

    if extension == sg:
        return applicationxsg1000rom

    # apache
    if extension == sfv:
        return textxsfv

    # iana
    if extension == sfs:
        return applicationvndspotfiresfs

    # iana
    if extension == sfdhdstx:
        return applicationvndhydrostatixsofdata

    if extension in (sfc, smc):
        return applicationvndnintendosnesrom

    # iana
    if extension == setreg:
        return applicationsetregistrationinitiation

    # iana
    if extension == setpay:
        return applicationsetpaymentinitiation

    if extension == service:
        return textxdbusservice

    # apache
    if extension == ser:
        return applicationjavaserializedobject

    # iana
    if extension == sensmlx:
        return applicationsensmlxml

    # iana
    if extension == senmlx:
        return applicationsenmlxml

    # iana
    if extension == semf:
        return applicationvndsemf

    # iana
    if extension == semd:
        return applicationvndsemd

    # iana
    if extension == sema:
        return applicationvndsema

    # iana
    if extension in (seed, dataless):
        return applicationvndfdsnseed

    # iana
    if extension == see:
        return applicationvndseemail

    # nginx
    if extension == sea:
        return applicationxsea

    if extension in (sdw, vor, sgl):
        return applicationvndstardivisionwriter

    if extension == sds:
        return applicationvndstardivisionchart

    # iana
    if extension in (sdkm, sdkd):
        return applicationvndsolentsdkmxml

    if extension in (sdd, sdp):
        return applicationvndstardivisionimpress

    if extension == sdc:
        return applicationvndstardivisioncalc

    if extension == sda:
        return applicationvndstardivisiondraw

    # apache
    if extension == scurl:
        return textvndcurlscurl

    if extension == scss:
        return textxscss

    # iana
    if extension == scs:
        return applicationscvpcvresponse

    # iana
    if extension == scq:
        return applicationscvpcvrequest

    if extension in (sconstruct, sconscript):
        return textxscons

    if extension in (scm, ss):
        return textxscheme

    # apache
    if extension == scd:
        return applicationxmsschedule

    if extension == scala:
        return textxscala

    # iana
    if extension == sc:
        return applicationvndibmsecurecontainer

    # iana
    if extension == sbml:
        return applicationsbmlxml

    if extension in (sav, zsav):
        return applicationxspsssav

    if extension == sass:
        return textxsass

    if extension == sap:
        return applicationxthomsonsapimage

    if extension == sami:
        return applicationxsami

    if extension == sam:
        return applicationxamipro

    # iana
    if extension == saf:
        return applicationvndyamahasmafaudio

    if extension == s3m:
        return audioxs3m

    # apache
    if extension in (s, asm):
        return textxasm

    if extension == rw2:
        return imagexpanasonicrw2

    if extension in (rv, rvx):
        return videovndrnrealvideo

    # iana
    if extension == rusd:
        return applicationrouteusdxml

    # nginx
    if extension == run:
        return applicationxmakeself

    if extension == rtx:
        return textrichtext

    if extension == rtf:
        return applicationrtf

    if extension == rt:
        return textvndrnrealtext

    if extension == rst:
        return textxrst

    if extension == rss:
        return applicationrssxml

    # iana
    if extension == rsheet:
        return applicationurcressheetxml

    # apache
    if extension == rsd:
        return applicationrsdxml

    # iana
    if extension == rsat:
        return applicationatscrsatxml

    if extension == rs:
        return textrust

    # iana
    if extension == rq:
        return applicationsparqlquery

    # iana
    if extension == rpst:
        return applicationvndnokiaradiopreset

    # iana
    if extension == rpss:
        return applicationvndnokiaradiopresets

    if extension == rpm:
        return applicationxrpm

    # iana
    if extension == rp9:
        return applicationvndcloantorp9

    if extension == rp:
        return imagevndrnrealpix

    # iana
    if extension == roa:
        return applicationrpkiroa

    if extension == rnc:
        return applicationrelaxngcompactsyntax

    # apache
    if extension == rmp:
        return audioxpnrealaudioplugin

    if extension == rmail:
        return messagexgnurmail

    if extension in (rm, rmj, rmm, rms, rmx, rmvb):
        return applicationvndrnrealmedia

    if extension == rle:
        return imagerle

    # iana
    if extension == rld:
        return applicationresourcelistsdiffxml

    # iana
    if extension == rlc:
        return imagevndfujixeroxedmicsrlc

    # iana
    if extension == rl:
        return applicationresourcelistsxml

    # apache
    if extension == ris:
        return applicationxresearchinfosystems

    # iana
    if extension == rip:
        return audiovndrip

    # iana
    if extension == rif:
        return applicationreginfoxml

    if extension == rgb:
        return imagexrgb

    # apache
    if extension == res:
        return applicationxdtbresourcexml

    # iana
    if extension == rep:
        return applicationvndbusinessobjects

    # iana
    if extension == relo:
        return applicationp2poverlayxml

    if extension == rej:
        return textxreject

    if extension == reg:
        return textxmsregedit

    if extension == readme:
        return textxreadme

    # iana
    if extension == rdz:
        return applicationvnddatavisionrdz

    if extension in (rdf, rdfs, owl):
        return applicationrdfxml

    # iana
    if extension == rcprofile:
        return applicationvndipunpluggedrcprofile

    if extension == rb:
        return applicationxruby

    if extension in (rawdiskimagexz, imgxz):
        return applicationxrawdiskimagexzcompressed

    if extension in (rawdiskimage, img):
        return applicationxrawdiskimage

    if extension == raw:
        return imagexpanasonicrw

    if extension == ras:
        return imagexcmuraster

    if extension == rar:
        return applicationvndrar

    # iana
    if extension == rapd:
        return applicationrouteapdxml

    if extension == raml:
        return applicationramlyaml

    if extension == ram:
        return applicationram

    if extension == raf:
        return imagexfujiraf

    if extension in (ra, rax):
        return audiovndrnrealaudio

    # iana
    if extension in (qxd, qxt, qwd, qwt, qxl, qxb):
        return applicationvndquarkquarkxpress

    if extension == qtl:
        return applicationxquicktimemedialink

    if extension == qtif:
        return imagexquicktime

    if extension in (qti, qtigz):
        return applicationxqtiplot

    if extension in (qt, mov, moov, qtvr):
        return videoquicktime

    # iana
    if extension == qps:
        return applicationvndpublisharedeltatree

    if extension == qp:
        return applicationxqpress

    if extension in (qml, qmltypes, qmlproject):
        return textxqml

    if extension == qif:
        return applicationxqw

    # iana
    if extension == qfx:
        return applicationvndintuqfx

    if extension in (qcow2, qcow):
        return applicationxqemudisk

    # iana
    if extension == qbo:
        return applicationvndintuqbo

    # iana
    if extension == qam:
        return applicationvndepsonquickanime

    if extension in (pyx, wsgi):
        return textxpython

    # iana
    if extension == pyv:
        return videovndmsplayreadymediapyv

    if extension == pysu:
        return applicationxpyspreadspreadsheet

    if extension == pys:
        return applicationxpyspreadbzspreadsheet

    if extension in (pyc, pyo):
        return applicationxpythonbytecode

    # iana
    if extension == pya:
        return audiovndmsplayreadymediapya

    if extension in (py, py3, py3x):
        return textxpython3

    # iana
    if extension == pwn:
        return applicationvnd3mpostitnotes

    if extension == pw:
        return applicationxpw

    # iana
    if extension == pvb:
        return applicationvnd3gpppicbwvar

    if extension == pub:
        return applicationvndmspublisher

    # iana
    if extension == ptid:
        return applicationvndpviptid1

    # iana
    if extension == pti:
        return imageprspti

    if extension == psw:
        return applicationxpocketword

    # iana
    if extension == pskcxml:
        return applicationpskcxml

    if extension == psgz:
        return applicationxgzpostscript

    if extension == psflib:
        return audioxpsflib

    if extension == psfgz:
        return applicationxgzfontlinuxpsf

    if extension == psf:
        return applicationxfontlinuxpsf

    if extension == psd:
        return imagevndadobephotoshop

    if extension == psbz2:
        return applicationxbzpostscript

    # iana
    if extension == psb:
        return applicationvnd3gpppicbwsmall

    if extension == ps:
        return applicationpostscript

    # iana
    if extension == provx:
        return applicationprovenancexml

    # apache
    if extension == prf:
        return applicationpicsrules

    # iana
    if extension == pre:
        return applicationvndlotusfreelance

    if extension in (pqa, oprc):
        return applicationvndpalm

    if extension in (ppz, ppt, pps, pot):
        return applicationvndmspowerpoint

    if extension == pptx:
        return applicationvndopenxmlformatsofficedocumentpresentationmlpresentation

    if extension == pptm:
        return applicationvndmspowerpointpresentationmacroenabled12

    if extension == ppsx:
        return applicationvndopenxmlformatsofficedocumentpresentationmlslideshow

    if extension == ppsm:
        return applicationvndmspowerpointslideshowmacroenabled12

    if extension == ppm:
        return imagexportablepixmap

    # iana
    if extension == ppd:
        return applicationvndcupsppd

    if extension == ppam:
        return applicationvndmspowerpointaddinmacroenabled12

    if extension == potx:
        return applicationvndopenxmlformatsofficedocumentpresentationmltemplate

    if extension == potm:
        return applicationvndmspowerpointtemplatemacroenabled12

    # iana
    if extension == portpkg:
        return applicationvndmacportsportpkg

    if extension == por:
        return applicationxspsspor

    if extension in (pomxml, settingsxml):
        return textxmavenxml

    if extension == po:
        return textxgettexttranslation

    if extension == pntg:
        return imagexmacpaint

    if extension == pnm:
        return imagexportableanymap

    if extension == png:
        return imagepng

    # iana
    if extension == pml:
        return applicationvndctcposml

    if extension == pls:
        return audioxscpls

    if extension == pln:
        return applicationxplanperfect

    # iana
    if extension == plf:
        return applicationvndpocketlearn

    # iana
    if extension == plc:
        return applicationvndmobiusplc

    # iana
    if extension == plb:
        return applicationvnd3gpppicbwlarge

    if extension == pla:
        return audioxiriverpla

    if extension in (pl, pm, al, perl, pod, t):
        return applicationxperl

    if extension == pkpass:
        return applicationvndapplepkpass

    if extension == pkipath:
        return applicationpkixpkipath

    # iana
    if extension == pki:
        return applicationpkixcmp

    if extension == pk:
        return applicationxtexpk

    if extension in (php, php3, php4, php5, phps):
        return applicationxphp

    if extension in (pgp, gpg, asc):
        return applicationpgpencrypted

    if extension == pgn:
        return applicationvndchesspgn

    if extension == pgm:
        return imagexportablegraymap

    # iana
    if extension == pfr:
        return applicationfonttdpfr

    if extension in (pfa, pfb, gsf, pfm):
        return applicationxfonttype1

    if extension == pef:
        return imagexpentaxpef

    if extension == pdfxz:
        return applicationxxzpdf

    if extension == pdflz:
        return applicationxlzpdf

    if extension == pdfgz:
        return applicationxgzpdf

    if extension == pdfbz2:
        return applicationxbzpdf

    if extension == pdf:
        return applicationpdf

    if extension == pde:
        return textxprocessing

    if extension in (pdb, pdc):
        return applicationxaportisdoc

    if extension == pcx:
        return imagevndzbrushpcx

    # apache
    if extension == pcurl:
        return applicationvndcurlpcurl

    if extension in (pct, pict, pict1, pict2, pic):
        return imagexpict

    # iana
    if extension == pclxl:
        return applicationvndhppclxl

    if extension == pcl:
        return applicationvndhppcl

    if extension in (pcf, pcfz, pcfgz):
        return applicationxfontpcf

    if extension == pce:
        return applicationxpcenginerom

    if extension == pcd:
        return imagexphotocd

    if extension in (pcap, cap, dmp):
        return applicationvndtcpdumppcap

    if extension == pbm:
        return imagexportablebitmap

    # iana
    if extension == pbd:
        return applicationvndpowerbuilder6

    # iana
    if extension == paw:
        return applicationvndpawaafile

    if extension == pat:
        return imagexgimppat

    if extension == par2:
        return applicationxpar2

    if extension == pak:
        return applicationxpak

    # iana
    if extension == pages:
        return applicationvndapplepages

    if extension == pack:
        return applicationxjavapack200

    if extension == pac:
        return applicationxnsproxyautoconfig

    if extension == p8e:
        return applicationpkcs8encrypted

    if extension == p8:
        return applicationpkcs8

    if extension == p7s:
        return applicationpkcs7signature

    # apache
    if extension == p7r:
        return applicationxpkcs7certreqresp

    if extension in (p7c, p7m):
        return applicationpkcs7mime

    if extension in (p7b, spc):
        return applicationxpkcs7certificates

    if extension in (p65, pm6, pmd):
        return applicationxpagemaker

    if extension in (p12, pfx):
        return applicationpkcs12

    if extension == p10:
        return applicationpkcs10

    if extension in (p, pas):
        return textxpascal

    if extension == oxt:
        return applicationvndopenofficeorgextension

    if extension in (oxps, xps):
        return applicationoxps

    if extension == owx:
        return applicationowlxml

    if extension == ovf:
        return applicationxvirtualboxovf

    if extension == ova:
        return applicationxvirtualboxova

    if extension == ott:
        return applicationvndoasisopendocumenttexttemplate

    if extension == ots:
        return applicationvndoasisopendocumentspreadsheettemplate

    if extension == otp:
        return applicationvndoasisopendocumentpresentationtemplate

    # iana
    if extension == oti:
        return applicationvndoasisopendocumentimagetemplate

    if extension == oth:
        return applicationvndoasisopendocumenttextweb

    if extension == otg:
        return applicationvndoasisopendocumentgraphicstemplate

    if extension in (otf, odft):
        return applicationvndoasisopendocumentformulatemplate

    if extension == otc:
        return applicationvndoasisopendocumentcharttemplate

    # iana
    if extension == osm:
        return applicationvndopenstreetmapdataxml

    # iana
    if extension == osfpvg:
        return applicationvndyamahaopenscoreformatosfpvgxml

    # iana
    if extension == osf:
        return applicationvndyamahaopenscoreformat

    # iana
    if extension == org:
        return applicationvndlotusorganizer

    if extension == orf:
        return imagexolympusorf

    if extension == ora:
        return imageopenraster

    if extension == opml:
        return textxopmlxml

    # iana
    if extension == opf:
        return applicationoebpspackagexml

    if extension == ooc:
        return textxooc

    # apache
    if extension in (onetoc, onetoc2, onetmp, onepkg):
        return applicationonenote

    # apache
    if extension == omdoc:
        return applicationomdocxml

    if extension == oleo:
        return applicationxoleo

    if extension == ogx:
        return applicationogg

    if extension == ogv:
        return videoogg

    if extension == ogm:
        return videoxogmogg

    # iana
    if extension == ogex:
        return modelvndopengex

    if extension in (oga, ogg, opus):
        return audioogg

    if extension == odt:
        return applicationvndoasisopendocumenttext

    if extension == ods:
        return applicationvndoasisopendocumentspreadsheet

    if extension == odp:
        return applicationvndoasisopendocumentpresentation

    if extension == odm:
        return applicationvndoasisopendocumenttextmaster

    if extension == odi:
        return applicationvndoasisopendocumentimage

    if extension == odg:
        return applicationvndoasisopendocumentgraphics

    if extension == odf:
        return applicationvndoasisopendocumentformula

    if extension == odc:
        return applicationvndoasisopendocumentchart

    if extension == odb:
        return applicationvndoasisopendocumentdatabase

    if extension == oda:
        return applicationoda

    if extension == ocl:
        return textxocl

    if extension == obj:
        return applicationxtgif

    # iana
    if extension == obgx:
        return applicationvndopenbloxgamexml

    # apache
    if extension == obd:
        return applicationxmsbinder

    # iana
    if extension == oas:
        return applicationvndfujitsuoasys

    # iana
    if extension == oa3:
        return applicationvndfujitsuoasys3

    # iana
    if extension == oa2:
        return applicationvndfujitsuoasys2

    if extension == o:
        return applicationxobject

    if extension == nzb:
        return applicationxnzb

    # iana
    if extension == numbers:
        return applicationvndapplenumbers

    # iana
    if extension in (ntf, nitf):
        return applicationvndnitf

    # iana
    if extension == nt:
        return applicationntriples

    if extension == nsv:
        return videoxnsv

    # iana
    if extension == nsf:
        return applicationvndlotusnotes

    if extension == nsc:
        return applicationxnetshowchannel

    # iana
    if extension == nq:
        return applicationnquads

    # iana
    if extension == npx:
        return imagevndnetfpx

    # iana
    if extension == nnw:
        return applicationvndnoblenetweb

    # iana
    if extension == nns:
        return applicationvndnoblenetsealer

    # iana
    if extension == nnd:
        return applicationvndnoblenetdirectory

    # iana
    if extension == nml:
        return applicationvndenliven

    # iana
    if extension == nlu:
        return applicationvndneurolanguagenlu

    if extension == ngp:
        return applicationxneogeopocketrom

    # iana
    if extension == ngdat:
        return applicationvndnokiangagedata

    if extension == ngc:
        return applicationxneogeopocketcolorrom

    # iana
    if extension == ngage:
        return applicationvndnokiangagesymbianinstall

    if extension == nfo:
        return textxnfo

    if extension in (nes, nez, unf, unif):
        return applicationxnesrom

    if extension == nef:
        return imagexnikonnef

    if extension == nds:
        return applicationxnintendodsrom

    # apache
    if extension == ncx:
        return applicationxdtbncxxml

    # iana
    if extension == nbp:
        return applicationvndwolframplayer

    if extension in (nb, ma, mb):
        return applicationmathematica

    if extension in (n64, z64, v64):
        return applicationxn64rom

    # iana
    if extension == n3:
        return textn3

    # iana
    if extension == mxs:
        return applicationvndtriscapemxs

    # iana
    if extension in (mxml, xhvml, xvml, xvm):
        return applicationxvxml

    # iana
    if extension == mxmf:
        return audiomobilexmf

    # iana
    if extension == mxl:
        return applicationvndrecordaremusicxml

    if extension == mxf:
        return applicationmxf

    # iana
    if extension == mwf:
        return applicationvndmfer

    # apache
    if extension in (mvb, m13, m14):
        return applicationxmsmediaview

    # iana
    if extension == musicxml:
        return applicationvndrecordaremusicxmlxml

    # iana
    if extension == musd:
        return applicationmmtusdxml

    # iana
    if extension == mus:
        return applicationvndmusician

    if extension in (mup, _not):
        return textxmup

    # iana
    if extension == mtl:
        return modelmtl

    if extension == msx:
        return applicationxmsxrom

    # iana
    if extension == msty:
        return applicationvndmuveestyle

    if extension == msod:
        return imagexmsod

    # iana
    if extension == msl:
        return applicationvndmobiusmsl

    if extension == msi:
        return applicationxmsi

    # iana
    if extension in (msh, mesh, silo):
        return modelmesh

    if extension == msg:
        return applicationvndmsoutlook

    # iana
    if extension == msf:
        return applicationvndepsonmsf

    # iana
    if extension == mseq:
        return applicationvndmseq

    # iana
    if extension == mseed:
        return applicationvndfdsnmseed

    # iana
    if extension == mscml:
        return applicationmediaservercontrolxml

    if extension == ms:
        return textxtroffms

    if extension == mrw:
        return imagexminoltamrw

    if extension in (mrml, mrl):
        return textxmrml

    # iana
    if extension == mrcx:
        return applicationmarcxmlxml

    # iana
    if extension == mrc:
        return applicationmarc

    # iana
    if extension == mqy:
        return applicationvndmobiusmqy

    # iana
    if extension == mpy:
        return applicationvndibmminipay

    # iana
    if extension == mpt:
        return applicationvndmsproject

    # iana
    if extension == mpn:
        return applicationvndmophunapplication

    # iana
    if extension == mpm:
        return applicationvndblueicemultipass

    # iana
    if extension == mpkg:
        return applicationvndappleinstallerxml

    if extension in (mpeg, mpg, mpe, vob, _090909vdr, m1v, m2v):
        return videompeg

    # iana
    if extension == mpd:
        return applicationdashxml

    if extension in (mpc, mpp, mp):
        return audioxmusepack

    # iana
    if extension in (mp4s, m4p):
        return applicationmp4

    if extension in (mp4, m4v, f4v, lrv, mp4v, mpg4):
        return videomp4

    if extension in (mp3, mpga, mp2a, m2a, m3a):
        return audiompeg

    if extension == mp2:
        return audiomp2

    if extension == movie:
        return videoxsgimovie

    if extension == mof:
        return textxmof

    # iana
    if extension == mods:
        return applicationmodsxml

    if extension in (mod, ult, uni, m15, mtm, _669, med):
        return audioxmod

    if extension == moc:
        return textxmoc

    if extension in (mobi, prc):
        return applicationxmobipocketebook

    if extension == mo3:
        return audioxmo3

    # apache
    if extension == mny:
        return applicationxmsmoney

    if extension == mng:
        return videoxmng

    # iana
    if extension == mmr:
        return imagevndfujixeroxedmicsmmr

    if extension in (mml, mathml):
        return applicationmathmlxml

    if extension in (mmf, smaf):
        return applicationxsmaf

    # iana
    if extension == mmd:
        return applicationvndchipnutskaraokemmd

    if extension == mm:
        return textxtroffmm

    # apache
    if extension == mlp:
        return applicationvnddolbymlp

    if extension in (ml, mli):
        return textxocaml

    if extension in (mkv, mks):
        return videoxmatroska

    if extension == mka:
        return audioxmatroska

    if extension == mk3d:
        return videoxmatroska3d

    if extension in (mjpeg, mjpg):
        return videoxmjpeg

    if extension in (mj2, mjp2):
        return videomj2

    if extension == minipsf:
        return audioxminipsf

    if extension == mif:
        return applicationxmif

    # apache
    if extension == mie:
        return applicationxmie

    if extension in (mid, midi, kar, rmi):
        return audiomidi

    if extension in (mhtml, mht):
        return applicationxmimearchive

    # iana
    if extension == mgz:
        return applicationvndproteusmagazine

    if extension == mgp:
        return applicationxmagicpoint

    # iana
    if extension == mft:
        return applicationrpkimanifest

    # iana
    if extension == mfm:
        return applicationvndmfmp

    # iana
    if extension == mets:
        return applicationmetsxml

    if extension == metalink:
        return applicationmetalinkxml

    if extension == meta4:
        return applicationmetalink4xml

    if extension in (mesonbuild, mesonoptionstxt):
        return textxmeson

    if extension == me:
        return textxtroffme

    if extension == mdi:
        return imagevndmsmodi

    if extension == mdb:
        return applicationvndmsaccess

    if extension in (md, mkd, markdown):
        return textmarkdown

    # apache
    if extension == mcurl:
        return textvndcurlmcurl

    # iana
    if extension == mcd:
        return applicationvndmcd

    if extension == mc2:
        return textvndsenxwarpscript

    # iana
    if extension == mc1:
        return applicationvndmedcalcdata

    if extension == mbox:
        return applicationmbox

    # iana
    if extension == mbk:
        return applicationvndmobiusmbk

    if extension in (manifest, appcache):
        return textcachemanifest

    if extension == man:
        return applicationxtroffman

    if extension in (makefile, gnumakefile, mk, mak):
        return textxmakefile

    # iana
    if extension == mag:
        return applicationvndecowinchart

    # iana
    if extension == maei:
        return applicationmmtaeixml

    # iana
    if extension == mads:
        return applicationmadsxml

    if extension == mab:
        return applicationxmarkaby

    if extension == m7:
        return applicationxthomsoncartridgememo7

    if extension == m4r:
        return audioxm4r

    if extension in (m4b, f4b):
        return audioxm4b

    if extension in (m4a, f4a, mp4a):
        return audiomp4

    if extension == m4:
        return applicationxm4

    if extension in (m3u, m3u8, vlc):
        return audioxmpegurl

    if extension in (m2t, m2ts, mts, cpi, clpi, mpl, mpls, bdm, bdmv):
        return videomp2t

    # iana
    if extension in (m21, mp21):
        return applicationmp21

    if extension in (m1u, m4u, mxu):
        return videovndmpegurl

    if extension == m:
        return textxobjcsrc

    if extension == lzo:
        return applicationxlzop

    if extension == lzma:
        return applicationxlzma

    if extension == lz4:
        return applicationxlz4

    if extension == lz:
        return applicationxlzip

    if extension == lyx:
        return applicationxlyx

    if extension == ly:
        return textxlilypond

    if extension == lws:
        return imagexlws

    if extension == lwp:
        return applicationvndlotuswordpro

    if extension in (lwo, lwob):
        return imagexlwo

    # iana
    if extension == lvp:
        return audiovndlucentvoice

    if extension == luac:
        return applicationxluabytecode

    if extension == lua:
        return textxlua

    # iana
    if extension == ltf:
        return applicationvndfrogansltf

    if extension == lrz:
        return applicationxlrzip

    # iana
    if extension == lrm:
        return applicationvndmslrm

    # iana
    if extension == lostxml:
        return applicationlostxml

    if extension == log:
        return textxlog

    if extension in (loas, xhe):
        return audiousac

    if extension == lnx:
        return applicationxatarilynxrom

    # apache
    if extension == lnk:
        return applicationxmsshortcut

    if extension == litcoffee:
        return textcoffeescript

    # iana
    if extension == link66:
        return applicationvndroute66link66xml

    if extension == lhz:
        return applicationxlhz

    if extension == lhs:
        return textxliteratehaskell

    if extension in (lha, lzh):
        return applicationxlha

    # iana
    if extension == lgr:
        return applicationlgrxml

    if extension == less:
        return textless

    # iana
    if extension == les:
        return applicationvndhhelessonplayer

    if extension == ldif:
        return textxldif

    # iana
    if extension == lbe:
        return applicationvndllamagraphicslifebalanceexchangexml

    # iana
    if extension == lbd:
        return applicationvndllamagraphicslifebalancedesktop

    # iana
    if extension == lasxml:
        return applicationvndlaslasxml

    if extension == la:
        return applicationxsharedlibraryla

    if extension in (kwd, kwt):
        return applicationxkword

    if extension == kud:
        return applicationxkugar

    # iana
    if extension in (ktz, ktr):
        return applicationvndkahootz

    if extension == ktx:
        return imagektx

    if extension == kt:
        return textxkotlin

    if extension == ksp:
        return applicationxkspread

    if extension == kra:
        return applicationxkrita

    # apache
    if extension == kpxx:
        return applicationvnddskeypoint

    if extension in (kpr, kpt):
        return applicationxkpresenter

    if extension == kpm:
        return applicationxkpovmodeler

    if extension == kon:
        return applicationxkontour

    # iana
    if extension in (kne, knp):
        return applicationvndkinar

    if extension == kmz:
        return applicationvndgoogleearthkmz

    if extension == kml:
        return applicationvndgoogleearthkmlxml

    if extension == kil:
        return applicationxkillustrator

    # iana
    if extension == kia:
        return applicationvndkidspiration

    if extension == kfo:
        return applicationxkformula

    # iana
    if extension == keynote:
        return applicationvndapplekeynote

    if extension == kexis:
        return applicationxkexiprojectshortcut

    if extension == kexic:
        return applicationxkexiconnectiondata

    if extension == kexi:
        return applicationxkexiprojectsqlite2

    if extension == kdc:
        return imagexkodakkdc

    if extension == kdbx:
        return applicationxkeepass2

    if extension == karbon:
        return applicationxkarbon

    if extension == k7:
        return applicationxthomsoncassette

    if extension == k25:
        return imagexkodakk25

    # iana
    if extension == jxss:
        return imagejxss

    # iana
    if extension == jxsi:
        return imagejxsi

    # iana
    if extension == jxsc:
        return imagejxsc

    # iana
    if extension == jxs:
        return imagejxs

    # iana
    if extension == jxrs:
        return imagejxrs

    # iana
    if extension == jxra:
        return imagejxra

    # iana
    if extension == jxr:
        return imagejxr

    if extension == jsx:
        return textjsx

    if extension == jsonpatch:
        return applicationjsonpatchjson

    # apache
    if extension == jsonml:
        return applicationjsonmljson

    if extension == jsonld:
        return applicationldjson

    if extension == json5:
        return applicationjson5

    if extension in (json, map):
        return applicationjson

    if extension in (js, jsm, mjs):
        return applicationjavascript

    if extension == jrd:
        return applicationjrdjson

    if extension in (jpr, jpx):
        return applicationxjbuilderproject

    if extension in (jpm, jpgm):
        return imagejpm

    # iana
    if extension == jph:
        return imagejph

    # iana
    if extension == jpgv:
        return videojpeg

    if extension in (jpg, jpeg, jpe):
        return imagejpeg

    if extension == jpf:
        return imagejpx

    if extension in (jp2, jpg2):
        return imagejp2

    # iana
    if extension == joda:
        return applicationvndjoostjodaarchive

    if extension == jnlp:
        return applicationxjavajnlpfile

    if extension == jng:
        return imagexjng

    # iana
    if extension == jlt:
        return applicationvndhpjlyt

    # iana
    if extension == jls:
        return imagejls

    if extension in (jks, ks, cacerts):
        return applicationxjavakeystore

    # iana
    if extension == jisp:
        return applicationvndjisp

    # iana
    if extension == jhc:
        return imagejphc

    if extension == jceks:
        return applicationxjavajcekeystore

    if extension == java:
        return textxjava

    # nginx
    if extension == jardiff:
        return applicationxjavaarchivediff

    if extension == jar:
        return applicationxjavaarchive

    # iana
    if extension == jam:
        return applicationvndjam

    if extension == jade:
        return textjade

    if extension == jad:
        return textvndsunj2meappdescriptor

    if extension in (j2c, j2k, jpc):
        return imagexjp2codestream

    # iana
    if extension == ivu:
        return applicationvndimmervisionivu

    # iana
    if extension == ivp:
        return applicationvndimmervisionivp

    # iana
    if extension == its:
        return applicationitsxml

    # iana
    if extension == itp:
        return applicationvndshanainformedformtemplate

    if extension == it87:
        return applicationxit87

    if extension == it:
        return audioxit

    if extension in (iso, iso9660):
        return applicationxcdimage

    # iana
    if extension == irp:
        return applicationvndirepositorypackagexml

    # iana
    if extension == irm:
        return applicationvndibmrightsmanagement

    if extension == ipynb:
        return applicationxipynbjson

    if extension == iptables:
        return textxiptables

    if extension == ips:
        return applicationxipspatch

    # iana
    if extension == ipk:
        return applicationvndshanainformedpackage

    # iana
    if extension == ipfix:
        return applicationipfix

    # iana
    if extension == iota:
        return applicationvndastraeasoftwareiota

    if extension == install:
        return textxinstall

    # iana
    if extension in (ink, inkml):
        return applicationinkmlxml

    if extension in (imy, ime):
        return textximelody

    # iana
    if extension == ims:
        return applicationvndmsims

    # iana
    if extension == imp:
        return applicationvndaccpacsimplyimp

    # iana
    if extension == iif:
        return applicationvndshanainformedinterchange

    # iana
    if extension == igx:
        return applicationvndmicrografxigx

    if extension in (igs, iges):
        return modeliges

    # iana
    if extension == igm:
        return applicationvndinsorsigm

    # iana
    if extension == igl:
        return applicationvndigloader

    # iana
    if extension == ifm:
        return applicationvndshanainformedformdata

    if extension in (iff, ilbm, lbm):
        return imagexilbm

    if extension == ief:
        return imageief

    if extension == idl:
        return textxidl

    if extension == ico:
        return imagevndmicrosofticon

    if extension == icns:
        return imagexicns

    # apache
    if extension == ice:
        return xconferencexcooltalk

    if extension in (icc, icm):
        return applicationvndiccprofile

    if extension == ica:
        return applicationxica

    # iana
    if extension == i2g:
        return applicationvndintergeo

    if extension == hwt:
        return applicationxhwt

    if extension == hwp:
        return applicationxhwp

    # iana
    if extension == hvs:
        return applicationvndyamahahvscript

    # iana
    if extension == hvp:
        return applicationvndyamahahvvoice

    # iana
    if extension == hvd:
        return applicationvndyamahahvdic

    # iana
    if extension == htke:
        return applicationvndkenameaapp

    # nginx
    if extension == htc:
        return textxcomponent

    # iana
    if extension == hsj2:
        return imagehsj2

    if extension == hs:
        return textxhaskell

    # iana
    if extension == hqx:
        return applicationmacbinhex40

    # iana
    if extension == hps:
        return applicationvndhphps

    # iana
    if extension == hpid:
        return applicationvndhphpid

    if extension == hpgl:
        return applicationvndhphpgl

    if extension == hlp:
        return applicationwinhlp

    if extension == hjson:
        return applicationhjson

    if extension in (hh, hp, hpp, h, hxx):
        return textxchdr

    if extension == hfe:
        return applicationxhfefloppyimage

    # iana
    if extension == held:
        return applicationatscheldxml

    # iana
    if extension == hej2:
        return imagehej2k

    # iana
    if extension == heifs:
        return imageheifsequence

    # iana
    if extension == heics:
        return imageheicsequence

    if extension in (heic, heif):
        return imageheif

    if extension in (hdf, hdf4, h4, hdf5, h5):
        return applicationxhdf

    if extension == hdd:
        return applicationxvirtualboxhdd

    if extension == hbs:
        return textxhandlebarstemplate

    # iana
    if extension == hbci:
        return applicationvndhbci

    # iana
    if extension == hal:
        return applicationvndhalxml

    # iana
    if extension == h264:
        return videoh264

    # iana
    if extension == h263:
        return videoh263

    # iana
    if extension == h261:
        return videoh261

    if extension == gz:
        return applicationgzip

    # iana
    if extension == gxt:
        return applicationvndgeonext

    # apache
    if extension == gxf:
        return applicationgxf

    if extension == gvp:
        return textxgooglevideopointer

    if extension == gv:
        return textvndgraphviz

    # iana
    if extension == gtw:
        return modelvndgtw

    # iana
    if extension == gtm:
        return applicationvndgroovetoolmessage

    if extension == gsm:
        return audioxgsm

    if extension == gslides:
        return applicationvndgoogleappspresentation

    if extension == gsheet:
        return applicationvndgoogleappsspreadsheet

    if extension == gs:
        return textxgenie

    # iana
    if extension == grxml:
        return applicationsrgsxml

    # iana
    if extension == grv:
        return applicationvndgrooveinjector

    if extension in (groovy, gvy, gy, gsh):
        return textxgroovy

    # apache
    if extension == gramps:
        return applicationxgrampsxml

    # iana
    if extension == gram:
        return applicationsrgs

    if extension == gradle:
        return textxgradle

    if extension == gra:
        return applicationxgraphite

    # iana
    if extension in (gqf, gqs):
        return applicationvndgrafeq

    if extension == gpx:
        return applicationgpxxml

    # iana
    if extension == gph:
        return applicationvndflographit

    if extension in (gp, gplt, gnuplot):
        return applicationxgnuplot

    if extension == go:
        return textxgo

    if extension == gnumeric:
        return applicationxgnumeric

    if extension in (gnucash, gnc, xac):
        return applicationxgnucash

    if extension == gnd:
        return applicationgnunetdirectory

    # iana
    if extension == gmx:
        return applicationvndgmx

    if extension == gmonout:
        return applicationxprofile

    if extension in (gmo, mo):
        return applicationxgettexttranslation

    if extension == gml:
        return applicationgmlxml

    # iana
    if extension == gltf:
        return modelgltfjson

    # iana
    if extension == glb:
        return modelgltfbinary

    if extension == glade:
        return applicationxglade

    # iana
    if extension == gim:
        return applicationvndgrooveidentitymessage

    if extension == gih:
        return imagexgimpgih

    if extension == gif:
        return imagegif

    # iana
    if extension == ghf:
        return applicationvndgroovehelp

    # iana
    if extension == ggt:
        return applicationvndgeogebratool

    # iana
    if extension == ggb:
        return applicationvndgeogebrafile

    if extension == gg:
        return applicationxgamegearrom

    if extension == gf:
        return applicationxtexgf

    # iana
    if extension in (gex, gre):
        return applicationvndgeometryexplorer

    if extension == geojson:
        return applicationgeojson

    # iana
    if extension == geo:
        return applicationvnddynageo

    if extension in (gen, sgd):
        return applicationxgenesisrom

    if extension in (ged, gedcom):
        return applicationxgedcom

    if extension == gdoc:
        return applicationvndgoogleappsdocument

    # iana
    if extension == gdl:
        return modelvndgdl

    if extension == gcode:
        return textxgcode

    # apache
    if extension == gca:
        return applicationxgcacompressed

    if extension == gbr:
        return imagexgimpgbr

    if extension in (gbc, cgb):
        return applicationxgameboycolorrom

    if extension in (gba, agb):
        return applicationxgbarom

    if extension in (gb, sgb):
        return applicationxgameboyrom

    # apache
    if extension == gam:
        return applicationxtads

    # iana
    if extension == gac:
        return applicationvndgrooveaccount

    # iana
    if extension == g3w:
        return applicationvndgeospace

    if extension == g3:
        return imagefaxg3

    # iana
    if extension == g2w:
        return applicationvndgeoplan

    # iana
    if extension == fzs:
        return applicationvndfuzzysheet

    # iana
    if extension in (fxp, fxpl):
        return applicationvndadobefxp

    if extension == fxm:
        return videoxjavafx

    # iana
    if extension == fvt:
        return videovndfvt

    # apache
    if extension == fti:
        return applicationvndanserwebfundstransferinitiation

    # iana
    if extension == ftc:
        return applicationvndfluxtimeclip

    # iana
    if extension == fst:
        return imagevndfst

    # iana
    if extension == fsc:
        return applicationvndfscweblaunch

    # iana
    if extension == fpx:
        return imagevndfpx

    if extension == fodt:
        return applicationvndoasisopendocumenttextflatxml

    if extension == fods:
        return applicationvndoasisopendocumentspreadsheetflatxml

    if extension == fodp:
        return applicationvndoasisopendocumentpresentationflatxml

    if extension == fodg:
        return applicationvndoasisopendocumentgraphicsflatxml

    if extension in (fo, xslfo):
        return textxxslfo

    # iana
    if extension == fnc:
        return applicationvndfrogansfnc

    if extension in (fm, frame, maker, book):
        return applicationvndframemaker

    # iana
    if extension == fly:
        return textvndfly

    # iana
    if extension == flx:
        return textvndfmiflexstor

    if extension == flw:
        return applicationxkivio

    if extension == flv:
        return videoxflv

    # iana
    if extension == flo:
        return applicationvndmicrografxflo

    if extension in (fli, flc):
        return videoxflic

    if extension == flatpakrepo:
        return applicationvndflatpakrepo

    if extension == flatpakref:
        return applicationvndflatpakref

    if extension in (flatpak, xdgapp):
        return applicationvndflatpak

    if extension == flac:
        return audioflac

    if extension == fl:
        return applicationxfluid

    if extension == fits:
        return imagefits

    if extension == fig:
        return imagexxfig

    # apache
    if extension in (fh, fhc, fh4, fh5, fh7):
        return imagexfreehand

    # iana
    if extension == fg5:
        return applicationvndfujitsuoasysgp

    if extension == feature:
        return textxgherkin

    # iana
    if extension == felaunch:
        return applicationvnddenovofcselayoutlink

    # iana
    if extension == fdt:
        return applicationfdtxml

    if extension == fds:
        return applicationxfdsdisk

    # iana
    if extension == fdf:
        return applicationvndfdf

    if extension in (fd, qd):
        return applicationxrawfloppydiskimage

    # iana
    if extension == fcs:
        return applicationvndisacfcs

    # iana
    if extension == fcdt:
        return applicationvndadobeformscentralfcdt

    # iana
    if extension == fbs:
        return imagevndfastbidsheet

    if extension == fb2zip:
        return applicationxzipcompressedfb2

    if extension == fb2:
        return applicationxfictionbookxml

    if extension in (f, f90, f95, _for, f77):
        return textxfortran

    # iana
    if extension == ez3:
        return applicationvndezpixpackage

    # iana
    if extension == ez2:
        return applicationvndezpixalbum

    if extension == ez:
        return applicationandrewinset

    # iana
    if extension == ext:
        return applicationvndnovadigmext

    if extension == exr:
        return imagexexr

    # iana
    if extension == exi:
        return applicationexi

    if extension == exe:
        return applicationxmsdosexecutable

    # apache
    if extension == evy:
        return applicationxenvoy

    # apache
    if extension == eva:
        return applicationxeva

    if extension == etx:
        return textxsetext

    if extension == etheme:
        return applicationxetheme

    # iana
    if extension == esf:
        return applicationvndepsonesf

    # iana
    if extension == esa:
        return applicationvndosgisubsystem

    # iana
    if extension in (es3, et3):
        return applicationvndeszigno3xml

    if extension in (es, ecma):
        return applicationecmascript

    if extension == erl:
        return textxerlang

    if extension == epub:
        return applicationepubzip

    if extension in (epsgz, epsigz, epsfgz):
        return imagexgzeps

    if extension in (epsbz2, epsibz2, epsfbz2):
        return imagexbzeps

    if extension in (eps, epsi, epsf):
        return imagexeps

    # iana
    if extension == eot:
        return applicationvndmsfontobject

    # iana
    if extension == eol:
        return audiovnddigitalwinds

    if extension == ent:
        return applicationxmlexternalparsedentity

    # apache
    if extension == emz:
        return applicationxmsmetafile

    if extension == emp:
        return applicationvndemusicemusicpackage

    # iana
    if extension == emotionml:
        return applicationemotionmlxml

    # iana
    if extension == emma:
        return applicationemmaxml

    if extension in (eml, mime):
        return messagerfc822

    if extension == emf:
        return imageemf

    if extension == el:
        return textxemacslisp

    # iana
    if extension == ei6:
        return applicationvndpgosasli

    if extension == egon:
        return applicationxegon

    # iana
    if extension == efif:
        return applicationvndpicsel

    # iana
    if extension == edx:
        return applicationvndnovadigmedx

    # iana
    if extension == edm:
        return applicationvndnovadigmedm

    # iana
    if extension == ecelp9600:
        return audiovndnueraecelp9600

    # iana
    if extension == ecelp7470:
        return audiovndnueraecelp7470

    # iana
    if extension == ecelp4800:
        return audiovndnueraecelp4800

    if extension in (e, eif):
        return textxeiffel

    # iana
    if extension == dxp:
        return applicationvndspotfiredxp

    if extension == dxf:
        return imagevnddxf

    if extension == dwg:
        return imagevnddwg

    # iana
    if extension == dwf:
        return modelvnddwf

    # iana
    if extension == dwd:
        return applicationatscdwdxml

    if extension == dvigz:
        return applicationxgzdvi

    if extension == dvibz2:
        return applicationxbzdvi

    if extension == dvi:
        return applicationxdvi

    # iana
    if extension == dvb:
        return videovnddvbfile

    if extension == dv:
        return videodv

    if extension == dtshd:
        return audiovnddtshd

    if extension == dts:
        return audiovnddts

    if extension == dtd:
        return applicationxmldtd

    # apache
    if extension == dtb:
        return applicationxdtbookxml

    # iana
    if extension == dssc:
        return applicationdsscder

    if extension == dsl:
        return textxdsl

    # iana
    if extension == dsc:
        return textprslinestag

    # iana
    if extension == drle:
        return imagedicomrle

    # iana
    if extension == dra:
        return audiovnddra

    # iana
    if extension == dpg:
        return applicationvnddpgraph

    # iana
    if extension == dp:
        return applicationvndosgidp

    if extension == dotx:
        return applicationvndopenxmlformatsofficedocumentwordprocessingmltemplate

    if extension == dotm:
        return applicationvndmswordtemplatemacroenabled12

    if extension == dot:
        return applicationmswordtemplate

    if extension == docx:
        return applicationvndopenxmlformatsofficedocumentwordprocessingmldocument

    if extension == docm:
        return applicationvndmsworddocumentmacroenabled12

    if extension == doc:
        return applicationmsword

    if extension == dng:
        return imagexadobedng

    # iana
    if extension == dna:
        return applicationvnddna

    if extension == dmg:
        return applicationxapplediskimage

    if extension in (djvu, djv):
        return imagevnddjvu

    # iana
    if extension == dispositionnotification:
        return messagedispositionnotification

    # iana
    if extension == dis:
        return applicationvndmobiusdis

    # apache
    if extension in (dir, dxr, cst, cct, cxt, w3d, fgd, swa):
        return applicationxdirector

    if extension in (diff, patch):
        return textxpatch

    if extension in (dicomdir, dcm):
        return applicationdicom

    # apache
    if extension == dic:
        return textxc

    if extension == dia:
        return applicationxdiadiagram

    # apache
    if extension == dgc:
        return applicationxdgccompressed

    # iana
    if extension == dfac:
        return applicationvnddreamfactory

    if extension in (desktop, kdelnk):
        return applicationxdesktop

    if extension in (der, crt, cert, pem):
        return applicationxx509cacert

    if extension in (deb, udeb):
        return applicationvnddebianbinarypackage

    if extension == dds:
        return imagexdds

    # iana
    if extension == ddf:
        return applicationvndsyncmldmddfxml

    # iana
    if extension == ddd:
        return applicationvndfujixeroxddd

    # iana
    if extension == dd2:
        return applicationvndomadd2xml

    # apache
    if extension == dcurl:
        return textvndcurldcurl

    if extension == dcr:
        return imagexkodakdcr

    if extension == dcl:
        return textxdcl

    if extension == dc:
        return applicationxdcrom

    if extension in (dbk, docbook):
        return applicationxdocbookxml

    if extension == dbf:
        return applicationxdbf

    # iana
    if extension == davmount:
        return applicationdavmountxml

    # iana
    if extension == dart:
        return applicationvnddart

    if extension == dar:
        return applicationxdar

    # iana
    if extension == daf:
        return applicationvndmobiusdaf

    # iana
    if extension == dae:
        return modelvndcolladaxml

    if extension in (d, di):
        return textxdsrc

    # iana
    if extension == cww:
        return applicationprscww

    if extension == cwk:
        return applicationxappleworksdocument

    # iana
    if extension == curl:
        return textvndcurl

    if extension == cur:
        return imagexwinbitmap

    if extension == cue:
        return applicationxcue

    # apache
    if extension == cu:
        return applicationcuseeme

    if extension == csvs:
        return textcsvschema

    if extension == csv:
        return textcsv

    if extension == css:
        return textcss

    # iana
    if extension == csp:
        return applicationvndcommonspace

    # apache
    if extension == csml:
        return chemicalxcsml

    # iana
    if extension == csl:
        return applicationvndcitationstylesstylexml

    if extension == csh:
        return applicationxcsh

    if extension == cs:
        return textxcsharp

    # iana
    if extension == cryptonote:
        return applicationvndrigcryptonote

    if extension == crx:
        return applicationxchromeextension

    if extension == crw:
        return imagexcanoncrw

    if extension == crl:
        return applicationpkixcrl

    if extension == credits:
        return textxcredits

    # apache
    if extension == crd:
        return applicationxmscardfile

    if extension == cr2:
        return imagexcanoncr2

    # apache
    if extension == cpt:
        return applicationmaccompactpro

    if extension in (cpp, cxx, cc, c):
        return textxcsrc

    if extension == cpiogz:
        return applicationxcpiocompressed

    if extension == cpio:
        return applicationxcpio

    if extension == core:
        return applicationxcore

    if extension == copying:
        return textxcopying

    # apache
    if extension in (com, bat):
        return applicationxmsdownload

    if extension == coffee:
        return applicationvndcoffeescript

    # apache
    if extension == cod:
        return applicationvndrimcod

    # apache
    if extension == cmx:
        return imagexcmx

    # iana
    if extension == cmp:
        return applicationvndyellowrivercustommenu

    # apache
    if extension == cml:
        return chemicalxcml

    # apache
    if extension == cmdf:
        return chemicalxcmdf

    # iana
    if extension == cmc:
        return applicationvndcosmocaller

    if extension in (cmake, cmakeliststxt):
        return textxcmake

    # apache
    if extension == clp:
        return applicationxmsclip

    # iana
    if extension == clkx:
        return applicationvndcrickclicker

    # iana
    if extension == clkw:
        return applicationvndcrickclickerwordbank

    # iana
    if extension == clkt:
        return applicationvndcrickclickertemplate

    # iana
    if extension == clkp:
        return applicationvndcrickclickerpalette

    # iana
    if extension == clkk:
        return applicationvndcrickclickerkeyboard

    if extension == _class:
        return applicationxjava

    # iana
    if extension == cla:
        return applicationvndclaymore

    if extension == cl:
        return textxopenclsrc

    # iana
    if extension == cjs:
        return applicationnode

    # iana
    if extension == cil:
        return applicationvndmsartgalry

    # iana
    if extension == cii:
        return applicationvndanserwebcertificateissueinitiation

    # apache
    if extension == cif:
        return chemicalxcif

    if extension == chrt:
        return applicationxkchart

    if extension == chm:
        return applicationvndmshtmlhelp

    # apache
    if extension == chat:
        return applicationxchat

    if extension == changelog:
        return textxchangelog

    if extension == cgm:
        return imagecgm

    # apache
    if extension == cfs:
        return applicationxcfscompressed

    if extension == cer:
        return applicationpkixcert

    # iana
    if extension == cdy:
        return applicationvndcinderella

    # iana
    if extension == cdxml:
        return applicationvndchemdrawxml

    # apache
    if extension == cdx:
        return chemicalxcdx

    if extension == cdr:
        return applicationvndcoreldraw

    # iana
    if extension == cdmiq:
        return applicationcdmiqueue

    # iana
    if extension == cdmio:
        return applicationcdmiobject

    # iana
    if extension == cdmid:
        return applicationcdmidomain

    # iana
    if extension == cdmic:
        return applicationcdmicontainer

    # iana
    if extension == cdmia:
        return applicationcdmicapability

    # iana
    if extension == cdkey:
        return applicationvndmediastationcdkey

    # iana
    if extension == cdfx:
        return applicationcdfxxml

    if extension in (cdf, nc):
        return applicationxnetcdf

    # iana
    if extension == cdbcmsg:
        return applicationvndcontactcmsg

    # iana
    if extension == ccxml:
        return applicationccxmlxml

    # nginx
    if extension == cco:
        return applicationxcocoa

    if extension == ccmx:
        return applicationxccmx

    if extension == cbz:
        return applicationvndcomicbookzip

    if extension == cbt:
        return applicationxcbt

    if extension == cbr:
        return applicationvndcomicbookrar

    if extension in (cbl, cob):
        return textxcobol

    # apache
    if extension == cba:
        return applicationxcbr

    if extension == cb7:
        return applicationxcb7

    # apache
    if extension == cat:
        return applicationvndmspkiseccat

    # apache
    if extension == car:
        return applicationvndcurlcar

    # apache
    if extension == caf:
        return audioxcaf

    if extension == cab:
        return applicationvndmscabcompressed

    # iana
    if extension in (c4g, c4d, c4f, c4p, c4u):
        return applicationvndclonkc4group

    # iana
    if extension == c11amz:
        return applicationvndcluetrustcartomobileconfigpkg

    # iana
    if extension == c11amc:
        return applicationvndcluetrustcartomobileconfig

    if extension in (bz2, bz):
        return applicationxbzip

    # iana
    if extension == btif:
        return imageprsbtif

    # iana
    if extension == bsp:
        return modelvndvalvesourcecompiledmap

    if extension == bsdiff:
        return applicationxbsdiff

    if extension == bps:
        return applicationxbpspatch

    # apache
    if extension == boz:
        return applicationxbzip2

    # iana
    if extension == box:
        return applicationvndpreviewsystemsbox

    if extension in (bmp, dib):
        return imagebmp

    # iana
    if extension == bmml:
        return applicationvndbalsamiqbmmlxml

    # iana
    if extension == bmi:
        return applicationvndbmi

    if extension in (blender, blend):
        return applicationxblender

    # apache
    if extension in (blb, blorb):
        return applicationxblorb

    # iana
    if extension in (bin, dms, lrf, mar, dist, distz, bpk, dump, elc, deploy, dll, msp, msm, buffer):
        return applicationoctetstream

    if extension == bib:
        return textxbibtex

    # iana
    if extension == bh2:
        return applicationvndfujitsuoasysprs

    # iana
    if extension == bed:
        return applicationvndrealvncbed

    if extension == bdoc:
        return applicationbdoc

    if extension == bdf:
        return applicationxfontbdf

    if extension == bcpio:
        return applicationxbcpio

    if extension in (bak, old, sik):
        return applicationxtrash

    if extension in (azw3, kfx):
        return applicationvndamazonmobi8ebook

    # apache
    if extension == azw:
        return applicationvndamazonebook

    # iana
    if extension == azv:
        return imagevndairzipacceleratorazv

    # iana
    if extension == azs:
        return applicationvndairzipfilesecureazs

    # iana
    if extension == azf:
        return applicationvndairzipfilesecureazf

    if extension == axv:
        return videoannodex

    if extension == axa:
        return audioannodex

    if extension == awk:
        return applicationxawk

    if extension == awb:
        return audioamrwb

    if extension == aw:
        return applicationxapplixword

    if extension == avifs:
        return imageavifsequence

    if extension == avif:
        return imageavif

    if extension in (avi, avf, divx):
        return videoxmsvideo

    if extension in (automount, device, mount, path, scope, slice, socket, swap, target, timer):
        return textxsystemdunit

    if extension == authors:
        return textxauthors

    if extension in (au, snd):
        return audiobasic

    # iana
    if extension == atx:
        return applicationvndantixgamecomponent

    # iana
    if extension == atomsvc:
        return applicationatomsvcxml

    # iana
    if extension == atomdeleted:
        return applicationatomdeletedxml

    # iana
    if extension == atomcat:
        return applicationatomcatxml

    if extension == atom:
        return applicationatomxml

    # iana
    if extension in (atc, acutc):
        return applicationvndacucorp

    if extension in (asx, wax, wvx, wmx):
        return audioxmsasx

    if extension == asp:
        return applicationxasp

    # iana
    if extension == aso:
        return applicationvndaccpacsimplyaso

    if extension == asf:
        return applicationvndmsasf

    if extension in (asd, fasl, lisp, ros):
        return textxcommonlisp

    if extension == _as:
        return applicationxapplixspreadsheet

    if extension == arw:
        return imagexsonyarw

    if extension == arj:
        return applicationxarj

    # apache
    if extension == arc:
        return applicationxfreearc

    # iana
    if extension == apr:
        return applicationvndlotusapproach

    # apache
    if extension == application:
        return applicationxmsapplication

    if extension == appimage:
        return applicationxiso9660appimage

    if extension == apng:
        return imageapng

    if extension == apk:
        return applicationvndandroidpackagearchive

    if extension == ape:
        return audioxape

    if extension == anx:
        return applicationannodex

    if extension == anim19j:
        return videoxanim

    if extension == ani:
        return applicationxnavianimation

    if extension == amz:
        return audioxamzxml

    if extension == amr:
        return audioamr

    # iana
    if extension == ami:
        return applicationvndamigaami

    if extension == alz:
        return applicationxalz

    # iana
    if extension == ait:
        return applicationvnddvbait

    # apache
    if extension == air:
        return applicationvndadobeairapplicationinstallerpackagezip

    if extension in (aiff, aif):
        return audioxaiff

    if extension in (aifc, aiffc):
        return audioxaifc

    if extension == ai:
        return applicationillustrator

    # iana
    if extension == ahead:
        return applicationvndaheadspace

    if extension == ag:
        return imagexapplixgraphics

    # iana
    if extension in (afp, listafp, list3820):
        return applicationvndibmmodcap

    if extension == afm:
        return applicationxfontafm

    # iana
    if extension == aep:
        return applicationvndaudiograph

    # apache
    if extension == adp:
        return audioadpcm

    if extension == adf:
        return applicationxamigadiskformat

    if extension in (adb, ads):
        return textxadasrc

    # iana
    if extension == acu:
        return applicationvndacucobol

    if extension == ace:
        return applicationxace

    # iana
    if extension == acc:
        return applicationvndamericandynamicsacc

    if extension == ac3:
        return audioac3

    # iana
    if extension == ac:
        return applicationpkixattrcert

    if extension in (abw, abwcrashed, abwgz, zabw):
        return applicationxabiword

    # apache
    if extension == aas:
        return applicationxauthorwareseg

    # apache
    if extension == aam:
        return applicationxauthorwaremap

    if extension in (aac, adts):
        return audioaac

    # apache
    if extension in (aab, x32, u32, vox):
        return applicationxauthorwarebin

    if extension in (aa, aax):
        return audioxpnaudibleaudio

    if extension == a78:
        return applicationxatari7800rom

    if extension == a26:
        return applicationxatari2600rom

    if extension in (a, ar):
        return applicationxarchive

    if extension == _7z:
        return applicationx7zcompressed

    if extension == _602:
        return applicationxt602

    # iana
    if extension == _3mf:
        return model3mf

    if extension in (_3gp, _3gpp, _3ga):
        return video3gpp

    if extension in (_3g2, _3gp2, _3gpp2):
        return video3gpp2

    if extension == _3ds:
        return imagex3ds

    # iana
    if extension == _3dml:
        return textvndin3d3dml

    if extension in (_32x, mdx):
        return applicationxgenesis32xrom

    # iana
    if extension == _1km:
        return applicationvnd1000mindsdecisionmodelxml

    if extension in (_123, wk1, wk3, wk4, wks):
        return applicationvndlotus123

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
