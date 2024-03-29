import os
from enum import Enum, unique, auto

#constants
applicationvndlotus123 = "application/vnd.lotus-1-2-3"
_123 = "123"
wk1 = "wk1"
wk3 = "wk3"
wk4 = "wk4"
wks = "wks"
applicationvnd1000mindsdecisionmodel_xml = "application/vnd.1000minds.decision-model+xml"
_1km = "1km"
applicationxgenesis32xrom = "application/x-genesis-32x-rom"
_32x = "32x"
mdx = "mdx"
textvndin3d3dml = "text/vnd.in3d.3dml"
_3dml = "3dml"
applicationxnintendo3dsrom = "application/x-nintendo-3ds-rom"
_3ds = "3ds"
cci = "cci"
applicationxnintendo3dsexecutable = "application/x-nintendo-3ds-executable"
_3dsx = "3dsx"
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
_7z001 = "7z001"
applicationxarchive = "application/x-archive"
a = "a"
ar = "ar"
applicationxatari2600rom = "application/x-atari-2600-rom"
a26 = "a26"
applicationxatari7800rom = "application/x-atari-7800-rom"
a78 = "a78"
audioxpnaudibleaudio = "audio/x-pn-audibleaudio"
aa = "aa"
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
audiovndaudibleaax = "audio/vnd.audible.aax"
aax = "aax"
audiovndaudibleaaxc = "audio/vnd.audible.aaxc"
aaxc = "aaxc"
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
applicationvndage = "application/vnd.age"
age = "age"
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
applicationvndadobeairapplicationinstallerpackage_zip = "application/vnd.adobe.air-application-installer-package+zip"
air = "air"
applicationvnddvbait = "application/vnd.dvb.ait"
ait = "ait"
applicationxalz = "application/x-alz"
alz = "alz"
applicationvndamigaami = "application/vnd.amiga.ami"
ami = "ami"
applicationautomationmlaml_xml = "application/automationml-aml+xml"
aml = "aml"
applicationautomationmlamlx_zip = "application/automationml-amlx+zip"
amlx = "amlx"
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
applicationappinstaller = "application/appinstaller"
appinstaller = "appinstaller"
applicationxmsapplication = "application/x-ms-application"
application = "application"
applicationappx = "application/appx"
appx = "appx"
applicationappxbundle = "application/appxbundle"
appxbundle = "appxbundle"
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
applicationxasar = "application/x-asar"
asar = "asar"
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
imageastc = "image/astc"
astc = "astc"
audioxmsasx = "audio/x-ms-asx"
asx = "asx"
wax = "wax"
wvx = "wvx"
wmx = "wmx"
applicationvndacucorp = "application/vnd.acucorp"
atc = "atc"
acutc = "acutc"
applicationatom_xml = "application/atom+xml"
atom = "atom"
applicationatomcat_xml = "application/atomcat+xml"
atomcat = "atomcat"
applicationatomdeleted_xml = "application/atomdeleted+xml"
atomdeleted = "atomdeleted"
applicationatomsvc_xml = "application/atomsvc+xml"
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
imageavci = "image/avci"
avci = "avci"
imageavcs = "image/avcs"
avcs = "avcs"
videovndavi = "video/vnd.avi"
avi = "avi"
avf = "avf"
divx = "divx"
imageavif = "image/avif"
avif = "avif"
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
imagevndpcob16 = "image/vnd.pco.b16"
b16 = "b16"
applicationxtrash = "application/x-trash"
bak = "bak"
old = "old"
sik = "sik"
textxbasic = "text/x-basic"
bas = "bas"
applicationxbat = "application/x-bat"
bat = "bat"
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
videovndradgamettoolsbink = "video/vnd.radgamettools.bink"
bik = "bik"
bk2 = "bk2"
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
msp = "msp"
msm = "msm"
buffer = "buffer"
applicationxblorb = "application/x-blorb"
blb = "blb"
blorb = "blorb"
applicationxblender = "application/x-blender"
blend = "blend"
blender = "blender"
textxblueprint = "text/x-blueprint"
blp = "blp"
applicationvndbmi = "application/vnd.bmi"
bmi = "bmi"
applicationvndbalsamiqbmml_xml = "application/vnd.balsamiq.bmml+xml"
bmml = "bmml"
imagebmp = "image/bmp"
bmp = "bmp"
dib = "dib"
applicationvndpreviewsystemsbox = "application/vnd.previewsystems.box"
box = "box"
applicationxbpspatch = "application/x-bps-patch"
bps = "bps"
chemicalxpdb = "chemical/x-pdb"
brk = "brk"
applicationxbsdiff = "application/x-bsdiff"
bsdiff = "bsdiff"
modelvndvalvesourcecompiledmap = "model/vnd.valve.source.compiled-map"
bsp = "bsp"
imageprsbtif = "image/prs.btif"
btif = "btif"
btf = "btf"
applicationxbzip1 = "application/x-bzip1"
bz = "bz"
applicationxbzip2 = "application/x-bzip2"
bz2 = "bz2"
boz = "boz"
applicationxbzip3 = "application/x-bzip3"
bz3 = "bz3"
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
applicationcbor = "application/cbor"
cbor = "cbor"
applicationvndcomicbookrar = "application/vnd.comicbook-rar"
cbr = "cbr"
applicationxcbt = "application/x-cbt"
cbt = "cbt"
applicationvndcomicbook_zip = "application/vnd.comicbook+zip"
cbz = "cbz"
applicationxccmx = "application/x-ccmx"
ccmx = "ccmx"
applicationxcocoa = "application/x-cocoa"
cco = "cco"
applicationccxml_xml = "application/ccxml+xml"
ccxml = "ccxml"
applicationvndcontactcmsg = "application/vnd.contact.cmsg"
cdbcmsg = "cdbcmsg"
applicationxnetcdf = "application/x-netcdf"
cdf = "cdf"
nc = "nc"
applicationcdfx_xml = "application/cdfx+xml"
cdfx = "cdfx"
applicationxdiscjugglercdimage = "application/x-discjuggler-cd-image"
cdi = "cdi"
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
applicationvndchemdraw_xml = "application/vnd.chemdraw+xml"
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
applicationxmamechd = "application/x-mame-chd"
chd = "chd"
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
modelvndcld = "model/vnd.cld"
cld = "cld"
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
textxcopying = "text/x-copying"
copying = "copying"
applicationxcore = "application/x-core"
core = "core"
applicationxcpio = "application/x-cpio"
cpio = "cpio"
applicationxcpiocompressed = "application/x-cpio-compressed"
cpiogz = "cpiogz"
textxc__src = "text/x-c++src"
cpp = "cpp"
cxx = "cxx"
cc = "cc"
c = "c"
applicationmaccompactpro = "application/mac-compactpro"
cpt = "cpt"
textxcrystal = "text/x-crystal"
cr = "cr"
imagexcanoncr2 = "image/x-canon-cr2"
cr2 = "cr2"
imagexcanoncr3 = "image/x-canon-cr3"
cr3 = "cr3"
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
applicationvndcitationstylesstyle_xml = "application/vnd.citationstyles.style+xml"
csl = "csl"
chemicalxcsml = "chemical/x-csml"
csml = "csml"
applicationxcompressediso = "application/x-compressed-iso"
cso = "cso"
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
applicationcwl = "application/cwl"
cwl = "cwl"
applicationprscww = "application/prs.cww"
cww = "cww"
textxdsrc = "text/x-dsrc"
d = "d"
di = "di"
modelvndcollada_xml = "model/vnd.collada+xml"
dae = "dae"
applicationvndmobiusdaf = "application/vnd.mobius.daf"
daf = "daf"
applicationxdar = "application/x-dar"
dar = "dar"
applicationvnddart = "application/vnd.dart"
dart = "dart"
applicationdavmount_xml = "application/davmount+xml"
davmount = "davmount"
applicationvnddbf = "application/vnd.dbf"
dbf = "dbf"
applicationxdocbook_xml = "application/x-docbook+xml"
dbk = "dbk"
docbook = "docbook"
textxdcl = "text/x-dcl"
dcl = "dcl"
imagexkodakdcr = "image/x-kodak-dcr"
dcr = "dcr"
textvndcurldcurl = "text/vnd.curl.dcurl"
dcurl = "dcurl"
applicationvndomadd2_xml = "application/vnd.oma.dd2+xml"
dd2 = "dd2"
applicationvndfujixeroxddd = "application/vnd.fujixerox.ddd"
ddd = "ddd"
applicationvndsyncmldmddf_xml = "application/vnd.syncml.dmddf+xml"
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
audioxdff = "audio/x-dff"
dff = "dff"
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
imagedpx = "image/dpx"
dpx = "dpx"
audiovnddra = "audio/vnd.dra"
dra = "dra"
applicationxexcellon = "application/x-excellon"
drl = "drl"
imagedicomrle = "image/dicom-rle"
drle = "drle"
textprslinestag = "text/prs.lines.tag"
dsc = "dsc"
audioxdsf = "audio/x-dsf"
dsf = "dsf"
textxdsl = "text/x-dsl"
dsl = "dsl"
applicationdssc_der = "application/dssc+der"
dssc = "dssc"
textxdevicetreebinary = "text/x-devicetree-binary"
dtb = "dtb"
applicationxmldtd = "application/xml-dtd"
dtd = "dtd"
audiovnddts = "audio/vnd.dts"
dts = "dts"
audiovnddtshd = "audio/vnd.dts.hd"
dtshd = "dtshd"
textxdevicetreesource = "text/x-devicetree-source"
dtsi = "dtsi"
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
applicationatscdwd_xml = "application/atsc-dwd+xml"
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
applicationvndmicrosoftportableexecutable = "application/vnd.microsoft.portable-executable"
efi = "efi"
ocx = "ocx"
sys = "sys"
lib = "lib"
applicationvndpicsel = "application/vnd.picsel"
efif = "efif"
applicationxegon = "application/x-egon"
egon = "egon"
applicationvndmicrosoftwindowsthumbnailcache = "application/vnd.microsoft.windows.thumbnail-cache"
ehthumbsdb = "ehthumbsdb"
ehthumbsvistadb = "ehthumbsvistadb"
imagedb = "imagedb"
musicthumbsdb = "musicthumbsdb"
thumbsdb = "thumbsdb"
tvthumbdb = "tvthumbdb"
videodb = "videodb"
applicationvndpgosasli = "application/vnd.pg.osasli"
ei6 = "ei6"
textxemacslisp = "text/x-emacs-lisp"
el = "el"
imageemf = "image/emf"
emf = "emf"
messagerfc822 = "message/rfc822"
eml = "eml"
mime = "mime"
applicationemma_xml = "application/emma+xml"
emma = "emma"
applicationemotionml_xml = "application/emotionml+xml"
emotionml = "emotionml"
applicationvndemusicemusic_package = "application/vnd.emusic-emusic_package"
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
applicationepub_zip = "application/epub+zip"
epub = "epub"
applicationxerislink_cbor = "application/x-eris-link+cbor"
eris = "eris"
textxerlang = "text/x-erlang"
erl = "erl"
applicationecmascript = "application/ecmascript"
es = "es"
ecma = "ecma"
applicationvndeszigno3_xml = "application/vnd.eszigno3+xml"
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
textxelixir = "text/x-elixir"
ex = "ex"
exs = "exs"
applicationxmsdownload = "application/x-msdownload"
exe = "exe"
dll = "dll"
cpl = "cpl"
drv = "drv"
scr = "scr"
com = "com"
applicationexi = "application/exi"
exi = "exi"
applicationexpress = "application/express"
exp = "exp"
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
applicationxfictionbook_xml = "application/x-fictionbook+xml"
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
applicationfdf = "application/fdf"
fdf = "fdf"
applicationxfdsdisk = "application/x-fds-disk"
fds = "fds"
applicationfdt_xml = "application/fdt+xml"
fdt = "fdt"
applicationvnddenovofcselayoutlink = "application/vnd.denovo.fcselayout-link"
fe_launch = "fe_launch"
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
applicationxfishscript = "application/x-fishscript"
fish = "fish"
applicationfits = "application/fits"
fits = "fits"
fit = "fit"
fts = "fts"
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
imageg3fax = "image/g3fax"
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
applicationxgerberjob = "application/x-gerber-job"
gbrjob = "gbrjob"
applicationxgcacompressed = "application/x-gca-compressed"
gca = "gca"
textxgcode = "text/x.gcode"
gcode = "gcode"
applicationxgdscript = "application/x-gdscript"
gd = "gd"
applicationxgdromcue = "application/x-gd-rom-cue"
gdi = "gdi"
modelvndgdl = "model/vnd.gdl"
gdl = "gdl"
applicationvndgoogleappsdocument = "application/vnd.google-apps.document"
gdoc = "gdoc"
applicationxgodotshader = "application/x-godot-shader"
gdshader = "gdshader"
textvndfamilysearchgedcom = "text/vnd.familysearch.gedcom"
ged = "ged"
gedcom = "gedcom"
applicationxgenesisrom = "application/x-genesis-rom"
gen = "gen"
sgd = "sgd"
applicationvnddynageo = "application/vnd.dynageo"
geo = "geo"
applicationgeo_json = "application/geo+json"
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
modelgltf_json = "model/gltf+json"
gltf = "gltf"
applicationgml_xml = "application/gml+xml"
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
applicationgpx_xml = "application/gpx+xml"
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
applicationsrgs_xml = "application/srgs+xml"
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
textxgcodegx = "text/x-gcode-gx"
gx = "gx"
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
applicationvndhal_xml = "application/vnd.hal+xml"
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
hif = "hif"
imageheicsequence = "image/heic-sequence"
heics = "heics"
imageheifsequence = "image/heif-sequence"
heifs = "heifs"
imagehej2k = "image/hej2k"
hej2 = "hej2"
applicationatscheld_xml = "application/atsc-held+xml"
held = "held"
applicationxhfefloppyimage = "application/x-hfe-floppy-image"
hfe = "hfe"
textxc__hdr = "text/x-c++hdr"
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
applicationinkml_xml = "application/inkml+xml"
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
applicationxipynb_json = "application/x-ipynb+json"
ipynb = "ipynb"
applicationvndibmrightsmanagement = "application/vnd.ibm.rights-management"
irm = "irm"
applicationvndirepositorypackage_xml = "application/vnd.irepository.package+xml"
irp = "irp"
applicationvndefiiso = "application/vnd.efi.iso"
iso = "iso"
iso9660 = "iso9660"
audioxit = "audio/x-it"
it = "it"
applicationxit87 = "application/x-it87"
it87 = "it87"
applicationvndshanainformedformtemplate = "application/vnd.shana.informed.formtemplate"
itp = "itp"
applicationits_xml = "application/its+xml"
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
applicationjavaarchive = "application/java-archive"
jar = "jar"
war = "war"
ear = "ear"
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
textjulia = "text/julia"
jl = "jl"
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
jfif = "jfif"
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
applicationjrd_json = "application/jrd+json"
jrd = "jrd"
textjavascript = "text/javascript"
js = "js"
jsm = "jsm"
mjs = "mjs"
textjscriptencode = "text/jscript.encode"
jse = "jse"
applicationjson = "application/json"
json = "json"
map = "map"
applicationjson5 = "application/json5"
json5 = "json5"
applicationld_json = "application/ld+json"
jsonld = "jsonld"
applicationjsonml_json = "application/jsonml+json"
jsonml = "jsonml"
applicationjsonpatch_json = "application/json-patch+json"
jsonpatch = "jsonpatch"
textjsx = "text/jsx"
jsx = "jsx"
modeljt = "model/jt"
jt = "jt"
imagejxl = "image/jxl"
jxl = "jxl"
imagejxr = "image/jxr"
jxr = "jxr"
hdp = "hdp"
wdp = "wdp"
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
applicationxkformula = "application/x-kformula"
kfo = "kfo"
applicationvndkidspiration = "application/vnd.kidspiration"
kia = "kia"
applicationxkillustrator = "application/x-killustrator"
kil = "kil"
applicationvndgoogleearthkml_xml = "application/vnd.google-earth.kml+xml"
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
krz = "krz"
applicationxkspread = "application/x-kspread"
ksp = "ksp"
textxkaitaistruct = "text/x-kaitai-struct"
ksy = "ksy"
textxkotlin = "text/x-kotlin"
kt = "kt"
imagektx = "image/ktx"
ktx = "ktx"
imagektx2 = "image/ktx2"
ktx2 = "ktx2"
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
applicationvndlaslas_xml = "application/vnd.las.las+xml"
lasxml = "lasxml"
applicationvndllamagraphicslifebalancedesktop = "application/vnd.llamagraphics.life-balance.desktop"
lbd = "lbd"
applicationvndllamagraphicslifebalanceexchange_xml = "application/vnd.llamagraphics.life-balance.exchange+xml"
lbe = "lbe"
textxldif = "text/x-ldif"
ldif = "ldif"
applicationvndhhelessonplayer = "application/vnd.hhe.lesson-player"
les = "les"
textless = "text/less"
less = "less"
applicationlgr_xml = "application/lgr+xml"
lgr = "lgr"
applicationxlha = "application/x-lha"
lha = "lha"
lzh = "lzh"
textxliteratehaskell = "text/x-literate-haskell"
lhs = "lhs"
applicationxlhz = "application/x-lhz"
lhz = "lhz"
applicationvndroute66link66_xml = "application/vnd.route66.link66+xml"
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
applicationlost_xml = "application/lost+xml"
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
videoisosegment = "video/iso.segment"
m4s = "m4s"
applicationxthomsoncartridgememo7 = "application/x-thomson-cartridge-memo7"
m7 = "m7"
applicationxmarkaby = "application/x-markaby"
mab = "mab"
applicationmads_xml = "application/mads+xml"
mads = "mads"
applicationmmtaei_xml = "application/mmt-aei+xml"
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
_19 = "19"
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
applicationxlmdb = "application/x-lmdb"
mdb = "mdb"
lmdb = "lmdb"
imagevndmsmodi = "image/vnd.ms-modi"
mdi = "mdi"
textxtroffme = "text/x-troff-me"
me = "me"
textxmeson = "text/x-meson"
mesonbuild = "mesonbuild"
mesonoptionstxt = "mesonoptionstxt"
applicationmetalink4_xml = "application/metalink4+xml"
meta4 = "meta4"
applicationmetalink_xml = "application/metalink+xml"
metalink = "metalink"
applicationmets_xml = "application/mets+xml"
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
textxobjc__src = "text/x-objc++src"
mm = "mm"
applicationvndchipnutskaraokemmd = "application/vnd.chipnuts.karaoke-mmd"
mmd = "mmd"
applicationvndsmaf = "application/vnd.smaf"
mmf = "mmf"
smaf = "smaf"
applicationmathml_xml = "application/mathml+xml"
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
applicationmods_xml = "application/mods+xml"
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
audioxmusepack = "audio/x-musepack"
mpc = "mpc"
mpp = "mpp"
mp = "mp"
applicationdash_xml = "application/dash+xml"
mpd = "mpd"
videompeg = "video/mpeg"
mpeg = "mpeg"
mpg = "mpg"
mpe = "mpe"
vob = "vob"
_090909vdr = "090909vdr"
m1v = "m1v"
m2v = "m2v"
applicationmediapolicydataset_xml = "application/media-policy-dataset+xml"
mpf = "mpf"
applicationmp4 = "application/mp4"
mpg4 = "mpg4"
mp4s = "mp4s"
m4p = "m4p"
applicationvndappleinstaller_xml = "application/vnd.apple.installer+xml"
mpkg = "mpkg"
textxmpl2 = "text/x-mpl2"
mpl = "mpl"
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
applicationmarcxml_xml = "application/marcxml+xml"
mrcx = "mrcx"
textxmrml = "text/x-mrml"
mrml = "mrml"
mrl = "mrl"
applicationxmodrinthmodpack_zip = "application/x-modrinth-modpack+zip"
mrpack = "mrpack"
imagexminoltamrw = "image/x-minolta-mrw"
mrw = "mrw"
textxtroffms = "text/x-troff-ms"
ms = "ms"
applicationmediaservercontrol_xml = "application/mediaservercontrol+xml"
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
applicationmsix = "application/msix"
msix = "msix"
applicationmsixbundle = "application/msixbundle"
msixbundle = "msixbundle"
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
applicationmmtusd_xml = "application/mmt-usd+xml"
musd = "musd"
applicationvndrecordaremusicxml_xml = "application/vnd.recordare.musicxml+xml"
musicxml = "musicxml"
applicationxmsmediaview = "application/x-msmediaview"
mvb = "mvb"
m13 = "m13"
m14 = "m14"
applicationvndmapboxvectortile = "application/vnd.mapbox-vector-tile"
mvt = "mvt"
applicationvndmfer = "application/vnd.mfer"
mwf = "mwf"
applicationmxf = "application/mxf"
mxf = "mxf"
applicationvndrecordaremusicxml = "application/vnd.recordare.musicxml"
mxl = "mxl"
audiomobilexmf = "audio/mobile-xmf"
mxmf = "mxmf"
applicationxv_xml = "application/xv+xml"
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
applicationxdtbncx_xml = "application/x-dtbncx+xml"
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
textxnim = "text/x-nim"
nim = "nim"
textxnimscript = "text/x-nimscript"
nims = "nims"
nimble = "nimble"
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
imagexnikonnrw = "image/x-nikon-nrw"
nrw = "nrw"
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
applicationxnuscript = "application/x-nuscript"
nu = "nu"
applicationvndapplenumbers = "application/vnd.apple.numbers"
numbers = "numbers"
applicationxnzb = "application/x-nzb"
nzb = "nzb"
applicationxobject = "application/x-object"
o = "o"
mod = "mod"
applicationvndfujitsuoasys2 = "application/vnd.fujitsu.oasys2"
oa2 = "oa2"
applicationvndfujitsuoasys3 = "application/vnd.fujitsu.oasys3"
oa3 = "oa3"
applicationvndfujitsuoasys = "application/vnd.fujitsu.oasys"
oas = "oas"
applicationxmsbinder = "application/x-msbinder"
obd = "obd"
applicationvndopenbloxgame_xml = "application/vnd.openblox.game+xml"
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
videoxogm_ogg = "video/x-ogm+ogg"
ogm = "ogm"
videoogg = "video/ogg"
ogv = "ogv"
applicationogg = "application/ogg"
ogx = "ogx"
applicationxoleo = "application/x-oleo"
oleo = "oleo"
applicationomdoc_xml = "application/omdoc+xml"
omdoc = "omdoc"
applicationonenote = "application/onenote"
onetoc = "onetoc"
onetoc2 = "onetoc2"
onetmp = "onetmp"
onepkg = "onepkg"
textxooc = "text/x-ooc"
ooc = "ooc"
applicationxopenvpnprofile = "application/x-openvpn-profile"
openvpn = "openvpn"
ovpn = "ovpn"
applicationoebpspackage_xml = "application/oebps-package+xml"
opf = "opf"
textxopml_xml = "text/x-opml+xml"
opml = "opml"
imageopenraster = "image/openraster"
ora = "ora"
imagexolympusorf = "image/x-olympus-orf"
orf = "orf"
textorg = "text/org"
org = "org"
applicationvndyamahaopenscoreformat = "application/vnd.yamaha.openscoreformat"
osf = "osf"
applicationvndyamahaopenscoreformatosfpvg_xml = "application/vnd.yamaha.openscoreformat.osfpvg+xml"
osfpvg = "osfpvg"
applicationvndopenstreetmapdata_xml = "application/vnd.openstreetmap.data+xml"
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
applicationovf = "application/ovf"
ova = "ova"
applicationxvirtualboxovf = "application/x-virtualbox-ovf"
ovf = "ovf"
applicationowl_xml = "application/owl+xml"
owx = "owx"
applicationoxps = "application/oxps"
oxps = "oxps"
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
applicationxperfdata = "application/x-perf-data"
perfdata = "perfdata"
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
textxmaven_xml = "text/x-maven+xml"
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
applicationxgodotproject = "application/x-godot-project"
projectgodot = "projectgodot"
applicationprovenance_xml = "application/provenance+xml"
provx = "provx"
applicationpostscript = "application/postscript"
ps = "ps"
applicationxpowershell = "application/x-powershell"
ps1 = "ps1"
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
applicationpskc_xml = "application/pskc+xml"
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
pyi = "pyi"
audiovndmsplayreadymediapya = "audio/vnd.ms-playready.media.pya"
pya = "pya"
applicationxpythonbytecode = "application/x-python-bytecode"
pyc = "pyc"
pyo = "pyo"
modelvndpythapyox = "model/vnd.pytha.pyox"
pyox = "pyox"
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
applicationxqeddisk = "application/x-qed-disk"
qed = "qed"
applicationvndintuqfx = "application/vnd.intu.qfx"
qfx = "qfx"
applicationxqw = "application/x-qw"
qif = "qif"
textxqml = "text/x-qml"
qml = "qml"
qmltypes = "qmltypes"
qmlproject = "qmlproject"
imageqoi = "image/qoi"
qoi = "qoi"
applicationxqpress = "application/x-qpress"
qp = "qp"
applicationvndpublisharedeltatree = "application/vnd.publishare-delta-tree"
qps = "qps"
applicationsparqlquery = "application/sparql-query"
qs = "qs"
rq = "rq"
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
applicationraml_yaml = "application/raml+yaml"
raml = "raml"
applicationrouteapd_xml = "application/route-apd+xml"
rapd = "rapd"
applicationvndrar = "application/vnd.rar"
rar = "rar"
imagexcmuraster = "image/x-cmu-raster"
ras = "ras"
imagexpanasonicrw = "image/x-panasonic-rw"
raw = "raw"
applicationvndefiimg = "application/vnd.efi.img"
rawdiskimage = "rawdiskimage"
img = "img"
applicationxrawdiskimagexzcompressed = "application/x-raw-disk-image-xz-compressed"
rawdiskimagexz = "rawdiskimagexz"
imgxz = "imgxz"
applicationxruby = "application/x-ruby"
rb = "rb"
applicationvndipunpluggedrcprofile = "application/vnd.ipunplugged.rcprofile"
rcprofile = "rcprofile"
applicationrdf_xml = "application/rdf+xml"
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
applicationp2poverlay_xml = "application/p2p-overlay+xml"
relo = "relo"
applicationvndbusinessobjects = "application/vnd.businessobjects"
rep = "rep"
applicationxgodotresource = "application/x-godot-resource"
res = "res"
tres = "tres"
imagexrgb = "image/x-rgb"
rgb = "rgb"
applicationreginfo_xml = "application/reginfo+xml"
rif = "rif"
audiovndrip = "audio/vnd.rip"
rip = "rip"
applicationxresearchinfosystems = "application/x-research-info-systems"
ris = "ris"
applicationresourcelists_xml = "application/resource-lists+xml"
rl = "rl"
imagevndfujixeroxedmicsrlc = "image/vnd.fujixerox.edmics-rlc"
rlc = "rlc"
applicationresourcelistsdiff_xml = "application/resource-lists-diff+xml"
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
textrust = "text/rust"
rs = "rs"
applicationatscrsat_xml = "application/atsc-rsat+xml"
rsat = "rsat"
applicationrsd_xml = "application/rsd+xml"
rsd = "rsd"
applicationurcressheet_xml = "application/urc-ressheet+xml"
rsheet = "rsheet"
applicationrss_xml = "application/rss+xml"
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
applicationrouteusd_xml = "application/route-usd+xml"
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
textxsagemath = "text/x-sagemath"
sage = "sage"
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
applicationsbml_xml = "application/sbml+xml"
sbml = "sbml"
textxscala = "text/x-scala"
scala = "scala"
sc = "sc"
applicationxmsschedule = "application/x-msschedule"
scd = "scd"
textxscheme = "text/x-scheme"
scm = "scm"
ss = "ss"
applicationxgodotscene = "application/x-godot-scene"
scn = "scn"
tscn = "tscn"
escn = "escn"
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
applicationvndsolentsdkm_xml = "application/vnd.solent.sdkm+xml"
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
applicationsenml_xml = "application/senml+xml"
senmlx = "senmlx"
applicationsensml_xml = "application/sensml+xml"
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
applicationshf_xml = "application/shf+xml"
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
applicationroutestsid_xml = "application/route-s-tsid+xml"
sls = "sls"
applicationvndepsonsalt = "application/vnd.epson.salt"
slt = "slt"
applicationvndstepmaniastepchart = "application/vnd.stepmania.stepchart"
sm = "sm"
applicationvndstardivisionmail = "application/vnd.stardivision.mail"
smd = "smd"
applicationvndstardivisionmath = "application/vnd.stardivision.math"
smf = "smf"
applicationsmil_xml = "application/smil+xml"
smil = "smil"
smi = "smi"
sml = "sml"
kino = "kino"
videovndradgamettoolssmacker = "video/vnd.radgamettools.smacker"
smk = "smk"
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
so09 = "so09"
applicationxfontspeedo = "application/x-font-speedo"
spd = "spd"
textspdx = "text/spdx"
spdx = "spdx"
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
applicationxapplesystemprofiler_xml = "application/x-apple-systemprofiler+xml"
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
applicationsru_xml = "application/sru+xml"
sru = "sru"
applicationsparqlresults_xml = "application/sparql-results+xml"
srx = "srx"
textxssa = "text/x-ssa"
ssa = "ssa"
ass = "ass"
applicationssdl_xml = "application/ssdl+xml"
ssdl = "ssdl"
applicationvndkodakdescriptor = "application/vnd.kodak-descriptor"
sse = "sse"
applicationvndepsonssf = "application/vnd.epson.ssf"
ssf = "ssf"
applicationssml_xml = "application/ssml+xml"
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
modelstep_xml = "model/step+xml"
stpx = "stpx"
modelstepxml_zip = "model/step-xml+zip"
stpxz = "stpxz"
modelstep_zip = "model/step+zip"
stpz = "stpz"
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
imagesvg_xml = "image/svg+xml"
svg = "svg"
imagesvg_xmlcompressed = "image/svg+xml-compressed"
svgz = "svgz"
svggz = "svggz"
textxsvhdr = "text/x-svhdr"
svh = "svh"
applicationvndadobeflashmovie = "application/vnd.adobe.flash.movie"
swf = "swf"
spl = "spl"
applicationvndaristanetworksswi = "application/vnd.aristanetworks.swi"
swi = "swi"
applicationswid_xml = "application/swid+xml"
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
audioxtak = "audio/x-tak"
tak = "tak"
applicationvndtaointentmodulearchive = "application/vnd.tao.intent-module-archive"
tao = "tao"
imagevndtencenttap = "image/vnd.tencent.tap"
tap = "tap"
applicationxtar = "application/x-tar"
tar = "tar"
gtar = "gtar"
gem = "gem"
applicationxbzip1compressedtar = "application/x-bzip1-compressed-tar"
tarbz = "tarbz"
tbz = "tbz"
applicationxbzip2compressedtar = "application/x-bzip2-compressed-tar"
tarbz2 = "tarbz2"
tbz2 = "tbz2"
tb2 = "tb2"
applicationxbzip3compressedtar = "application/x-bzip3-compressed-tar"
tarbz3 = "tarbz3"
tbz3 = "tbz3"
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
applicationurctargetdesc_xml = "application/urc-targetdesc+xml"
td = "td"
applicationvndsmartteacher = "application/vnd.smart.teacher"
teacher = "teacher"
applicationtei_xml = "application/tei+xml"
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
applicationthraud_xml = "application/thraud+xml"
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
applicationxtiledtmx = "application/x-tiled-tmx"
tmx = "tmx"
applicationvndmstnef = "application/vnd.ms-tnef"
tnef = "tnef"
tnf = "tnf"
winmaildat = "winmaildat"
applicationxcdrdaotoc = "application/x-cdrdao-toc"
toc = "toc"
textxtodotxt = "text/x-todo-txt"
todotxt = "todotxt"
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
textvndtrolltechlinguist = "text/vnd.trolltech.linguist"
ts = "ts"
applicationtimestampeddata = "application/timestamped-data"
tsd = "tsd"
texttabseparatedvalues = "text/tab-separated-values"
tsv = "tsv"
applicationxtiledtsx = "application/x-tiled-tsx"
tsx = "tsx"
audioxtta = "audio/x-tta"
tta = "tta"
fontcollection = "font/collection"
ttc = "ttc"
fontttf = "font/ttf"
ttf = "ttf"
textturtle = "text/turtle"
ttl = "ttl"
applicationttml_xml = "application/ttml+xml"
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
textxtypst = "text/x-typst"
typ = "typ"
modelu3d = "model/u3d"
u3d = "u3d"
messageglobaldeliverystatus = "message/global-delivery-status"
u8dsn = "u8dsn"
messageglobalheaders = "message/global-headers"
u8hdr = "u8hdr"
messageglobaldispositionnotification = "message/global-disposition-notification"
u8mdn = "u8mdn"
messageglobal = "message/global"
u8msg = "u8msg"
applicationubjson = "application/ubjson"
ubj = "ubj"
applicationvndufdl = "application/vnd.ufdl"
ufd = "ufd"
ufdl = "ufdl"
applicationxufraw = "application/x-ufraw"
ufraw = "ufraw"
applicationxdesigner = "application/x-designer"
ui = "ui"
textxuil = "text/x-uil"
uil = "uil"
audioxmod = "audio/x-mod"
ult = "ult"
uni = "uni"
m15 = "m15"
mtm = "mtm"
_669 = "669"
med = "med"
applicationxglulx = "application/x-glulx"
ulx = "ulx"
applicationvndumajin = "application/vnd.umajin"
umj = "umj"
applicationvndunity = "application/vnd.unity"
unityweb = "unityweb"
applicationvnduoml_xml = "application/vnd.uoml+xml"
uoml = "uoml"
uo = "uo"
texturilist = "text/uri-list"
uri = "uri"
uris = "uris"
urls = "urls"
applicationxmswinurl = "application/x-mswinurl"
url = "url"
modelvndusda = "model/vnd.usda"
usda = "usda"
modelvndusdz_zip = "model/vnd.usdz+zip"
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
applicationvnddecettml_xml = "application/vnd.dece.ttml+xml"
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
textvbscriptencode = "text/vbscript.encode"
vbe = "vbe"
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
applicationxvdidisk = "application/x-vdi-disk"
vdi = "vdi"
modelvndsapvds = "model/vnd.sap.vds"
vds = "vds"
textxvhdl = "text/x-vhdl"
vhd = "vhd"
vhdl = "vhdl"
applicationxvhdxdisk = "application/x-vhdx-disk"
vhdx = "vhdx"
applicationvndvisionary = "application/vnd.visionary"
vis = "vis"
videovndvivo = "video/vnd.vivo"
viv = "viv"
vivo = "vivo"
applicationxvmdkdisk = "application/x-vmdk-disk"
vmdk = "vmdk"
audioxvoc = "audio/x-voc"
voc = "voc"
applicationxvhddisk = "application/x-vhd-disk"
vpc = "vpc"
modelvrml = "model/vrml"
vrm = "vrm"
vrml = "vrml"
wrl = "wrl"
applicationvndvisio = "application/vnd.visio"
vsd = "vsd"
vst = "vst"
vsw = "vsw"
vss = "vss"
applicationvndmsvisiodrawingmacroenabledmain_xml = "application/vnd.ms-visio.drawing.macroenabled.main+xml"
vsdm = "vsdm"
applicationvndmsvisiodrawingmain_xml = "application/vnd.ms-visio.drawing.main+xml"
vsdx = "vsdx"
applicationvndvsf = "application/vnd.vsf"
vsf = "vsf"
applicationvndmsvisiostencilmacroenabledmain_xml = "application/vnd.ms-visio.stencil.macroenabled.main+xml"
vssm = "vssm"
applicationvndmsvisiostencilmain_xml = "application/vnd.ms-visio.stencil.main+xml"
vssx = "vssx"
applicationvndmsvisiotemplatemacroenabledmain_xml = "application/vnd.ms-visio.template.macroenabled.main+xml"
vstm = "vstm"
applicationvndmsvisiotemplatemain_xml = "application/vnd.ms-visio.template.main+xml"
vstx = "vstx"
imagevndvalvesourcetexture = "image/vnd.valve.source.texture"
vtf = "vtf"
textvtt = "text/vtt"
vtt = "vtt"
modelvndvtu = "model/vnd.vtu"
vtu = "vtu"
applicationvoicexml_xml = "application/voicexml+xml"
vxml = "vxml"
applicationxwiiwad = "application/x-wii-wad"
wad = "wad"
applicationvndsunwadl_xml = "application/vnd.sun.wadl+xml"
wadl = "wadl"
applicationwasm = "application/wasm"
wasm = "wasm"
audiovndwave = "audio/vnd.wave"
wav = "wav"
applicationxquattropro = "application/x-quattropro"
wb1 = "wb1"
wb2 = "wb2"
wb3 = "wb3"
imagevndwapwbmp = "image/vnd.wap.wbmp"
wbmp = "wbmp"
applicationvndcriticaltoolswbs_xml = "application/vnd.criticaltools.wbs+xml"
wbs = "wbs"
applicationvndwapwbxml = "application/vnd.wap.wbxml"
wbxml = "wbxml"
applicationvndmsworks = "application/vnd.ms-works"
wcm = "wcm"
wdb = "wdb"
wps = "wps"
xlr = "xlr"
audiowebm = "audio/webm"
weba = "weba"
applicationxwebappmanifest_json = "application/x-web-app-manifest+json"
webapp = "webapp"
videowebm = "video/webm"
webm = "webm"
applicationmanifest_json = "application/manifest+json"
webmanifest = "webmanifest"
imagewebp = "image/webp"
webp = "webp"
applicationvndpmiwidget = "application/vnd.pmi.widget"
wg = "wg"
textwgsl = "text/wgsl"
wgsl = "wgsl"
applicationwidget = "application/widget"
wgt = "wgt"
applicationwatcherinfo_xml = "application/watcherinfo+xml"
wif = "wif"
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
applicationwsdl_xml = "application/wsdl+xml"
wsdl = "wsdl"
applicationwspolicy_xml = "application/wspolicy+xml"
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
x_b = "x_b"
modelvndparasolidtransmittext = "model/vnd.parasolid.transmit.text"
x_t = "x_t"
modelx3d_xml = "model/x3d+xml"
x3d = "x3d"
x3dz = "x3dz"
modelx3d_binary = "model/x3d+binary"
x3db = "x3db"
x3dbz = "x3dbz"
modelx3d_vrml = "model/x3d+vrml"
x3dv = "x3dv"
x3dvz = "x3dvz"
imagexsigmax3f = "image/x-sigma-x3f"
x3f = "x3f"
applicationxaml_xml = "application/xaml+xml"
xaml = "xaml"
applicationxsilverlightapp = "application/x-silverlight-app"
xap = "xap"
applicationxxar = "application/x-xar"
xar = "xar"
pkg = "pkg"
applicationxcapatt_xml = "application/xcap-att+xml"
xav = "xav"
applicationxmsxbap = "application/x-ms-xbap"
xbap = "xbap"
applicationvndfujixeroxdocuworksbinder = "application/vnd.fujixerox.docuworks.binder"
xbd = "xbd"
applicationxxbel = "application/x-xbel"
xbel = "xbel"
imagexxbitmap = "image/x-xbitmap"
xbm = "xbm"
applicationxcapcaps_xml = "application/xcap-caps+xml"
xca = "xca"
imagexxcf = "image/x-xcf"
xcf = "xcf"
imagexcompressedxcf = "image/x-compressed-xcf"
xcfgz = "xcfgz"
xcfbz2 = "xcfbz2"
applicationcalendar_xml = "application/calendar+xml"
xcs = "xcs"
applicationxcapdiff_xml = "application/xcap-diff+xml"
xdf = "xdf"
applicationvndsyncmldm_xml = "application/vnd.syncml.dm+xml"
xdm = "xdm"
applicationvndadobexdp_xml = "application/vnd.adobe.xdp+xml"
xdp = "xdp"
applicationdssc_xml = "application/dssc+xml"
xdssc = "xdssc"
applicationvndfujixeroxdocuworks = "application/vnd.fujixerox.docuworks"
xdw = "xdw"
applicationxcapel_xml = "application/xcap-el+xml"
xel = "xel"
applicationxenc_xml = "application/xenc+xml"
xenc = "xenc"
applicationpatchopserror_xml = "application/patch-ops-error+xml"
xer = "xer"
applicationvndadobexfdf = "application/vnd.adobe.xfdf"
xfdf = "xfdf"
applicationvndxfdl = "application/vnd.xfdl"
xfdl = "xfdl"
applicationvndpwgxhtmlprint_xml = "application/vnd.pwg-xhtml-print+xml"
xhtm = "xhtm"
applicationxhtml_xml = "application/xhtml+xml"
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
applicationxliff_xml = "application/xliff+xml"
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
applicationxcapns_xml = "application/xcap-ns+xml"
xns = "xns"
applicationvndolpcsugar = "application/vnd.olpc-sugar"
xo = "xo"
applicationxop_xml = "application/xop+xml"
xop = "xop"
applicationxxpinstall = "application/x-xpinstall"
xpi = "xpi"
applicationxproc_xml = "application/xproc+xml"
xpl = "xpl"
imagexxpixmap = "image/x-xpixmap"
xpm = "xpm"
applicationvndisxpr = "application/vnd.is-xpr"
xpr = "xpr"
applicationvndmsxpsdocument = "application/vnd.ms-xpsdocument"
xps = "xps"
applicationvndinterconformnet = "application/vnd.intercon.formnet"
xpw = "xpw"
xpx = "xpx"
applicationprsxsf_xml = "application/prs.xsf+xml"
xsf = "xsf"
applicationxslt_xml = "application/xslt+xml"
xsl = "xsl"
xslt = "xslt"
applicationvndsyncml_xml = "application/vnd.syncml+xml"
xsm = "xsm"
applicationxspf_xml = "application/xspf+xml"
xspf = "xspf"
applicationvndmozillaxul_xml = "application/vnd.mozilla.xul+xml"
xul = "xul"
imagexxwindowdump = "image/x-xwindowdump"
xwd = "xwd"
chemicalxxyz = "chemical/x-xyz"
xyz = "xyz"
applicationxxz = "application/x-xz"
xz = "xz"
applicationyaml = "application/yaml"
yaml = "yaml"
yml = "yml"
applicationyang = "application/yang"
yang = "yang"
applicationyin_xml = "application/yin+xml"
yin = "yin"
textxsuseymp = "text/x-suse-ymp"
ymp = "ymp"
videovndyoutubeyt = "video/vnd.youtube.yt"
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
applicationvndzzazzdeck_xml = "application/vnd.zzazz.deck+xml"
zaz = "zaz"
applicationxopenzim = "application/x-openzim"
zim = "zim"
applicationzip = "application/zip"
zip = "zip"
zipx = "zipx"
applicationvndzul = "application/vnd.zul"
zir = "zir"
zirz = "zirz"
applicationvndhandheldentertainment_xml = "application/vnd.handheld-entertainment+xml"
zmm = "zmm"
applicationxzoo = "application/x-zoo"
zoo = "zoo"
applicationxzpaq = "application/x-zpaq"
zpaq = "zpaq"
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

    if extension == zpaq:
        return applicationxzpaq

    if extension == zoo:
        return applicationxzoo

    # iana
    if extension == zmm:
        return applicationvndhandheldentertainment_xml

    # iana
    if extension in (zir, zirz):
        return applicationvndzul

    if extension in (zip, zipx):
        return applicationzip

    if extension == zim:
        return applicationxopenzim

    # iana
    if extension == zaz:
        return applicationvndzzazzdeck_xml

    # apache
    if extension in (z1, z2, z3, z4, z5, z6, z7, z8):
        return applicationxzmachine

    if extension == z:
        return applicationxcompress

    if extension == yt:
        return videovndyoutubeyt

    if extension == ymp:
        return textxsuseymp

    # iana
    if extension == yin:
        return applicationyin_xml

    # iana
    if extension == yang:
        return applicationyang

    if extension in (yaml, yml):
        return applicationyaml

    if extension == xz:
        return applicationxxz

    # apache
    if extension == xyz:
        return chemicalxxyz

    if extension == xwd:
        return imagexxwindowdump

    if extension == xul:
        return applicationvndmozillaxul_xml

    if extension == xspf:
        return applicationxspf_xml

    # iana
    if extension == xsm:
        return applicationvndsyncml_xml

    if extension in (xsl, xslt):
        return applicationxslt_xml

    # iana
    if extension == xsf:
        return applicationprsxsf_xml

    # iana
    if extension in (xpw, xpx):
        return applicationvndinterconformnet

    if extension == xps:
        return applicationvndmsxpsdocument

    # iana
    if extension == xpr:
        return applicationvndisxpr

    if extension == xpm:
        return imagexxpixmap

    # apache
    if extension == xpl:
        return applicationxproc_xml

    if extension == xpi:
        return applicationxxpinstall

    # iana
    if extension == xop:
        return applicationxop_xml

    # iana
    if extension == xo:
        return applicationvndolpcsugar

    # iana
    if extension == xns:
        return applicationxcapns_xml

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
        return applicationxliff_xml

    if extension == xlam:
        return applicationvndmsexceladdinmacroenabled12

    # iana
    if extension == xif:
        return imagevndxiff

    if extension == xi:
        return audioxxi

    if extension in (xhtml, xht, html, htm):
        return applicationxhtml_xml

    # iana
    if extension == xhtm:
        return applicationvndpwgxhtmlprint_xml

    # iana
    if extension == xfdl:
        return applicationvndxfdl

    # apache
    if extension == xfdf:
        return applicationvndadobexfdf

    # iana
    if extension == xer:
        return applicationpatchopserror_xml

    # iana
    if extension == xenc:
        return applicationxenc_xml

    # iana
    if extension == xel:
        return applicationxcapel_xml

    # iana
    if extension == xdw:
        return applicationvndfujixeroxdocuworks

    # iana
    if extension == xdssc:
        return applicationdssc_xml

    # iana
    if extension == xdp:
        return applicationvndadobexdp_xml

    # iana
    if extension == xdm:
        return applicationvndsyncmldm_xml

    # iana
    if extension == xdf:
        return applicationxcapdiff_xml

    # iana
    if extension == xcs:
        return applicationcalendar_xml

    if extension in (xcfgz, xcfbz2):
        return imagexcompressedxcf

    if extension == xcf:
        return imagexxcf

    # iana
    if extension == xca:
        return applicationxcapcaps_xml

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
        return applicationxcapatt_xml

    if extension in (xar, pkg):
        return applicationxxar

    # apache
    if extension == xap:
        return applicationxsilverlightapp

    # apache
    if extension == xaml:
        return applicationxaml_xml

    if extension == x3f:
        return imagexsigmax3f

    # apache
    if extension in (x3dv, x3dvz):
        return modelx3d_vrml

    # apache
    if extension in (x3db, x3dbz):
        return modelx3d_binary

    # iana
    if extension in (x3d, x3dz):
        return modelx3d_xml

    # iana
    if extension == x_t:
        return modelvndparasolidtransmittext

    # iana
    if extension == x_b:
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
        return applicationwspolicy_xml

    # iana
    if extension == wsdl:
        return applicationwsdl_xml

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
    if extension == wif:
        return applicationwatcherinfo_xml

    # iana
    if extension == wgt:
        return applicationwidget

    # iana
    if extension == wgsl:
        return textwgsl

    # iana
    if extension == wg:
        return applicationvndpmiwidget

    if extension == webp:
        return imagewebp

    # iana
    if extension == webmanifest:
        return applicationmanifest_json

    if extension == webm:
        return videowebm

    if extension == webapp:
        return applicationxwebappmanifest_json

    # apache
    if extension == weba:
        return audiowebm

    if extension in (wcm, wdb, wps, xlr):
        return applicationvndmsworks

    # iana
    if extension == wbxml:
        return applicationvndwapwbxml

    # iana
    if extension == wbs:
        return applicationvndcriticaltoolswbs_xml

    if extension == wbmp:
        return imagevndwapwbmp

    if extension in (wb1, wb2, wb3):
        return applicationxquattropro

    if extension == wav:
        return audiovndwave

    if extension == wasm:
        return applicationwasm

    # iana
    if extension == wadl:
        return applicationvndsunwadl_xml

    if extension == wad:
        return applicationxwiiwad

    # iana
    if extension == vxml:
        return applicationvoicexml_xml

    # iana
    if extension == vtu:
        return modelvndvtu

    if extension == vtt:
        return textvtt

    # iana
    if extension == vtf:
        return imagevndvalvesourcetexture

    if extension == vstx:
        return applicationvndmsvisiotemplatemain_xml

    if extension == vstm:
        return applicationvndmsvisiotemplatemacroenabledmain_xml

    if extension == vssx:
        return applicationvndmsvisiostencilmain_xml

    if extension == vssm:
        return applicationvndmsvisiostencilmacroenabledmain_xml

    # iana
    if extension == vsf:
        return applicationvndvsf

    if extension == vsdx:
        return applicationvndmsvisiodrawingmain_xml

    if extension == vsdm:
        return applicationvndmsvisiodrawingmacroenabledmain_xml

    if extension in (vsd, vst, vsw, vss):
        return applicationvndvisio

    if extension in (vrm, vrml, wrl):
        return modelvrml

    if extension == vpc:
        return applicationxvhddisk

    if extension == voc:
        return audioxvoc

    if extension == vmdk:
        return applicationxvmdkdisk

    if extension in (viv, vivo):
        return videovndvivo

    # iana
    if extension == vis:
        return applicationvndvisionary

    if extension == vhdx:
        return applicationxvhdxdisk

    if extension in (vhd, vhdl):
        return textxvhdl

    # iana
    if extension == vds:
        return modelvndsapvds

    if extension == vdi:
        return applicationxvdidisk

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

    if extension == vbe:
        return textvbscriptencode

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
        return applicationvnddecettml_xml

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
        return modelvndusdz_zip

    # iana
    if extension == usda:
        return modelvndusda

    if extension == url:
        return applicationxmswinurl

    # iana
    if extension in (uri, uris, urls):
        return texturilist

    # iana
    if extension in (uoml, uo):
        return applicationvnduoml_xml

    # iana
    if extension == unityweb:
        return applicationvndunity

    # iana
    if extension == umj:
        return applicationvndumajin

    # apache
    if extension == ulx:
        return applicationxglulx

    if extension in (ult, uni, m15, mtm, _669, med):
        return audioxmod

    if extension == uil:
        return textxuil

    if extension == ui:
        return applicationxdesigner

    if extension == ufraw:
        return applicationxufraw

    # iana
    if extension in (ufd, ufdl):
        return applicationvndufdl

    if extension == ubj:
        return applicationubjson

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

    # iana
    if extension == u3d:
        return modelu3d

    if extension == typ:
        return textxtypst

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
        return applicationttml_xml

    if extension == ttl:
        return textturtle

    if extension == ttf:
        return fontttf

    if extension == ttc:
        return fontcollection

    if extension == tta:
        return audioxtta

    if extension == tsx:
        return applicationxtiledtsx

    if extension == tsv:
        return texttabseparatedvalues

    # iana
    if extension == tsd:
        return applicationtimestampeddata

    if extension == ts:
        return textvndtrolltechlinguist

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

    if extension == todotxt:
        return textxtodotxt

    if extension == toc:
        return applicationxcdrdaotoc

    if extension in (tnef, tnf, winmaildat):
        return applicationvndmstnef

    if extension == tmx:
        return applicationxtiledtmx

    # iana
    if extension == tmo:
        return applicationvndtmobilelivetv

    if extension in (tif, tiff):
        return imagetiff

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
        return applicationthraud_xml

    if extension in (texi, texinfo):
        return textxtexinfo

    if extension in (tex, ltx, sty, cls, dtx, ins, latex):
        return textxtex

    # iana
    if extension in (tei, teicorpus):
        return applicationtei_xml

    # iana
    if extension == teacher:
        return applicationvndsmartteacher

    # iana
    if extension == td:
        return applicationurctargetdesc_xml

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

    if extension in (tarbz3, tbz3):
        return applicationxbzip3compressedtar

    if extension in (tarbz2, tbz2, tb2):
        return applicationxbzip2compressedtar

    if extension in (tarbz, tbz):
        return applicationxbzip1compressedtar

    if extension in (tar, gtar, gem):
        return applicationxtar

    # iana
    if extension == tap:
        return imagevndtencenttap

    # iana
    if extension == tao:
        return applicationvndtaointentmodulearchive

    if extension == tak:
        return audioxtak

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
        return applicationswid_xml

    # iana
    if extension == swi:
        return applicationvndaristanetworksswi

    if extension in (swf, spl):
        return applicationvndadobeflashmovie

    if extension == svh:
        return textxsvhdr

    if extension in (svgz, svggz):
        return imagesvg_xmlcompressed

    if extension == svg:
        return imagesvg_xml

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

    # iana
    if extension == stpz:
        return modelstep_zip

    # iana
    if extension == stpxz:
        return modelstepxml_zip

    # iana
    if extension == stpx:
        return modelstep_xml

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
        return applicationssml_xml

    # iana
    if extension == ssf:
        return applicationvndepsonssf

    # iana
    if extension == sse:
        return applicationvndkodakdescriptor

    # apache
    if extension == ssdl:
        return applicationssdl_xml

    if extension in (ssa, ass):
        return textxssa

    if extension == srx:
        return applicationsparqlresults_xml

    # iana
    if extension == sru:
        return applicationsru_xml

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
        return applicationxapplesystemprofiler_xml

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

    # iana
    if extension == spdx:
        return textspdx

    if extension == spd:
        return applicationxfontspeedo

    if extension in (so, so09):
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

    if extension == smk:
        return videovndradgamettoolssmacker

    if extension in (smil, smi, sml, kino):
        return applicationsmil_xml

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
        return applicationroutestsid_xml

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
        return applicationshf_xml

    # iana
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
        return applicationsensml_xml

    # iana
    if extension == senmlx:
        return applicationsenml_xml

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
        return applicationvndsolentsdkm_xml

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

    if extension in (scn, tscn, escn):
        return applicationxgodotscene

    if extension in (scm, ss):
        return textxscheme

    # apache
    if extension == scd:
        return applicationxmsschedule

    if extension in (scala, sc):
        return textxscala

    # iana
    if extension == sbml:
        return applicationsbml_xml

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

    if extension == sage:
        return textxsagemath

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
        return applicationrouteusd_xml

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
        return applicationrss_xml

    # iana
    if extension == rsheet:
        return applicationurcressheet_xml

    # apache
    if extension == rsd:
        return applicationrsd_xml

    # iana
    if extension == rsat:
        return applicationatscrsat_xml

    if extension == rs:
        return textrust

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
        return applicationresourcelistsdiff_xml

    # iana
    if extension == rlc:
        return imagevndfujixeroxedmicsrlc

    # iana
    if extension == rl:
        return applicationresourcelists_xml

    # apache
    if extension == ris:
        return applicationxresearchinfosystems

    # iana
    if extension == rip:
        return audiovndrip

    # iana
    if extension == rif:
        return applicationreginfo_xml

    if extension == rgb:
        return imagexrgb

    if extension in (res, tres):
        return applicationxgodotresource

    # iana
    if extension == rep:
        return applicationvndbusinessobjects

    # iana
    if extension == relo:
        return applicationp2poverlay_xml

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
        return applicationrdf_xml

    # iana
    if extension == rcprofile:
        return applicationvndipunpluggedrcprofile

    if extension == rb:
        return applicationxruby

    if extension in (rawdiskimagexz, imgxz):
        return applicationxrawdiskimagexzcompressed

    if extension in (rawdiskimage, img):
        return applicationvndefiimg

    if extension == raw:
        return imagexpanasonicrw

    if extension == ras:
        return imagexcmuraster

    if extension == rar:
        return applicationvndrar

    # iana
    if extension == rapd:
        return applicationrouteapd_xml

    if extension == raml:
        return applicationraml_yaml

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

    if extension in (qs, rq):
        return applicationsparqlquery

    # iana
    if extension == qps:
        return applicationvndpublisharedeltatree

    if extension == qp:
        return applicationxqpress

    if extension == qoi:
        return imageqoi

    if extension in (qml, qmltypes, qmlproject):
        return textxqml

    if extension == qif:
        return applicationxqw

    # iana
    if extension == qfx:
        return applicationvndintuqfx

    if extension == qed:
        return applicationxqeddisk

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

    # iana
    if extension == pyox:
        return modelvndpythapyox

    if extension in (pyc, pyo):
        return applicationxpythonbytecode

    # iana
    if extension == pya:
        return audiovndmsplayreadymediapya

    if extension in (py, py3, py3x, pyi):
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
        return applicationpskc_xml

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

    if extension == ps1:
        return applicationxpowershell

    if extension == ps:
        return applicationpostscript

    # iana
    if extension == provx:
        return applicationprovenance_xml

    if extension == projectgodot:
        return applicationxgodotproject

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
        return textxmaven_xml

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

    if extension == pfr:
        return applicationfonttdpfr

    if extension in (pfa, pfb, gsf, pfm):
        return applicationxfonttype1

    if extension == perfdata:
        return applicationxperfdata

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

    if extension == oxps:
        return applicationoxps

    if extension == owx:
        return applicationowl_xml

    if extension == ovf:
        return applicationxvirtualboxovf

    if extension == ova:
        return applicationovf

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
        return applicationvndopenstreetmapdata_xml

    # iana
    if extension == osfpvg:
        return applicationvndyamahaopenscoreformatosfpvg_xml

    # iana
    if extension == osf:
        return applicationvndyamahaopenscoreformat

    if extension == org:
        return textorg

    if extension == orf:
        return imagexolympusorf

    if extension == ora:
        return imageopenraster

    if extension == opml:
        return textxopml_xml

    # iana
    if extension == opf:
        return applicationoebpspackage_xml

    if extension in (openvpn, ovpn):
        return applicationxopenvpnprofile

    if extension == ooc:
        return textxooc

    # apache
    if extension in (onetoc, onetoc2, onetmp, onepkg):
        return applicationonenote

    # apache
    if extension == omdoc:
        return applicationomdoc_xml

    if extension == oleo:
        return applicationxoleo

    if extension == ogx:
        return applicationogg

    if extension == ogv:
        return videoogg

    if extension == ogm:
        return videoxogm_ogg

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
        return applicationvndopenbloxgame_xml

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

    if extension in (o, mod):
        return applicationxobject

    if extension == nzb:
        return applicationxnzb

    if extension == numbers:
        return applicationvndapplenumbers

    if extension == nu:
        return applicationxnuscript

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

    if extension == nrw:
        return imagexnikonnrw

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

    if extension in (nims, nimble):
        return textxnimscript

    if extension == nim:
        return textxnim

    if extension == ngp:
        return applicationxneogeopocketrom

    # iana
    if extension == ngdat:
        return applicationvndnokiangagedata

    if extension == ngc:
        return applicationxneogeopocketcolorrom

    # apache
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
        return applicationxdtbncx_xml

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
        return applicationxv_xml

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

    # iana
    if extension == mvt:
        return applicationvndmapboxvectortile

    # apache
    if extension in (mvb, m13, m14):
        return applicationxmsmediaview

    # iana
    if extension == musicxml:
        return applicationvndrecordaremusicxml_xml

    # iana
    if extension == musd:
        return applicationmmtusd_xml

    # iana
    if extension == mus:
        return applicationvndmusician

    if extension in (mup, _not):
        return textxmup

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

    if extension == msixbundle:
        return applicationmsixbundle

    if extension == msix:
        return applicationmsix

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
        return applicationmediaservercontrol_xml

    if extension == ms:
        return textxtroffms

    if extension == mrw:
        return imagexminoltamrw

    if extension == mrpack:
        return applicationxmodrinthmodpack_zip

    if extension in (mrml, mrl):
        return textxmrml

    # iana
    if extension == mrcx:
        return applicationmarcxml_xml

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

    if extension == mpl:
        return textxmpl2

    # iana
    if extension == mpkg:
        return applicationvndappleinstaller_xml

    # iana
    if extension in (mpg4, mp4s, m4p):
        return applicationmp4

    # iana
    if extension == mpf:
        return applicationmediapolicydataset_xml

    if extension in (mpeg, mpg, mpe, vob, _090909vdr, m1v, m2v):
        return videompeg

    # iana
    if extension == mpd:
        return applicationdash_xml

    if extension in (mpc, mpp, mp):
        return audioxmusepack

    if extension in (mp4, m4v, f4v, lrv, mp4v):
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
        return applicationmods_xml

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
        return applicationmathml_xml

    if extension in (mmf, smaf):
        return applicationvndsmaf

    # iana
    if extension == mmd:
        return applicationvndchipnutskaraokemmd

    if extension == mm:
        return textxobjc__src

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
        return applicationmets_xml

    if extension == metalink:
        return applicationmetalink_xml

    if extension == meta4:
        return applicationmetalink4_xml

    if extension in (mesonbuild, mesonoptionstxt):
        return textxmeson

    if extension == me:
        return textxtroffme

    if extension == mdi:
        return imagevndmsmodi

    if extension in (mdb, lmdb):
        return applicationxlmdb

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

    if extension in (man, _19):
        return applicationxtroffman

    if extension in (makefile, gnumakefile, mk, mak):
        return textxmakefile

    # iana
    if extension == mag:
        return applicationvndecowinchart

    # iana
    if extension == maei:
        return applicationmmtaei_xml

    # iana
    if extension == mads:
        return applicationmads_xml

    if extension == mab:
        return applicationxmarkaby

    if extension == m7:
        return applicationxthomsoncartridgememo7

    # iana
    if extension == m4s:
        return videoisosegment

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

    if extension in (m2t, m2ts, mts, cpi, clpi, mpls, bdm, bdmv):
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

    # apache
    if extension == ltf:
        return applicationvndfrogansltf

    if extension == lrz:
        return applicationxlrzip

    # iana
    if extension == lrm:
        return applicationvndmslrm

    # iana
    if extension == lostxml:
        return applicationlost_xml

    if extension == log:
        return textxlog

    if extension in (loas, xhe):
        return audiousac

    if extension == lnx:
        return applicationxatarilynxrom

    if extension == lnk:
        return applicationxmsshortcut

    if extension == litcoffee:
        return textcoffeescript

    # iana
    if extension == link66:
        return applicationvndroute66link66_xml

    if extension == lhz:
        return applicationxlhz

    if extension == lhs:
        return textxliteratehaskell

    if extension in (lha, lzh):
        return applicationxlha

    # iana
    if extension == lgr:
        return applicationlgr_xml

    if extension == less:
        return textless

    # iana
    if extension == les:
        return applicationvndhhelessonplayer

    if extension == ldif:
        return textxldif

    # iana
    if extension == lbe:
        return applicationvndllamagraphicslifebalanceexchange_xml

    # iana
    if extension == lbd:
        return applicationvndllamagraphicslifebalancedesktop

    # iana
    if extension == lasxml:
        return applicationvndlaslas_xml

    if extension == la:
        return applicationxsharedlibraryla

    if extension in (kwd, kwt):
        return applicationxkword

    if extension == kud:
        return applicationxkugar

    # iana
    if extension in (ktz, ktr):
        return applicationvndkahootz

    if extension == ktx2:
        return imagektx2

    if extension == ktx:
        return imagektx

    if extension == kt:
        return textxkotlin

    if extension == ksy:
        return textxkaitaistruct

    if extension == ksp:
        return applicationxkspread

    if extension in (kra, krz):
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
        return applicationvndgoogleearthkml_xml

    if extension == kil:
        return applicationxkillustrator

    # iana
    if extension == kia:
        return applicationvndkidspiration

    if extension == kfo:
        return applicationxkformula

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

    if extension in (jxr, hdp, wdp):
        return imagejxr

    if extension == jxl:
        return imagejxl

    # iana
    if extension == jt:
        return modeljt

    if extension == jsx:
        return textjsx

    if extension == jsonpatch:
        return applicationjsonpatch_json

    # apache
    if extension == jsonml:
        return applicationjsonml_json

    if extension == jsonld:
        return applicationld_json

    if extension == json5:
        return applicationjson5

    if extension in (json, map):
        return applicationjson

    if extension == jse:
        return textjscriptencode

    if extension in (js, jsm, mjs):
        return textjavascript

    if extension == jrd:
        return applicationjrd_json

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

    if extension in (jpg, jpeg, jpe, jfif):
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

    if extension == jl:
        return textjulia

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

    if extension in (jar, war, ear):
        return applicationjavaarchive

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

    if extension == its:
        return applicationits_xml

    # iana
    if extension == itp:
        return applicationvndshanainformedformtemplate

    if extension == it87:
        return applicationxit87

    if extension == it:
        return audioxit

    if extension in (iso, iso9660):
        return applicationvndefiiso

    # iana
    if extension == irp:
        return applicationvndirepositorypackage_xml

    # iana
    if extension == irm:
        return applicationvndibmrightsmanagement

    if extension == ipynb:
        return applicationxipynb_json

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
        return applicationinkml_xml

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

    if extension == htc:
        return textxcomponent

    # iana
    if extension == hsj2:
        return imagehsj2

    if extension == hs:
        return textxhaskell

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
        return textxc__hdr

    if extension == hfe:
        return applicationxhfefloppyimage

    # iana
    if extension == held:
        return applicationatscheld_xml

    # iana
    if extension == hej2:
        return imagehej2k

    # iana
    if extension == heifs:
        return imageheifsequence

    # iana
    if extension == heics:
        return imageheicsequence

    if extension in (heic, heif, hif):
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
        return applicationvndhal_xml

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

    if extension == gx:
        return textxgcodegx

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
        return applicationsrgs_xml

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
        return applicationgpx_xml

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
        return applicationgml_xml

    if extension == gltf:
        return modelgltf_json

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
        return applicationgeo_json

    # iana
    if extension == geo:
        return applicationvnddynageo

    if extension in (gen, sgd):
        return applicationxgenesisrom

    if extension in (ged, gedcom):
        return textvndfamilysearchgedcom

    if extension == gdshader:
        return applicationxgodotshader

    if extension == gdoc:
        return applicationvndgoogleappsdocument

    # iana
    if extension == gdl:
        return modelvndgdl

    if extension == gdi:
        return applicationxgdromcue

    if extension == gd:
        return applicationxgdscript

    if extension == gcode:
        return textxgcode

    # apache
    if extension == gca:
        return applicationxgcacompressed

    if extension == gbrjob:
        return applicationxgerberjob

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
        return imageg3fax

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

    # apache
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

    if extension in (fits, fit, fts):
        return applicationfits

    if extension == fish:
        return applicationxfishscript

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
    if extension == fe_launch:
        return applicationvnddenovofcselayoutlink

    # iana
    if extension == fdt:
        return applicationfdt_xml

    if extension == fds:
        return applicationxfdsdisk

    # iana
    if extension == fdf:
        return applicationfdf

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
        return applicationxfictionbook_xml

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
    if extension == exp:
        return applicationexpress

    # iana
    if extension == exi:
        return applicationexi

    if extension in (exe, dll, cpl, drv, scr, com):
        return applicationxmsdownload

    if extension in (ex, exs):
        return textxelixir

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
        return applicationvndeszigno3_xml

    if extension in (es, ecma):
        return applicationecmascript

    if extension == erl:
        return textxerlang

    if extension == eris:
        return applicationxerislink_cbor

    if extension == epub:
        return applicationepub_zip

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
        return applicationvndemusicemusic_package

    # iana
    if extension == emotionml:
        return applicationemotionml_xml

    # iana
    if extension == emma:
        return applicationemma_xml

    if extension in (eml, mime):
        return messagerfc822

    if extension == emf:
        return imageemf

    if extension == el:
        return textxemacslisp

    # iana
    if extension == ei6:
        return applicationvndpgosasli

    if extension in (ehthumbsdb, ehthumbsvistadb, imagedb, musicthumbsdb, thumbsdb, tvthumbdb, videodb):
        return applicationvndmicrosoftwindowsthumbnailcache

    if extension == egon:
        return applicationxegon

    # iana
    if extension == efif:
        return applicationvndpicsel

    if extension in (efi, ocx, sys, lib):
        return applicationvndmicrosoftportableexecutable

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
        return applicationatscdwd_xml

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

    if extension == dtsi:
        return textxdevicetreesource

    if extension == dtshd:
        return audiovnddtshd

    if extension == dts:
        return audiovnddts

    if extension == dtd:
        return applicationxmldtd

    if extension == dtb:
        return textxdevicetreebinary

    # iana
    if extension == dssc:
        return applicationdssc_der

    if extension == dsl:
        return textxdsl

    if extension == dsf:
        return audioxdsf

    # iana
    if extension == dsc:
        return textprslinestag

    # iana
    if extension == drle:
        return imagedicomrle

    if extension == drl:
        return applicationxexcellon

    # iana
    if extension == dra:
        return audiovnddra

    # iana
    if extension == dpx:
        return imagedpx

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

    if extension == dff:
        return audioxdff

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
        return applicationvndsyncmldmddf_xml

    # iana
    if extension == ddd:
        return applicationvndfujixeroxddd

    # iana
    if extension == dd2:
        return applicationvndomadd2_xml

    # apache
    if extension == dcurl:
        return textvndcurldcurl

    if extension == dcr:
        return imagexkodakdcr

    if extension == dcl:
        return textxdcl

    if extension in (dbk, docbook):
        return applicationxdocbook_xml

    if extension == dbf:
        return applicationvnddbf

    # iana
    if extension == davmount:
        return applicationdavmount_xml

    if extension == dart:
        return applicationvnddart

    if extension == dar:
        return applicationxdar

    # iana
    if extension == daf:
        return applicationvndmobiusdaf

    # iana
    if extension == dae:
        return modelvndcollada_xml

    if extension in (d, di):
        return textxdsrc

    # iana
    if extension == cww:
        return applicationprscww

    # iana
    if extension == cwl:
        return applicationcwl

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

    if extension == cso:
        return applicationxcompressediso

    # apache
    if extension == csml:
        return chemicalxcsml

    # iana
    if extension == csl:
        return applicationvndcitationstylesstyle_xml

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

    if extension == cr3:
        return imagexcanoncr3

    if extension == cr2:
        return imagexcanoncr2

    if extension == cr:
        return textxcrystal

    # apache
    if extension == cpt:
        return applicationmaccompactpro

    if extension in (cpp, cxx, cc, c):
        return textxc__src

    if extension == cpiogz:
        return applicationxcpiocompressed

    if extension == cpio:
        return applicationxcpio

    if extension == core:
        return applicationxcore

    if extension == copying:
        return textxcopying

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

    # iana
    if extension == cld:
        return modelvndcld

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

    if extension == chd:
        return applicationxmamechd

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
        return applicationvndchemdraw_xml

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

    if extension == cdi:
        return applicationxdiscjugglercdimage

    # iana
    if extension == cdfx:
        return applicationcdfx_xml

    if extension in (cdf, nc):
        return applicationxnetcdf

    # iana
    if extension == cdbcmsg:
        return applicationvndcontactcmsg

    # iana
    if extension == ccxml:
        return applicationccxml_xml

    # nginx
    if extension == cco:
        return applicationxcocoa

    if extension == ccmx:
        return applicationxccmx

    if extension == cbz:
        return applicationvndcomicbook_zip

    if extension == cbt:
        return applicationxcbt

    if extension == cbr:
        return applicationvndcomicbookrar

    if extension == cbor:
        return applicationcbor

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

    if extension == bz3:
        return applicationxbzip3

    if extension in (bz2, boz):
        return applicationxbzip2

    if extension == bz:
        return applicationxbzip1

    # iana
    if extension in (btif, btf):
        return imageprsbtif

    # iana
    if extension == bsp:
        return modelvndvalvesourcecompiledmap

    if extension == bsdiff:
        return applicationxbsdiff

    if extension == brk:
        return chemicalxpdb

    if extension == bps:
        return applicationxbpspatch

    # iana
    if extension == box:
        return applicationvndpreviewsystemsbox

    if extension in (bmp, dib):
        return imagebmp

    # iana
    if extension == bmml:
        return applicationvndbalsamiqbmml_xml

    # iana
    if extension == bmi:
        return applicationvndbmi

    if extension == blp:
        return textxblueprint

    if extension in (blend, blender):
        return applicationxblender

    # apache
    if extension in (blb, blorb):
        return applicationxblorb

    # iana
    if extension in (bin, dms, lrf, mar, dist, distz, bpk, dump, elc, deploy, msp, msm, buffer):
        return applicationoctetstream

    if extension in (bik, bk2):
        return videovndradgamettoolsbink

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

    if extension == bat:
        return applicationxbat

    if extension == bas:
        return textxbasic

    if extension in (bak, old, sik):
        return applicationxtrash

    # iana
    if extension == b16:
        return imagevndpcob16

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

    if extension in (avif, avifs):
        return imageavif

    if extension in (avi, avf, divx):
        return videovndavi

    # iana
    if extension == avcs:
        return imageavcs

    # iana
    if extension == avci:
        return imageavci

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
        return applicationatomsvc_xml

    # iana
    if extension == atomdeleted:
        return applicationatomdeleted_xml

    # iana
    if extension == atomcat:
        return applicationatomcat_xml

    if extension == atom:
        return applicationatom_xml

    # iana
    if extension in (atc, acutc):
        return applicationvndacucorp

    if extension in (asx, wax, wvx, wmx):
        return audioxmsasx

    if extension == astc:
        return imageastc

    if extension == asp:
        return applicationxasp

    # iana
    if extension == aso:
        return applicationvndaccpacsimplyaso

    if extension == asf:
        return applicationvndmsasf

    if extension in (asd, fasl, lisp, ros):
        return textxcommonlisp

    if extension == asar:
        return applicationxasar

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

    if extension == appxbundle:
        return applicationappxbundle

    if extension == appx:
        return applicationappx

    # apache
    if extension == application:
        return applicationxmsapplication

    if extension == appinstaller:
        return applicationappinstaller

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
    if extension == amlx:
        return applicationautomationmlamlx_zip

    # iana
    if extension == aml:
        return applicationautomationmlaml_xml

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
        return applicationvndadobeairapplicationinstallerpackage_zip

    if extension in (aiff, aif):
        return audioxaiff

    if extension in (aifc, aiffc):
        return audioxaifc

    if extension == ai:
        return applicationillustrator

    # iana
    if extension == ahead:
        return applicationvndaheadspace

    # iana
    if extension == age:
        return applicationvndage

    if extension == ag:
        return imagexapplixgraphics

    # apache
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

    if extension == aaxc:
        return audiovndaudibleaaxc

    if extension == aax:
        return audiovndaudibleaax

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

    if extension == aa:
        return audioxpnaudibleaudio

    if extension == a78:
        return applicationxatari7800rom

    if extension == a26:
        return applicationxatari2600rom

    if extension in (a, ar):
        return applicationxarchive

    if extension in (_7z, _7z001):
        return applicationx7zcompressed

    if extension == _602:
        return applicationxt602

    if extension == _3mf:
        return model3mf

    if extension in (_3gp, _3gpp, _3ga):
        return video3gpp

    if extension in (_3g2, _3gp2, _3gpp2):
        return video3gpp2

    if extension == _3dsx:
        return applicationxnintendo3dsexecutable

    if extension in (_3ds, cci):
        return applicationxnintendo3dsrom

    # iana
    if extension == _3dml:
        return textvndin3d3dml

    if extension in (_32x, mdx):
        return applicationxgenesis32xrom

    # iana
    if extension == _1km:
        return applicationvnd1000mindsdecisionmodel_xml

    if extension in (_123, wk1, wk3, wk4, wks):
        return applicationvndlotus123

def getMimeTypeFileExtensions(mimeType):
    """
    Returns a list of possible file extensions for the given mime type
    :param str mimeType A mime Type
    """
    #getMimeTypeFileExtensions body

    if mimeType == applicationzlib:
        return [ "zz" ]

    if mimeType == applicationzstd:
        return [ "zst" ]

    if mimeType == applicationxzpaq:
        return [ "zpaq" ]

    if mimeType == applicationxzoo:
        return [ "zoo" ]

    if mimeType == applicationvndhandheldentertainment_xml:
        return [ "zmm" ]

    if mimeType == applicationvndzul:
        return [ "zir", "zirz" ]

    if mimeType == applicationzip:
        return [ "zip", "zipx" ]

    if mimeType == applicationxopenzim:
        return [ "zim" ]

    if mimeType == applicationvndzzazzdeck_xml:
        return [ "zaz" ]

    if mimeType == applicationxzmachine:
        return [ "z1", "z2", "z3", "z4", "z5", "z6", "z7", "z8" ]

    if mimeType == applicationxcompress:
        return [ "z" ]

    if mimeType == videovndyoutubeyt:
        return [ "yt" ]

    if mimeType == textxsuseymp:
        return [ "ymp" ]

    if mimeType == applicationyin_xml:
        return [ "yin" ]

    if mimeType == applicationyang:
        return [ "yang" ]

    if mimeType == applicationyaml:
        return [ "yaml", "yml" ]

    if mimeType == applicationxxz:
        return [ "xz" ]

    if mimeType == chemicalxxyz:
        return [ "xyz" ]

    if mimeType == imagexxwindowdump:
        return [ "xwd" ]

    if mimeType == applicationvndmozillaxul_xml:
        return [ "xul" ]

    if mimeType == applicationxspf_xml:
        return [ "xspf" ]

    if mimeType == applicationvndsyncml_xml:
        return [ "xsm" ]

    if mimeType == applicationxslt_xml:
        return [ "xsl", "xslt" ]

    if mimeType == applicationprsxsf_xml:
        return [ "xsf" ]

    if mimeType == applicationvndinterconformnet:
        return [ "xpw", "xpx" ]

    if mimeType == applicationvndmsxpsdocument:
        return [ "xps" ]

    if mimeType == applicationvndisxpr:
        return [ "xpr" ]

    if mimeType == imagexxpixmap:
        return [ "xpm" ]

    if mimeType == applicationxproc_xml:
        return [ "xpl" ]

    if mimeType == applicationxxpinstall:
        return [ "xpi" ]

    if mimeType == applicationxop_xml:
        return [ "xop" ]

    if mimeType == applicationvndolpcsugar:
        return [ "xo" ]

    if mimeType == applicationxcapns_xml:
        return [ "xns" ]

    if mimeType == applicationxml:
        return [ "xml", "xbl", "xsd", "rng" ]

    if mimeType == textxxmi:
        return [ "xmi" ]

    if mimeType == audioxxmf:
        return [ "xmf" ]

    if mimeType == audioxxm:
        return [ "xm" ]

    if mimeType == applicationvndopenxmlformatsofficedocumentspreadsheetmltemplate:
        return [ "xltx" ]

    if mimeType == applicationvndmsexceltemplatemacroenabled12:
        return [ "xltm" ]

    if mimeType == applicationvndopenxmlformatsofficedocumentspreadsheetmlsheet:
        return [ "xlsx" ]

    if mimeType == applicationvndmsexcelsheetmacroenabled12:
        return [ "xlsm" ]

    if mimeType == applicationvndmsexcelsheetbinarymacroenabled12:
        return [ "xlsb" ]

    if mimeType == applicationvndmsexcel:
        return [ "xls", "xlc", "xll", "xlm", "xlw", "xla", "xlt", "xld" ]

    if mimeType == applicationxliff_xml:
        return [ "xlf", "xliff" ]

    if mimeType == applicationvndmsexceladdinmacroenabled12:
        return [ "xlam" ]

    if mimeType == imagevndxiff:
        return [ "xif" ]

    if mimeType == audioxxi:
        return [ "xi" ]

    if mimeType == applicationxhtml_xml:
        return [ "xhtml", "xht", "html", "htm" ]

    if mimeType == applicationvndpwgxhtmlprint_xml:
        return [ "xhtm" ]

    if mimeType == applicationvndxfdl:
        return [ "xfdl" ]

    if mimeType == applicationvndadobexfdf:
        return [ "xfdf" ]

    if mimeType == applicationpatchopserror_xml:
        return [ "xer" ]

    if mimeType == applicationxenc_xml:
        return [ "xenc" ]

    if mimeType == applicationxcapel_xml:
        return [ "xel" ]

    if mimeType == applicationvndfujixeroxdocuworks:
        return [ "xdw" ]

    if mimeType == applicationdssc_xml:
        return [ "xdssc" ]

    if mimeType == applicationvndadobexdp_xml:
        return [ "xdp" ]

    if mimeType == applicationvndsyncmldm_xml:
        return [ "xdm" ]

    if mimeType == applicationxcapdiff_xml:
        return [ "xdf" ]

    if mimeType == applicationcalendar_xml:
        return [ "xcs" ]

    if mimeType == imagexcompressedxcf:
        return [ "xcfgz", "xcfbz2" ]

    if mimeType == imagexxcf:
        return [ "xcf" ]

    if mimeType == applicationxcapcaps_xml:
        return [ "xca" ]

    if mimeType == imagexxbitmap:
        return [ "xbm" ]

    if mimeType == applicationxxbel:
        return [ "xbel" ]

    if mimeType == applicationvndfujixeroxdocuworksbinder:
        return [ "xbd" ]

    if mimeType == applicationxmsxbap:
        return [ "xbap" ]

    if mimeType == applicationxcapatt_xml:
        return [ "xav" ]

    if mimeType == applicationxxar:
        return [ "xar", "pkg" ]

    if mimeType == applicationxsilverlightapp:
        return [ "xap" ]

    if mimeType == applicationxaml_xml:
        return [ "xaml" ]

    if mimeType == imagexsigmax3f:
        return [ "x3f" ]

    if mimeType == modelx3d_vrml:
        return [ "x3dv", "x3dvz" ]

    if mimeType == modelx3d_binary:
        return [ "x3db", "x3dbz" ]

    if mimeType == modelx3d_xml:
        return [ "x3d", "x3dz" ]

    if mimeType == modelvndparasolidtransmittext:
        return [ "x_t" ]

    if mimeType == modelvndparasolidtransmitbinary:
        return [ "x_b" ]

    if mimeType == applicationxwwf:
        return [ "wwf" ]

    if mimeType == audioxwavpackcorrection:
        return [ "wvc" ]

    if mimeType == audioxwavpack:
        return [ "wv", "wvp" ]

    if mimeType == applicationvndwebturbo:
        return [ "wtb" ]

    if mimeType == applicationwspolicy_xml:
        return [ "wspolicy" ]

    if mimeType == applicationwsdl_xml:
        return [ "wsdl" ]

    if mimeType == applicationxwonderswancolorrom:
        return [ "wsc" ]

    if mimeType == applicationxwonderswanrom:
        return [ "ws" ]

    if mimeType == applicationxmswrite:
        return [ "wri" ]

    if mimeType == applicationvndwqd:
        return [ "wqd" ]

    if mimeType == applicationvndmswpl:
        return [ "wpl" ]

    if mimeType == applicationxwpg:
        return [ "wpg" ]

    if mimeType == applicationvndwordperfect:
        return [ "wp", "wp4", "wp5", "wp6", "wpd", "wpp" ]

    if mimeType == fontwoff2:
        return [ "woff2" ]

    if mimeType == fontwoff:
        return [ "woff" ]

    if mimeType == applicationxmswmz:
        return [ "wmz" ]

    if mimeType == videoxmswmv:
        return [ "wmv" ]

    if mimeType == applicationvndwapwmlscriptc:
        return [ "wmlsc" ]

    if mimeType == textvndwapwmlscript:
        return [ "wmls" ]

    if mimeType == applicationvndwapwmlc:
        return [ "wmlc" ]

    if mimeType == textvndwapwml:
        return [ "wml" ]

    if mimeType == imagewmf:
        return [ "wmf" ]

    if mimeType == applicationxmswmd:
        return [ "wmd" ]

    if mimeType == audioxmswma:
        return [ "wma" ]

    if mimeType == videoxmswm:
        return [ "wm" ]

    if mimeType == applicationxpartialdownload:
        return [ "wkdownload", "crdownload", "part" ]

    if mimeType == applicationxmswim:
        return [ "wim", "swm" ]

    if mimeType == applicationwatcherinfo_xml:
        return [ "wif" ]

    if mimeType == applicationwidget:
        return [ "wgt" ]

    if mimeType == textwgsl:
        return [ "wgsl" ]

    if mimeType == applicationvndpmiwidget:
        return [ "wg" ]

    if mimeType == imagewebp:
        return [ "webp" ]

    if mimeType == applicationmanifest_json:
        return [ "webmanifest" ]

    if mimeType == videowebm:
        return [ "webm" ]

    if mimeType == applicationxwebappmanifest_json:
        return [ "webapp" ]

    if mimeType == audiowebm:
        return [ "weba" ]

    if mimeType == applicationvndmsworks:
        return [ "wcm", "wdb", "wps", "xlr" ]

    if mimeType == applicationvndwapwbxml:
        return [ "wbxml" ]

    if mimeType == applicationvndcriticaltoolswbs_xml:
        return [ "wbs" ]

    if mimeType == imagevndwapwbmp:
        return [ "wbmp" ]

    if mimeType == applicationxquattropro:
        return [ "wb1", "wb2", "wb3" ]

    if mimeType == audiovndwave:
        return [ "wav" ]

    if mimeType == applicationwasm:
        return [ "wasm" ]

    if mimeType == applicationvndsunwadl_xml:
        return [ "wadl" ]

    if mimeType == applicationxwiiwad:
        return [ "wad" ]

    if mimeType == applicationvoicexml_xml:
        return [ "vxml" ]

    if mimeType == modelvndvtu:
        return [ "vtu" ]

    if mimeType == textvtt:
        return [ "vtt" ]

    if mimeType == imagevndvalvesourcetexture:
        return [ "vtf" ]

    if mimeType == applicationvndmsvisiotemplatemain_xml:
        return [ "vstx" ]

    if mimeType == applicationvndmsvisiotemplatemacroenabledmain_xml:
        return [ "vstm" ]

    if mimeType == applicationvndmsvisiostencilmain_xml:
        return [ "vssx" ]

    if mimeType == applicationvndmsvisiostencilmacroenabledmain_xml:
        return [ "vssm" ]

    if mimeType == applicationvndvsf:
        return [ "vsf" ]

    if mimeType == applicationvndmsvisiodrawingmain_xml:
        return [ "vsdx" ]

    if mimeType == applicationvndmsvisiodrawingmacroenabledmain_xml:
        return [ "vsdm" ]

    if mimeType == applicationvndvisio:
        return [ "vsd", "vst", "vsw", "vss" ]

    if mimeType == modelvrml:
        return [ "vrm", "vrml", "wrl" ]

    if mimeType == applicationxvhddisk:
        return [ "vpc" ]

    if mimeType == audioxvoc:
        return [ "voc" ]

    if mimeType == applicationxvmdkdisk:
        return [ "vmdk" ]

    if mimeType == videovndvivo:
        return [ "viv", "vivo" ]

    if mimeType == applicationvndvisionary:
        return [ "vis" ]

    if mimeType == applicationxvhdxdisk:
        return [ "vhdx" ]

    if mimeType == textxvhdl:
        return [ "vhd", "vhdl" ]

    if mimeType == modelvndsapvds:
        return [ "vds" ]

    if mimeType == applicationxvdidisk:
        return [ "vdi" ]

    if mimeType == applicationvndvcx:
        return [ "vcx" ]

    if mimeType == textcalendar:
        return [ "vcs", "ics", "ifb" ]

    if mimeType == applicationvndgroovevcard:
        return [ "vcg" ]

    if mimeType == applicationxcdlink:
        return [ "vcd" ]

    if mimeType == textvcard:
        return [ "vcard", "vcf", "vct", "gcrd" ]

    if mimeType == textvbscript:
        return [ "vbs" ]

    if mimeType == applicationxvirtualboxvboxextpack:
        return [ "vbox-extpack" ]

    if mimeType == applicationxvirtualboxvbox:
        return [ "vbox" ]

    if mimeType == textvbscriptencode:
        return [ "vbe" ]

    if mimeType == applicationxvirtualboyrom:
        return [ "vb" ]

    if mimeType == textxvala:
        return [ "vala", "vapi" ]

    if mimeType == textxverilog:
        return [ "v" ]

    if mimeType == applicationvnddecezip:
        return [ "uvz", "uvvz" ]

    if mimeType == applicationvnddeceunspecified:
        return [ "uvx", "uvvx" ]

    if mimeType == videovnddecevideo:
        return [ "uvv", "uvvv" ]

    if mimeType == videovnduvvump4:
        return [ "uvu", "uvvu" ]

    if mimeType == applicationvnddecettml_xml:
        return [ "uvt", "uvvt" ]

    if mimeType == videovnddecesd:
        return [ "uvs", "uvvs" ]

    if mimeType == videovnddecepd:
        return [ "uvp", "uvvp" ]

    if mimeType == videovnddecemobile:
        return [ "uvm", "uvvm" ]

    if mimeType == imagevnddecegraphic:
        return [ "uvi", "uvvi", "uvg", "uvvg" ]

    if mimeType == videovnddecehd:
        return [ "uvh", "uvvh" ]

    if mimeType == applicationvnddecedata:
        return [ "uvf", "uvvf", "uvd", "uvvd" ]

    if mimeType == audiovnddeceaudio:
        return [ "uva", "uvva" ]

    if mimeType == textxuuencode:
        return [ "uue", "uu" ]

    if mimeType == applicationvnduiqtheme:
        return [ "utz" ]

    if mimeType == applicationxustar:
        return [ "ustar" ]

    if mimeType == modelvndusdz_zip:
        return [ "usdz" ]

    if mimeType == modelvndusda:
        return [ "usda" ]

    if mimeType == applicationxmswinurl:
        return [ "url" ]

    if mimeType == texturilist:
        return [ "uri", "uris", "urls" ]

    if mimeType == applicationvnduoml_xml:
        return [ "uoml", "uo" ]

    if mimeType == applicationvndunity:
        return [ "unityweb" ]

    if mimeType == applicationvndumajin:
        return [ "umj" ]

    if mimeType == applicationxglulx:
        return [ "ulx" ]

    if mimeType == audioxmod:
        return [ "ult", "uni", "m15", "mtm", "669", "med" ]

    if mimeType == textxuil:
        return [ "uil" ]

    if mimeType == applicationxdesigner:
        return [ "ui" ]

    if mimeType == applicationxufraw:
        return [ "ufraw" ]

    if mimeType == applicationvndufdl:
        return [ "ufd", "ufdl" ]

    if mimeType == applicationubjson:
        return [ "ubj" ]

    if mimeType == messageglobal:
        return [ "u8msg" ]

    if mimeType == messageglobaldispositionnotification:
        return [ "u8mdn" ]

    if mimeType == messageglobalheaders:
        return [ "u8hdr" ]

    if mimeType == messageglobaldeliverystatus:
        return [ "u8dsn" ]

    if mimeType == modelu3d:
        return [ "u3d" ]

    if mimeType == textxtypst:
        return [ "typ" ]

    if mimeType == textplain:
        return [ "txt", "text", "conf", "def", "list", "in", "ini" ]

    if mimeType == applicationvndmobiustxf:
        return [ "txf" ]

    if mimeType == applicationvndgenomatixtuxedo:
        return [ "txd" ]

    if mimeType == textxtwig:
        return [ "twig" ]

    if mimeType == applicationvndsimtechmindmapper:
        return [ "twd", "twds" ]

    if mimeType == applicationxfontttx:
        return [ "ttx" ]

    if mimeType == applicationttml_xml:
        return [ "ttml" ]

    if mimeType == textturtle:
        return [ "ttl" ]

    if mimeType == fontttf:
        return [ "ttf" ]

    if mimeType == fontcollection:
        return [ "ttc" ]

    if mimeType == audioxtta:
        return [ "tta" ]

    if mimeType == applicationxtiledtsx:
        return [ "tsx" ]

    if mimeType == texttabseparatedvalues:
        return [ "tsv" ]

    if mimeType == applicationtimestampeddata:
        return [ "tsd" ]

    if mimeType == textvndtrolltechlinguist:
        return [ "ts" ]

    if mimeType == applicationxmsterminal:
        return [ "trm" ]

    if mimeType == applicationtrig:
        return [ "trig" ]

    if mimeType == applicationvndtrueapp:
        return [ "tra" ]

    if mimeType == texttroff:
        return [ "tr", "roff" ]

    if mimeType == applicationvndtridtpt:
        return [ "tpt" ]

    if mimeType == applicationvndgroovetooltemplate:
        return [ "tpl" ]

    if mimeType == applicationxbittorrent:
        return [ "torrent" ]

    if mimeType == applicationtoml:
        return [ "toml" ]

    if mimeType == textxtodotxt:
        return [ "todotxt" ]

    if mimeType == applicationxcdrdaotoc:
        return [ "toc" ]

    if mimeType == applicationvndmstnef:
        return [ "tnef", "tnf", "winmaildat" ]

    if mimeType == applicationxtiledtmx:
        return [ "tmx" ]

    if mimeType == applicationvndtmobilelivetv:
        return [ "tmo" ]

    if mimeType == imagetiff:
        return [ "tif", "tiff" ]

    if mimeType == applicationvndmsofficetheme:
        return [ "thmx" ]

    if mimeType == applicationxwindowsthemepack:
        return [ "themepack" ]

    if mimeType == applicationxtheme:
        return [ "theme" ]

    if mimeType == imagextga:
        return [ "tga", "icb", "tpic", "vda" ]

    if mimeType == imagetifffx:
        return [ "tfx" ]

    if mimeType == applicationxtextfm:
        return [ "tfm" ]

    if mimeType == applicationthraud_xml:
        return [ "tfi" ]

    if mimeType == textxtexinfo:
        return [ "texi", "texinfo" ]

    if mimeType == textxtex:
        return [ "tex", "ltx", "sty", "cls", "dtx", "ins", "latex" ]

    if mimeType == applicationtei_xml:
        return [ "tei", "teicorpus" ]

    if mimeType == applicationvndsmartteacher:
        return [ "teacher" ]

    if mimeType == applicationurctargetdesc_xml:
        return [ "td" ]

    if mimeType == texttcl:
        return [ "tcl", "tk" ]

    if mimeType == applicationvnd3gpp2tcap:
        return [ "tcap" ]

    if mimeType == applicationxzstdcompressedtar:
        return [ "tarzst", "tzst" ]

    if mimeType == applicationxtarz:
        return [ "tarz", "taz" ]

    if mimeType == applicationxxzcompressedtar:
        return [ "tarxz", "txz" ]

    if mimeType == applicationxtzo:
        return [ "tarlzo", "tzo" ]

    if mimeType == applicationxlzmacompressedtar:
        return [ "tarlzma", "tlz" ]

    if mimeType == applicationxlz4compressedtar:
        return [ "tarlz4" ]

    if mimeType == applicationxlzipcompressedtar:
        return [ "tarlz" ]

    if mimeType == applicationxlrzipcompressedtar:
        return [ "tarlrz", "tlrz" ]

    if mimeType == applicationxcompressedtar:
        return [ "targz", "tgz" ]

    if mimeType == applicationxbzip3compressedtar:
        return [ "tarbz3", "tbz3" ]

    if mimeType == applicationxbzip2compressedtar:
        return [ "tarbz2", "tbz2", "tb2" ]

    if mimeType == applicationxbzip1compressedtar:
        return [ "tarbz", "tbz" ]

    if mimeType == applicationxtar:
        return [ "tar", "gtar", "gem" ]

    if mimeType == imagevndtencenttap:
        return [ "tap" ]

    if mimeType == applicationvndtaointentmodulearchive:
        return [ "tao" ]

    if mimeType == audioxtak:
        return [ "tak" ]

    if mimeType == applicationvndmynfc:
        return [ "taglet" ]

    if mimeType == imaget38:
        return [ "t38" ]

    if mimeType == applicationxt3vmimage:
        return [ "t3" ]

    if mimeType == textxtxt2tags:
        return [ "t2t" ]

    if mimeType == textspreadsheet:
        return [ "sylk", "slk" ]

    if mimeType == applicationvndsunxmlwriter:
        return [ "sxw" ]

    if mimeType == applicationvndsunxmlmath:
        return [ "sxm" ]

    if mimeType == applicationvndsunxmlimpress:
        return [ "sxi" ]

    if mimeType == applicationvndsunxmlwriterglobal:
        return [ "sxg" ]

    if mimeType == applicationvndsunxmldraw:
        return [ "sxd" ]

    if mimeType == applicationvndsunxmlcalc:
        return [ "sxc" ]

    if mimeType == applicationswid_xml:
        return [ "swidtag" ]

    if mimeType == applicationvndaristanetworksswi:
        return [ "swi" ]

    if mimeType == applicationvndadobeflashmovie:
        return [ "swf", "spl" ]

    if mimeType == textxsvhdr:
        return [ "svh" ]

    if mimeType == imagesvg_xmlcompressed:
        return [ "svgz", "svggz" ]

    if mimeType == imagesvg_xml:
        return [ "svg" ]

    if mimeType == applicationvndsvd:
        return [ "svd" ]

    if mimeType == applicationvnddvbservice:
        return [ "svc" ]

    if mimeType == applicationxsv4crc:
        return [ "sv4crc" ]

    if mimeType == applicationxsv4cpio:
        return [ "sv4cpio" ]

    if mimeType == textxsvsrc:
        return [ "sv" ]

    if mimeType == applicationvndsuscalendar:
        return [ "sus", "susp" ]

    if mimeType == imagexsunraster:
        return [ "sun" ]

    if mimeType == textxmicrodvd:
        return [ "sub" ]

    if mimeType == textstylus:
        return [ "stylus", "styl" ]

    if mimeType == applicationvndsunxmlwritertemplate:
        return [ "stw" ]

    if mimeType == applicationvndpgformat:
        return [ "str" ]

    if mimeType == modelstep_zip:
        return [ "stpz" ]

    if mimeType == modelstepxml_zip:
        return [ "stpxz" ]

    if mimeType == modelstep_xml:
        return [ "stpx" ]

    if mimeType == audioxstm:
        return [ "stm" ]

    if mimeType == modelstl:
        return [ "stl" ]

    if mimeType == applicationhyperstudio:
        return [ "stk" ]

    if mimeType == applicationvndsunxmlimpresstemplate:
        return [ "sti" ]

    if mimeType == applicationvndwtstf:
        return [ "stf" ]

    if mimeType == applicationvndsunxmldrawtemplate:
        return [ "std" ]

    if mimeType == applicationvndsunxmlcalctemplate:
        return [ "stc" ]

    if mimeType == applicationvndsailingtrackertrack:
        return [ "st" ]

    if mimeType == applicationssml_xml:
        return [ "ssml" ]

    if mimeType == applicationvndepsonssf:
        return [ "ssf" ]

    if mimeType == applicationvndkodakdescriptor:
        return [ "sse" ]

    if mimeType == applicationssdl_xml:
        return [ "ssdl" ]

    if mimeType == textxssa:
        return [ "ssa", "ass" ]

    if mimeType == applicationsparqlresults_xml:
        return [ "srx" ]

    if mimeType == applicationsru_xml:
        return [ "sru" ]

    if mimeType == applicationxsubrip:
        return [ "srt" ]

    if mimeType == imagexsonysrf:
        return [ "srf" ]

    if mimeType == applicationxsourcerpm:
        return [ "srcrpm", "spm" ]

    if mimeType == applicationxwaissource:
        return [ "src" ]

    if mimeType == imagexsonysr2:
        return [ "sr2" ]

    if mimeType == applicationvndsquashfs:
        return [ "sqsh" ]

    if mimeType == applicationvndsqlite3:
        return [ "sqlite3" ]

    if mimeType == applicationxsqlite2:
        return [ "sqlite2" ]

    if mimeType == applicationsql:
        return [ "sql" ]

    if mimeType == applicationxapplesystemprofiler_xml:
        return [ "spx" ]

    if mimeType == applicationscvpvprequest:
        return [ "spq" ]

    if mimeType == applicationscvpvpresponse:
        return [ "spp" ]

    if mimeType == textvndin3dspot:
        return [ "spot" ]

    if mimeType == applicationvndyamahasmafphrase:
        return [ "spf" ]

    if mimeType == textxrpmspec:
        return [ "spec" ]

    if mimeType == textspdx:
        return [ "spdx" ]

    if mimeType == applicationxfontspeedo:
        return [ "spd" ]

    if mimeType == applicationxsharedlib:
        return [ "so", "so09" ]

    if mimeType == applicationxfontsnf:
        return [ "snf" ]

    if mimeType == applicationvndsnap:
        return [ "snap" ]

    if mimeType == applicationvndstepmaniapackage:
        return [ "smzip" ]

    if mimeType == videoxsmv:
        return [ "smv" ]

    if mimeType == applicationxsmsrom:
        return [ "sms" ]

    if mimeType == videovndradgamettoolssmacker:
        return [ "smk" ]

    if mimeType == applicationsmil_xml:
        return [ "smil", "smi", "sml", "kino" ]

    if mimeType == applicationvndstardivisionmath:
        return [ "smf" ]

    if mimeType == applicationvndstardivisionmail:
        return [ "smd" ]

    if mimeType == applicationvndstepmaniastepchart:
        return [ "sm" ]

    if mimeType == applicationvndepsonsalt:
        return [ "slt" ]

    if mimeType == applicationroutestsid_xml:
        return [ "sls" ]

    if mimeType == textslim:
        return [ "slim", "slm" ]

    if mimeType == applicationvndopenxmlformatsofficedocumentpresentationmlslide:
        return [ "sldx" ]

    if mimeType == applicationvndmspowerpointslidemacroenabled12:
        return [ "sldm" ]

    if mimeType == applicationpgpkeys:
        return [ "skr", "pkr", "key" ]

    if mimeType == applicationvndkoan:
        return [ "skp", "skd", "skt", "skm" ]

    if mimeType == imagexskencil:
        return [ "sk", "sk1" ]

    if mimeType == applicationsieve:
        return [ "siv", "sieve" ]

    if mimeType == applicationxstuffitx:
        return [ "sitx" ]

    if mimeType == applicationxstuffit:
        return [ "sit" ]

    if mimeType == xepocxsisxapp:
        return [ "sisx" ]

    if mimeType == applicationvndsymbianinstall:
        return [ "sis" ]

    if mimeType == audiosilk:
        return [ "sil" ]

    if mimeType == applicationpgpsignature:
        return [ "sig" ]

    if mimeType == audioprssid:
        return [ "sid", "psid" ]

    if mimeType == applicationxsiag:
        return [ "siag" ]

    if mimeType == texthtml:
        return [ "shtml" ]

    if mimeType == applicationxshorten:
        return [ "shn" ]

    if mimeType == applicationshf_xml:
        return [ "shf" ]

    if mimeType == textshex:
        return [ "shex" ]

    if mimeType == applicationxshar:
        return [ "shar" ]

    if mimeType == applicationxdiashape:
        return [ "shape" ]

    if mimeType == applicationxshellscript:
        return [ "sh" ]

    if mimeType == textsgml:
        return [ "sgml", "sgm" ]

    if mimeType == imagexsgi:
        return [ "sgi" ]

    if mimeType == applicationxgosgf:
        return [ "sgf" ]

    if mimeType == applicationxsg1000rom:
        return [ "sg" ]

    if mimeType == textxsfv:
        return [ "sfv" ]

    if mimeType == applicationvndspotfiresfs:
        return [ "sfs" ]

    if mimeType == applicationvndhydrostatixsofdata:
        return [ "sfd-hdstx" ]

    if mimeType == applicationvndnintendosnesrom:
        return [ "sfc", "smc" ]

    if mimeType == applicationsetregistrationinitiation:
        return [ "setreg" ]

    if mimeType == applicationsetpaymentinitiation:
        return [ "setpay" ]

    if mimeType == textxdbusservice:
        return [ "service" ]

    if mimeType == applicationjavaserializedobject:
        return [ "ser" ]

    if mimeType == applicationsensml_xml:
        return [ "sensmlx" ]

    if mimeType == applicationsenml_xml:
        return [ "senmlx" ]

    if mimeType == applicationvndsemf:
        return [ "semf" ]

    if mimeType == applicationvndsemd:
        return [ "semd" ]

    if mimeType == applicationvndsema:
        return [ "sema" ]

    if mimeType == applicationvndfdsnseed:
        return [ "seed", "dataless" ]

    if mimeType == applicationvndseemail:
        return [ "see" ]

    if mimeType == applicationxsea:
        return [ "sea" ]

    if mimeType == applicationvndstardivisionwriter:
        return [ "sdw", "vor", "sgl" ]

    if mimeType == applicationvndstardivisionchart:
        return [ "sds" ]

    if mimeType == applicationvndsolentsdkm_xml:
        return [ "sdkm", "sdkd" ]

    if mimeType == applicationvndstardivisionimpress:
        return [ "sdd", "sdp" ]

    if mimeType == applicationvndstardivisioncalc:
        return [ "sdc" ]

    if mimeType == applicationvndstardivisiondraw:
        return [ "sda" ]

    if mimeType == textvndcurlscurl:
        return [ "scurl" ]

    if mimeType == textxscss:
        return [ "scss" ]

    if mimeType == applicationscvpcvresponse:
        return [ "scs" ]

    if mimeType == applicationscvpcvrequest:
        return [ "scq" ]

    if mimeType == textxscons:
        return [ "sconstruct", "sconscript" ]

    if mimeType == applicationxgodotscene:
        return [ "scn", "tscn", "escn" ]

    if mimeType == textxscheme:
        return [ "scm", "ss" ]

    if mimeType == applicationxmsschedule:
        return [ "scd" ]

    if mimeType == textxscala:
        return [ "scala", "sc" ]

    if mimeType == applicationsbml_xml:
        return [ "sbml" ]

    if mimeType == applicationxspsssav:
        return [ "sav", "zsav" ]

    if mimeType == textxsass:
        return [ "sass" ]

    if mimeType == applicationxthomsonsapimage:
        return [ "sap" ]

    if mimeType == applicationxsami:
        return [ "sami" ]

    if mimeType == applicationxamipro:
        return [ "sam" ]

    if mimeType == textxsagemath:
        return [ "sage" ]

    if mimeType == applicationvndyamahasmafaudio:
        return [ "saf" ]

    if mimeType == audioxs3m:
        return [ "s3m" ]

    if mimeType == textxasm:
        return [ "s", "asm" ]

    if mimeType == imagexpanasonicrw2:
        return [ "rw2" ]

    if mimeType == videovndrnrealvideo:
        return [ "rv", "rvx" ]

    if mimeType == applicationrouteusd_xml:
        return [ "rusd" ]

    if mimeType == applicationxmakeself:
        return [ "run" ]

    if mimeType == textrichtext:
        return [ "rtx" ]

    if mimeType == applicationrtf:
        return [ "rtf" ]

    if mimeType == textvndrnrealtext:
        return [ "rt" ]

    if mimeType == textxrst:
        return [ "rst" ]

    if mimeType == applicationrss_xml:
        return [ "rss" ]

    if mimeType == applicationurcressheet_xml:
        return [ "rsheet" ]

    if mimeType == applicationrsd_xml:
        return [ "rsd" ]

    if mimeType == applicationatscrsat_xml:
        return [ "rsat" ]

    if mimeType == textrust:
        return [ "rs" ]

    if mimeType == applicationvndnokiaradiopreset:
        return [ "rpst" ]

    if mimeType == applicationvndnokiaradiopresets:
        return [ "rpss" ]

    if mimeType == applicationxrpm:
        return [ "rpm" ]

    if mimeType == applicationvndcloantorp9:
        return [ "rp9" ]

    if mimeType == imagevndrnrealpix:
        return [ "rp" ]

    if mimeType == applicationrpkiroa:
        return [ "roa" ]

    if mimeType == applicationrelaxngcompactsyntax:
        return [ "rnc" ]

    if mimeType == audioxpnrealaudioplugin:
        return [ "rmp" ]

    if mimeType == messagexgnurmail:
        return [ "rmail" ]

    if mimeType == applicationvndrnrealmedia:
        return [ "rm", "rmj", "rmm", "rms", "rmx", "rmvb" ]

    if mimeType == imagerle:
        return [ "rle" ]

    if mimeType == applicationresourcelistsdiff_xml:
        return [ "rld" ]

    if mimeType == imagevndfujixeroxedmicsrlc:
        return [ "rlc" ]

    if mimeType == applicationresourcelists_xml:
        return [ "rl" ]

    if mimeType == applicationxresearchinfosystems:
        return [ "ris" ]

    if mimeType == audiovndrip:
        return [ "rip" ]

    if mimeType == applicationreginfo_xml:
        return [ "rif" ]

    if mimeType == imagexrgb:
        return [ "rgb" ]

    if mimeType == applicationxgodotresource:
        return [ "res", "tres" ]

    if mimeType == applicationvndbusinessobjects:
        return [ "rep" ]

    if mimeType == applicationp2poverlay_xml:
        return [ "relo" ]

    if mimeType == textxreject:
        return [ "rej" ]

    if mimeType == textxmsregedit:
        return [ "reg" ]

    if mimeType == textxreadme:
        return [ "readme" ]

    if mimeType == applicationvnddatavisionrdz:
        return [ "rdz" ]

    if mimeType == applicationrdf_xml:
        return [ "rdf", "rdfs", "owl" ]

    if mimeType == applicationvndipunpluggedrcprofile:
        return [ "rcprofile" ]

    if mimeType == applicationxruby:
        return [ "rb" ]

    if mimeType == applicationxrawdiskimagexzcompressed:
        return [ "rawdiskimagexz", "imgxz" ]

    if mimeType == applicationvndefiimg:
        return [ "rawdiskimage", "img" ]

    if mimeType == imagexpanasonicrw:
        return [ "raw" ]

    if mimeType == imagexcmuraster:
        return [ "ras" ]

    if mimeType == applicationvndrar:
        return [ "rar" ]

    if mimeType == applicationrouteapd_xml:
        return [ "rapd" ]

    if mimeType == applicationraml_yaml:
        return [ "raml" ]

    if mimeType == applicationram:
        return [ "ram" ]

    if mimeType == imagexfujiraf:
        return [ "raf" ]

    if mimeType == audiovndrnrealaudio:
        return [ "ra", "rax" ]

    if mimeType == applicationvndquarkquarkxpress:
        return [ "qxd", "qxt", "qwd", "qwt", "qxl", "qxb" ]

    if mimeType == applicationxquicktimemedialink:
        return [ "qtl" ]

    if mimeType == imagexquicktime:
        return [ "qtif" ]

    if mimeType == applicationxqtiplot:
        return [ "qti", "qtigz" ]

    if mimeType == videoquicktime:
        return [ "qt", "mov", "moov", "qtvr" ]

    if mimeType == applicationsparqlquery:
        return [ "qs", "rq" ]

    if mimeType == applicationvndpublisharedeltatree:
        return [ "qps" ]

    if mimeType == applicationxqpress:
        return [ "qp" ]

    if mimeType == imageqoi:
        return [ "qoi" ]

    if mimeType == textxqml:
        return [ "qml", "qmltypes", "qmlproject" ]

    if mimeType == applicationxqw:
        return [ "qif" ]

    if mimeType == applicationvndintuqfx:
        return [ "qfx" ]

    if mimeType == applicationxqeddisk:
        return [ "qed" ]

    if mimeType == applicationxqemudisk:
        return [ "qcow2", "qcow" ]

    if mimeType == applicationvndintuqbo:
        return [ "qbo" ]

    if mimeType == applicationvndepsonquickanime:
        return [ "qam" ]

    if mimeType == textxpython:
        return [ "pyx", "wsgi" ]

    if mimeType == videovndmsplayreadymediapyv:
        return [ "pyv" ]

    if mimeType == applicationxpyspreadspreadsheet:
        return [ "pysu" ]

    if mimeType == applicationxpyspreadbzspreadsheet:
        return [ "pys" ]

    if mimeType == modelvndpythapyox:
        return [ "pyox" ]

    if mimeType == applicationxpythonbytecode:
        return [ "pyc", "pyo" ]

    if mimeType == audiovndmsplayreadymediapya:
        return [ "pya" ]

    if mimeType == textxpython3:
        return [ "py", "py3", "py3x", "pyi" ]

    if mimeType == applicationvnd3mpostitnotes:
        return [ "pwn" ]

    if mimeType == applicationxpw:
        return [ "pw" ]

    if mimeType == applicationvnd3gpppicbwvar:
        return [ "pvb" ]

    if mimeType == applicationvndmspublisher:
        return [ "pub" ]

    if mimeType == applicationvndpviptid1:
        return [ "ptid" ]

    if mimeType == imageprspti:
        return [ "pti" ]

    if mimeType == applicationxpocketword:
        return [ "psw" ]

    if mimeType == applicationpskc_xml:
        return [ "pskcxml" ]

    if mimeType == applicationxgzpostscript:
        return [ "psgz" ]

    if mimeType == audioxpsflib:
        return [ "psflib" ]

    if mimeType == applicationxgzfontlinuxpsf:
        return [ "psfgz" ]

    if mimeType == applicationxfontlinuxpsf:
        return [ "psf" ]

    if mimeType == imagevndadobephotoshop:
        return [ "psd" ]

    if mimeType == applicationxbzpostscript:
        return [ "psbz2" ]

    if mimeType == applicationvnd3gpppicbwsmall:
        return [ "psb" ]

    if mimeType == applicationxpowershell:
        return [ "ps1" ]

    if mimeType == applicationpostscript:
        return [ "ps" ]

    if mimeType == applicationprovenance_xml:
        return [ "provx" ]

    if mimeType == applicationxgodotproject:
        return [ "projectgodot" ]

    if mimeType == applicationpicsrules:
        return [ "prf" ]

    if mimeType == applicationvndlotusfreelance:
        return [ "pre" ]

    if mimeType == applicationvndpalm:
        return [ "pqa", "oprc" ]

    if mimeType == applicationvndmspowerpoint:
        return [ "ppz", "ppt", "pps", "pot" ]

    if mimeType == applicationvndopenxmlformatsofficedocumentpresentationmlpresentation:
        return [ "pptx" ]

    if mimeType == applicationvndmspowerpointpresentationmacroenabled12:
        return [ "pptm" ]

    if mimeType == applicationvndopenxmlformatsofficedocumentpresentationmlslideshow:
        return [ "ppsx" ]

    if mimeType == applicationvndmspowerpointslideshowmacroenabled12:
        return [ "ppsm" ]

    if mimeType == imagexportablepixmap:
        return [ "ppm" ]

    if mimeType == applicationvndcupsppd:
        return [ "ppd" ]

    if mimeType == applicationvndmspowerpointaddinmacroenabled12:
        return [ "ppam" ]

    if mimeType == applicationvndopenxmlformatsofficedocumentpresentationmltemplate:
        return [ "potx" ]

    if mimeType == applicationvndmspowerpointtemplatemacroenabled12:
        return [ "potm" ]

    if mimeType == applicationvndmacportsportpkg:
        return [ "portpkg" ]

    if mimeType == applicationxspsspor:
        return [ "por" ]

    if mimeType == textxmaven_xml:
        return [ "pomxml", "settingsxml" ]

    if mimeType == textxgettexttranslation:
        return [ "po" ]

    if mimeType == imagexmacpaint:
        return [ "pntg" ]

    if mimeType == imagexportableanymap:
        return [ "pnm" ]

    if mimeType == imagepng:
        return [ "png" ]

    if mimeType == applicationvndctcposml:
        return [ "pml" ]

    if mimeType == audioxscpls:
        return [ "pls" ]

    if mimeType == applicationxplanperfect:
        return [ "pln" ]

    if mimeType == applicationvndpocketlearn:
        return [ "plf" ]

    if mimeType == applicationvndmobiusplc:
        return [ "plc" ]

    if mimeType == applicationvnd3gpppicbwlarge:
        return [ "plb" ]

    if mimeType == audioxiriverpla:
        return [ "pla" ]

    if mimeType == applicationxperl:
        return [ "pl", "pm", "al", "perl", "pod", "t" ]

    if mimeType == applicationvndapplepkpass:
        return [ "pkpass" ]

    if mimeType == applicationpkixpkipath:
        return [ "pkipath" ]

    if mimeType == applicationpkixcmp:
        return [ "pki" ]

    if mimeType == applicationxtexpk:
        return [ "pk" ]

    if mimeType == applicationxphp:
        return [ "php", "php3", "php4", "php5", "phps" ]

    if mimeType == applicationpgpencrypted:
        return [ "pgp", "gpg", "asc" ]

    if mimeType == applicationvndchesspgn:
        return [ "pgn" ]

    if mimeType == imagexportablegraymap:
        return [ "pgm" ]

    if mimeType == applicationfonttdpfr:
        return [ "pfr" ]

    if mimeType == applicationxfonttype1:
        return [ "pfa", "pfb", "gsf", "pfm" ]

    if mimeType == applicationxperfdata:
        return [ "perfdata" ]

    if mimeType == imagexpentaxpef:
        return [ "pef" ]

    if mimeType == applicationxxzpdf:
        return [ "pdfxz" ]

    if mimeType == applicationxlzpdf:
        return [ "pdflz" ]

    if mimeType == applicationxgzpdf:
        return [ "pdfgz" ]

    if mimeType == applicationxbzpdf:
        return [ "pdfbz2" ]

    if mimeType == applicationpdf:
        return [ "pdf" ]

    if mimeType == textxprocessing:
        return [ "pde" ]

    if mimeType == applicationxaportisdoc:
        return [ "pdb", "pdc" ]

    if mimeType == imagevndzbrushpcx:
        return [ "pcx" ]

    if mimeType == applicationvndcurlpcurl:
        return [ "pcurl" ]

    if mimeType == imagexpict:
        return [ "pct", "pict", "pict1", "pict2", "pic" ]

    if mimeType == applicationvndhppclxl:
        return [ "pclxl" ]

    if mimeType == applicationvndhppcl:
        return [ "pcl" ]

    if mimeType == applicationxfontpcf:
        return [ "pcf", "pcfz", "pcfgz" ]

    if mimeType == applicationxpcenginerom:
        return [ "pce" ]

    if mimeType == imagexphotocd:
        return [ "pcd" ]

    if mimeType == applicationvndtcpdumppcap:
        return [ "pcap", "cap", "dmp" ]

    if mimeType == imagexportablebitmap:
        return [ "pbm" ]

    if mimeType == applicationvndpowerbuilder6:
        return [ "pbd" ]

    if mimeType == applicationvndpawaafile:
        return [ "paw" ]

    if mimeType == imagexgimppat:
        return [ "pat" ]

    if mimeType == applicationxpar2:
        return [ "par2" ]

    if mimeType == applicationxpak:
        return [ "pak" ]

    if mimeType == applicationvndapplepages:
        return [ "pages" ]

    if mimeType == applicationxjavapack200:
        return [ "pack" ]

    if mimeType == applicationxnsproxyautoconfig:
        return [ "pac" ]

    if mimeType == applicationpkcs8encrypted:
        return [ "p8e" ]

    if mimeType == applicationpkcs8:
        return [ "p8" ]

    if mimeType == applicationpkcs7signature:
        return [ "p7s" ]

    if mimeType == applicationxpkcs7certreqresp:
        return [ "p7r" ]

    if mimeType == applicationpkcs7mime:
        return [ "p7c", "p7m" ]

    if mimeType == applicationxpkcs7certificates:
        return [ "p7b", "spc" ]

    if mimeType == applicationxpagemaker:
        return [ "p65", "pm6", "pmd" ]

    if mimeType == applicationpkcs12:
        return [ "p12", "pfx" ]

    if mimeType == applicationpkcs10:
        return [ "p10" ]

    if mimeType == textxpascal:
        return [ "p", "pas" ]

    if mimeType == applicationvndopenofficeorgextension:
        return [ "oxt" ]

    if mimeType == applicationoxps:
        return [ "oxps" ]

    if mimeType == applicationowl_xml:
        return [ "owx" ]

    if mimeType == applicationxvirtualboxovf:
        return [ "ovf" ]

    if mimeType == applicationovf:
        return [ "ova" ]

    if mimeType == applicationvndoasisopendocumenttexttemplate:
        return [ "ott" ]

    if mimeType == applicationvndoasisopendocumentspreadsheettemplate:
        return [ "ots" ]

    if mimeType == applicationvndoasisopendocumentpresentationtemplate:
        return [ "otp" ]

    if mimeType == applicationvndoasisopendocumentimagetemplate:
        return [ "oti" ]

    if mimeType == applicationvndoasisopendocumenttextweb:
        return [ "oth" ]

    if mimeType == applicationvndoasisopendocumentgraphicstemplate:
        return [ "otg" ]

    if mimeType == applicationvndoasisopendocumentformulatemplate:
        return [ "otf", "odft" ]

    if mimeType == applicationvndoasisopendocumentcharttemplate:
        return [ "otc" ]

    if mimeType == applicationvndopenstreetmapdata_xml:
        return [ "osm" ]

    if mimeType == applicationvndyamahaopenscoreformatosfpvg_xml:
        return [ "osfpvg" ]

    if mimeType == applicationvndyamahaopenscoreformat:
        return [ "osf" ]

    if mimeType == textorg:
        return [ "org" ]

    if mimeType == imagexolympusorf:
        return [ "orf" ]

    if mimeType == imageopenraster:
        return [ "ora" ]

    if mimeType == textxopml_xml:
        return [ "opml" ]

    if mimeType == applicationoebpspackage_xml:
        return [ "opf" ]

    if mimeType == applicationxopenvpnprofile:
        return [ "openvpn", "ovpn" ]

    if mimeType == textxooc:
        return [ "ooc" ]

    if mimeType == applicationonenote:
        return [ "onetoc", "onetoc2", "onetmp", "onepkg" ]

    if mimeType == applicationomdoc_xml:
        return [ "omdoc" ]

    if mimeType == applicationxoleo:
        return [ "oleo" ]

    if mimeType == applicationogg:
        return [ "ogx" ]

    if mimeType == videoogg:
        return [ "ogv" ]

    if mimeType == videoxogm_ogg:
        return [ "ogm" ]

    if mimeType == modelvndopengex:
        return [ "ogex" ]

    if mimeType == audioogg:
        return [ "oga", "ogg", "opus" ]

    if mimeType == applicationvndoasisopendocumenttext:
        return [ "odt" ]

    if mimeType == applicationvndoasisopendocumentspreadsheet:
        return [ "ods" ]

    if mimeType == applicationvndoasisopendocumentpresentation:
        return [ "odp" ]

    if mimeType == applicationvndoasisopendocumenttextmaster:
        return [ "odm" ]

    if mimeType == applicationvndoasisopendocumentimage:
        return [ "odi" ]

    if mimeType == applicationvndoasisopendocumentgraphics:
        return [ "odg" ]

    if mimeType == applicationvndoasisopendocumentformula:
        return [ "odf" ]

    if mimeType == applicationvndoasisopendocumentchart:
        return [ "odc" ]

    if mimeType == applicationvndoasisopendocumentdatabase:
        return [ "odb" ]

    if mimeType == applicationoda:
        return [ "oda" ]

    if mimeType == textxocl:
        return [ "ocl" ]

    if mimeType == applicationxtgif:
        return [ "obj" ]

    if mimeType == applicationvndopenbloxgame_xml:
        return [ "obgx" ]

    if mimeType == applicationxmsbinder:
        return [ "obd" ]

    if mimeType == applicationvndfujitsuoasys:
        return [ "oas" ]

    if mimeType == applicationvndfujitsuoasys3:
        return [ "oa3" ]

    if mimeType == applicationvndfujitsuoasys2:
        return [ "oa2" ]

    if mimeType == applicationxobject:
        return [ "o", "mod" ]

    if mimeType == applicationxnzb:
        return [ "nzb" ]

    if mimeType == applicationvndapplenumbers:
        return [ "numbers" ]

    if mimeType == applicationxnuscript:
        return [ "nu" ]

    if mimeType == applicationvndnitf:
        return [ "ntf", "nitf" ]

    if mimeType == applicationntriples:
        return [ "nt" ]

    if mimeType == videoxnsv:
        return [ "nsv" ]

    if mimeType == applicationvndlotusnotes:
        return [ "nsf" ]

    if mimeType == applicationxnetshowchannel:
        return [ "nsc" ]

    if mimeType == imagexnikonnrw:
        return [ "nrw" ]

    if mimeType == applicationnquads:
        return [ "nq" ]

    if mimeType == imagevndnetfpx:
        return [ "npx" ]

    if mimeType == applicationvndnoblenetweb:
        return [ "nnw" ]

    if mimeType == applicationvndnoblenetsealer:
        return [ "nns" ]

    if mimeType == applicationvndnoblenetdirectory:
        return [ "nnd" ]

    if mimeType == applicationvndenliven:
        return [ "nml" ]

    if mimeType == applicationvndneurolanguagenlu:
        return [ "nlu" ]

    if mimeType == textxnimscript:
        return [ "nims", "nimble" ]

    if mimeType == textxnim:
        return [ "nim" ]

    if mimeType == applicationxneogeopocketrom:
        return [ "ngp" ]

    if mimeType == applicationvndnokiangagedata:
        return [ "ngdat" ]

    if mimeType == applicationxneogeopocketcolorrom:
        return [ "ngc" ]

    if mimeType == applicationvndnokiangagesymbianinstall:
        return [ "n-gage" ]

    if mimeType == textxnfo:
        return [ "nfo" ]

    if mimeType == applicationxnesrom:
        return [ "nes", "nez", "unf", "unif" ]

    if mimeType == imagexnikonnef:
        return [ "nef" ]

    if mimeType == applicationxnintendodsrom:
        return [ "nds" ]

    if mimeType == applicationxdtbncx_xml:
        return [ "ncx" ]

    if mimeType == applicationvndwolframplayer:
        return [ "nbp" ]

    if mimeType == applicationmathematica:
        return [ "nb", "ma", "mb" ]

    if mimeType == applicationxn64rom:
        return [ "n64", "z64", "v64" ]

    if mimeType == textn3:
        return [ "n3" ]

    if mimeType == applicationvndtriscapemxs:
        return [ "mxs" ]

    if mimeType == applicationxv_xml:
        return [ "mxml", "xhvml", "xvml", "xvm" ]

    if mimeType == audiomobilexmf:
        return [ "mxmf" ]

    if mimeType == applicationvndrecordaremusicxml:
        return [ "mxl" ]

    if mimeType == applicationmxf:
        return [ "mxf" ]

    if mimeType == applicationvndmfer:
        return [ "mwf" ]

    if mimeType == applicationvndmapboxvectortile:
        return [ "mvt" ]

    if mimeType == applicationxmsmediaview:
        return [ "mvb", "m13", "m14" ]

    if mimeType == applicationvndrecordaremusicxml_xml:
        return [ "musicxml" ]

    if mimeType == applicationmmtusd_xml:
        return [ "musd" ]

    if mimeType == applicationvndmusician:
        return [ "mus" ]

    if mimeType == textxmup:
        return [ "mup", "not" ]

    if mimeType == modelmtl:
        return [ "mtl" ]

    if mimeType == applicationxmsxrom:
        return [ "msx" ]

    if mimeType == applicationvndmuveestyle:
        return [ "msty" ]

    if mimeType == imagexmsod:
        return [ "msod" ]

    if mimeType == applicationvndmobiusmsl:
        return [ "msl" ]

    if mimeType == applicationmsixbundle:
        return [ "msixbundle" ]

    if mimeType == applicationmsix:
        return [ "msix" ]

    if mimeType == applicationxmsi:
        return [ "msi" ]

    if mimeType == modelmesh:
        return [ "msh", "mesh", "silo" ]

    if mimeType == applicationvndmsoutlook:
        return [ "msg" ]

    if mimeType == applicationvndepsonmsf:
        return [ "msf" ]

    if mimeType == applicationvndmseq:
        return [ "mseq" ]

    if mimeType == applicationvndfdsnmseed:
        return [ "mseed" ]

    if mimeType == applicationmediaservercontrol_xml:
        return [ "mscml" ]

    if mimeType == textxtroffms:
        return [ "ms" ]

    if mimeType == imagexminoltamrw:
        return [ "mrw" ]

    if mimeType == applicationxmodrinthmodpack_zip:
        return [ "mrpack" ]

    if mimeType == textxmrml:
        return [ "mrml", "mrl" ]

    if mimeType == applicationmarcxml_xml:
        return [ "mrcx" ]

    if mimeType == applicationmarc:
        return [ "mrc" ]

    if mimeType == applicationvndmobiusmqy:
        return [ "mqy" ]

    if mimeType == applicationvndibmminipay:
        return [ "mpy" ]

    if mimeType == applicationvndmsproject:
        return [ "mpt" ]

    if mimeType == applicationvndmophunapplication:
        return [ "mpn" ]

    if mimeType == applicationvndblueicemultipass:
        return [ "mpm" ]

    if mimeType == textxmpl2:
        return [ "mpl" ]

    if mimeType == applicationvndappleinstaller_xml:
        return [ "mpkg" ]

    if mimeType == applicationmp4:
        return [ "mpg4", "mp4s", "m4p" ]

    if mimeType == applicationmediapolicydataset_xml:
        return [ "mpf" ]

    if mimeType == videompeg:
        return [ "mpeg", "mpg", "mpe", "vob", "090909vdr", "m1v", "m2v" ]

    if mimeType == applicationdash_xml:
        return [ "mpd" ]

    if mimeType == audioxmusepack:
        return [ "mpc", "mpp", "mp" ]

    if mimeType == videomp4:
        return [ "mp4", "m4v", "f4v", "lrv", "mp4v" ]

    if mimeType == audiompeg:
        return [ "mp3", "mpga", "mp2a", "m2a", "m3a" ]

    if mimeType == audiomp2:
        return [ "mp2" ]

    if mimeType == videoxsgimovie:
        return [ "movie" ]

    if mimeType == textxmof:
        return [ "mof" ]

    if mimeType == applicationmods_xml:
        return [ "mods" ]

    if mimeType == textxmoc:
        return [ "moc" ]

    if mimeType == applicationxmobipocketebook:
        return [ "mobi", "prc" ]

    if mimeType == audioxmo3:
        return [ "mo3" ]

    if mimeType == applicationxmsmoney:
        return [ "mny" ]

    if mimeType == videoxmng:
        return [ "mng" ]

    if mimeType == imagevndfujixeroxedmicsmmr:
        return [ "mmr" ]

    if mimeType == applicationmathml_xml:
        return [ "mml", "mathml" ]

    if mimeType == applicationvndsmaf:
        return [ "mmf", "smaf" ]

    if mimeType == applicationvndchipnutskaraokemmd:
        return [ "mmd" ]

    if mimeType == textxobjc__src:
        return [ "mm" ]

    if mimeType == applicationvnddolbymlp:
        return [ "mlp" ]

    if mimeType == textxocaml:
        return [ "ml", "mli" ]

    if mimeType == videoxmatroska:
        return [ "mkv", "mks" ]

    if mimeType == audioxmatroska:
        return [ "mka" ]

    if mimeType == videoxmatroska3d:
        return [ "mk3d" ]

    if mimeType == videoxmjpeg:
        return [ "mjpeg", "mjpg" ]

    if mimeType == videomj2:
        return [ "mj2", "mjp2" ]

    if mimeType == audioxminipsf:
        return [ "minipsf" ]

    if mimeType == applicationxmif:
        return [ "mif" ]

    if mimeType == applicationxmie:
        return [ "mie" ]

    if mimeType == audiomidi:
        return [ "mid", "midi", "kar", "rmi" ]

    if mimeType == applicationxmimearchive:
        return [ "mhtml", "mht" ]

    if mimeType == applicationvndproteusmagazine:
        return [ "mgz" ]

    if mimeType == applicationxmagicpoint:
        return [ "mgp" ]

    if mimeType == applicationrpkimanifest:
        return [ "mft" ]

    if mimeType == applicationvndmfmp:
        return [ "mfm" ]

    if mimeType == applicationmets_xml:
        return [ "mets" ]

    if mimeType == applicationmetalink_xml:
        return [ "metalink" ]

    if mimeType == applicationmetalink4_xml:
        return [ "meta4" ]

    if mimeType == textxmeson:
        return [ "mesonbuild", "mesonoptionstxt" ]

    if mimeType == textxtroffme:
        return [ "me" ]

    if mimeType == imagevndmsmodi:
        return [ "mdi" ]

    if mimeType == applicationxlmdb:
        return [ "mdb", "lmdb" ]

    if mimeType == textmarkdown:
        return [ "md", "mkd", "markdown" ]

    if mimeType == textvndcurlmcurl:
        return [ "mcurl" ]

    if mimeType == applicationvndmcd:
        return [ "mcd" ]

    if mimeType == textvndsenxwarpscript:
        return [ "mc2" ]

    if mimeType == applicationvndmedcalcdata:
        return [ "mc1" ]

    if mimeType == applicationmbox:
        return [ "mbox" ]

    if mimeType == applicationvndmobiusmbk:
        return [ "mbk" ]

    if mimeType == textcachemanifest:
        return [ "manifest", "appcache" ]

    if mimeType == applicationxtroffman:
        return [ "man", "19" ]

    if mimeType == textxmakefile:
        return [ "makefile", "gnumakefile", "mk", "mak" ]

    if mimeType == applicationvndecowinchart:
        return [ "mag" ]

    if mimeType == applicationmmtaei_xml:
        return [ "maei" ]

    if mimeType == applicationmads_xml:
        return [ "mads" ]

    if mimeType == applicationxmarkaby:
        return [ "mab" ]

    if mimeType == applicationxthomsoncartridgememo7:
        return [ "m7" ]

    if mimeType == videoisosegment:
        return [ "m4s" ]

    if mimeType == audioxm4r:
        return [ "m4r" ]

    if mimeType == audioxm4b:
        return [ "m4b", "f4b" ]

    if mimeType == audiomp4:
        return [ "m4a", "f4a", "mp4a" ]

    if mimeType == applicationxm4:
        return [ "m4" ]

    if mimeType == audioxmpegurl:
        return [ "m3u", "m3u8", "vlc" ]

    if mimeType == videomp2t:
        return [ "m2t", "m2ts", "mts", "cpi", "clpi", "mpls", "bdm", "bdmv" ]

    if mimeType == applicationmp21:
        return [ "m21", "mp21" ]

    if mimeType == videovndmpegurl:
        return [ "m1u", "m4u", "mxu" ]

    if mimeType == textxobjcsrc:
        return [ "m" ]

    if mimeType == applicationxlzop:
        return [ "lzo" ]

    if mimeType == applicationxlzma:
        return [ "lzma" ]

    if mimeType == applicationxlz4:
        return [ "lz4" ]

    if mimeType == applicationxlzip:
        return [ "lz" ]

    if mimeType == applicationxlyx:
        return [ "lyx" ]

    if mimeType == textxlilypond:
        return [ "ly" ]

    if mimeType == imagexlws:
        return [ "lws" ]

    if mimeType == applicationvndlotuswordpro:
        return [ "lwp" ]

    if mimeType == imagexlwo:
        return [ "lwo", "lwob" ]

    if mimeType == audiovndlucentvoice:
        return [ "lvp" ]

    if mimeType == applicationxluabytecode:
        return [ "luac" ]

    if mimeType == textxlua:
        return [ "lua" ]

    if mimeType == applicationvndfrogansltf:
        return [ "ltf" ]

    if mimeType == applicationxlrzip:
        return [ "lrz" ]

    if mimeType == applicationvndmslrm:
        return [ "lrm" ]

    if mimeType == applicationlost_xml:
        return [ "lostxml" ]

    if mimeType == textxlog:
        return [ "log" ]

    if mimeType == audiousac:
        return [ "loas", "xhe" ]

    if mimeType == applicationxatarilynxrom:
        return [ "lnx" ]

    if mimeType == applicationxmsshortcut:
        return [ "lnk" ]

    if mimeType == textcoffeescript:
        return [ "litcoffee" ]

    if mimeType == applicationvndroute66link66_xml:
        return [ "link66" ]

    if mimeType == applicationxlhz:
        return [ "lhz" ]

    if mimeType == textxliteratehaskell:
        return [ "lhs" ]

    if mimeType == applicationxlha:
        return [ "lha", "lzh" ]

    if mimeType == applicationlgr_xml:
        return [ "lgr" ]

    if mimeType == textless:
        return [ "less" ]

    if mimeType == applicationvndhhelessonplayer:
        return [ "les" ]

    if mimeType == textxldif:
        return [ "ldif" ]

    if mimeType == applicationvndllamagraphicslifebalanceexchange_xml:
        return [ "lbe" ]

    if mimeType == applicationvndllamagraphicslifebalancedesktop:
        return [ "lbd" ]

    if mimeType == applicationvndlaslas_xml:
        return [ "lasxml" ]

    if mimeType == applicationxsharedlibraryla:
        return [ "la" ]

    if mimeType == applicationxkword:
        return [ "kwd", "kwt" ]

    if mimeType == applicationxkugar:
        return [ "kud" ]

    if mimeType == applicationvndkahootz:
        return [ "ktz", "ktr" ]

    if mimeType == imagektx2:
        return [ "ktx2" ]

    if mimeType == imagektx:
        return [ "ktx" ]

    if mimeType == textxkotlin:
        return [ "kt" ]

    if mimeType == textxkaitaistruct:
        return [ "ksy" ]

    if mimeType == applicationxkspread:
        return [ "ksp" ]

    if mimeType == applicationxkrita:
        return [ "kra", "krz" ]

    if mimeType == applicationvnddskeypoint:
        return [ "kpxx" ]

    if mimeType == applicationxkpresenter:
        return [ "kpr", "kpt" ]

    if mimeType == applicationxkpovmodeler:
        return [ "kpm" ]

    if mimeType == applicationxkontour:
        return [ "kon" ]

    if mimeType == applicationvndkinar:
        return [ "kne", "knp" ]

    if mimeType == applicationvndgoogleearthkmz:
        return [ "kmz" ]

    if mimeType == applicationvndgoogleearthkml_xml:
        return [ "kml" ]

    if mimeType == applicationxkillustrator:
        return [ "kil" ]

    if mimeType == applicationvndkidspiration:
        return [ "kia" ]

    if mimeType == applicationxkformula:
        return [ "kfo" ]

    if mimeType == applicationxkexiprojectshortcut:
        return [ "kexis" ]

    if mimeType == applicationxkexiconnectiondata:
        return [ "kexic" ]

    if mimeType == applicationxkexiprojectsqlite2:
        return [ "kexi" ]

    if mimeType == imagexkodakkdc:
        return [ "kdc" ]

    if mimeType == applicationxkeepass2:
        return [ "kdbx" ]

    if mimeType == applicationxkarbon:
        return [ "karbon" ]

    if mimeType == applicationxthomsoncassette:
        return [ "k7" ]

    if mimeType == imagexkodakk25:
        return [ "k25" ]

    if mimeType == imagejxss:
        return [ "jxss" ]

    if mimeType == imagejxsi:
        return [ "jxsi" ]

    if mimeType == imagejxsc:
        return [ "jxsc" ]

    if mimeType == imagejxs:
        return [ "jxs" ]

    if mimeType == imagejxrs:
        return [ "jxrs" ]

    if mimeType == imagejxra:
        return [ "jxra" ]

    if mimeType == imagejxr:
        return [ "jxr", "hdp", "wdp" ]

    if mimeType == imagejxl:
        return [ "jxl" ]

    if mimeType == modeljt:
        return [ "jt" ]

    if mimeType == textjsx:
        return [ "jsx" ]

    if mimeType == applicationjsonpatch_json:
        return [ "jsonpatch" ]

    if mimeType == applicationjsonml_json:
        return [ "jsonml" ]

    if mimeType == applicationld_json:
        return [ "jsonld" ]

    if mimeType == applicationjson5:
        return [ "json5" ]

    if mimeType == applicationjson:
        return [ "json", "map" ]

    if mimeType == textjscriptencode:
        return [ "jse" ]

    if mimeType == textjavascript:
        return [ "js", "jsm", "mjs" ]

    if mimeType == applicationjrd_json:
        return [ "jrd" ]

    if mimeType == applicationxjbuilderproject:
        return [ "jpr", "jpx" ]

    if mimeType == imagejpm:
        return [ "jpm", "jpgm" ]

    if mimeType == imagejph:
        return [ "jph" ]

    if mimeType == videojpeg:
        return [ "jpgv" ]

    if mimeType == imagejpeg:
        return [ "jpg", "jpeg", "jpe", "jfif" ]

    if mimeType == imagejpx:
        return [ "jpf" ]

    if mimeType == imagejp2:
        return [ "jp2", "jpg2" ]

    if mimeType == applicationvndjoostjodaarchive:
        return [ "joda" ]

    if mimeType == applicationxjavajnlpfile:
        return [ "jnlp" ]

    if mimeType == imagexjng:
        return [ "jng" ]

    if mimeType == applicationvndhpjlyt:
        return [ "jlt" ]

    if mimeType == imagejls:
        return [ "jls" ]

    if mimeType == textjulia:
        return [ "jl" ]

    if mimeType == applicationxjavakeystore:
        return [ "jks", "ks", "cacerts" ]

    if mimeType == applicationvndjisp:
        return [ "jisp" ]

    if mimeType == imagejphc:
        return [ "jhc" ]

    if mimeType == applicationxjavajcekeystore:
        return [ "jceks" ]

    if mimeType == textxjava:
        return [ "java" ]

    if mimeType == applicationxjavaarchivediff:
        return [ "jardiff" ]

    if mimeType == applicationjavaarchive:
        return [ "jar", "war", "ear" ]

    if mimeType == applicationvndjam:
        return [ "jam" ]

    if mimeType == textjade:
        return [ "jade" ]

    if mimeType == textvndsunj2meappdescriptor:
        return [ "jad" ]

    if mimeType == imagexjp2codestream:
        return [ "j2c", "j2k", "jpc" ]

    if mimeType == applicationvndimmervisionivu:
        return [ "ivu" ]

    if mimeType == applicationvndimmervisionivp:
        return [ "ivp" ]

    if mimeType == applicationits_xml:
        return [ "its" ]

    if mimeType == applicationvndshanainformedformtemplate:
        return [ "itp" ]

    if mimeType == applicationxit87:
        return [ "it87" ]

    if mimeType == audioxit:
        return [ "it" ]

    if mimeType == applicationvndefiiso:
        return [ "iso", "iso9660" ]

    if mimeType == applicationvndirepositorypackage_xml:
        return [ "irp" ]

    if mimeType == applicationvndibmrightsmanagement:
        return [ "irm" ]

    if mimeType == applicationxipynb_json:
        return [ "ipynb" ]

    if mimeType == textxiptables:
        return [ "iptables" ]

    if mimeType == applicationxipspatch:
        return [ "ips" ]

    if mimeType == applicationvndshanainformedpackage:
        return [ "ipk" ]

    if mimeType == applicationipfix:
        return [ "ipfix" ]

    if mimeType == applicationvndastraeasoftwareiota:
        return [ "iota" ]

    if mimeType == textxinstall:
        return [ "install" ]

    if mimeType == applicationinkml_xml:
        return [ "ink", "inkml" ]

    if mimeType == textximelody:
        return [ "imy", "ime" ]

    if mimeType == applicationvndmsims:
        return [ "ims" ]

    if mimeType == applicationvndaccpacsimplyimp:
        return [ "imp" ]

    if mimeType == applicationvndshanainformedinterchange:
        return [ "iif" ]

    if mimeType == applicationvndmicrografxigx:
        return [ "igx" ]

    if mimeType == modeliges:
        return [ "igs", "iges" ]

    if mimeType == applicationvndinsorsigm:
        return [ "igm" ]

    if mimeType == applicationvndigloader:
        return [ "igl" ]

    if mimeType == applicationvndshanainformedformdata:
        return [ "ifm" ]

    if mimeType == imagexilbm:
        return [ "iff", "ilbm", "lbm" ]

    if mimeType == imageief:
        return [ "ief" ]

    if mimeType == textxidl:
        return [ "idl" ]

    if mimeType == imagevndmicrosofticon:
        return [ "ico" ]

    if mimeType == imagexicns:
        return [ "icns" ]

    if mimeType == xconferencexcooltalk:
        return [ "ice" ]

    if mimeType == applicationvndiccprofile:
        return [ "icc", "icm" ]

    if mimeType == applicationxica:
        return [ "ica" ]

    if mimeType == applicationvndintergeo:
        return [ "i2g" ]

    if mimeType == applicationxhwt:
        return [ "hwt" ]

    if mimeType == applicationxhwp:
        return [ "hwp" ]

    if mimeType == applicationvndyamahahvscript:
        return [ "hvs" ]

    if mimeType == applicationvndyamahahvvoice:
        return [ "hvp" ]

    if mimeType == applicationvndyamahahvdic:
        return [ "hvd" ]

    if mimeType == applicationvndkenameaapp:
        return [ "htke" ]

    if mimeType == textxcomponent:
        return [ "htc" ]

    if mimeType == imagehsj2:
        return [ "hsj2" ]

    if mimeType == textxhaskell:
        return [ "hs" ]

    if mimeType == applicationmacbinhex40:
        return [ "hqx" ]

    if mimeType == applicationvndhphps:
        return [ "hps" ]

    if mimeType == applicationvndhphpid:
        return [ "hpid" ]

    if mimeType == applicationvndhphpgl:
        return [ "hpgl" ]

    if mimeType == applicationwinhlp:
        return [ "hlp" ]

    if mimeType == applicationhjson:
        return [ "hjson" ]

    if mimeType == textxc__hdr:
        return [ "hh", "hp", "hpp", "h", "hxx" ]

    if mimeType == applicationxhfefloppyimage:
        return [ "hfe" ]

    if mimeType == applicationatscheld_xml:
        return [ "held" ]

    if mimeType == imagehej2k:
        return [ "hej2" ]

    if mimeType == imageheifsequence:
        return [ "heifs" ]

    if mimeType == imageheicsequence:
        return [ "heics" ]

    if mimeType == imageheif:
        return [ "heic", "heif", "hif" ]

    if mimeType == applicationxhdf:
        return [ "hdf", "hdf4", "h4", "hdf5", "h5" ]

    if mimeType == applicationxvirtualboxhdd:
        return [ "hdd" ]

    if mimeType == textxhandlebarstemplate:
        return [ "hbs" ]

    if mimeType == applicationvndhbci:
        return [ "hbci" ]

    if mimeType == applicationvndhal_xml:
        return [ "hal" ]

    if mimeType == videoh264:
        return [ "h264" ]

    if mimeType == videoh263:
        return [ "h263" ]

    if mimeType == videoh261:
        return [ "h261" ]

    if mimeType == applicationgzip:
        return [ "gz" ]

    if mimeType == applicationvndgeonext:
        return [ "gxt" ]

    if mimeType == applicationgxf:
        return [ "gxf" ]

    if mimeType == textxgcodegx:
        return [ "gx" ]

    if mimeType == textxgooglevideopointer:
        return [ "gvp" ]

    if mimeType == textvndgraphviz:
        return [ "gv" ]

    if mimeType == modelvndgtw:
        return [ "gtw" ]

    if mimeType == applicationvndgroovetoolmessage:
        return [ "gtm" ]

    if mimeType == audioxgsm:
        return [ "gsm" ]

    if mimeType == applicationvndgoogleappspresentation:
        return [ "gslides" ]

    if mimeType == applicationvndgoogleappsspreadsheet:
        return [ "gsheet" ]

    if mimeType == textxgenie:
        return [ "gs" ]

    if mimeType == applicationsrgs_xml:
        return [ "grxml" ]

    if mimeType == applicationvndgrooveinjector:
        return [ "grv" ]

    if mimeType == textxgroovy:
        return [ "groovy", "gvy", "gy", "gsh" ]

    if mimeType == applicationxgrampsxml:
        return [ "gramps" ]

    if mimeType == applicationsrgs:
        return [ "gram" ]

    if mimeType == textxgradle:
        return [ "gradle" ]

    if mimeType == applicationxgraphite:
        return [ "gra" ]

    if mimeType == applicationvndgrafeq:
        return [ "gqf", "gqs" ]

    if mimeType == applicationgpx_xml:
        return [ "gpx" ]

    if mimeType == applicationvndflographit:
        return [ "gph" ]

    if mimeType == applicationxgnuplot:
        return [ "gp", "gplt", "gnuplot" ]

    if mimeType == textxgo:
        return [ "go" ]

    if mimeType == applicationxgnumeric:
        return [ "gnumeric" ]

    if mimeType == applicationxgnucash:
        return [ "gnucash", "gnc", "xac" ]

    if mimeType == applicationgnunetdirectory:
        return [ "gnd" ]

    if mimeType == applicationvndgmx:
        return [ "gmx" ]

    if mimeType == applicationxprofile:
        return [ "gmonout" ]

    if mimeType == applicationxgettexttranslation:
        return [ "gmo", "mo" ]

    if mimeType == applicationgml_xml:
        return [ "gml" ]

    if mimeType == modelgltf_json:
        return [ "gltf" ]

    if mimeType == modelgltfbinary:
        return [ "glb" ]

    if mimeType == applicationxglade:
        return [ "glade" ]

    if mimeType == applicationvndgrooveidentitymessage:
        return [ "gim" ]

    if mimeType == imagexgimpgih:
        return [ "gih" ]

    if mimeType == imagegif:
        return [ "gif" ]

    if mimeType == applicationvndgroovehelp:
        return [ "ghf" ]

    if mimeType == applicationvndgeogebratool:
        return [ "ggt" ]

    if mimeType == applicationvndgeogebrafile:
        return [ "ggb" ]

    if mimeType == applicationxgamegearrom:
        return [ "gg" ]

    if mimeType == applicationxtexgf:
        return [ "gf" ]

    if mimeType == applicationvndgeometryexplorer:
        return [ "gex", "gre" ]

    if mimeType == applicationgeo_json:
        return [ "geojson" ]

    if mimeType == applicationvnddynageo:
        return [ "geo" ]

    if mimeType == applicationxgenesisrom:
        return [ "gen", "sgd" ]

    if mimeType == textvndfamilysearchgedcom:
        return [ "ged", "gedcom" ]

    if mimeType == applicationxgodotshader:
        return [ "gdshader" ]

    if mimeType == applicationvndgoogleappsdocument:
        return [ "gdoc" ]

    if mimeType == modelvndgdl:
        return [ "gdl" ]

    if mimeType == applicationxgdromcue:
        return [ "gdi" ]

    if mimeType == applicationxgdscript:
        return [ "gd" ]

    if mimeType == textxgcode:
        return [ "gcode" ]

    if mimeType == applicationxgcacompressed:
        return [ "gca" ]

    if mimeType == applicationxgerberjob:
        return [ "gbrjob" ]

    if mimeType == imagexgimpgbr:
        return [ "gbr" ]

    if mimeType == applicationxgameboycolorrom:
        return [ "gbc", "cgb" ]

    if mimeType == applicationxgbarom:
        return [ "gba", "agb" ]

    if mimeType == applicationxgameboyrom:
        return [ "gb", "sgb" ]

    if mimeType == applicationxtads:
        return [ "gam" ]

    if mimeType == applicationvndgrooveaccount:
        return [ "gac" ]

    if mimeType == applicationvndgeospace:
        return [ "g3w" ]

    if mimeType == imageg3fax:
        return [ "g3" ]

    if mimeType == applicationvndgeoplan:
        return [ "g2w" ]

    if mimeType == applicationvndfuzzysheet:
        return [ "fzs" ]

    if mimeType == applicationvndadobefxp:
        return [ "fxp", "fxpl" ]

    if mimeType == videoxjavafx:
        return [ "fxm" ]

    if mimeType == videovndfvt:
        return [ "fvt" ]

    if mimeType == applicationvndanserwebfundstransferinitiation:
        return [ "fti" ]

    if mimeType == applicationvndfluxtimeclip:
        return [ "ftc" ]

    if mimeType == imagevndfst:
        return [ "fst" ]

    if mimeType == applicationvndfscweblaunch:
        return [ "fsc" ]

    if mimeType == imagevndfpx:
        return [ "fpx" ]

    if mimeType == applicationvndoasisopendocumenttextflatxml:
        return [ "fodt" ]

    if mimeType == applicationvndoasisopendocumentspreadsheetflatxml:
        return [ "fods" ]

    if mimeType == applicationvndoasisopendocumentpresentationflatxml:
        return [ "fodp" ]

    if mimeType == applicationvndoasisopendocumentgraphicsflatxml:
        return [ "fodg" ]

    if mimeType == textxxslfo:
        return [ "fo", "xslfo" ]

    if mimeType == applicationvndfrogansfnc:
        return [ "fnc" ]

    if mimeType == applicationvndframemaker:
        return [ "fm", "frame", "maker", "book" ]

    if mimeType == textvndfly:
        return [ "fly" ]

    if mimeType == textvndfmiflexstor:
        return [ "flx" ]

    if mimeType == applicationxkivio:
        return [ "flw" ]

    if mimeType == videoxflv:
        return [ "flv" ]

    if mimeType == applicationvndmicrografxflo:
        return [ "flo" ]

    if mimeType == videoxflic:
        return [ "fli", "flc" ]

    if mimeType == applicationvndflatpakrepo:
        return [ "flatpakrepo" ]

    if mimeType == applicationvndflatpakref:
        return [ "flatpakref" ]

    if mimeType == applicationvndflatpak:
        return [ "flatpak", "xdgapp" ]

    if mimeType == audioflac:
        return [ "flac" ]

    if mimeType == applicationxfluid:
        return [ "fl" ]

    if mimeType == applicationfits:
        return [ "fits", "fit", "fts" ]

    if mimeType == applicationxfishscript:
        return [ "fish" ]

    if mimeType == imagexxfig:
        return [ "fig" ]

    if mimeType == imagexfreehand:
        return [ "fh", "fhc", "fh4", "fh5", "fh7" ]

    if mimeType == applicationvndfujitsuoasysgp:
        return [ "fg5" ]

    if mimeType == textxgherkin:
        return [ "feature" ]

    if mimeType == applicationvnddenovofcselayoutlink:
        return [ "fe_launch" ]

    if mimeType == applicationfdt_xml:
        return [ "fdt" ]

    if mimeType == applicationxfdsdisk:
        return [ "fds" ]

    if mimeType == applicationfdf:
        return [ "fdf" ]

    if mimeType == applicationxrawfloppydiskimage:
        return [ "fd", "qd" ]

    if mimeType == applicationvndisacfcs:
        return [ "fcs" ]

    if mimeType == applicationvndadobeformscentralfcdt:
        return [ "fcdt" ]

    if mimeType == imagevndfastbidsheet:
        return [ "fbs" ]

    if mimeType == applicationxzipcompressedfb2:
        return [ "fb2zip" ]

    if mimeType == applicationxfictionbook_xml:
        return [ "fb2" ]

    if mimeType == textxfortran:
        return [ "f", "f90", "f95", "for", "f77" ]

    if mimeType == applicationvndezpixpackage:
        return [ "ez3" ]

    if mimeType == applicationvndezpixalbum:
        return [ "ez2" ]

    if mimeType == applicationandrewinset:
        return [ "ez" ]

    if mimeType == applicationvndnovadigmext:
        return [ "ext" ]

    if mimeType == imagexexr:
        return [ "exr" ]

    if mimeType == applicationexpress:
        return [ "exp" ]

    if mimeType == applicationexi:
        return [ "exi" ]

    if mimeType == applicationxmsdownload:
        return [ "exe", "dll", "cpl", "drv", "scr", "com" ]

    if mimeType == textxelixir:
        return [ "ex", "exs" ]

    if mimeType == applicationxenvoy:
        return [ "evy" ]

    if mimeType == applicationxeva:
        return [ "eva" ]

    if mimeType == textxsetext:
        return [ "etx" ]

    if mimeType == applicationxetheme:
        return [ "etheme" ]

    if mimeType == applicationvndepsonesf:
        return [ "esf" ]

    if mimeType == applicationvndosgisubsystem:
        return [ "esa" ]

    if mimeType == applicationvndeszigno3_xml:
        return [ "es3", "et3" ]

    if mimeType == applicationecmascript:
        return [ "es", "ecma" ]

    if mimeType == textxerlang:
        return [ "erl" ]

    if mimeType == applicationxerislink_cbor:
        return [ "eris" ]

    if mimeType == applicationepub_zip:
        return [ "epub" ]

    if mimeType == imagexgzeps:
        return [ "epsgz", "epsigz", "epsfgz" ]

    if mimeType == imagexbzeps:
        return [ "epsbz2", "epsibz2", "epsfbz2" ]

    if mimeType == imagexeps:
        return [ "eps", "epsi", "epsf" ]

    if mimeType == applicationvndmsfontobject:
        return [ "eot" ]

    if mimeType == audiovnddigitalwinds:
        return [ "eol" ]

    if mimeType == applicationxmlexternalparsedentity:
        return [ "ent" ]

    if mimeType == applicationxmsmetafile:
        return [ "emz" ]

    if mimeType == applicationvndemusicemusic_package:
        return [ "emp" ]

    if mimeType == applicationemotionml_xml:
        return [ "emotionml" ]

    if mimeType == applicationemma_xml:
        return [ "emma" ]

    if mimeType == messagerfc822:
        return [ "eml", "mime" ]

    if mimeType == imageemf:
        return [ "emf" ]

    if mimeType == textxemacslisp:
        return [ "el" ]

    if mimeType == applicationvndpgosasli:
        return [ "ei6" ]

    if mimeType == applicationvndmicrosoftwindowsthumbnailcache:
        return [ "ehthumbsdb", "ehthumbsvistadb", "imagedb", "musicthumbsdb", "thumbsdb", "tvthumbdb", "videodb" ]

    if mimeType == applicationxegon:
        return [ "egon" ]

    if mimeType == applicationvndpicsel:
        return [ "efif" ]

    if mimeType == applicationvndmicrosoftportableexecutable:
        return [ "efi", "ocx", "sys", "lib" ]

    if mimeType == applicationvndnovadigmedx:
        return [ "edx" ]

    if mimeType == applicationvndnovadigmedm:
        return [ "edm" ]

    if mimeType == audiovndnueraecelp9600:
        return [ "ecelp9600" ]

    if mimeType == audiovndnueraecelp7470:
        return [ "ecelp7470" ]

    if mimeType == audiovndnueraecelp4800:
        return [ "ecelp4800" ]

    if mimeType == textxeiffel:
        return [ "e", "eif" ]

    if mimeType == applicationvndspotfiredxp:
        return [ "dxp" ]

    if mimeType == imagevnddxf:
        return [ "dxf" ]

    if mimeType == imagevnddwg:
        return [ "dwg" ]

    if mimeType == modelvnddwf:
        return [ "dwf" ]

    if mimeType == applicationatscdwd_xml:
        return [ "dwd" ]

    if mimeType == applicationxgzdvi:
        return [ "dvigz" ]

    if mimeType == applicationxbzdvi:
        return [ "dvibz2" ]

    if mimeType == applicationxdvi:
        return [ "dvi" ]

    if mimeType == videovnddvbfile:
        return [ "dvb" ]

    if mimeType == videodv:
        return [ "dv" ]

    if mimeType == textxdevicetreesource:
        return [ "dtsi" ]

    if mimeType == audiovnddtshd:
        return [ "dtshd" ]

    if mimeType == audiovnddts:
        return [ "dts" ]

    if mimeType == applicationxmldtd:
        return [ "dtd" ]

    if mimeType == textxdevicetreebinary:
        return [ "dtb" ]

    if mimeType == applicationdssc_der:
        return [ "dssc" ]

    if mimeType == textxdsl:
        return [ "dsl" ]

    if mimeType == audioxdsf:
        return [ "dsf" ]

    if mimeType == textprslinestag:
        return [ "dsc" ]

    if mimeType == imagedicomrle:
        return [ "drle" ]

    if mimeType == applicationxexcellon:
        return [ "drl" ]

    if mimeType == audiovnddra:
        return [ "dra" ]

    if mimeType == imagedpx:
        return [ "dpx" ]

    if mimeType == applicationvnddpgraph:
        return [ "dpg" ]

    if mimeType == applicationvndosgidp:
        return [ "dp" ]

    if mimeType == applicationvndopenxmlformatsofficedocumentwordprocessingmltemplate:
        return [ "dotx" ]

    if mimeType == applicationvndmswordtemplatemacroenabled12:
        return [ "dotm" ]

    if mimeType == applicationmswordtemplate:
        return [ "dot" ]

    if mimeType == applicationvndopenxmlformatsofficedocumentwordprocessingmldocument:
        return [ "docx" ]

    if mimeType == applicationvndmsworddocumentmacroenabled12:
        return [ "docm" ]

    if mimeType == applicationmsword:
        return [ "doc" ]

    if mimeType == imagexadobedng:
        return [ "dng" ]

    if mimeType == applicationvnddna:
        return [ "dna" ]

    if mimeType == applicationxapplediskimage:
        return [ "dmg" ]

    if mimeType == imagevnddjvu:
        return [ "djvu", "djv" ]

    if mimeType == messagedispositionnotification:
        return [ "disposition-notification" ]

    if mimeType == applicationvndmobiusdis:
        return [ "dis" ]

    if mimeType == applicationxdirector:
        return [ "dir", "dxr", "cst", "cct", "cxt", "w3d", "fgd", "swa" ]

    if mimeType == textxpatch:
        return [ "diff", "patch" ]

    if mimeType == applicationdicom:
        return [ "dicomdir", "dcm" ]

    if mimeType == textxc:
        return [ "dic" ]

    if mimeType == applicationxdiadiagram:
        return [ "dia" ]

    if mimeType == applicationxdgccompressed:
        return [ "dgc" ]

    if mimeType == audioxdff:
        return [ "dff" ]

    if mimeType == applicationvnddreamfactory:
        return [ "dfac" ]

    if mimeType == applicationxdesktop:
        return [ "desktop", "kdelnk" ]

    if mimeType == applicationxx509cacert:
        return [ "der", "crt", "cert", "pem" ]

    if mimeType == applicationvnddebianbinarypackage:
        return [ "deb", "udeb" ]

    if mimeType == imagexdds:
        return [ "dds" ]

    if mimeType == applicationvndsyncmldmddf_xml:
        return [ "ddf" ]

    if mimeType == applicationvndfujixeroxddd:
        return [ "ddd" ]

    if mimeType == applicationvndomadd2_xml:
        return [ "dd2" ]

    if mimeType == textvndcurldcurl:
        return [ "dcurl" ]

    if mimeType == imagexkodakdcr:
        return [ "dcr" ]

    if mimeType == textxdcl:
        return [ "dcl" ]

    if mimeType == applicationxdocbook_xml:
        return [ "dbk", "docbook" ]

    if mimeType == applicationvnddbf:
        return [ "dbf" ]

    if mimeType == applicationdavmount_xml:
        return [ "davmount" ]

    if mimeType == applicationvnddart:
        return [ "dart" ]

    if mimeType == applicationxdar:
        return [ "dar" ]

    if mimeType == applicationvndmobiusdaf:
        return [ "daf" ]

    if mimeType == modelvndcollada_xml:
        return [ "dae" ]

    if mimeType == textxdsrc:
        return [ "d", "di" ]

    if mimeType == applicationprscww:
        return [ "cww" ]

    if mimeType == applicationcwl:
        return [ "cwl" ]

    if mimeType == applicationxappleworksdocument:
        return [ "cwk" ]

    if mimeType == textvndcurl:
        return [ "curl" ]

    if mimeType == imagexwinbitmap:
        return [ "cur" ]

    if mimeType == applicationxcue:
        return [ "cue" ]

    if mimeType == applicationcuseeme:
        return [ "cu" ]

    if mimeType == textcsvschema:
        return [ "csvs" ]

    if mimeType == textcsv:
        return [ "csv" ]

    if mimeType == textcss:
        return [ "css" ]

    if mimeType == applicationvndcommonspace:
        return [ "csp" ]

    if mimeType == applicationxcompressediso:
        return [ "cso" ]

    if mimeType == chemicalxcsml:
        return [ "csml" ]

    if mimeType == applicationvndcitationstylesstyle_xml:
        return [ "csl" ]

    if mimeType == applicationxcsh:
        return [ "csh" ]

    if mimeType == textxcsharp:
        return [ "cs" ]

    if mimeType == applicationvndrigcryptonote:
        return [ "cryptonote" ]

    if mimeType == applicationxchromeextension:
        return [ "crx" ]

    if mimeType == imagexcanoncrw:
        return [ "crw" ]

    if mimeType == applicationpkixcrl:
        return [ "crl" ]

    if mimeType == textxcredits:
        return [ "credits" ]

    if mimeType == applicationxmscardfile:
        return [ "crd" ]

    if mimeType == imagexcanoncr3:
        return [ "cr3" ]

    if mimeType == imagexcanoncr2:
        return [ "cr2" ]

    if mimeType == textxcrystal:
        return [ "cr" ]

    if mimeType == applicationmaccompactpro:
        return [ "cpt" ]

    if mimeType == textxc__src:
        return [ "cpp", "cxx", "cc", "c" ]

    if mimeType == applicationxcpiocompressed:
        return [ "cpiogz" ]

    if mimeType == applicationxcpio:
        return [ "cpio" ]

    if mimeType == applicationxcore:
        return [ "core" ]

    if mimeType == textxcopying:
        return [ "copying" ]

    if mimeType == applicationvndcoffeescript:
        return [ "coffee" ]

    if mimeType == applicationvndrimcod:
        return [ "cod" ]

    if mimeType == imagexcmx:
        return [ "cmx" ]

    if mimeType == applicationvndyellowrivercustommenu:
        return [ "cmp" ]

    if mimeType == chemicalxcml:
        return [ "cml" ]

    if mimeType == chemicalxcmdf:
        return [ "cmdf" ]

    if mimeType == applicationvndcosmocaller:
        return [ "cmc" ]

    if mimeType == textxcmake:
        return [ "cmake", "cmakeliststxt" ]

    if mimeType == applicationxmsclip:
        return [ "clp" ]

    if mimeType == applicationvndcrickclicker:
        return [ "clkx" ]

    if mimeType == applicationvndcrickclickerwordbank:
        return [ "clkw" ]

    if mimeType == applicationvndcrickclickertemplate:
        return [ "clkt" ]

    if mimeType == applicationvndcrickclickerpalette:
        return [ "clkp" ]

    if mimeType == applicationvndcrickclickerkeyboard:
        return [ "clkk" ]

    if mimeType == modelvndcld:
        return [ "cld" ]

    if mimeType == applicationxjava:
        return [ "class" ]

    if mimeType == applicationvndclaymore:
        return [ "cla" ]

    if mimeType == textxopenclsrc:
        return [ "cl" ]

    if mimeType == applicationnode:
        return [ "cjs" ]

    if mimeType == applicationvndmsartgalry:
        return [ "cil" ]

    if mimeType == applicationvndanserwebcertificateissueinitiation:
        return [ "cii" ]

    if mimeType == chemicalxcif:
        return [ "cif" ]

    if mimeType == applicationxkchart:
        return [ "chrt" ]

    if mimeType == applicationvndmshtmlhelp:
        return [ "chm" ]

    if mimeType == applicationxmamechd:
        return [ "chd" ]

    if mimeType == applicationxchat:
        return [ "chat" ]

    if mimeType == textxchangelog:
        return [ "changelog" ]

    if mimeType == imagecgm:
        return [ "cgm" ]

    if mimeType == applicationxcfscompressed:
        return [ "cfs" ]

    if mimeType == applicationpkixcert:
        return [ "cer" ]

    if mimeType == applicationvndcinderella:
        return [ "cdy" ]

    if mimeType == applicationvndchemdraw_xml:
        return [ "cdxml" ]

    if mimeType == chemicalxcdx:
        return [ "cdx" ]

    if mimeType == applicationvndcoreldraw:
        return [ "cdr" ]

    if mimeType == applicationcdmiqueue:
        return [ "cdmiq" ]

    if mimeType == applicationcdmiobject:
        return [ "cdmio" ]

    if mimeType == applicationcdmidomain:
        return [ "cdmid" ]

    if mimeType == applicationcdmicontainer:
        return [ "cdmic" ]

    if mimeType == applicationcdmicapability:
        return [ "cdmia" ]

    if mimeType == applicationvndmediastationcdkey:
        return [ "cdkey" ]

    if mimeType == applicationxdiscjugglercdimage:
        return [ "cdi" ]

    if mimeType == applicationcdfx_xml:
        return [ "cdfx" ]

    if mimeType == applicationxnetcdf:
        return [ "cdf", "nc" ]

    if mimeType == applicationvndcontactcmsg:
        return [ "cdbcmsg" ]

    if mimeType == applicationccxml_xml:
        return [ "ccxml" ]

    if mimeType == applicationxcocoa:
        return [ "cco" ]

    if mimeType == applicationxccmx:
        return [ "ccmx" ]

    if mimeType == applicationvndcomicbook_zip:
        return [ "cbz" ]

    if mimeType == applicationxcbt:
        return [ "cbt" ]

    if mimeType == applicationvndcomicbookrar:
        return [ "cbr" ]

    if mimeType == applicationcbor:
        return [ "cbor" ]

    if mimeType == textxcobol:
        return [ "cbl", "cob" ]

    if mimeType == applicationxcbr:
        return [ "cba" ]

    if mimeType == applicationxcb7:
        return [ "cb7" ]

    if mimeType == applicationvndmspkiseccat:
        return [ "cat" ]

    if mimeType == applicationvndcurlcar:
        return [ "car" ]

    if mimeType == audioxcaf:
        return [ "caf" ]

    if mimeType == applicationvndmscabcompressed:
        return [ "cab" ]

    if mimeType == applicationvndclonkc4group:
        return [ "c4g", "c4d", "c4f", "c4p", "c4u" ]

    if mimeType == applicationvndcluetrustcartomobileconfigpkg:
        return [ "c11amz" ]

    if mimeType == applicationvndcluetrustcartomobileconfig:
        return [ "c11amc" ]

    if mimeType == applicationxbzip3:
        return [ "bz3" ]

    if mimeType == applicationxbzip2:
        return [ "bz2", "boz" ]

    if mimeType == applicationxbzip1:
        return [ "bz" ]

    if mimeType == imageprsbtif:
        return [ "btif", "btf" ]

    if mimeType == modelvndvalvesourcecompiledmap:
        return [ "bsp" ]

    if mimeType == applicationxbsdiff:
        return [ "bsdiff" ]

    if mimeType == chemicalxpdb:
        return [ "brk" ]

    if mimeType == applicationxbpspatch:
        return [ "bps" ]

    if mimeType == applicationvndpreviewsystemsbox:
        return [ "box" ]

    if mimeType == imagebmp:
        return [ "bmp", "dib" ]

    if mimeType == applicationvndbalsamiqbmml_xml:
        return [ "bmml" ]

    if mimeType == applicationvndbmi:
        return [ "bmi" ]

    if mimeType == textxblueprint:
        return [ "blp" ]

    if mimeType == applicationxblender:
        return [ "blend", "blender" ]

    if mimeType == applicationxblorb:
        return [ "blb", "blorb" ]

    if mimeType == applicationoctetstream:
        return [ "bin", "dms", "lrf", "mar", "dist", "distz", "bpk", "dump", "elc", "deploy", "msp", "msm", "buffer" ]

    if mimeType == videovndradgamettoolsbink:
        return [ "bik", "bk2" ]

    if mimeType == textxbibtex:
        return [ "bib" ]

    if mimeType == applicationvndfujitsuoasysprs:
        return [ "bh2" ]

    if mimeType == applicationvndrealvncbed:
        return [ "bed" ]

    if mimeType == applicationbdoc:
        return [ "bdoc" ]

    if mimeType == applicationxfontbdf:
        return [ "bdf" ]

    if mimeType == applicationxbcpio:
        return [ "bcpio" ]

    if mimeType == applicationxbat:
        return [ "bat" ]

    if mimeType == textxbasic:
        return [ "bas" ]

    if mimeType == applicationxtrash:
        return [ "bak", "old", "sik" ]

    if mimeType == imagevndpcob16:
        return [ "b16" ]

    if mimeType == applicationvndamazonmobi8ebook:
        return [ "azw3", "kfx" ]

    if mimeType == applicationvndamazonebook:
        return [ "azw" ]

    if mimeType == imagevndairzipacceleratorazv:
        return [ "azv" ]

    if mimeType == applicationvndairzipfilesecureazs:
        return [ "azs" ]

    if mimeType == applicationvndairzipfilesecureazf:
        return [ "azf" ]

    if mimeType == videoannodex:
        return [ "axv" ]

    if mimeType == audioannodex:
        return [ "axa" ]

    if mimeType == applicationxawk:
        return [ "awk" ]

    if mimeType == audioamrwb:
        return [ "awb" ]

    if mimeType == applicationxapplixword:
        return [ "aw" ]

    if mimeType == imageavif:
        return [ "avif", "avifs" ]

    if mimeType == videovndavi:
        return [ "avi", "avf", "divx" ]

    if mimeType == imageavcs:
        return [ "avcs" ]

    if mimeType == imageavci:
        return [ "avci" ]

    if mimeType == textxsystemdunit:
        return [ "automount", "device", "mount", "path", "scope", "slice", "socket", "swap", "target", "timer" ]

    if mimeType == textxauthors:
        return [ "authors" ]

    if mimeType == audiobasic:
        return [ "au", "snd" ]

    if mimeType == applicationvndantixgamecomponent:
        return [ "atx" ]

    if mimeType == applicationatomsvc_xml:
        return [ "atomsvc" ]

    if mimeType == applicationatomdeleted_xml:
        return [ "atomdeleted" ]

    if mimeType == applicationatomcat_xml:
        return [ "atomcat" ]

    if mimeType == applicationatom_xml:
        return [ "atom" ]

    if mimeType == applicationvndacucorp:
        return [ "atc", "acutc" ]

    if mimeType == audioxmsasx:
        return [ "asx", "wax", "wvx", "wmx" ]

    if mimeType == imageastc:
        return [ "astc" ]

    if mimeType == applicationxasp:
        return [ "asp" ]

    if mimeType == applicationvndaccpacsimplyaso:
        return [ "aso" ]

    if mimeType == applicationvndmsasf:
        return [ "asf" ]

    if mimeType == textxcommonlisp:
        return [ "asd", "fasl", "lisp", "ros" ]

    if mimeType == applicationxasar:
        return [ "asar" ]

    if mimeType == applicationxapplixspreadsheet:
        return [ "as" ]

    if mimeType == imagexsonyarw:
        return [ "arw" ]

    if mimeType == applicationxarj:
        return [ "arj" ]

    if mimeType == applicationxfreearc:
        return [ "arc" ]

    if mimeType == applicationvndlotusapproach:
        return [ "apr" ]

    if mimeType == applicationappxbundle:
        return [ "appxbundle" ]

    if mimeType == applicationappx:
        return [ "appx" ]

    if mimeType == applicationxmsapplication:
        return [ "application" ]

    if mimeType == applicationappinstaller:
        return [ "appinstaller" ]

    if mimeType == applicationxiso9660appimage:
        return [ "appimage" ]

    if mimeType == imageapng:
        return [ "apng" ]

    if mimeType == applicationvndandroidpackagearchive:
        return [ "apk" ]

    if mimeType == audioxape:
        return [ "ape" ]

    if mimeType == applicationannodex:
        return [ "anx" ]

    if mimeType == videoxanim:
        return [ "anim19j" ]

    if mimeType == applicationxnavianimation:
        return [ "ani" ]

    if mimeType == audioxamzxml:
        return [ "amz" ]

    if mimeType == audioamr:
        return [ "amr" ]

    if mimeType == applicationautomationmlamlx_zip:
        return [ "amlx" ]

    if mimeType == applicationautomationmlaml_xml:
        return [ "aml" ]

    if mimeType == applicationvndamigaami:
        return [ "ami" ]

    if mimeType == applicationxalz:
        return [ "alz" ]

    if mimeType == applicationvnddvbait:
        return [ "ait" ]

    if mimeType == applicationvndadobeairapplicationinstallerpackage_zip:
        return [ "air" ]

    if mimeType == audioxaiff:
        return [ "aiff", "aif" ]

    if mimeType == audioxaifc:
        return [ "aifc", "aiffc" ]

    if mimeType == applicationillustrator:
        return [ "ai" ]

    if mimeType == applicationvndaheadspace:
        return [ "ahead" ]

    if mimeType == applicationvndage:
        return [ "age" ]

    if mimeType == imagexapplixgraphics:
        return [ "ag" ]

    if mimeType == applicationvndibmmodcap:
        return [ "afp", "listafp", "list3820" ]

    if mimeType == applicationxfontafm:
        return [ "afm" ]

    if mimeType == applicationvndaudiograph:
        return [ "aep" ]

    if mimeType == audioadpcm:
        return [ "adp" ]

    if mimeType == applicationxamigadiskformat:
        return [ "adf" ]

    if mimeType == textxadasrc:
        return [ "adb", "ads" ]

    if mimeType == applicationvndacucobol:
        return [ "acu" ]

    if mimeType == applicationxace:
        return [ "ace" ]

    if mimeType == applicationvndamericandynamicsacc:
        return [ "acc" ]

    if mimeType == audioac3:
        return [ "ac3" ]

    if mimeType == applicationpkixattrcert:
        return [ "ac" ]

    if mimeType == applicationxabiword:
        return [ "abw", "abwcrashed", "abwgz", "zabw" ]

    if mimeType == audiovndaudibleaaxc:
        return [ "aaxc" ]

    if mimeType == audiovndaudibleaax:
        return [ "aax" ]

    if mimeType == applicationxauthorwareseg:
        return [ "aas" ]

    if mimeType == applicationxauthorwaremap:
        return [ "aam" ]

    if mimeType == audioaac:
        return [ "aac", "adts" ]

    if mimeType == applicationxauthorwarebin:
        return [ "aab", "x32", "u32", "vox" ]

    if mimeType == audioxpnaudibleaudio:
        return [ "aa" ]

    if mimeType == applicationxatari7800rom:
        return [ "a78" ]

    if mimeType == applicationxatari2600rom:
        return [ "a26" ]

    if mimeType == applicationxarchive:
        return [ "a", "ar" ]

    if mimeType == applicationx7zcompressed:
        return [ "7z", "7z001" ]

    if mimeType == applicationxt602:
        return [ "602" ]

    if mimeType == model3mf:
        return [ "3mf" ]

    if mimeType == video3gpp:
        return [ "3gp", "3gpp", "3ga" ]

    if mimeType == video3gpp2:
        return [ "3g2", "3gp2", "3gpp2" ]

    if mimeType == applicationxnintendo3dsexecutable:
        return [ "3dsx" ]

    if mimeType == applicationxnintendo3dsrom:
        return [ "3ds", "cci" ]

    if mimeType == textvndin3d3dml:
        return [ "3dml" ]

    if mimeType == applicationxgenesis32xrom:
        return [ "32x", "mdx" ]

    if mimeType == applicationvnd1000mindsdecisionmodel_xml:
        return [ "1km" ]

    if mimeType == applicationvndlotus123:
        return [ "123", "wk1", "wk3", "wk4", "wks" ]
    
    return []

def getFileCategory(fileName):
    """
    Returns a file category for the given file name
    :param str fileName A file name, file extension or file path specification
    """
    extension = __getExt(fileName)
    if extension in (_7z, "7zip", ace, air, apk, "appxbundle", "arc", arj, "asec", "bar", bz2, "bzip", cab, "cso", deb, "dlc", dmg, gz, "gzip", hqx, "inv", "ipa", iso, "isz", jar, "msu", "nbh", pak, rar, rpm, sis, sisx, sit, "sitd", sitx, tar, targz, tgz, "webarchive", xap, z, zip):
        return FileCategory.Archive

    if extension in (_3ga, aac, aiff, amr, ape, "arf", asf, asx, "cda", "dvf", flac, "gp4", "gp5", gpx, "logic", m4a, m4b, "m4p", midi, mp3, ogg, "pcm", "rec", snd, "sng", "uax", wav, wma, wpl, "zab"):
        return FileCategory.Audio

    if extension in (_as, asm, asp, "aspx", bat, c, "cp", cpp, cs, css, "gradle", htm, "inc", jad, java, js, json, "jsp", "lib", m, "matlab", ml, o, perl, php, pl, "ps1", py, rb, "rc", rss, "scpt", sh, sql, src, "swift", "vb", "vbs", "ws", "xaml", "xcodeproj", xml, xsd, xsl, xslt, yml):
        return FileCategory.Code

    if extension in (abw, "aww", azw, "azw3", "azw4", cbr, cbz, chm, "cnt", "dbx", djvu, doc, docm, docx, dot, dotm, dotx, epub, fb2, "iba", "ibooks", "ind", "indd", "lit", mht, mobi, mpp, odf, odt, ott, "pages", pmd, "prn", "prproj", ps, pub, "pwi", rep, rtf, sdd, sdw, "shs", "snp", sxw, tpl, vsd, "wlmp", wpd, wps, wri):
        return FileCategory.Document

    if extension in (bmp, cpt, dds, dib, dng, "dt2", emf, gif, ico, "icon", icns, jpeg, jpg, pcx, pic, png, psd, "psdx", raw, tga, "thm", tif, tiff, wbmp, "wdp", webp):
        return FileCategory.Image

    if extension in (oxps, pdf, xps):
        return FileCategory.PDF

    if extension in (key, "keynote", pot, potx, pps, ppsx, ppt, pptm, pptx):
        return FileCategory.Presentation

    if extension in (ods, "numbers", sdc, xls, xlsx, xlsb):
        return FileCategory.Spreadsheet

    if extension in ("alx", application, csv, "eng", html, log, "lrc", "lst", nfo, opml, "plist", reg, srt, sub, "tbl", text, txt):
        return FileCategory.Text

    if extension in ("264", _3g2, _3gp, avi, "bik", "dash", "dat", "dvr", flv, h264, m2t, m2ts, m4v, mkv, mod, mov, mp4, mpeg, mpg, "mswmm", mts, ogv, rmvb, swf, "tod", "tp", ts, vob, webm, wmv):
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