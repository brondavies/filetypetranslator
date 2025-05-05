import os
from enum import Enum, unique, auto

#constants
_090909vdr = "090909vdr"
_123 = "123"
_19 = "19"
_1km = "1km"
_210 = "210"
_32x = "32x"
_3dml = "3dml"
_3ds = "3ds"
_3dsx = "3dsx"
_3g2 = "3g2"
_3ga = "3ga"
_3gp = "3gp"
_3gp2 = "3gp2"
_3gpp = "3gpp"
_3gpp2 = "3gpp2"
_3mf = "3mf"
_602 = "602"
_669 = "669"
_7z = "7z"
_7z001 = "7z001"
_as = "as"
_class = "class"
_def = "def"
_for = "for"
_in = "in"
_not = "not"
a = "a"
a26 = "a26"
a78 = "a78"
aa = "aa"
aab = "aab"
aac = "aac"
aam = "aam"
aas = "aas"
aax = "aax"
aaxc = "aaxc"
abw = "abw"
abwcrashed = "abwcrashed"
abwgz = "abwgz"
ac = "ac"
ac3 = "ac3"
acc = "acc"
ace = "ace"
acu = "acu"
acutc = "acutc"
adb = "adb"
adf = "adf"
adp = "adp"
ads = "ads"
adts = "adts"
aep = "aep"
afm = "afm"
afp = "afp"
ag = "ag"
agb = "agb"
age = "age"
ahead = "ahead"
ai = "ai"
aif = "aif"
aifc = "aifc"
aiff = "aiff"
aiffc = "aiffc"
air = "air"
ait = "ait"
al = "al"
alz = "alz"
ami = "ami"
aml = "aml"
amlx = "amlx"
amr = "amr"
amz = "amz"
ani = "ani"
anim19j = "anim19j"
anx = "anx"
ape = "ape"
apk = "apk"
apng = "apng"
appcache = "appcache"
appimage = "appimage"
appinstaller = "appinstaller"
application = "application"
applicationandrewinset = "application/andrew-inset"
applicationannodex = "application/annodex"
applicationappinstaller = "application/appinstaller"
applicationappx = "application/appx"
applicationappxbundle = "application/appxbundle"
applicationatom_xml = "application/atom+xml"
applicationatomcat_xml = "application/atomcat+xml"
applicationatomdeleted_xml = "application/atomdeleted+xml"
applicationatomsvc_xml = "application/atomsvc+xml"
applicationatscdwd_xml = "application/atsc-dwd+xml"
applicationatscheld_xml = "application/atsc-held+xml"
applicationatscrsat_xml = "application/atsc-rsat+xml"
applicationautomationmlaml_xml = "application/automationml-aml+xml"
applicationautomationmlamlx_zip = "application/automationml-amlx+zip"
applicationbdoc = "application/bdoc"
applicationbuildstream_yaml = "application/buildstream+yaml"
applicationcalendar_xml = "application/calendar+xml"
applicationcbor = "application/cbor"
applicationccxml_xml = "application/ccxml+xml"
applicationcdfx_xml = "application/cdfx+xml"
applicationcdmicapability = "application/cdmi-capability"
applicationcdmicontainer = "application/cdmi-container"
applicationcdmidomain = "application/cdmi-domain"
applicationcdmiobject = "application/cdmi-object"
applicationcdmiqueue = "application/cdmi-queue"
applicationcuseeme = "application/cu-seeme"
applicationcwl = "application/cwl"
applicationdash_xml = "application/dash+xml"
applicationdavmount_xml = "application/davmount+xml"
applicationdicom = "application/dicom"
applicationdocbook_xml = "application/docbook+xml"
applicationdssc_der = "application/dssc+der"
applicationdssc_xml = "application/dssc+xml"
applicationecmascript = "application/ecmascript"
applicationemma_xml = "application/emma+xml"
applicationemotionml_xml = "application/emotionml+xml"
applicationepub_zip = "application/epub+zip"
applicationexi = "application/exi"
applicationexpress = "application/express"
applicationfdf = "application/fdf"
applicationfdt_xml = "application/fdt+xml"
applicationfits = "application/fits"
applicationfonttdpfr = "application/font-tdpfr"
applicationgeo_json = "application/geo+json"
applicationgml_xml = "application/gml+xml"
applicationgnunetdirectory = "application/gnunet-directory"
applicationgpx_xml = "application/gpx+xml"
applicationgxf = "application/gxf"
applicationgzip = "application/gzip"
applicationhjson = "application/hjson"
applicationhta = "application/hta"
applicationhyperstudio = "application/hyperstudio"
applicationillustrator = "application/illustrator"
applicationinkml_xml = "application/inkml+xml"
applicationipfix = "application/ipfix"
applicationits_xml = "application/its+xml"
applicationjavaarchive = "application/java-archive"
applicationjavaserializedobject = "application/java-serialized-object"
applicationjrd_json = "application/jrd+json"
applicationjson = "application/json"
applicationjson5 = "application/json5"
applicationjsonml_json = "application/jsonml+json"
applicationjsonpatch_json = "application/json-patch+json"
applicationld_json = "application/ld+json"
applicationlgr_xml = "application/lgr+xml"
applicationlost_xml = "application/lost+xml"
applicationmacbinhex40 = "application/mac-binhex40"
applicationmaccompactpro = "application/mac-compactpro"
applicationmads_xml = "application/mads+xml"
applicationmanifest_json = "application/manifest+json"
applicationmarc = "application/marc"
applicationmarcxml_xml = "application/marcxml+xml"
applicationmathematica = "application/mathematica"
applicationmathml_xml = "application/mathml+xml"
applicationmbox = "application/mbox"
applicationmediapolicydataset_xml = "application/media-policy-dataset+xml"
applicationmediaservercontrol_xml = "application/mediaservercontrol+xml"
applicationmetalink_xml = "application/metalink+xml"
applicationmetalink4_xml = "application/metalink4+xml"
applicationmets_xml = "application/mets+xml"
applicationmicrosoftpatch = "application/microsoftpatch"
applicationmicrosoftupdate = "application/microsoftupdate"
applicationmmtaei_xml = "application/mmt-aei+xml"
applicationmmtusd_xml = "application/mmt-usd+xml"
applicationmods_xml = "application/mods+xml"
applicationmp21 = "application/mp21"
applicationmp4 = "application/mp4"
applicationmsix = "application/msix"
applicationmsixbundle = "application/msixbundle"
applicationmsword = "application/msword"
applicationmswordtemplate = "application/msword-template"
applicationmxf = "application/mxf"
applicationnquads = "application/n-quads"
applicationntriples = "application/n-triples"
applicationoctetstream = "application/octet-stream"
applicationoda = "application/oda"
applicationoebpspackage_xml = "application/oebps-package+xml"
applicationogg = "application/ogg"
applicationomdoc_xml = "application/omdoc+xml"
applicationonenote = "application/onenote"
applicationovf = "application/ovf"
applicationowl_xml = "application/owl+xml"
applicationoxps = "application/oxps"
applicationp2poverlay_xml = "application/p2p-overlay+xml"
applicationpatchopserror_xml = "application/patch-ops-error+xml"
applicationpdf = "application/pdf"
applicationpgpencrypted = "application/pgp-encrypted"
applicationpgpkeys = "application/pgp-keys"
applicationpgpsignature = "application/pgp-signature"
applicationpicsrules = "application/pics-rules"
applicationpkcs10 = "application/pkcs10"
applicationpkcs12 = "application/pkcs12"
applicationpkcs7mime = "application/pkcs7-mime"
applicationpkcs7signature = "application/pkcs7-signature"
applicationpkcs8 = "application/pkcs8"
applicationpkcs8encrypted = "application/pkcs8-encrypted"
applicationpkixattrcert = "application/pkix-attr-cert"
applicationpkixcert = "application/pkix-cert"
applicationpkixcmp = "application/pkixcmp"
applicationpkixcrl = "application/pkix-crl"
applicationpkixpkipath = "application/pkix-pkipath"
applicationpostscript = "application/postscript"
applicationprovenance_xml = "application/provenance+xml"
applicationprscww = "application/prs.cww"
applicationprsxsf_xml = "application/prs.xsf+xml"
applicationpskc_xml = "application/pskc+xml"
applicationram = "application/ram"
applicationraml_yaml = "application/raml+yaml"
applicationrdf_xml = "application/rdf+xml"
applicationreginfo_xml = "application/reginfo+xml"
applicationrelaxngcompactsyntax = "application/relax-ng-compact-syntax"
applicationresourcelists_xml = "application/resource-lists+xml"
applicationresourcelistsdiff_xml = "application/resource-lists-diff+xml"
applicationrouteapd_xml = "application/route-apd+xml"
applicationroutestsid_xml = "application/route-s-tsid+xml"
applicationrouteusd_xml = "application/route-usd+xml"
applicationrpkimanifest = "application/rpki-manifest"
applicationrpkiroa = "application/rpki-roa"
applicationrsd_xml = "application/rsd+xml"
applicationrss_xml = "application/rss+xml"
applicationrtf = "application/rtf"
applicationsbml_xml = "application/sbml+xml"
applicationscvpcvrequest = "application/scvp-cv-request"
applicationscvpcvresponse = "application/scvp-cv-response"
applicationscvpvprequest = "application/scvp-vp-request"
applicationscvpvpresponse = "application/scvp-vp-response"
applicationsenml_xml = "application/senml+xml"
applicationsensml_xml = "application/sensml+xml"
applicationsetpaymentinitiation = "application/set-payment-initiation"
applicationsetregistrationinitiation = "application/set-registration-initiation"
applicationshf_xml = "application/shf+xml"
applicationsieve = "application/sieve"
applicationsmil_xml = "application/smil+xml"
applicationsparqlquery = "application/sparql-query"
applicationsparqlresults_xml = "application/sparql-results+xml"
applicationsql = "application/sql"
applicationsrgs = "application/srgs"
applicationsrgs_xml = "application/srgs+xml"
applicationsru_xml = "application/sru+xml"
applicationssdl_xml = "application/ssdl+xml"
applicationssml_xml = "application/ssml+xml"
applicationswid_xml = "application/swid+xml"
applicationtei_xml = "application/tei+xml"
applicationthraud_xml = "application/thraud+xml"
applicationtimestampeddata = "application/timestamped-data"
applicationtoml = "application/toml"
applicationtrig = "application/trig"
applicationttml_xml = "application/ttml+xml"
applicationtypescript = "application/typescript"
applicationubjson = "application/ubjson"
applicationurcressheet_xml = "application/urc-ressheet+xml"
applicationurctargetdesc_xml = "application/urc-targetdesc+xml"
applicationvnd1000mindsdecisionmodel_xml = "application/vnd.1000minds.decision-model+xml"
applicationvnd3gpp2tcap = "application/vnd.3gpp2.tcap"
applicationvnd3gpppicbwlarge = "application/vnd.3gpp.pic-bw-large"
applicationvnd3gpppicbwsmall = "application/vnd.3gpp.pic-bw-small"
applicationvnd3gpppicbwvar = "application/vnd.3gpp.pic-bw-var"
applicationvnd3mpostitnotes = "application/vnd.3m.post-it-notes"
applicationvndaccpacsimplyaso = "application/vnd.accpac.simply.aso"
applicationvndaccpacsimplyimp = "application/vnd.accpac.simply.imp"
applicationvndacucobol = "application/vnd.acucobol"
applicationvndacucorp = "application/vnd.acucorp"
applicationvndadobeairapplicationinstallerpackage_zip = "application/vnd.adobe.air-application-installer-package+zip"
applicationvndadobeflashmovie = "application/vnd.adobe.flash.movie"
applicationvndadobeformscentralfcdt = "application/vnd.adobe.formscentral.fcdt"
applicationvndadobefxp = "application/vnd.adobe.fxp"
applicationvndadobexdp_xml = "application/vnd.adobe.xdp+xml"
applicationvndadobexfdf = "application/vnd.adobe.xfdf"
applicationvndage = "application/vnd.age"
applicationvndaheadspace = "application/vnd.ahead.space"
applicationvndairzipfilesecureazf = "application/vnd.airzip.filesecure.azf"
applicationvndairzipfilesecureazs = "application/vnd.airzip.filesecure.azs"
applicationvndamazonebook = "application/vnd.amazon.ebook"
applicationvndamazonmobi8ebook = "application/vnd.amazon.mobi8-ebook"
applicationvndamericandynamicsacc = "application/vnd.americandynamics.acc"
applicationvndamigaami = "application/vnd.amiga.ami"
applicationvndandroidpackagearchive = "application/vnd.android.package-archive"
applicationvndanserwebcertificateissueinitiation = "application/vnd.anser-web-certificate-issue-initiation"
applicationvndanserwebfundstransferinitiation = "application/vnd.anser-web-funds-transfer-initiation"
applicationvndantixgamecomponent = "application/vnd.antix.game-component"
applicationvndapacheparquet = "application/vnd.apache.parquet"
applicationvndappleinstaller_xml = "application/vnd.apple.installer+xml"
applicationvndapplenumbers = "application/vnd.apple.numbers"
applicationvndapplepages = "application/vnd.apple.pages"
applicationvndapplepkpass = "application/vnd.apple.pkpass"
applicationvndapplepkpasses = "application/vnd.apple.pkpasses"
applicationvndaristanetworksswi = "application/vnd.aristanetworks.swi"
applicationvndastraeasoftwareiota = "application/vnd.astraea-software.iota"
applicationvndaudiograph = "application/vnd.audiograph"
applicationvndautodeskfbx = "application/vnd.autodesk.fbx"
applicationvndbalsamiqbmml_xml = "application/vnd.balsamiq.bmml+xml"
applicationvndblueicemultipass = "application/vnd.blueice.multipass"
applicationvndbmi = "application/vnd.bmi"
applicationvndbusinessobjects = "application/vnd.businessobjects"
applicationvndchemdraw_xml = "application/vnd.chemdraw+xml"
applicationvndchesspgn = "application/vnd.chess-pgn"
applicationvndchipnutskaraokemmd = "application/vnd.chipnuts.karaoke-mmd"
applicationvndcinderella = "application/vnd.cinderella"
applicationvndcitationstylesstyle_xml = "application/vnd.citationstyles.style+xml"
applicationvndclaymore = "application/vnd.claymore"
applicationvndcloantorp9 = "application/vnd.cloanto.rp9"
applicationvndclonkc4group = "application/vnd.clonk.c4group"
applicationvndcluetrustcartomobileconfig = "application/vnd.cluetrust.cartomobile-config"
applicationvndcluetrustcartomobileconfigpkg = "application/vnd.cluetrust.cartomobile-config-pkg"
applicationvndcoffeescript = "application/vnd.coffeescript"
applicationvndcomicbook_zip = "application/vnd.comicbook+zip"
applicationvndcomicbookrar = "application/vnd.comicbook-rar"
applicationvndcommonspace = "application/vnd.commonspace"
applicationvndcontactcmsg = "application/vnd.contact.cmsg"
applicationvndcoreldraw = "application/vnd.corel-draw"
applicationvndcosmocaller = "application/vnd.cosmocaller"
applicationvndcrickclicker = "application/vnd.crick.clicker"
applicationvndcrickclickerkeyboard = "application/vnd.crick.clicker.keyboard"
applicationvndcrickclickerpalette = "application/vnd.crick.clicker.palette"
applicationvndcrickclickertemplate = "application/vnd.crick.clicker.template"
applicationvndcrickclickerwordbank = "application/vnd.crick.clicker.wordbank"
applicationvndcriticaltoolswbs_xml = "application/vnd.criticaltools.wbs+xml"
applicationvndctcposml = "application/vnd.ctc-posml"
applicationvndcupsppd = "application/vnd.cups-ppd"
applicationvndcurlcar = "application/vnd.curl.car"
applicationvndcurlpcurl = "application/vnd.curl.pcurl"
applicationvnddart = "application/vnd.dart"
applicationvnddatavisionrdz = "application/vnd.data-vision.rdz"
applicationvnddbf = "application/vnd.dbf"
applicationvnddcmp_xml = "application/vnd.dcmp+xml"
applicationvnddebianbinarypackage = "application/vnd.debian.binary-package"
applicationvnddecedata = "application/vnd.dece.data"
applicationvnddecettml_xml = "application/vnd.dece.ttml+xml"
applicationvnddeceunspecified = "application/vnd.dece.unspecified"
applicationvnddecezip = "application/vnd.dece.zip"
applicationvnddenovofcselayoutlink = "application/vnd.denovo.fcselayout-link"
applicationvnddna = "application/vnd.dna"
applicationvnddolbymlp = "application/vnd.dolby.mlp"
applicationvnddpgraph = "application/vnd.dpgraph"
applicationvnddreamfactory = "application/vnd.dreamfactory"
applicationvnddskeypoint = "application/vnd.ds-keypoint"
applicationvnddvbait = "application/vnd.dvb.ait"
applicationvnddvbservice = "application/vnd.dvb.service"
applicationvnddynageo = "application/vnd.dynageo"
applicationvndecowinchart = "application/vnd.ecowin.chart"
applicationvndefiimg = "application/vnd.efi.img"
applicationvndefiiso = "application/vnd.efi.iso"
applicationvndemusicemusic_package = "application/vnd.emusic-emusic_package"
applicationvndenliven = "application/vnd.enliven"
applicationvndepsonesf = "application/vnd.epson.esf"
applicationvndepsonmsf = "application/vnd.epson.msf"
applicationvndepsonquickanime = "application/vnd.epson.quickanime"
applicationvndepsonsalt = "application/vnd.epson.salt"
applicationvndepsonssf = "application/vnd.epson.ssf"
applicationvndeszigno3_xml = "application/vnd.eszigno3+xml"
applicationvndezpixalbum = "application/vnd.ezpix-album"
applicationvndezpixpackage = "application/vnd.ezpix-package"
applicationvndfdsnmseed = "application/vnd.fdsn.mseed"
applicationvndfdsnseed = "application/vnd.fdsn.seed"
applicationvndflatpak = "application/vnd.flatpak"
applicationvndflatpakref = "application/vnd.flatpak.ref"
applicationvndflatpakrepo = "application/vnd.flatpak.repo"
applicationvndflographit = "application/vnd.flographit"
applicationvndfluxtimeclip = "application/vnd.fluxtime.clip"
applicationvndframemaker = "application/vnd.framemaker"
applicationvndfrogansfnc = "application/vnd.frogans.fnc"
applicationvndfrogansltf = "application/vnd.frogans.ltf"
applicationvndfscweblaunch = "application/vnd.fsc.weblaunch"
applicationvndfujitsuoasys = "application/vnd.fujitsu.oasys"
applicationvndfujitsuoasys2 = "application/vnd.fujitsu.oasys2"
applicationvndfujitsuoasys3 = "application/vnd.fujitsu.oasys3"
applicationvndfujitsuoasysgp = "application/vnd.fujitsu.oasysgp"
applicationvndfujitsuoasysprs = "application/vnd.fujitsu.oasysprs"
applicationvndfujixeroxddd = "application/vnd.fujixerox.ddd"
applicationvndfujixeroxdocuworks = "application/vnd.fujixerox.docuworks"
applicationvndfujixeroxdocuworksbinder = "application/vnd.fujixerox.docuworks.binder"
applicationvndfuzzysheet = "application/vnd.fuzzysheet"
applicationvndgenomatixtuxedo = "application/vnd.genomatix.tuxedo"
applicationvndgeogebrafile = "application/vnd.geogebra.file"
applicationvndgeogebraslides = "application/vnd.geogebra.slides"
applicationvndgeogebratool = "application/vnd.geogebra.tool"
applicationvndgeometryexplorer = "application/vnd.geometry-explorer"
applicationvndgeonext = "application/vnd.geonext"
applicationvndgeoplan = "application/vnd.geoplan"
applicationvndgeospace = "application/vnd.geospace"
applicationvndgmx = "application/vnd.gmx"
applicationvndgoogleappsdocument = "application/vnd.google-apps.document"
applicationvndgoogleappsdrawing = "application/vnd.google-apps.drawing"
applicationvndgoogleappsform = "application/vnd.google-apps.form"
applicationvndgoogleappsjam = "application/vnd.google-apps.jam"
applicationvndgoogleappsmap = "application/vnd.google-apps.map"
applicationvndgoogleappspresentation = "application/vnd.google-apps.presentation"
applicationvndgoogleappsscript = "application/vnd.google-apps.script"
applicationvndgoogleappssite = "application/vnd.google-apps.site"
applicationvndgoogleappsspreadsheet = "application/vnd.google-apps.spreadsheet"
applicationvndgoogleearthkml_xml = "application/vnd.google-earth.kml+xml"
applicationvndgoogleearthkmz = "application/vnd.google-earth.kmz"
applicationvndgovskxmldatacontainer_xml = "application/vnd.gov.sk.xmldatacontainer+xml"
applicationvndgrafeq = "application/vnd.grafeq"
applicationvndgrooveaccount = "application/vnd.groove-account"
applicationvndgroovehelp = "application/vnd.groove-help"
applicationvndgrooveidentitymessage = "application/vnd.groove-identity-message"
applicationvndgrooveinjector = "application/vnd.groove-injector"
applicationvndgroovetoolmessage = "application/vnd.groove-tool-message"
applicationvndgroovetooltemplate = "application/vnd.groove-tool-template"
applicationvndgroovevcard = "application/vnd.groove-vcard"
applicationvndhal_xml = "application/vnd.hal+xml"
applicationvndhandheldentertainment_xml = "application/vnd.handheld-entertainment+xml"
applicationvndhbci = "application/vnd.hbci"
applicationvndhhelessonplayer = "application/vnd.hhe.lesson-player"
applicationvndhphpgl = "application/vnd.hp-hpgl"
applicationvndhphpid = "application/vnd.hp-hpid"
applicationvndhphps = "application/vnd.hp-hps"
applicationvndhpjlyt = "application/vnd.hp-jlyt"
applicationvndhppcl = "application/vnd.hp-pcl"
applicationvndhppclxl = "application/vnd.hp-pclxl"
applicationvndhydrostatixsofdata = "application/vnd.hydrostatix.sof-data"
applicationvndibmminipay = "application/vnd.ibm.minipay"
applicationvndibmmodcap = "application/vnd.ibm.modcap"
applicationvndibmrightsmanagement = "application/vnd.ibm.rights-management"
applicationvndiccprofile = "application/vnd.iccprofile"
applicationvndigloader = "application/vnd.igloader"
applicationvndimmervisionivp = "application/vnd.immervision-ivp"
applicationvndimmervisionivu = "application/vnd.immervision-ivu"
applicationvndinsorsigm = "application/vnd.insors.igm"
applicationvndinterconformnet = "application/vnd.intercon.formnet"
applicationvndintergeo = "application/vnd.intergeo"
applicationvndintuqbo = "application/vnd.intu.qbo"
applicationvndintuqfx = "application/vnd.intu.qfx"
applicationvndipunpluggedrcprofile = "application/vnd.ipunplugged.rcprofile"
applicationvndirepositorypackage_xml = "application/vnd.irepository.package+xml"
applicationvndisacfcs = "application/vnd.isac.fcs"
applicationvndisxpr = "application/vnd.is-xpr"
applicationvndjam = "application/vnd.jam"
applicationvndjisp = "application/vnd.jisp"
applicationvndjoostjodaarchive = "application/vnd.joost.joda-archive"
applicationvndkahootz = "application/vnd.kahootz"
applicationvndkenameaapp = "application/vnd.kenameaapp"
applicationvndkidspiration = "application/vnd.kidspiration"
applicationvndkinar = "application/vnd.kinar"
applicationvndkoan = "application/vnd.koan"
applicationvndkodakdescriptor = "application/vnd.kodak-descriptor"
applicationvndlaslas_xml = "application/vnd.las.las+xml"
applicationvndllamagraphicslifebalancedesktop = "application/vnd.llamagraphics.life-balance.desktop"
applicationvndllamagraphicslifebalanceexchange_xml = "application/vnd.llamagraphics.life-balance.exchange+xml"
applicationvndlotus123 = "application/vnd.lotus-1-2-3"
applicationvndlotusapproach = "application/vnd.lotus-approach"
applicationvndlotusfreelance = "application/vnd.lotus-freelance"
applicationvndlotusnotes = "application/vnd.lotus-notes"
applicationvndlotuswordpro = "application/vnd.lotus-wordpro"
applicationvndmacportsportpkg = "application/vnd.macports.portpkg"
applicationvndmapboxvectortile = "application/vnd.mapbox-vector-tile"
applicationvndmcd = "application/vnd.mcd"
applicationvndmedcalcdata = "application/vnd.medcalcdata"
applicationvndmediastationcdkey = "application/vnd.mediastation.cdkey"
applicationvndmfer = "application/vnd.mfer"
applicationvndmfmp = "application/vnd.mfmp"
applicationvndmicrografxflo = "application/vnd.micrografx.flo"
applicationvndmicrografxigx = "application/vnd.micrografx.igx"
applicationvndmicrosoftportableexecutable = "application/vnd.microsoft.portable-executable"
applicationvndmicrosoftwindowsthumbnailcache = "application/vnd.microsoft.windows.thumbnail-cache"
applicationvndmobiusdaf = "application/vnd.mobius.daf"
applicationvndmobiusdis = "application/vnd.mobius.dis"
applicationvndmobiusmbk = "application/vnd.mobius.mbk"
applicationvndmobiusmqy = "application/vnd.mobius.mqy"
applicationvndmobiusmsl = "application/vnd.mobius.msl"
applicationvndmobiusplc = "application/vnd.mobius.plc"
applicationvndmobiustxf = "application/vnd.mobius.txf"
applicationvndmophunapplication = "application/vnd.mophun.application"
applicationvndmozillaxul_xml = "application/vnd.mozilla.xul+xml"
applicationvndmsartgalry = "application/vnd.ms-artgalry"
applicationvndmsasf = "application/vnd.ms-asf"
applicationvndmscabcompressed = "application/vnd.ms-cab-compressed"
applicationvndmseq = "application/vnd.mseq"
applicationvndmsexcel = "application/vnd.ms-excel"
applicationvndmsexceladdinmacroenabled12 = "application/vnd.ms-excel.addin.macroenabled.12"
applicationvndmsexcelsheetbinarymacroenabled12 = "application/vnd.ms-excel.sheet.binary.macroenabled.12"
applicationvndmsexcelsheetmacroenabled12 = "application/vnd.ms-excel.sheet.macroenabled.12"
applicationvndmsexceltemplatemacroenabled12 = "application/vnd.ms-excel.template.macroenabled.12"
applicationvndmsfontobject = "application/vnd.ms-fontobject"
applicationvndmshtmlhelp = "application/vnd.ms-htmlhelp"
applicationvndmsims = "application/vnd.ms-ims"
applicationvndmslrm = "application/vnd.ms-lrm"
applicationvndmsofficetheme = "application/vnd.ms-officetheme"
applicationvndmsoutlook = "application/vnd.ms-outlook"
applicationvndmspkiseccat = "application/vnd.ms-pki.seccat"
applicationvndmspowerpoint = "application/vnd.ms-powerpoint"
applicationvndmspowerpointaddinmacroenabled12 = "application/vnd.ms-powerpoint.addin.macroenabled.12"
applicationvndmspowerpointpresentationmacroenabled12 = "application/vnd.ms-powerpoint.presentation.macroenabled.12"
applicationvndmspowerpointslidemacroenabled12 = "application/vnd.ms-powerpoint.slide.macroenabled.12"
applicationvndmspowerpointslideshowmacroenabled12 = "application/vnd.ms-powerpoint.slideshow.macroenabled.12"
applicationvndmspowerpointtemplatemacroenabled12 = "application/vnd.ms-powerpoint.template.macroenabled.12"
applicationvndmsproject = "application/vnd.ms-project"
applicationvndmspublisher = "application/vnd.ms-publisher"
applicationvndmstnef = "application/vnd.ms-tnef"
applicationvndmsvisiodrawingmacroenabledmain_xml = "application/vnd.ms-visio.drawing.macroenabled.main+xml"
applicationvndmsvisiodrawingmain_xml = "application/vnd.ms-visio.drawing.main+xml"
applicationvndmsvisiostencilmacroenabledmain_xml = "application/vnd.ms-visio.stencil.macroenabled.main+xml"
applicationvndmsvisiostencilmain_xml = "application/vnd.ms-visio.stencil.main+xml"
applicationvndmsvisiotemplatemacroenabledmain_xml = "application/vnd.ms-visio.template.macroenabled.main+xml"
applicationvndmsvisiotemplatemain_xml = "application/vnd.ms-visio.template.main+xml"
applicationvndmsvisioviewer = "application/vnd.ms-visio.viewer"
applicationvndmsworddocumentmacroenabled12 = "application/vnd.ms-word.document.macroenabled.12"
applicationvndmswordtemplatemacroenabled12 = "application/vnd.ms-word.template.macroenabled.12"
applicationvndmsworks = "application/vnd.ms-works"
applicationvndmswpl = "application/vnd.ms-wpl"
applicationvndmsxpsdocument = "application/vnd.ms-xpsdocument"
applicationvndmusician = "application/vnd.musician"
applicationvndmuveestyle = "application/vnd.muvee.style"
applicationvndmynfc = "application/vnd.mynfc"
applicationvndnatobindingdataobject_xml = "application/vnd.nato.bindingdataobject+xml"
applicationvndneurolanguagenlu = "application/vnd.neurolanguage.nlu"
applicationvndnintendosnesrom = "application/vnd.nintendo.snes.rom"
applicationvndnitf = "application/vnd.nitf"
applicationvndnoblenetdirectory = "application/vnd.noblenet-directory"
applicationvndnoblenetsealer = "application/vnd.noblenet-sealer"
applicationvndnoblenetweb = "application/vnd.noblenet-web"
applicationvndnokiangagedata = "application/vnd.nokia.n-gage.data"
applicationvndnokiangagesymbianinstall = "application/vnd.nokia.n-gage.symbian.install"
applicationvndnokiaradiopreset = "application/vnd.nokia.radio-preset"
applicationvndnokiaradiopresets = "application/vnd.nokia.radio-presets"
applicationvndnovadigmedm = "application/vnd.novadigm.edm"
applicationvndnovadigmedx = "application/vnd.novadigm.edx"
applicationvndnovadigmext = "application/vnd.novadigm.ext"
applicationvndoasisopendocumentbase = "application/vnd.oasis.opendocument.base"
applicationvndoasisopendocumentchart = "application/vnd.oasis.opendocument.chart"
applicationvndoasisopendocumentcharttemplate = "application/vnd.oasis.opendocument.chart-template"
applicationvndoasisopendocumentformula = "application/vnd.oasis.opendocument.formula"
applicationvndoasisopendocumentformulatemplate = "application/vnd.oasis.opendocument.formula-template"
applicationvndoasisopendocumentgraphics = "application/vnd.oasis.opendocument.graphics"
applicationvndoasisopendocumentgraphicsflatxml = "application/vnd.oasis.opendocument.graphics-flat-xml"
applicationvndoasisopendocumentgraphicstemplate = "application/vnd.oasis.opendocument.graphics-template"
applicationvndoasisopendocumentimage = "application/vnd.oasis.opendocument.image"
applicationvndoasisopendocumentimagetemplate = "application/vnd.oasis.opendocument.image-template"
applicationvndoasisopendocumentpresentation = "application/vnd.oasis.opendocument.presentation"
applicationvndoasisopendocumentpresentationflatxml = "application/vnd.oasis.opendocument.presentation-flat-xml"
applicationvndoasisopendocumentpresentationtemplate = "application/vnd.oasis.opendocument.presentation-template"
applicationvndoasisopendocumentspreadsheet = "application/vnd.oasis.opendocument.spreadsheet"
applicationvndoasisopendocumentspreadsheetflatxml = "application/vnd.oasis.opendocument.spreadsheet-flat-xml"
applicationvndoasisopendocumentspreadsheettemplate = "application/vnd.oasis.opendocument.spreadsheet-template"
applicationvndoasisopendocumenttext = "application/vnd.oasis.opendocument.text"
applicationvndoasisopendocumenttextflatxml = "application/vnd.oasis.opendocument.text-flat-xml"
applicationvndoasisopendocumenttextmaster = "application/vnd.oasis.opendocument.text-master"
applicationvndoasisopendocumenttextmastertemplate = "application/vnd.oasis.opendocument.text-master-template"
applicationvndoasisopendocumenttexttemplate = "application/vnd.oasis.opendocument.text-template"
applicationvndoasisopendocumenttextweb = "application/vnd.oasis.opendocument.text-web"
applicationvndolpcsugar = "application/vnd.olpc-sugar"
applicationvndomadd2_xml = "application/vnd.oma.dd2+xml"
applicationvndopenbloxgame_xml = "application/vnd.openblox.game+xml"
applicationvndopenofficeorgextension = "application/vnd.openofficeorg.extension"
applicationvndopenstreetmapdata_xml = "application/vnd.openstreetmap.data+xml"
applicationvndopenxmlformatsofficedocumentpresentationmlpresentation = "application/vnd.openxmlformats-officedocument.presentationml.presentation"
applicationvndopenxmlformatsofficedocumentpresentationmlslide = "application/vnd.openxmlformats-officedocument.presentationml.slide"
applicationvndopenxmlformatsofficedocumentpresentationmlslideshow = "application/vnd.openxmlformats-officedocument.presentationml.slideshow"
applicationvndopenxmlformatsofficedocumentpresentationmltemplate = "application/vnd.openxmlformats-officedocument.presentationml.template"
applicationvndopenxmlformatsofficedocumentspreadsheetmlsheet = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
applicationvndopenxmlformatsofficedocumentspreadsheetmltemplate = "application/vnd.openxmlformats-officedocument.spreadsheetml.template"
applicationvndopenxmlformatsofficedocumentwordprocessingmldocument = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
applicationvndopenxmlformatsofficedocumentwordprocessingmltemplate = "application/vnd.openxmlformats-officedocument.wordprocessingml.template"
applicationvndosgidp = "application/vnd.osgi.dp"
applicationvndosgisubsystem = "application/vnd.osgi.subsystem"
applicationvndpalm = "application/vnd.palm"
applicationvndpawaafile = "application/vnd.pawaafile"
applicationvndpgformat = "application/vnd.pg.format"
applicationvndpgosasli = "application/vnd.pg.osasli"
applicationvndpicsel = "application/vnd.picsel"
applicationvndpmiwidget = "application/vnd.pmi.widget"
applicationvndpocketlearn = "application/vnd.pocketlearn"
applicationvndpowerbuilder6 = "application/vnd.powerbuilder6"
applicationvndpreviewsystemsbox = "application/vnd.previewsystems.box"
applicationvndprocratebrushset = "application/vnd.procrate.brushset"
applicationvndprocreatebrush = "application/vnd.procreate.brush"
applicationvndprocreatedream = "application/vnd.procreate.dream"
applicationvndproteusmagazine = "application/vnd.proteus.magazine"
applicationvndpublisharedeltatree = "application/vnd.publishare-delta-tree"
applicationvndpviptid1 = "application/vnd.pvi.ptid1"
applicationvndpwgxhtmlprint_xml = "application/vnd.pwg-xhtml-print+xml"
applicationvndquarkquarkxpress = "application/vnd.quark.quarkxpress"
applicationvndrar = "application/vnd.rar"
applicationvndrealvncbed = "application/vnd.realvnc.bed"
applicationvndrecordaremusicxml = "application/vnd.recordare.musicxml"
applicationvndrecordaremusicxml_xml = "application/vnd.recordare.musicxml+xml"
applicationvndrigcryptonote = "application/vnd.rig.cryptonote"
applicationvndrimcod = "application/vnd.rim.cod"
applicationvndrnrealmedia = "application/vnd.rn-realmedia"
applicationvndroute66link66_xml = "application/vnd.route66.link66+xml"
applicationvndsailingtrackertrack = "application/vnd.sailingtracker.track"
applicationvndseemail = "application/vnd.seemail"
applicationvndsema = "application/vnd.sema"
applicationvndsemd = "application/vnd.semd"
applicationvndsemf = "application/vnd.semf"
applicationvndshanainformedformdata = "application/vnd.shana.informed.formdata"
applicationvndshanainformedformtemplate = "application/vnd.shana.informed.formtemplate"
applicationvndshanainformedinterchange = "application/vnd.shana.informed.interchange"
applicationvndshanainformedpackage = "application/vnd.shana.informed.package"
applicationvndsimtechmindmapper = "application/vnd.simtech-mindmapper"
applicationvndsmaf = "application/vnd.smaf"
applicationvndsmartteacher = "application/vnd.smart.teacher"
applicationvndsnap = "application/vnd.snap"
applicationvndsolentsdkm_xml = "application/vnd.solent.sdkm+xml"
applicationvndspotfiredxp = "application/vnd.spotfire.dxp"
applicationvndsqlite3 = "application/vnd.sqlite3"
applicationvndsquashfs = "application/vnd.squashfs"
applicationvndstardivisionimpresspacked = "application/vnd.stardivision.impress-packed"
applicationvndstardivisionmail = "application/vnd.stardivision.mail"
applicationvndstepmaniapackage = "application/vnd.stepmania.package"
applicationvndstepmaniastepchart = "application/vnd.stepmania.stepchart"
applicationvndsunwadl_xml = "application/vnd.sun.wadl+xml"
applicationvndsunxmlcalc = "application/vnd.sun.xml.calc"
applicationvndsunxmlcalctemplate = "application/vnd.sun.xml.calc.template"
applicationvndsunxmldraw = "application/vnd.sun.xml.draw"
applicationvndsunxmldrawtemplate = "application/vnd.sun.xml.draw.template"
applicationvndsunxmlimpress = "application/vnd.sun.xml.impress"
applicationvndsunxmlimpresstemplate = "application/vnd.sun.xml.impress.template"
applicationvndsunxmlmath = "application/vnd.sun.xml.math"
applicationvndsunxmlwriter = "application/vnd.sun.xml.writer"
applicationvndsunxmlwriterglobal = "application/vnd.sun.xml.writer.global"
applicationvndsunxmlwritertemplate = "application/vnd.sun.xml.writer.template"
applicationvndsuscalendar = "application/vnd.sus-calendar"
applicationvndsvd = "application/vnd.svd"
applicationvndsymbianinstall = "application/vnd.symbian.install"
applicationvndsyncml_xml = "application/vnd.syncml+xml"
applicationvndsyncmldm_xml = "application/vnd.syncml.dm+xml"
applicationvndsyncmldmddf_xml = "application/vnd.syncml.dmddf+xml"
applicationvndtaointentmodulearchive = "application/vnd.tao.intent-module-archive"
applicationvndtcpdumppcap = "application/vnd.tcpdump.pcap"
applicationvndtmobilelivetv = "application/vnd.tmobile-livetv"
applicationvndtridtpt = "application/vnd.trid.tpt"
applicationvndtriscapemxs = "application/vnd.triscape.mxs"
applicationvndtrueapp = "application/vnd.trueapp"
applicationvndufdl = "application/vnd.ufdl"
applicationvnduiqtheme = "application/vnd.uiq.theme"
applicationvndumajin = "application/vnd.umajin"
applicationvndunity = "application/vnd.unity"
applicationvnduoml_xml = "application/vnd.uoml+xml"
applicationvndvcx = "application/vnd.vcx"
applicationvndvisio = "application/vnd.visio"
applicationvndvisionary = "application/vnd.visionary"
applicationvndvsf = "application/vnd.vsf"
applicationvndwapwbxml = "application/vnd.wap.wbxml"
applicationvndwapwmlc = "application/vnd.wap.wmlc"
applicationvndwapwmlscriptc = "application/vnd.wap.wmlscriptc"
applicationvndwebturbo = "application/vnd.webturbo"
applicationvndwolframplayer = "application/vnd.wolfram.player"
applicationvndwordperfect = "application/vnd.wordperfect"
applicationvndwqd = "application/vnd.wqd"
applicationvndwtstf = "application/vnd.wt.stf"
applicationvndxfdl = "application/vnd.xfdl"
applicationvndyamahahvdic = "application/vnd.yamaha.hv-dic"
applicationvndyamahahvscript = "application/vnd.yamaha.hv-script"
applicationvndyamahahvvoice = "application/vnd.yamaha.hv-voice"
applicationvndyamahaopenscoreformat = "application/vnd.yamaha.openscoreformat"
applicationvndyamahaopenscoreformatosfpvg_xml = "application/vnd.yamaha.openscoreformat.osfpvg+xml"
applicationvndyamahasmafaudio = "application/vnd.yamaha.smaf-audio"
applicationvndyamahasmafphrase = "application/vnd.yamaha.smaf-phrase"
applicationvndyellowrivercustommenu = "application/vnd.yellowriver-custom-menu"
applicationvndzul = "application/vnd.zul"
applicationvndzzazzdeck_xml = "application/vnd.zzazz.deck+xml"
applicationvoicexml_xml = "application/voicexml+xml"
applicationwasm = "application/wasm"
applicationwatcherinfo_xml = "application/watcherinfo+xml"
applicationwidget = "application/widget"
applicationwinhlp = "application/winhlp"
applicationwsdl_xml = "application/wsdl+xml"
applicationwspolicy_xml = "application/wspolicy+xml"
applicationx7zcompressed = "application/x-7z-compressed"
applicationxabiword = "application/x-abiword"
applicationxace = "application/x-ace"
applicationxalz = "application/x-alz"
applicationxamigadiskformat = "application/x-amiga-disk-format"
applicationxamipro = "application/x-amipro"
applicationxaml_xml = "application/xaml+xml"
applicationxaportisdoc = "application/x-aportisdoc"
applicationxapplediskimage = "application/x-apple-diskimage"
applicationxapplesystemprofiler_xml = "application/x-apple-systemprofiler+xml"
applicationxappleworksdocument = "application/x-appleworks-document"
applicationxapplixspreadsheet = "application/x-applix-spreadsheet"
applicationxapplixword = "application/x-applix-word"
applicationxarchive = "application/x-archive"
applicationxarj = "application/x-arj"
applicationxasar = "application/x-asar"
applicationxasp = "application/x-asp"
applicationxatari2600rom = "application/x-atari-2600-rom"
applicationxatari7800rom = "application/x-atari-7800-rom"
applicationxatarilynxrom = "application/x-atari-lynx-rom"
applicationxauthorwarebin = "application/x-authorware-bin"
applicationxauthorwaremap = "application/x-authorware-map"
applicationxauthorwareseg = "application/x-authorware-seg"
applicationxawk = "application/x-awk"
applicationxbat = "application/x-bat"
applicationxbcpio = "application/x-bcpio"
applicationxbittorrent = "application/x-bittorrent"
applicationxblender = "application/x-blender"
applicationxblorb = "application/x-blorb"
applicationxbpspatch = "application/x-bps-patch"
applicationxbsdiff = "application/x-bsdiff"
applicationxbzdvi = "application/x-bzdvi"
applicationxbzip1 = "application/x-bzip1"
applicationxbzip1compressedtar = "application/x-bzip1-compressed-tar"
applicationxbzip2 = "application/x-bzip2"
applicationxbzip2compressedtar = "application/x-bzip2-compressed-tar"
applicationxbzip3 = "application/x-bzip3"
applicationxbzip3compressedtar = "application/x-bzip3-compressed-tar"
applicationxbzpdf = "application/x-bzpdf"
applicationxbzpostscript = "application/x-bzpostscript"
applicationxcapatt_xml = "application/xcap-att+xml"
applicationxcapcaps_xml = "application/xcap-caps+xml"
applicationxcapdiff_xml = "application/xcap-diff+xml"
applicationxcapel_xml = "application/xcap-el+xml"
applicationxcapns_xml = "application/xcap-ns+xml"
applicationxcb7 = "application/x-cb7"
applicationxcbr = "application/x-cbr"
applicationxcbt = "application/x-cbt"
applicationxccmx = "application/x-ccmx"
applicationxcdlink = "application/x-cdlink"
applicationxcdrdaotoc = "application/x-cdrdao-toc"
applicationxcfscompressed = "application/x-cfs-compressed"
applicationxchat = "application/x-chat"
applicationxchromeextension = "application/x-chrome-extension"
applicationxcocoa = "application/x-cocoa"
applicationxcompress = "application/x-compress"
applicationxcompressediso = "application/x-compressed-iso"
applicationxcompressedtar = "application/x-compressed-tar"
applicationxcore = "application/x-core"
applicationxcpio = "application/x-cpio"
applicationxcpiocompressed = "application/x-cpio-compressed"
applicationxcsh = "application/x-csh"
applicationxcue = "application/x-cue"
applicationxdar = "application/x-dar"
applicationxdesigner = "application/x-designer"
applicationxdesktop = "application/x-desktop"
applicationxdgccompressed = "application/x-dgc-compressed"
applicationxdiadiagram = "application/x-dia-diagram"
applicationxdiashape = "application/x-dia-shape"
applicationxdirector = "application/x-director"
applicationxdiscjugglercdimage = "application/x-discjuggler-cd-image"
applicationxdtbncx_xml = "application/x-dtbncx+xml"
applicationxdvi = "application/x-dvi"
applicationxegon = "application/x-egon"
applicationxenc_xml = "application/xenc+xml"
applicationxenvoy = "application/x-envoy"
applicationxerislink_cbor = "application/x-eris-link+cbor"
applicationxetheme = "application/x-e-theme"
applicationxeva = "application/x-eva"
applicationxexcellon = "application/x-excellon"
applicationxfdsdisk = "application/x-fds-disk"
applicationxfictionbook_xml = "application/x-fictionbook+xml"
applicationxfishscript = "application/x-fishscript"
applicationxfluid = "application/x-fluid"
applicationxfontafm = "application/x-font-afm"
applicationxfontbdf = "application/x-font-bdf"
applicationxfontlinuxpsf = "application/x-font-linux-psf"
applicationxfontpcf = "application/x-font-pcf"
applicationxfontsnf = "application/x-font-snf"
applicationxfontspeedo = "application/x-font-speedo"
applicationxfontttx = "application/x-font-ttx"
applicationxfonttype1 = "application/x-font-type1"
applicationxfreearc = "application/x-freearc"
applicationxgameboycolorrom = "application/x-gameboy-color-rom"
applicationxgameboyrom = "application/x-gameboy-rom"
applicationxgamegearrom = "application/x-gamegear-rom"
applicationxgbarom = "application/x-gba-rom"
applicationxgcacompressed = "application/x-gca-compressed"
applicationxgdromcue = "application/x-gd-rom-cue"
applicationxgdscript = "application/x-gdscript"
applicationxgenesis32xrom = "application/x-genesis-32x-rom"
applicationxgenesisrom = "application/x-genesis-rom"
applicationxgerberjob = "application/x-gerber-job"
applicationxgettexttranslation = "application/x-gettext-translation"
applicationxglade = "application/x-glade"
applicationxglulx = "application/x-glulx"
applicationxgnucash = "application/x-gnucash"
applicationxgnumeric = "application/x-gnumeric"
applicationxgnuplot = "application/x-gnuplot"
applicationxgodotproject = "application/x-godot-project"
applicationxgodotresource = "application/x-godot-resource"
applicationxgodotscene = "application/x-godot-scene"
applicationxgodotshader = "application/x-godot-shader"
applicationxgosgf = "application/x-go-sgf"
applicationxgrampsxml = "application/x-gramps-xml"
applicationxgraphite = "application/x-graphite"
applicationxgzdvi = "application/x-gzdvi"
applicationxgzfontlinuxpsf = "application/x-gz-font-linux-psf"
applicationxgzpdf = "application/x-gzpdf"
applicationxgzpostscript = "application/x-gzpostscript"
applicationxhdf = "application/x-hdf"
applicationxhfefloppyimage = "application/x-hfe-floppy-image"
applicationxhtml_xml = "application/xhtml+xml"
applicationxhwp = "application/x-hwp"
applicationxhwt = "application/x-hwt"
applicationxica = "application/x-ica"
applicationxipspatch = "application/x-ips-patch"
applicationxipynb_json = "application/x-ipynb+json"
applicationxiso9660appimage = "application/x-iso9660-appimage"
applicationxit87 = "application/x-it87"
applicationxjava = "application/x-java"
applicationxjavaarchivediff = "application/x-java-archive-diff"
applicationxjavajcekeystore = "application/x-java-jce-keystore"
applicationxjavajnlpfile = "application/x-java-jnlp-file"
applicationxjavakeystore = "application/x-java-keystore"
applicationxjavapack200 = "application/x-java-pack200"
applicationxjbuilderproject = "application/x-jbuilder-project"
applicationxkarbon = "application/x-karbon"
applicationxkchart = "application/x-kchart"
applicationxkeepass2 = "application/x-keepass2"
applicationxkexiconnectiondata = "application/x-kexi-connectiondata"
applicationxkexiprojectshortcut = "application/x-kexiproject-shortcut"
applicationxkexiprojectsqlite2 = "application/x-kexiproject-sqlite2"
applicationxkformula = "application/x-kformula"
applicationxkillustrator = "application/x-killustrator"
applicationxkivio = "application/x-kivio"
applicationxkontour = "application/x-kontour"
applicationxkpovmodeler = "application/x-kpovmodeler"
applicationxkpresenter = "application/x-kpresenter"
applicationxkrita = "application/x-krita"
applicationxkspread = "application/x-kspread"
applicationxkugar = "application/x-kugar"
applicationxkword = "application/x-kword"
applicationxlha = "application/x-lha"
applicationxlhz = "application/x-lhz"
applicationxliff_xml = "application/xliff+xml"
applicationxlmdb = "application/x-lmdb"
applicationxlrzip = "application/x-lrzip"
applicationxlrzipcompressedtar = "application/x-lrzip-compressed-tar"
applicationxluabytecode = "application/x-lua-bytecode"
applicationxlyx = "application/x-lyx"
applicationxlz4 = "application/x-lz4"
applicationxlz4compressedtar = "application/x-lz4-compressed-tar"
applicationxlzip = "application/x-lzip"
applicationxlzipcompressedtar = "application/x-lzip-compressed-tar"
applicationxlzma = "application/x-lzma"
applicationxlzmacompressedtar = "application/x-lzma-compressed-tar"
applicationxlzop = "application/x-lzop"
applicationxlzpdf = "application/x-lzpdf"
applicationxm4 = "application/x-m4"
applicationxmagicpoint = "application/x-magicpoint"
applicationxmakeself = "application/x-makeself"
applicationxmamechd = "application/x-mame-chd"
applicationxmarkaby = "application/x-markaby"
applicationxmie = "application/x-mie"
applicationxmif = "application/x-mif"
applicationxmimearchive = "application/x-mimearchive"
applicationxml = "application/xml"
applicationxmldtd = "application/xml-dtd"
applicationxmlexternalparsedentity = "application/xml-external-parsed-entity"
applicationxmobipocketebook = "application/x-mobipocket-ebook"
applicationxmodrinthmodpack_zip = "application/x-modrinth-modpack+zip"
applicationxmsapplication = "application/x-ms-application"
applicationxmsbinder = "application/x-msbinder"
applicationxmscardfile = "application/x-mscardfile"
applicationxmsclip = "application/x-msclip"
applicationxmsdownload = "application/x-msdownload"
applicationxmsi = "application/x-msi"
applicationxmsmediaview = "application/x-msmediaview"
applicationxmsmetafile = "application/x-msmetafile"
applicationxmsmoney = "application/x-msmoney"
applicationxmsschedule = "application/x-msschedule"
applicationxmsshortcut = "application/x-ms-shortcut"
applicationxmsterminal = "application/x-msterminal"
applicationxmswim = "application/x-ms-wim"
applicationxmswinurl = "application/x-mswinurl"
applicationxmswmd = "application/x-ms-wmd"
applicationxmswmz = "application/x-ms-wmz"
applicationxmswrite = "application/x-mswrite"
applicationxmsxbap = "application/x-ms-xbap"
applicationxmsxrom = "application/x-msx-rom"
applicationxn64rom = "application/x-n64-rom"
applicationxnavianimation = "application/x-navi-animation"
applicationxneogeopocketcolorrom = "application/x-neo-geo-pocket-color-rom"
applicationxneogeopocketrom = "application/x-neo-geo-pocket-rom"
applicationxnesrom = "application/x-nes-rom"
applicationxnetcdf = "application/x-netcdf"
applicationxnetshowchannel = "application/x-netshow-channel"
applicationxnintendo3dsexecutable = "application/x-nintendo-3ds-executable"
applicationxnintendo3dsrom = "application/x-nintendo-3ds-rom"
applicationxnintendodsrom = "application/x-nintendo-ds-rom"
applicationxnintendoswitchxci = "application/x-nintendo-switch-xci"
applicationxnsproxyautoconfig = "application/x-ns-proxy-autoconfig"
applicationxnuscript = "application/x-nuscript"
applicationxnzb = "application/x-nzb"
applicationxobject = "application/x-object"
applicationxoleo = "application/x-oleo"
applicationxop_xml = "application/xop+xml"
applicationxopenvpnprofile = "application/x-openvpn-profile"
applicationxopenzim = "application/x-openzim"
applicationxpagemaker = "application/x-pagemaker"
applicationxpak = "application/x-pak"
applicationxpar2 = "application/x-par2"
applicationxpartialdownload = "application/x-partial-download"
applicationxpcapng = "application/x-pcapng"
applicationxpcenginerom = "application/x-pc-engine-rom"
applicationxperfdata = "application/x-perf-data"
applicationxperl = "application/x-perl"
applicationxphp = "application/x-php"
applicationxpkcs7certificates = "application/x-pkcs7-certificates"
applicationxpkcs7certreqresp = "application/x-pkcs7-certreqresp"
applicationxplanperfect = "application/x-planperfect"
applicationxpocketword = "application/x-pocket-word"
applicationxpowershell = "application/x-powershell"
applicationxproc_xml = "application/xproc+xml"
applicationxprofile = "application/x-profile"
applicationxpw = "application/x-pw"
applicationxpyspreadbzspreadsheet = "application/x-pyspread-bz-spreadsheet"
applicationxpyspreadspreadsheet = "application/x-pyspread-spreadsheet"
applicationxpythonbytecode = "application/x-python-bytecode"
applicationxqbrew = "application/x-qbrew"
applicationxqeddisk = "application/x-qed-disk"
applicationxqemudisk = "application/x-qemu-disk"
applicationxqpress = "application/x-qpress"
applicationxqtiplot = "application/x-qtiplot"
applicationxquattropro = "application/x-quattropro"
applicationxquicktimemedialink = "application/x-quicktime-media-link"
applicationxqw = "application/x-qw"
applicationxrawdiskimagexzcompressed = "application/x-raw-disk-image-xz-compressed"
applicationxrawfloppydiskimage = "application/x-raw-floppy-disk-image"
applicationxresearchinfosystems = "application/x-research-info-systems"
applicationxrpm = "application/x-rpm"
applicationxruby = "application/x-ruby"
applicationxrzip = "application/x-rzip"
applicationxrzipcompressedtar = "application/x-rzip-compressed-tar"
applicationxsami = "application/x-sami"
applicationxsea = "application/x-sea"
applicationxsg1000rom = "application/x-sg1000-rom"
applicationxshar = "application/x-shar"
applicationxsharedlib = "application/x-sharedlib"
applicationxsharedlibraryla = "application/x-shared-library-la"
applicationxshellscript = "application/x-shellscript"
applicationxshorten = "application/x-shorten"
applicationxsiag = "application/x-siag"
applicationxsilverlightapp = "application/x-silverlight-app"
applicationxslt_xml = "application/xslt+xml"
applicationxsmsrom = "application/x-sms-rom"
applicationxsourcerpm = "application/x-source-rpm"
applicationxspf_xml = "application/xspf+xml"
applicationxspsspor = "application/x-spss-por"
applicationxspsssav = "application/x-spss-sav"
applicationxsqlite2 = "application/x-sqlite2"
applicationxstarcalc = "application/x-starcalc"
applicationxstarchart = "application/x-starchart"
applicationxstardraw = "application/x-stardraw"
applicationxstarimpress = "application/x-starimpress"
applicationxstarmail = "application/x-starmail"
applicationxstarmath = "application/x-starmath"
applicationxstarwriter = "application/x-starwriter"
applicationxstarwriterglobal = "application/x-starwriter-global"
applicationxstuffit = "application/x-stuffit"
applicationxstuffitx = "application/x-stuffitx"
applicationxsubrip = "application/x-subrip"
applicationxsv4cpio = "application/x-sv4cpio"
applicationxsv4crc = "application/x-sv4crc"
applicationxsylk = "application/x-sylk"
applicationxt3vmimage = "application/x-t3vm-image"
applicationxt602 = "application/x-t602"
applicationxtads = "application/x-tads"
applicationxtar = "application/x-tar"
applicationxtarz = "application/x-tarz"
applicationxtexgf = "application/x-tex-gf"
applicationxtexpk = "application/x-tex-pk"
applicationxtextfm = "application/x-tex-tfm"
applicationxtgif = "application/x-tgif"
applicationxtheme = "application/x-theme"
applicationxthomsoncartridgememo7 = "application/x-thomson-cartridge-memo7"
applicationxthomsoncassette = "application/x-thomson-cassette"
applicationxthomsonsapimage = "application/x-thomson-sap-image"
applicationxtiledtmx = "application/x-tiled-tmx"
applicationxtiledtsx = "application/x-tiled-tsx"
applicationxtrash = "application/x-trash"
applicationxtroffman = "application/x-troff-man"
applicationxtzo = "application/x-tzo"
applicationxufraw = "application/x-ufraw"
applicationxustar = "application/x-ustar"
applicationxv_xml = "application/xv+xml"
applicationxvdidisk = "application/x-vdi-disk"
applicationxvhddisk = "application/x-vhd-disk"
applicationxvhdxdisk = "application/x-vhdx-disk"
applicationxvirtualboxhdd = "application/x-virtualbox-hdd"
applicationxvirtualboxovf = "application/x-virtualbox-ovf"
applicationxvirtualboxvbox = "application/x-virtualbox-vbox"
applicationxvirtualboxvboxextpack = "application/x-virtualbox-vbox-extpack"
applicationxvirtualboyrom = "application/x-virtual-boy-rom"
applicationxvmdkdisk = "application/x-vmdk-disk"
applicationxwaissource = "application/x-wais-source"
applicationxwebappmanifest_json = "application/x-web-app-manifest+json"
applicationxwiiwad = "application/x-wii-wad"
applicationxwindowsthemepack = "application/x-windows-themepack"
applicationxwonderswancolorrom = "application/x-wonderswan-color-rom"
applicationxwonderswanrom = "application/x-wonderswan-rom"
applicationxwpg = "application/x-wpg"
applicationxwwf = "application/x-wwf"
applicationxx509cacert = "application/x-x509-ca-cert"
applicationxxar = "application/x-xar"
applicationxxbel = "application/x-xbel"
applicationxxpinstall = "application/x-xpinstall"
applicationxxz = "application/x-xz"
applicationxxzcompressedtar = "application/x-xz-compressed-tar"
applicationxxzpdf = "application/x-xzpdf"
applicationxzipcompressedfb2 = "application/x-zip-compressed-fb2"
applicationxzmachine = "application/x-zmachine"
applicationxzoo = "application/x-zoo"
applicationxzpaq = "application/x-zpaq"
applicationxzstdcompressedtar = "application/x-zstd-compressed-tar"
applicationyaml = "application/yaml"
applicationyang = "application/yang"
applicationyin_xml = "application/yin+xml"
applicationzip = "application/zip"
applicationzip_dotlottie = "application/zip+dotlottie"
applicationzlib = "application/zlib"
applicationzstd = "application/zstd"
appx = "appx"
appxbundle = "appxbundle"
apr = "apr"
ar = "ar"
arc = "arc"
arj = "arj"
arw = "arw"
asar = "asar"
asc = "asc"
asd = "asd"
asf = "asf"
asm = "asm"
aso = "aso"
asp = "asp"
ass = "ass"
astc = "astc"
asx = "asx"
atc = "atc"
atom = "atom"
atomcat = "atomcat"
atomdeleted = "atomdeleted"
atomsvc = "atomsvc"
atx = "atx"
au = "au"
audioaac = "audio/aac"
audioac3 = "audio/ac3"
audioadpcm = "audio/adpcm"
audioamr = "audio/amr"
audioamrwb = "audio/amr-wb"
audioannodex = "audio/annodex"
audiobasic = "audio/basic"
audioflac = "audio/flac"
audiomidi = "audio/midi"
audiomobilexmf = "audio/mobile-xmf"
audiomp2 = "audio/mp2"
audiomp4 = "audio/mp4"
audiompeg = "audio/mpeg"
audioogg = "audio/ogg"
audioprssid = "audio/prs.sid"
audiosilk = "audio/silk"
audiousac = "audio/usac"
audiovndaudibleaax = "audio/vnd.audible.aax"
audiovndaudibleaaxc = "audio/vnd.audible.aaxc"
audiovnddeceaudio = "audio/vnd.dece.audio"
audiovnddigitalwinds = "audio/vnd.digital-winds"
audiovnddra = "audio/vnd.dra"
audiovnddts = "audio/vnd.dts"
audiovnddtshd = "audio/vnd.dts.hd"
audiovndlucentvoice = "audio/vnd.lucent.voice"
audiovndmsplayreadymediapya = "audio/vnd.ms-playready.media.pya"
audiovndnueraecelp4800 = "audio/vnd.nuera.ecelp4800"
audiovndnueraecelp7470 = "audio/vnd.nuera.ecelp7470"
audiovndnueraecelp9600 = "audio/vnd.nuera.ecelp9600"
audiovndrip = "audio/vnd.rip"
audiovndrnrealaudio = "audio/vnd.rn-realaudio"
audiovndwave = "audio/vnd.wave"
audiowebm = "audio/webm"
audioxaifc = "audio/x-aifc"
audioxaiff = "audio/x-aiff"
audioxamzxml = "audio/x-amzxml"
audioxape = "audio/x-ape"
audioxcaf = "audio/x-caf"
audioxdff = "audio/x-dff"
audioxdsf = "audio/x-dsf"
audioxgsm = "audio/x-gsm"
audioxiriverpla = "audio/x-iriver-pla"
audioxit = "audio/x-it"
audioxm4b = "audio/x-m4b"
audioxm4r = "audio/x-m4r"
audioxmatroska = "audio/x-matroska"
audioxminipsf = "audio/x-minipsf"
audioxmo3 = "audio/x-mo3"
audioxmod = "audio/x-mod"
audioxmpegurl = "audio/x-mpegurl"
audioxmsasx = "audio/x-ms-asx"
audioxmswma = "audio/x-ms-wma"
audioxmusepack = "audio/x-musepack"
audioxpnaudibleaudio = "audio/x-pn-audibleaudio"
audioxpnrealaudioplugin = "audio/x-pn-realaudio-plugin"
audioxpsflib = "audio/x-psflib"
audioxs3m = "audio/x-s3m"
audioxscpls = "audio/x-scpls"
audioxstm = "audio/x-stm"
audioxtak = "audio/x-tak"
audioxtta = "audio/x-tta"
audioxvoc = "audio/x-voc"
audioxwavpack = "audio/x-wavpack"
audioxwavpackcorrection = "audio/x-wavpack-correction"
audioxxi = "audio/x-xi"
audioxxm = "audio/x-xm"
audioxxmf = "audio/x-xmf"
authors = "authors"
automount = "automount"
avci = "avci"
avcs = "avcs"
avf = "avf"
avi = "avi"
avif = "avif"
avifs = "avifs"
aw = "aw"
awb = "awb"
awk = "awk"
axa = "axa"
axv = "axv"
azf = "azf"
azs = "azs"
azv = "azv"
azw = "azw"
azw3 = "azw3"
b16 = "b16"
bak = "bak"
bary = "bary"
bas = "bas"
bat = "bat"
bcpio = "bcpio"
bdf = "bdf"
bdm = "bdm"
bdmv = "bdmv"
bdo = "bdo"
bdoc = "bdoc"
bed = "bed"
bh2 = "bh2"
bib = "bib"
bik = "bik"
bin = "bin"
bk2 = "bk2"
blb = "blb"
blend = "blend"
blender = "blender"
blorb = "blorb"
blp = "blp"
bmi = "bmi"
bmml = "bmml"
bmp = "bmp"
book = "book"
box = "box"
boz = "boz"
bpk = "bpk"
bps = "bps"
brk = "brk"
brush = "brush"
brushset = "brushset"
bsdiff = "bsdiff"
bsp = "bsp"
bst = "bst"
btf = "btf"
btif = "btif"
buffer = "buffer"
bz = "bz"
bz2 = "bz2"
bz3 = "bz3"
c = "c"
c11amc = "c11amc"
c11amz = "c11amz"
c4d = "c4d"
c4f = "c4f"
c4g = "c4g"
c4p = "c4p"
c4u = "c4u"
cab = "cab"
cacerts = "cacerts"
caf = "caf"
cap = "cap"
car = "car"
cat = "cat"
cb7 = "cb7"
cba = "cba"
cbl = "cbl"
cbor = "cbor"
cbr = "cbr"
cbt = "cbt"
cbz = "cbz"
cc = "cc"
cci = "cci"
ccmx = "ccmx"
cco = "cco"
cct = "cct"
ccxml = "ccxml"
cdbcmsg = "cdbcmsg"
cdf = "cdf"
cdfx = "cdfx"
cdi = "cdi"
cdkey = "cdkey"
cdmia = "cdmia"
cdmic = "cdmic"
cdmid = "cdmid"
cdmio = "cdmio"
cdmiq = "cdmiq"
cdr = "cdr"
cdx = "cdx"
cdxml = "cdxml"
cdy = "cdy"
cel = "cel"
cer = "cer"
cert = "cert"
cfs = "cfs"
cgb = "cgb"
cgm = "cgm"
changelog = "changelog"
chat = "chat"
chd = "chd"
chemicalxcdx = "chemical/x-cdx"
chemicalxcif = "chemical/x-cif"
chemicalxcmdf = "chemical/x-cmdf"
chemicalxcml = "chemical/x-cml"
chemicalxcsml = "chemical/x-csml"
chemicalxpdb = "chemical/x-pdb"
chemicalxxyz = "chemical/x-xyz"
chm = "chm"
chrt = "chrt"
cif = "cif"
cii = "cii"
cil = "cil"
cjs = "cjs"
cl = "cl"
cla = "cla"
cld = "cld"
clkk = "clkk"
clkp = "clkp"
clkt = "clkt"
clkw = "clkw"
clkx = "clkx"
clp = "clp"
clpi = "clpi"
cls = "cls"
cmake = "cmake"
cmakeliststxt = "cmakeliststxt"
cmc = "cmc"
cmdf = "cmdf"
cml = "cml"
cmp = "cmp"
cmx = "cmx"
cob = "cob"
cod = "cod"
coffee = "coffee"
com = "com"
conf = "conf"
copying = "copying"
core = "core"
cpi = "cpi"
cpio = "cpio"
cpiogz = "cpiogz"
cpl = "cpl"
cpp = "cpp"
cpt = "cpt"
cr = "cr"
cr2 = "cr2"
cr3 = "cr3"
crd = "crd"
crdownload = "crdownload"
credits = "credits"
crl = "crl"
crt = "crt"
crw = "crw"
crx = "crx"
cryptonote = "cryptonote"
cs = "cs"
csh = "csh"
csl = "csl"
csml = "csml"
cso = "cso"
csp = "csp"
css = "css"
cst = "cst"
csv = "csv"
csvs = "csvs"
cts = "cts"
cu = "cu"
cue = "cue"
cur = "cur"
curl = "curl"
cwk = "cwk"
cwl = "cwl"
cww = "cww"
cxt = "cxt"
cxx = "cxx"
d = "d"
dae = "dae"
daf = "daf"
dar = "dar"
dart = "dart"
dataless = "dataless"
davmount = "davmount"
dbf = "dbf"
dbk = "dbk"
dcl = "dcl"
dcm = "dcm"
dcmp = "dcmp"
dcr = "dcr"
dcurl = "dcurl"
dd2 = "dd2"
ddd = "ddd"
ddf = "ddf"
dds = "dds"
deb = "deb"
deploy = "deploy"
der = "der"
desktop = "desktop"
device = "device"
dfac = "dfac"
dff = "dff"
dgc = "dgc"
di = "di"
dia = "dia"
dib = "dib"
dic = "dic"
dicomdir = "dicomdir"
diff = "diff"
dir = "dir"
dis = "dis"
dispositionnotification = "disposition-notification"
dist = "dist"
distz = "distz"
divx = "divx"
djv = "djv"
djvu = "djvu"
dll = "dll"
dmg = "dmg"
dmp = "dmp"
dms = "dms"
dna = "dna"
dng = "dng"
doc = "doc"
docbook = "docbook"
dockerfile = "dockerfile"
docm = "docm"
docx = "docx"
dot = "dot"
dotm = "dotm"
dotx = "dotx"
dp = "dp"
dpg = "dpg"
dpx = "dpx"
dra = "dra"
drl = "drl"
drle = "drle"
drm = "drm"
drv = "drv"
dsc = "dsc"
dsf = "dsf"
dsl = "dsl"
dssc = "dssc"
dtb = "dtb"
dtd = "dtd"
dts = "dts"
dtshd = "dtshd"
dtsi = "dtsi"
dtx = "dtx"
dump = "dump"
dv = "dv"
dvb = "dvb"
dvi = "dvi"
dvibz2 = "dvibz2"
dvigz = "dvigz"
dwd = "dwd"
dwf = "dwf"
dwg = "dwg"
dxf = "dxf"
dxp = "dxp"
dxr = "dxr"
e = "e"
ear = "ear"
ecelp4800 = "ecelp4800"
ecelp7470 = "ecelp7470"
ecelp9600 = "ecelp9600"
ecma = "ecma"
edm = "edm"
edx = "edx"
efi = "efi"
efif = "efif"
egon = "egon"
ehthumbsdb = "ehthumbsdb"
ehthumbsvistadb = "ehthumbsvistadb"
ei6 = "ei6"
eif = "eif"
el = "el"
elc = "elc"
emf = "emf"
eml = "eml"
emma = "emma"
emotionml = "emotionml"
emp = "emp"
emz = "emz"
ent = "ent"
eol = "eol"
eot = "eot"
eps = "eps"
epsbz2 = "epsbz2"
epsf = "epsf"
epsfbz2 = "epsfbz2"
epsfgz = "epsfgz"
epsgz = "epsgz"
epsi = "epsi"
epsibz2 = "epsibz2"
epsigz = "epsigz"
epub = "epub"
eris = "eris"
erl = "erl"
es = "es"
es3 = "es3"
esa = "esa"
escn = "escn"
esf = "esf"
et3 = "et3"
etheme = "etheme"
etx = "etx"
eva = "eva"
evy = "evy"
ex = "ex"
exe = "exe"
exi = "exi"
exp = "exp"
exr = "exr"
exs = "exs"
ext = "ext"
ez = "ez"
ez2 = "ez2"
ez3 = "ez3"
f = "f"
f4a = "f4a"
f4b = "f4b"
f4v = "f4v"
f77 = "f77"
f90 = "f90"
f95 = "f95"
fasl = "fasl"
fb2 = "fb2"
fb2zip = "fb2zip"
fbs = "fbs"
fbx = "fbx"
fcdt = "fcdt"
fcs = "fcs"
fd = "fd"
fdf = "fdf"
fds = "fds"
fdt = "fdt"
fe_launch = "fe_launch"
feature = "feature"
fg5 = "fg5"
fgd = "fgd"
fh = "fh"
fh4 = "fh4"
fh5 = "fh5"
fh7 = "fh7"
fhc = "fhc"
fig = "fig"
fish = "fish"
fit = "fit"
fits = "fits"
fl = "fl"
flac = "flac"
flatpak = "flatpak"
flatpakref = "flatpakref"
flatpakrepo = "flatpakrepo"
flc = "flc"
fli = "fli"
flo = "flo"
flv = "flv"
flw = "flw"
flx = "flx"
fly = "fly"
fm = "fm"
fnc = "fnc"
fo = "fo"
fodg = "fodg"
fodp = "fodp"
fods = "fods"
fodt = "fodt"
fontcollection = "font/collection"
fontttf = "font/ttf"
fontwoff = "font/woff"
fontwoff2 = "font/woff2"
fpx = "fpx"
frame = "frame"
fsc = "fsc"
fst = "fst"
ftc = "ftc"
fti = "fti"
fts = "fts"
fvt = "fvt"
fxm = "fxm"
fxp = "fxp"
fxpl = "fxpl"
fzs = "fzs"
g2w = "g2w"
g3 = "g3"
g3w = "g3w"
gac = "gac"
gam = "gam"
gb = "gb"
gba = "gba"
gbc = "gbc"
gbr = "gbr"
gbrjob = "gbrjob"
gca = "gca"
gcode = "gcode"
gcrd = "gcrd"
gd = "gd"
gdi = "gdi"
gdl = "gdl"
gdoc = "gdoc"
gdraw = "gdraw"
gdshader = "gdshader"
ged = "ged"
gedcom = "gedcom"
gem = "gem"
gen = "gen"
geo = "geo"
geojson = "geojson"
gex = "gex"
gf = "gf"
gform = "gform"
gg = "gg"
ggb = "ggb"
ggs = "ggs"
ggt = "ggt"
ghf = "ghf"
gif = "gif"
gih = "gih"
gim = "gim"
gjam = "gjam"
glade = "glade"
glb = "glb"
gltf = "gltf"
gmap = "gmap"
gml = "gml"
gmo = "gmo"
gmonout = "gmonout"
gmx = "gmx"
gnc = "gnc"
gnd = "gnd"
gnucash = "gnucash"
gnumakefile = "gnumakefile"
gnumeric = "gnumeric"
gnuplot = "gnuplot"
go = "go"
gp = "gp"
gpg = "gpg"
gph = "gph"
gplt = "gplt"
gpx = "gpx"
gqf = "gqf"
gqs = "gqs"
gra = "gra"
gradle = "gradle"
gram = "gram"
gramps = "gramps"
gre = "gre"
groovy = "groovy"
grv = "grv"
grxml = "grxml"
gs = "gs"
gscript = "gscript"
gsf = "gsf"
gsh = "gsh"
gsheet = "gsheet"
gsite = "gsite"
gslides = "gslides"
gsm = "gsm"
gtar = "gtar"
gtm = "gtm"
gtw = "gtw"
gv = "gv"
gvp = "gvp"
gvy = "gvy"
gx = "gx"
gxf = "gxf"
gxt = "gxt"
gy = "gy"
gz = "gz"
h = "h"
h261 = "h261"
h263 = "h263"
h264 = "h264"
h4 = "h4"
h5 = "h5"
hal = "hal"
hbci = "hbci"
hbs = "hbs"
hdd = "hdd"
hdf = "hdf"
hdf4 = "hdf4"
hdf5 = "hdf5"
hdp = "hdp"
hdr = "hdr"
heic = "heic"
heics = "heics"
heif = "heif"
heifs = "heifs"
hej2 = "hej2"
held = "held"
hfe = "hfe"
hh = "hh"
hif = "hif"
hjson = "hjson"
hlp = "hlp"
hp = "hp"
hpgl = "hpgl"
hpid = "hpid"
hpp = "hpp"
hps = "hps"
hqx = "hqx"
hs = "hs"
hta = "hta"
htc = "htc"
htke = "htke"
htm = "htm"
html = "html"
hvd = "hvd"
hvp = "hvp"
hvs = "hvs"
hwp = "hwp"
hwt = "hwt"
hxx = "hxx"
i2g = "i2g"
ica = "ica"
icalendar = "icalendar"
icb = "icb"
icc = "icc"
ice = "ice"
icm = "icm"
icns = "icns"
ico = "ico"
ics = "ics"
idl = "idl"
ief = "ief"
ifb = "ifb"
iff = "iff"
ifm = "ifm"
iges = "iges"
igl = "igl"
igm = "igm"
igs = "igs"
igx = "igx"
iif = "iif"
ilbm = "ilbm"
imageapng = "image/apng"
imageastc = "image/astc"
imageavci = "image/avci"
imageavcs = "image/avcs"
imageavif = "image/avif"
imagebmp = "image/bmp"
imagecgm = "image/cgm"
imagedb = "imagedb"
imagedicomrle = "image/dicom-rle"
imagedpx = "image/dpx"
imageemf = "image/emf"
imageg3fax = "image/g3fax"
imagegif = "image/gif"
imageheicsequence = "image/heic-sequence"
imageheif = "image/heif"
imageheifsequence = "image/heif-sequence"
imagehej2k = "image/hej2k"
imageief = "image/ief"
imagejaii = "image/jaii"
imagejais = "image/jais"
imagejls = "image/jls"
imagejp2 = "image/jp2"
imagejpeg = "image/jpeg"
imagejph = "image/jph"
imagejphc = "image/jphc"
imagejpm = "image/jpm"
imagejpx = "image/jpx"
imagejxl = "image/jxl"
imagejxr = "image/jxr"
imagejxra = "image/jxra"
imagejxrs = "image/jxrs"
imagejxs = "image/jxs"
imagejxsc = "image/jxsc"
imagejxsi = "image/jxsi"
imagejxss = "image/jxss"
imagektx = "image/ktx"
imagektx2 = "image/ktx2"
imageopenraster = "image/openraster"
imagepng = "image/png"
imageprsbtif = "image/prs.btif"
imageprspti = "image/prs.pti"
imageqoi = "image/qoi"
imagerle = "image/rle"
imagesvg_xml = "image/svg+xml"
imagesvg_xmlcompressed = "image/svg+xml-compressed"
imaget38 = "image/t38"
imagetiff = "image/tiff"
imagetifffx = "image/tiff-fx"
imagevndadobephotoshop = "image/vnd.adobe.photoshop"
imagevndairzipacceleratorazv = "image/vnd.airzip.accelerator.azv"
imagevnddecegraphic = "image/vnd.dece.graphic"
imagevnddjvu = "image/vnd.djvu"
imagevnddwg = "image/vnd.dwg"
imagevnddxf = "image/vnd.dxf"
imagevndfastbidsheet = "image/vnd.fastbidsheet"
imagevndfpx = "image/vnd.fpx"
imagevndfst = "image/vnd.fst"
imagevndfujixeroxedmicsmmr = "image/vnd.fujixerox.edmics-mmr"
imagevndfujixeroxedmicsrlc = "image/vnd.fujixerox.edmics-rlc"
imagevndmicrosofticon = "image/vnd.microsoft.icon"
imagevndmsmodi = "image/vnd.ms-modi"
imagevndnetfpx = "image/vnd.net-fpx"
imagevndpcob16 = "image/vnd.pco.b16"
imagevndradiance = "image/vnd.radiance"
imagevndrnrealpix = "image/vnd.rn-realpix"
imagevndtencenttap = "image/vnd.tencent.tap"
imagevndvalvesourcetexture = "image/vnd.valve.source.texture"
imagevndwapwbmp = "image/vnd.wap.wbmp"
imagevndxiff = "image/vnd.xiff"
imagevndzbrushpcx = "image/vnd.zbrush.pcx"
imagewebp = "image/webp"
imagewmf = "image/wmf"
imagexadobedng = "image/x-adobe-dng"
imagexapplixgraphics = "image/x-applix-graphics"
imagexbzeps = "image/x-bzeps"
imagexcanoncr2 = "image/x-canon-cr2"
imagexcanoncr3 = "image/x-canon-cr3"
imagexcanoncrw = "image/x-canon-crw"
imagexcmuraster = "image/x-cmu-raster"
imagexcmx = "image/x-cmx"
imagexcompressedxcf = "image/x-compressed-xcf"
imagexdds = "image/x-dds"
imagexeps = "image/x-eps"
imagexexr = "image/x-exr"
imagexfreehand = "image/x-freehand"
imagexfujiraf = "image/x-fuji-raf"
imagexgimpgbr = "image/x-gimp-gbr"
imagexgimpgih = "image/x-gimp-gih"
imagexgimppat = "image/x-gimp-pat"
imagexgzeps = "image/x-gzeps"
imagexicns = "image/x-icns"
imagexilbm = "image/x-ilbm"
imagexjng = "image/x-jng"
imagexjp2codestream = "image/x-jp2-codestream"
imagexkisscel = "image/x-kiss-cel"
imagexkodakdcr = "image/x-kodak-dcr"
imagexkodakk25 = "image/x-kodak-k25"
imagexkodakkdc = "image/x-kodak-kdc"
imagexlwo = "image/x-lwo"
imagexlws = "image/x-lws"
imagexmacpaint = "image/x-macpaint"
imagexminoltamrw = "image/x-minolta-mrw"
imagexmsod = "image/x-msod"
imagexnikonnef = "image/x-nikon-nef"
imagexnikonnrw = "image/x-nikon-nrw"
imagexolympusorf = "image/x-olympus-orf"
imagexpanasonicrw = "image/x-panasonic-rw"
imagexpanasonicrw2 = "image/x-panasonic-rw2"
imagexpentaxpef = "image/x-pentax-pef"
imagexpfm = "image/x-pfm"
imagexphm = "image/x-phm"
imagexphotocd = "image/x-photo-cd"
imagexpict = "image/x-pict"
imagexportableanymap = "image/x-portable-anymap"
imagexportablebitmap = "image/x-portable-bitmap"
imagexportablegraymap = "image/x-portable-graymap"
imagexportablepixmap = "image/x-portable-pixmap"
imagexpxr = "image/x-pxr"
imagexquicktime = "image/x-quicktime"
imagexrgb = "image/x-rgb"
imagexsct = "image/x-sct"
imagexsgi = "image/x-sgi"
imagexsigmax3f = "image/x-sigma-x3f"
imagexskencil = "image/x-skencil"
imagexsonyarw = "image/x-sony-arw"
imagexsonysr2 = "image/x-sony-sr2"
imagexsonysrf = "image/x-sony-srf"
imagexsunraster = "image/x-sun-raster"
imagextga = "image/x-tga"
imagexwinbitmap = "image/x-win-bitmap"
imagexxbitmap = "image/x-xbitmap"
imagexxcf = "image/x-xcf"
imagexxfig = "image/x-xfig"
imagexxpixmap = "image/x-xpixmap"
imagexxwindowdump = "image/x-xwindowdump"
ime = "ime"
img = "img"
imgxz = "imgxz"
imp = "imp"
ims = "ims"
imy = "imy"
ini = "ini"
ink = "ink"
inkml = "inkml"
ins = "ins"
install = "install"
iota = "iota"
ipfix = "ipfix"
ipk = "ipk"
ips = "ips"
iptables = "iptables"
ipynb = "ipynb"
irm = "irm"
irp = "irp"
iso = "iso"
iso9660 = "iso9660"
it = "it"
it87 = "it87"
itp = "itp"
its = "its"
ivp = "ivp"
ivu = "ivu"
j2c = "j2c"
j2k = "j2k"
jad = "jad"
jade = "jade"
jaii = "jaii"
jais = "jais"
jam = "jam"
jar = "jar"
jardiff = "jardiff"
java = "java"
jceks = "jceks"
jfif = "jfif"
jhc = "jhc"
jisp = "jisp"
jks = "jks"
jl = "jl"
jls = "jls"
jlt = "jlt"
jng = "jng"
jnlp = "jnlp"
joda = "joda"
jp2 = "jp2"
jpc = "jpc"
jpe = "jpe"
jpeg = "jpeg"
jpf = "jpf"
jpg = "jpg"
jpg2 = "jpg2"
jpgm = "jpgm"
jpgv = "jpgv"
jph = "jph"
jpm = "jpm"
jpr = "jpr"
jpx = "jpx"
jrd = "jrd"
js = "js"
jse = "jse"
jsm = "jsm"
json = "json"
json5 = "json5"
jsonld = "jsonld"
jsonml = "jsonml"
jsonpatch = "jsonpatch"
jsx = "jsx"
jt = "jt"
jxl = "jxl"
jxr = "jxr"
jxra = "jxra"
jxrs = "jxrs"
jxs = "jxs"
jxsc = "jxsc"
jxsi = "jxsi"
jxss = "jxss"
k25 = "k25"
k7 = "k7"
kar = "kar"
karbon = "karbon"
kcf = "kcf"
kdbx = "kdbx"
kdc = "kdc"
kdelnk = "kdelnk"
kexi = "kexi"
kexic = "kexic"
kexis = "kexis"
key = "key"
kfo = "kfo"
kfx = "kfx"
kia = "kia"
kil = "kil"
kino = "kino"
kml = "kml"
kmz = "kmz"
kne = "kne"
knp = "knp"
kon = "kon"
kpm = "kpm"
kpr = "kpr"
kpt = "kpt"
kpxx = "kpxx"
kra = "kra"
krz = "krz"
ks = "ks"
ksp = "ksp"
ksy = "ksy"
kt = "kt"
ktr = "ktr"
ktx = "ktx"
ktx2 = "ktx2"
ktz = "ktz"
kud = "kud"
kwd = "kwd"
kwt = "kwt"
la = "la"
lasxml = "lasxml"
latex = "latex"
lbd = "lbd"
lbe = "lbe"
lbm = "lbm"
ldif = "ldif"
les = "les"
less = "less"
lgr = "lgr"
lha = "lha"
lhs = "lhs"
lhz = "lhz"
lib = "lib"
link66 = "link66"
lisp = "lisp"
list = "list"
list3820 = "list3820"
listafp = "listafp"
litcoffee = "litcoffee"
lmdb = "lmdb"
lnk = "lnk"
lnx = "lnx"
loas = "loas"
log = "log"
lostxml = "lostxml"
lottie = "lottie"
lrf = "lrf"
lrm = "lrm"
lrv = "lrv"
lrz = "lrz"
ltf = "ltf"
ltx = "ltx"
lua = "lua"
luac = "luac"
lvp = "lvp"
lwo = "lwo"
lwob = "lwob"
lwp = "lwp"
lws = "lws"
ly = "ly"
lyx = "lyx"
lz = "lz"
lz4 = "lz4"
lzh = "lzh"
lzma = "lzma"
lzo = "lzo"
m = "m"
m13 = "m13"
m14 = "m14"
m15 = "m15"
m1u = "m1u"
m1v = "m1v"
m21 = "m21"
m2a = "m2a"
m2t = "m2t"
m2ts = "m2ts"
m2v = "m2v"
m3a = "m3a"
m3u = "m3u"
m3u8 = "m3u8"
m4 = "m4"
m4a = "m4a"
m4b = "m4b"
m4p = "m4p"
m4r = "m4r"
m4s = "m4s"
m4u = "m4u"
m4v = "m4v"
m7 = "m7"
ma = "ma"
mab = "mab"
mads = "mads"
maei = "maei"
mag = "mag"
mak = "mak"
makefile = "makefile"
maker = "maker"
man = "man"
manifest = "manifest"
map = "map"
mar = "mar"
markdown = "markdown"
mathml = "mathml"
mb = "mb"
mbk = "mbk"
mbox = "mbox"
mc1 = "mc1"
mc2 = "mc2"
mcd = "mcd"
mcurl = "mcurl"
md = "md"
mdb = "mdb"
mdi = "mdi"
mdx = "mdx"
me = "me"
med = "med"
mesh = "mesh"
mesonbuild = "mesonbuild"
mesonoptionstxt = "mesonoptionstxt"
messagedispositionnotification = "message/disposition-notification"
messageglobal = "message/global"
messageglobaldeliverystatus = "message/global-delivery-status"
messageglobaldispositionnotification = "message/global-disposition-notification"
messageglobalheaders = "message/global-headers"
messagerfc822 = "message/rfc822"
messagexgnurmail = "message/x-gnu-rmail"
meta4 = "meta4"
metalink = "metalink"
mets = "mets"
mfm = "mfm"
mft = "mft"
mgp = "mgp"
mgz = "mgz"
mht = "mht"
mhtml = "mhtml"
mid = "mid"
midi = "midi"
mie = "mie"
mif = "mif"
mime = "mime"
minipsf = "minipsf"
mj2 = "mj2"
mjp2 = "mjp2"
mjpeg = "mjpeg"
mjpg = "mjpg"
mjs = "mjs"
mk = "mk"
mk3d = "mk3d"
mka = "mka"
mkd = "mkd"
mks = "mks"
mkv = "mkv"
ml = "ml"
mli = "mli"
mlp = "mlp"
mm = "mm"
mmd = "mmd"
mmf = "mmf"
mml = "mml"
mmr = "mmr"
mng = "mng"
mny = "mny"
mo = "mo"
mo3 = "mo3"
mobi = "mobi"
moc = "moc"
mod = "mod"
model3mf = "model/3mf"
modelgltf_json = "model/gltf+json"
modelgltfbinary = "model/gltf-binary"
modeliges = "model/iges"
modeljt = "model/jt"
modelmesh = "model/mesh"
modelmtl = "model/mtl"
modelstep = "model/step"
modelstep_xml = "model/step+xml"
modelstep_zip = "model/step+zip"
modelstepxml_zip = "model/step-xml+zip"
modelstl = "model/stl"
modelu3d = "model/u3d"
modelvndbary = "model/vnd.bary"
modelvndcld = "model/vnd.cld"
modelvndcollada_xml = "model/vnd.collada+xml"
modelvnddwf = "model/vnd.dwf"
modelvndgdl = "model/vnd.gdl"
modelvndgtw = "model/vnd.gtw"
modelvndopengex = "model/vnd.opengex"
modelvndparasolidtransmitbinary = "model/vnd.parasolid.transmit.binary"
modelvndparasolidtransmittext = "model/vnd.parasolid.transmit.text"
modelvndpythapyox = "model/vnd.pytha.pyox"
modelvndsapvds = "model/vnd.sap.vds"
modelvndusda = "model/vnd.usda"
modelvndusdz_zip = "model/vnd.usdz+zip"
modelvndvalvesourcecompiledmap = "model/vnd.valve.source.compiled-map"
modelvndvtu = "model/vnd.vtu"
modelvrml = "model/vrml"
modelx3d_binary = "model/x3d+binary"
modelx3d_vrml = "model/x3d+vrml"
modelx3d_xml = "model/x3d+xml"
mods = "mods"
mof = "mof"
moov = "moov"
mount = "mount"
mov = "mov"
movie = "movie"
mp = "mp"
mp2 = "mp2"
mp21 = "mp21"
mp2a = "mp2a"
mp3 = "mp3"
mp4 = "mp4"
mp4a = "mp4a"
mp4s = "mp4s"
mp4v = "mp4v"
mpc = "mpc"
mpd = "mpd"
mpe = "mpe"
mpeg = "mpeg"
mpf = "mpf"
mpg = "mpg"
mpg4 = "mpg4"
mpga = "mpga"
mpkg = "mpkg"
mpl = "mpl"
mpls = "mpls"
mpm = "mpm"
mpn = "mpn"
mpp = "mpp"
mpt = "mpt"
mpy = "mpy"
mqy = "mqy"
mrc = "mrc"
mrcx = "mrcx"
mrl = "mrl"
mrml = "mrml"
mrpack = "mrpack"
mrw = "mrw"
ms = "ms"
mscml = "mscml"
mseed = "mseed"
mseq = "mseq"
msf = "msf"
msg = "msg"
msh = "msh"
msi = "msi"
msix = "msix"
msixbundle = "msixbundle"
msl = "msl"
msm = "msm"
msod = "msod"
msp = "msp"
msty = "msty"
msu = "msu"
msx = "msx"
mtl = "mtl"
mtm = "mtm"
mts = "mts"
mup = "mup"
mus = "mus"
musd = "musd"
musicthumbsdb = "musicthumbsdb"
musicxml = "musicxml"
mvb = "mvb"
mvt = "mvt"
mwf = "mwf"
mxf = "mxf"
mxl = "mxl"
mxmf = "mxmf"
mxml = "mxml"
mxs = "mxs"
mxu = "mxu"
n3 = "n3"
n64 = "n64"
nb = "nb"
nbp = "nbp"
nc = "nc"
ncx = "ncx"
nds = "nds"
nef = "nef"
nes = "nes"
nez = "nez"
nfo = "nfo"
ngage = "n-gage"
ngc = "ngc"
ngdat = "ngdat"
ngp = "ngp"
nim = "nim"
nimble = "nimble"
nims = "nims"
nitf = "nitf"
nix = "nix"
nlu = "nlu"
nml = "nml"
nnd = "nnd"
nns = "nns"
nnw = "nnw"
npx = "npx"
nq = "nq"
nrw = "nrw"
nsc = "nsc"
nsf = "nsf"
nsv = "nsv"
nt = "nt"
ntar = "ntar"
ntf = "ntf"
nu = "nu"
numbers = "numbers"
nzb = "nzb"
o = "o"
oa2 = "oa2"
oa3 = "oa3"
oas = "oas"
obd = "obd"
obgx = "obgx"
obj = "obj"
ocl = "ocl"
ocx = "ocx"
oda = "oda"
odb = "odb"
odc = "odc"
odf = "odf"
odft = "odft"
odg = "odg"
odi = "odi"
odm = "odm"
odp = "odp"
ods = "ods"
odt = "odt"
oga = "oga"
ogex = "ogex"
ogg = "ogg"
ogm = "ogm"
ogv = "ogv"
ogx = "ogx"
old = "old"
oleo = "oleo"
omdoc = "omdoc"
one = "one"
onea = "onea"
onepkg = "onepkg"
onetmp = "onetmp"
onetoc = "onetoc"
onetoc2 = "onetoc2"
ooc = "ooc"
openvpn = "openvpn"
opf = "opf"
opml = "opml"
oprc = "oprc"
opus = "opus"
ora = "ora"
orf = "orf"
org = "org"
osf = "osf"
osfpvg = "osfpvg"
osm = "osm"
otc = "otc"
otf = "otf"
otg = "otg"
oth = "oth"
oti = "oti"
otm = "otm"
otp = "otp"
ots = "ots"
ott = "ott"
ova = "ova"
ovf = "ovf"
ovpn = "ovpn"
owl = "owl"
owx = "owx"
oxps = "oxps"
oxt = "oxt"
p = "p"
p10 = "p10"
p12 = "p12"
p21 = "p21"
p65 = "p65"
p7b = "p7b"
p7c = "p7c"
p7m = "p7m"
p7r = "p7r"
p7s = "p7s"
p8 = "p8"
p8e = "p8e"
pac = "pac"
pack = "pack"
pages = "pages"
pak = "pak"
par2 = "par2"
parquet = "parquet"
part = "part"
pas = "pas"
pat = "pat"
patch = "patch"
path = "path"
paw = "paw"
pbd = "pbd"
pbm = "pbm"
pcap = "pcap"
pcapng = "pcapng"
pcd = "pcd"
pce = "pce"
pcf = "pcf"
pcfgz = "pcfgz"
pcfz = "pcfz"
pcl = "pcl"
pclxl = "pclxl"
pct = "pct"
pcurl = "pcurl"
pcx = "pcx"
pdb = "pdb"
pdc = "pdc"
pde = "pde"
pdf = "pdf"
pdfbz2 = "pdfbz2"
pdfgz = "pdfgz"
pdflz = "pdflz"
pdfxz = "pdfxz"
pef = "pef"
pem = "pem"
perfdata = "perfdata"
perl = "perl"
pfa = "pfa"
pfb = "pfb"
pfm = "pfm"
pfr = "pfr"
pfx = "pfx"
pgm = "pgm"
pgn = "pgn"
pgp = "pgp"
phm = "phm"
php = "php"
php3 = "php3"
php4 = "php4"
php5 = "php5"
phps = "phps"
pic = "pic"
pict = "pict"
pict1 = "pict1"
pict2 = "pict2"
pk = "pk"
pkg = "pkg"
pki = "pki"
pkipath = "pkipath"
pkpass = "pkpass"
pkpasses = "pkpasses"
pkr = "pkr"
pl = "pl"
pla = "pla"
plb = "plb"
plc = "plc"
plf = "plf"
pln = "pln"
pls = "pls"
pm = "pm"
pm6 = "pm6"
pmd = "pmd"
pml = "pml"
png = "png"
pnm = "pnm"
pntg = "pntg"
po = "po"
pod = "pod"
pomxml = "pomxml"
por = "por"
portpkg = "portpkg"
pot = "pot"
potm = "potm"
potx = "potx"
ppam = "ppam"
ppd = "ppd"
ppm = "ppm"
pps = "pps"
ppsm = "ppsm"
ppsx = "ppsx"
ppt = "ppt"
pptm = "pptm"
pptx = "pptx"
ppz = "ppz"
pqa = "pqa"
prc = "prc"
pre = "pre"
prf = "prf"
projectgodot = "projectgodot"
provx = "provx"
ps = "ps"
ps1 = "ps1"
psb = "psb"
psbz2 = "psbz2"
psd = "psd"
psf = "psf"
psfgz = "psfgz"
psflib = "psflib"
psgz = "psgz"
psid = "psid"
pskcxml = "pskcxml"
psw = "psw"
pti = "pti"
ptid = "ptid"
pub = "pub"
pvb = "pvb"
pw = "pw"
pwn = "pwn"
pxd = "pxd"
pxi = "pxi"
pxr = "pxr"
py = "py"
py2 = "py2"
py3 = "py3"
pya = "pya"
pyc = "pyc"
pyi = "pyi"
pyo = "pyo"
pyox = "pyox"
pys = "pys"
pysu = "pysu"
pyv = "pyv"
pyx = "pyx"
qam = "qam"
qbo = "qbo"
qbrew = "qbrew"
qcow = "qcow"
qcow2 = "qcow2"
qd = "qd"
qed = "qed"
qfx = "qfx"
qif = "qif"
qml = "qml"
qmlproject = "qmlproject"
qmltypes = "qmltypes"
qoi = "qoi"
qp = "qp"
qps = "qps"
qpw = "qpw"
qs = "qs"
qt = "qt"
qti = "qti"
qtif = "qtif"
qtigz = "qtigz"
qtl = "qtl"
qtvr = "qtvr"
qwd = "qwd"
qwt = "qwt"
qxb = "qxb"
qxd = "qxd"
qxl = "qxl"
qxp = "qxp"
qxt = "qxt"
ra = "ra"
raf = "raf"
ram = "ram"
raml = "raml"
rapd = "rapd"
rar = "rar"
ras = "ras"
raw = "raw"
rawdiskimage = "rawdiskimage"
rawdiskimagexz = "rawdiskimagexz"
rax = "rax"
rb = "rb"
rcprofile = "rcprofile"
rdf = "rdf"
rdfs = "rdfs"
rdz = "rdz"
readme = "readme"
reg = "reg"
rej = "rej"
relo = "relo"
rep = "rep"
res = "res"
rgb = "rgb"
rgbe = "rgbe"
rif = "rif"
rip = "rip"
ris = "ris"
rl = "rl"
rlc = "rlc"
rld = "rld"
rle = "rle"
rm = "rm"
rmail = "rmail"
rmi = "rmi"
rmj = "rmj"
rmm = "rmm"
rmp = "rmp"
rms = "rms"
rmvb = "rmvb"
rmx = "rmx"
rnc = "rnc"
rng = "rng"
roa = "roa"
roff = "roff"
ros = "ros"
rp = "rp"
rp9 = "rp9"
rpm = "rpm"
rpss = "rpss"
rpst = "rpst"
rq = "rq"
rs = "rs"
rsat = "rsat"
rsd = "rsd"
rsheet = "rsheet"
rss = "rss"
rst = "rst"
rt = "rt"
rtf = "rtf"
rtx = "rtx"
run = "run"
rusd = "rusd"
rv = "rv"
rvx = "rvx"
rw2 = "rw2"
rz = "rz"
s = "s"
s3m = "s3m"
saf = "saf"
sage = "sage"
sam = "sam"
sami = "sami"
sap = "sap"
sass = "sass"
sav = "sav"
sbml = "sbml"
sc = "sc"
scala = "scala"
scap = "scap"
scd = "scd"
scm = "scm"
scn = "scn"
sconscript = "sconscript"
sconstruct = "sconstruct"
scope = "scope"
scq = "scq"
scr = "scr"
scs = "scs"
scss = "scss"
sct = "sct"
scurl = "scurl"
sda = "sda"
sdc = "sdc"
sdd = "sdd"
sdkd = "sdkd"
sdkm = "sdkm"
sdm = "sdm"
sdp = "sdp"
sds = "sds"
sdw = "sdw"
sea = "sea"
see = "see"
seed = "seed"
sema = "sema"
semd = "semd"
semf = "semf"
senmlx = "senmlx"
sensmlx = "sensmlx"
ser = "ser"
service = "service"
setpay = "setpay"
setreg = "setreg"
settingsxml = "settingsxml"
sfc = "sfc"
sfdhdstx = "sfd-hdstx"
sfs = "sfs"
sfv = "sfv"
sg = "sg"
sgb = "sgb"
sgd = "sgd"
sgf = "sgf"
sgi = "sgi"
sgl = "sgl"
sgm = "sgm"
sgml = "sgml"
sh = "sh"
shape = "shape"
shar = "shar"
shex = "shex"
shf = "shf"
shn = "shn"
shtml = "shtml"
siag = "siag"
sid = "sid"
sieve = "sieve"
sig = "sig"
sik = "sik"
sil = "sil"
silo = "silo"
sis = "sis"
sisx = "sisx"
sit = "sit"
sitx = "sitx"
siv = "siv"
sk = "sk"
sk1 = "sk1"
skd = "skd"
skm = "skm"
skp = "skp"
skr = "skr"
skt = "skt"
sldm = "sldm"
sldx = "sldx"
slice = "slice"
slim = "slim"
slk = "slk"
slm = "slm"
sls = "sls"
slt = "slt"
sm = "sm"
smaf = "smaf"
smc = "smc"
smd = "smd"
smf = "smf"
smi = "smi"
smil = "smil"
smk = "smk"
sml = "sml"
sms = "sms"
smv = "smv"
smzip = "smzip"
snap = "snap"
snd = "snd"
snf = "snf"
so = "so"
so09 = "so09"
socket = "socket"
spc = "spc"
spd = "spd"
spdx = "spdx"
spec = "spec"
spf = "spf"
spl = "spl"
spm = "spm"
spot = "spot"
spp = "spp"
spq = "spq"
spx = "spx"
sqfs = "sqfs"
sql = "sql"
sqlite2 = "sqlite2"
sqlite3 = "sqlite3"
sqsh = "sqsh"
squashfs = "squashfs"
sr2 = "sr2"
src = "src"
srcrpm = "srcrpm"
srf = "srf"
srt = "srt"
sru = "sru"
srx = "srx"
ss = "ss"
ssa = "ssa"
ssdl = "ssdl"
sse = "sse"
ssf = "ssf"
ssml = "ssml"
st = "st"
stc = "stc"
std = "std"
step = "step"
stf = "stf"
sti = "sti"
stk = "stk"
stl = "stl"
stm = "stm"
stp = "stp"
stpnc = "stpnc"
stpx = "stpx"
stpxz = "stpxz"
stpz = "stpz"
str = "str"
stw = "stw"
sty = "sty"
styl = "styl"
stylus = "stylus"
sub = "sub"
sun = "sun"
sus = "sus"
susp = "susp"
sv = "sv"
sv4cpio = "sv4cpio"
sv4crc = "sv4crc"
svc = "svc"
svd = "svd"
svg = "svg"
svggz = "svggz"
svgz = "svgz"
svh = "svh"
swa = "swa"
swap = "swap"
swf = "swf"
swi = "swi"
swidtag = "swidtag"
swm = "swm"
sxc = "sxc"
sxd = "sxd"
sxg = "sxg"
sxi = "sxi"
sxm = "sxm"
sxw = "sxw"
sylk = "sylk"
sys = "sys"
t = "t"
t2t = "t2t"
t3 = "t3"
t38 = "t38"
taglet = "taglet"
tak = "tak"
tao = "tao"
tap = "tap"
tar = "tar"
tarbz = "tarbz"
tarbz2 = "tarbz2"
tarbz3 = "tarbz3"
target = "target"
targz = "targz"
tarlrz = "tarlrz"
tarlz = "tarlz"
tarlz4 = "tarlz4"
tarlzma = "tarlzma"
tarlzo = "tarlzo"
tarrz = "tarrz"
tarxz = "tarxz"
tarz = "tarz"
tarzst = "tarzst"
taz = "taz"
tb2 = "tb2"
tbz = "tbz"
tbz2 = "tbz2"
tbz3 = "tbz3"
tcap = "tcap"
tcl = "tcl"
td = "td"
teacher = "teacher"
tei = "tei"
teicorpus = "teicorpus"
tex = "tex"
texi = "texi"
texinfo = "texinfo"
text = "text"
textcachemanifest = "text/cache-manifest"
textcalendar = "text/calendar"
textcoffeescript = "text/coffeescript"
textcss = "text/css"
textcsv = "text/csv"
textcsvschema = "text/csv-schema"
texthtml = "text/html"
textjade = "text/jade"
textjavascript = "text/javascript"
textjscriptencode = "text/jscript.encode"
textjsx = "text/jsx"
textjulia = "text/julia"
textless = "text/less"
textmarkdown = "text/markdown"
textn3 = "text/n3"
textorg = "text/org"
textplain = "text/plain"
textprslinestag = "text/prs.lines.tag"
textrichtext = "text/richtext"
textrust = "text/rust"
textsgml = "text/sgml"
textshex = "text/shex"
textslim = "text/slim"
textspdx = "text/spdx"
textstylus = "text/stylus"
texttabseparatedvalues = "text/tab-separated-values"
texttcl = "text/tcl"
texttroff = "text/troff"
textturtle = "text/turtle"
texturilist = "text/uri-list"
textvbscript = "text/vbscript"
textvbscriptencode = "text/vbscript.encode"
textvcard = "text/vcard"
textvndcurl = "text/vnd.curl"
textvndcurldcurl = "text/vnd.curl.dcurl"
textvndcurlmcurl = "text/vnd.curl.mcurl"
textvndcurlscurl = "text/vnd.curl.scurl"
textvndfamilysearchgedcom = "text/vnd.familysearch.gedcom"
textvndfly = "text/vnd.fly"
textvndfmiflexstor = "text/vnd.fmi.flexstor"
textvndgraphviz = "text/vnd.graphviz"
textvndin3d3dml = "text/vnd.in3d.3dml"
textvndin3dspot = "text/vnd.in3d.spot"
textvndrnrealtext = "text/vnd.rn-realtext"
textvndsenxwarpscript = "text/vnd.senx.warpscript"
textvndsunj2meappdescriptor = "text/vnd.sun.j2me.app-descriptor"
textvndtypst = "text/vnd.typst"
textvndwapwml = "text/vnd.wap.wml"
textvndwapwmlscript = "text/vnd.wap.wmlscript"
textvtt = "text/vtt"
textwgsl = "text/wgsl"
textxadasrc = "text/x-adasrc"
textxasm = "text/x-asm"
textxauthors = "text/x-authors"
textxbasic = "text/x-basic"
textxbibtex = "text/x-bibtex"
textxblueprint = "text/x-blueprint"
textxc = "text/x-c"
textxc__hdr = "text/x-c++hdr"
textxc__src = "text/x-c++src"
textxchangelog = "text/x-changelog"
textxcmake = "text/x-cmake"
textxcobol = "text/x-cobol"
textxcommonlisp = "text/x-common-lisp"
textxcomponent = "text/x-component"
textxcopying = "text/x-copying"
textxcredits = "text/x-credits"
textxcrystal = "text/x-crystal"
textxcsharp = "text/x-csharp"
textxcython = "text/x-cython"
textxdbusservice = "text/x-dbus-service"
textxdcl = "text/x-dcl"
textxdevicetreebinary = "text/x-devicetree-binary"
textxdevicetreesource = "text/x-devicetree-source"
textxdockerfile = "text/x-dockerfile"
textxdsl = "text/x-dsl"
textxdsrc = "text/x-dsrc"
textxeiffel = "text/x-eiffel"
textxelixir = "text/x-elixir"
textxemacslisp = "text/x-emacs-lisp"
textxerlang = "text/x-erlang"
textxfortran = "text/x-fortran"
textxgcode = "text/x.gcode"
textxgcodegx = "text/x-gcode-gx"
textxgenie = "text/x-genie"
textxgettexttranslation = "text/x-gettext-translation"
textxgherkin = "text/x-gherkin"
textxgo = "text/x-go"
textxgooglevideopointer = "text/x-google-video-pointer"
textxgradle = "text/x-gradle"
textxgroovy = "text/x-groovy"
textxhandlebarstemplate = "text/x-handlebars-template"
textxhaskell = "text/x-haskell"
textxidl = "text/x-idl"
textximelody = "text/x-imelody"
textxinstall = "text/x-install"
textxiptables = "text/x-iptables"
textxjava = "text/x-java"
textxkaitaistruct = "text/x-kaitai-struct"
textxkotlin = "text/x-kotlin"
textxldif = "text/x-ldif"
textxlilypond = "text/x-lilypond"
textxliteratehaskell = "text/x-literate-haskell"
textxlog = "text/x-log"
textxlua = "text/x-lua"
textxmakefile = "text/x-makefile"
textxmaven_xml = "text/x-maven+xml"
textxmeson = "text/x-meson"
textxmicrodvd = "text/x-microdvd"
textxmoc = "text/x-moc"
textxmof = "text/x-mof"
textxmpl2 = "text/x-mpl2"
textxmrml = "text/x-mrml"
textxmsregedit = "text/x-ms-regedit"
textxmup = "text/x-mup"
textxnfo = "text/x-nfo"
textxnim = "text/x-nim"
textxnimscript = "text/x-nimscript"
textxnix = "text/x-nix"
textxobjc__src = "text/x-objc++src"
textxobjcsrc = "text/x-objcsrc"
textxocaml = "text/x-ocaml"
textxocl = "text/x-ocl"
textxooc = "text/x-ooc"
textxopenclsrc = "text/x-opencl-src"
textxopml_xml = "text/x-opml+xml"
textxpascal = "text/x-pascal"
textxpatch = "text/x-patch"
textxprocessing = "text/x-processing"
textxpython = "text/x-python"
textxpython2 = "text/x-python2"
textxpython3 = "text/x-python3"
textxqml = "text/x-qml"
textxreadme = "text/x-readme"
textxreject = "text/x-reject"
textxrpmspec = "text/x-rpm-spec"
textxrst = "text/x-rst"
textxsagemath = "text/x-sagemath"
textxsass = "text/x-sass"
textxscala = "text/x-scala"
textxscheme = "text/x-scheme"
textxscons = "text/x-scons"
textxscss = "text/x-scss"
textxsetext = "text/x-setext"
textxsfv = "text/x-sfv"
textxssa = "text/x-ssa"
textxsuseymp = "text/x-suse-ymp"
textxsvhdr = "text/x-svhdr"
textxsvsrc = "text/x-svsrc"
textxsystemdunit = "text/x-systemd-unit"
textxtex = "text/x-tex"
textxtexinfo = "text/x-texinfo"
textxtodotxt = "text/x-todo-txt"
textxtroffme = "text/x-troff-me"
textxtroffms = "text/x-troff-ms"
textxtwig = "text/x-twig"
textxtxt2tags = "text/x-txt2tags"
textxuil = "text/x-uil"
textxuuencode = "text/x-uuencode"
textxvala = "text/x-vala"
textxverilog = "text/x-verilog"
textxvhdl = "text/x-vhdl"
textxxmi = "text/x-xmi"
textxxslfo = "text/x-xslfo"
tfi = "tfi"
tfm = "tfm"
tfx = "tfx"
tga = "tga"
tgz = "tgz"
theme = "theme"
themepack = "themepack"
thmx = "thmx"
thumbsdb = "thumbsdb"
tif = "tif"
tiff = "tiff"
timer = "timer"
tk = "tk"
tlrz = "tlrz"
tlz = "tlz"
tmo = "tmo"
tmx = "tmx"
tnef = "tnef"
tnf = "tnf"
toc = "toc"
todotxt = "todotxt"
toml = "toml"
torrent = "torrent"
tpic = "tpic"
tpl = "tpl"
tpt = "tpt"
tr = "tr"
tra = "tra"
tres = "tres"
trig = "trig"
trm = "trm"
trz = "trz"
ts = "ts"
tscn = "tscn"
tsd = "tsd"
tsv = "tsv"
tsx = "tsx"
tta = "tta"
ttc = "ttc"
ttf = "ttf"
ttl = "ttl"
ttml = "ttml"
ttx = "ttx"
tvthumbdb = "tvthumbdb"
twd = "twd"
twds = "twds"
twig = "twig"
txd = "txd"
txf = "txf"
txt = "txt"
txz = "txz"
typ = "typ"
tzo = "tzo"
tzst = "tzst"
u32 = "u32"
u3d = "u3d"
u8dsn = "u8dsn"
u8hdr = "u8hdr"
u8mdn = "u8mdn"
u8msg = "u8msg"
ubj = "ubj"
udeb = "udeb"
ufd = "ufd"
ufdl = "ufdl"
ufraw = "ufraw"
ui = "ui"
uil = "uil"
ult = "ult"
ulx = "ulx"
umj = "umj"
unf = "unf"
uni = "uni"
unif = "unif"
unityweb = "unityweb"
uo = "uo"
uoml = "uoml"
uri = "uri"
uris = "uris"
url = "url"
urls = "urls"
usda = "usda"
usdz = "usdz"
ustar = "ustar"
utz = "utz"
uu = "uu"
uue = "uue"
uva = "uva"
uvd = "uvd"
uvf = "uvf"
uvg = "uvg"
uvh = "uvh"
uvi = "uvi"
uvm = "uvm"
uvp = "uvp"
uvs = "uvs"
uvt = "uvt"
uvu = "uvu"
uvv = "uvv"
uvva = "uvva"
uvvd = "uvvd"
uvvf = "uvvf"
uvvg = "uvvg"
uvvh = "uvvh"
uvvi = "uvvi"
uvvm = "uvvm"
uvvp = "uvvp"
uvvs = "uvvs"
uvvt = "uvvt"
uvvu = "uvvu"
uvvv = "uvvv"
uvvx = "uvvx"
uvvz = "uvvz"
uvx = "uvx"
uvz = "uvz"
v = "v"
v64 = "v64"
vala = "vala"
vapi = "vapi"
vb = "vb"
vbe = "vbe"
vbox = "vbox"
vboxextpack = "vbox-extpack"
vbs = "vbs"
vcard = "vcard"
vcd = "vcd"
vcf = "vcf"
vcg = "vcg"
vcs = "vcs"
vct = "vct"
vcx = "vcx"
vda = "vda"
vdi = "vdi"
vds = "vds"
vdx = "vdx"
vhd = "vhd"
vhdl = "vhdl"
vhdx = "vhdx"
video3gpp = "video/3gpp"
video3gpp2 = "video/3gpp2"
videoannodex = "video/annodex"
videodb = "videodb"
videodv = "video/dv"
videoh261 = "video/h261"
videoh263 = "video/h263"
videoh264 = "video/h264"
videoisosegment = "video/iso.segment"
videojpeg = "video/jpeg"
videomj2 = "video/mj2"
videomp2t = "video/mp2t"
videomp4 = "video/mp4"
videompeg = "video/mpeg"
videoogg = "video/ogg"
videoquicktime = "video/quicktime"
videovndavi = "video/vnd.avi"
videovnddecehd = "video/vnd.dece.hd"
videovnddecemobile = "video/vnd.dece.mobile"
videovnddecepd = "video/vnd.dece.pd"
videovnddecesd = "video/vnd.dece.sd"
videovnddecevideo = "video/vnd.dece.video"
videovnddvbfile = "video/vnd.dvb.file"
videovndfvt = "video/vnd.fvt"
videovndmpegurl = "video/vnd.mpegurl"
videovndmsplayreadymediapyv = "video/vnd.ms-playready.media.pyv"
videovndradgamettoolsbink = "video/vnd.radgamettools.bink"
videovndradgamettoolssmacker = "video/vnd.radgamettools.smacker"
videovndrnrealvideo = "video/vnd.rn-realvideo"
videovnduvvump4 = "video/vnd.uvvu.mp4"
videovndvivo = "video/vnd.vivo"
videovndyoutubeyt = "video/vnd.youtube.yt"
videowebm = "video/webm"
videoxanim = "video/x-anim"
videoxflic = "video/x-flic"
videoxflv = "video/x-flv"
videoxjavafx = "video/x-javafx"
videoxmatroska = "video/x-matroska"
videoxmatroska3d = "video/x-matroska-3d"
videoxmjpeg = "video/x-mjpeg"
videoxmng = "video/x-mng"
videoxmswm = "video/x-ms-wm"
videoxmswmv = "video/x-ms-wmv"
videoxnsv = "video/x-nsv"
videoxogm_ogg = "video/x-ogm+ogg"
videoxsgimovie = "video/x-sgi-movie"
videoxsmv = "video/x-smv"
vis = "vis"
viv = "viv"
vivo = "vivo"
vlc = "vlc"
vmdk = "vmdk"
vob = "vob"
voc = "voc"
vor = "vor"
vox = "vox"
vpc = "vpc"
vrm = "vrm"
vrml = "vrml"
vsd = "vsd"
vsdm = "vsdm"
vsdx = "vsdx"
vsf = "vsf"
vss = "vss"
vssm = "vssm"
vssx = "vssx"
vst = "vst"
vstm = "vstm"
vstx = "vstx"
vsw = "vsw"
vtf = "vtf"
vtt = "vtt"
vtu = "vtu"
vtx = "vtx"
vxml = "vxml"
w3d = "w3d"
wad = "wad"
wadl = "wadl"
war = "war"
wasm = "wasm"
wav = "wav"
wax = "wax"
wb1 = "wb1"
wb2 = "wb2"
wb3 = "wb3"
wbmp = "wbmp"
wbs = "wbs"
wbxml = "wbxml"
wcm = "wcm"
wdb = "wdb"
wdp = "wdp"
weba = "weba"
webapp = "webapp"
webm = "webm"
webmanifest = "webmanifest"
webp = "webp"
wg = "wg"
wgsl = "wgsl"
wgt = "wgt"
wif = "wif"
wim = "wim"
winmaildat = "winmaildat"
wk1 = "wk1"
wk3 = "wk3"
wk4 = "wk4"
wkdownload = "wkdownload"
wks = "wks"
wm = "wm"
wma = "wma"
wmd = "wmd"
wmf = "wmf"
wml = "wml"
wmlc = "wmlc"
wmls = "wmls"
wmlsc = "wmlsc"
wmv = "wmv"
wmx = "wmx"
wmz = "wmz"
woff = "woff"
woff2 = "woff2"
wp = "wp"
wp4 = "wp4"
wp5 = "wp5"
wp6 = "wp6"
wpd = "wpd"
wpg = "wpg"
wpl = "wpl"
wpp = "wpp"
wps = "wps"
wqd = "wqd"
wri = "wri"
wrl = "wrl"
ws = "ws"
wsc = "wsc"
wsdl = "wsdl"
wsgi = "wsgi"
wspolicy = "wspolicy"
wtb = "wtb"
wv = "wv"
wvc = "wvc"
wvp = "wvp"
wvx = "wvx"
wwf = "wwf"
x_b = "x_b"
x_t = "x_t"
x32 = "x32"
x3d = "x3d"
x3db = "x3db"
x3dbz = "x3dbz"
x3dv = "x3dv"
x3dvz = "x3dvz"
x3dz = "x3dz"
x3f = "x3f"
xac = "xac"
xaml = "xaml"
xap = "xap"
xar = "xar"
xav = "xav"
xbap = "xbap"
xbd = "xbd"
xbel = "xbel"
xbl = "xbl"
xbm = "xbm"
xca = "xca"
xcf = "xcf"
xcfbz2 = "xcfbz2"
xcfgz = "xcfgz"
xci = "xci"
xconferencexcooltalk = "x-conference/x-cooltalk"
xcs = "xcs"
xdcf = "xdcf"
xdf = "xdf"
xdgapp = "xdgapp"
xdm = "xdm"
xdp = "xdp"
xdssc = "xdssc"
xdw = "xdw"
xel = "xel"
xenc = "xenc"
xepocxsisxapp = "x-epoc/x-sisx-app"
xer = "xer"
xfdf = "xfdf"
xfdl = "xfdl"
xhe = "xhe"
xht = "xht"
xhtm = "xhtm"
xhtml = "xhtml"
xhvml = "xhvml"
xi = "xi"
xif = "xif"
xla = "xla"
xlam = "xlam"
xlc = "xlc"
xld = "xld"
xlf = "xlf"
xliff = "xliff"
xll = "xll"
xlm = "xlm"
xlr = "xlr"
xls = "xls"
xlsb = "xlsb"
xlsm = "xlsm"
xlsx = "xlsx"
xlt = "xlt"
xltm = "xltm"
xltx = "xltx"
xlw = "xlw"
xm = "xm"
xmf = "xmf"
xmi = "xmi"
xml = "xml"
xns = "xns"
xo = "xo"
xop = "xop"
xpi = "xpi"
xpl = "xpl"
xpm = "xpm"
xpr = "xpr"
xps = "xps"
xpw = "xpw"
xpx = "xpx"
xsd = "xsd"
xsf = "xsf"
xsl = "xsl"
xslfo = "xslfo"
xslt = "xslt"
xsm = "xsm"
xspf = "xspf"
xul = "xul"
xvm = "xvm"
xvml = "xvml"
xwd = "xwd"
xyz = "xyz"
xyze = "xyze"
xz = "xz"
yaml = "yaml"
yang = "yang"
yin = "yin"
yml = "yml"
ymp = "ymp"
yt = "yt"
z = "z"
z1 = "z1"
z2 = "z2"
z3 = "z3"
z4 = "z4"
z5 = "z5"
z6 = "z6"
z64 = "z64"
z7 = "z7"
z8 = "z8"
zabw = "zabw"
zaz = "zaz"
zim = "zim"
zip = "zip"
zipx = "zipx"
zir = "zir"
zirz = "zirz"
zmm = "zmm"
zoo = "zoo"
zpaq = "zpaq"
zsav = "zsav"
zst = "zst"
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
    if extension == xdcf:
        return applicationvndgovskxmldatacontainer_xml

    # iana
    if extension == xcs:
        return applicationcalendar_xml

    if extension == xci:
        return applicationxnintendoswitchxci

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

    if extension == wsgi:
        return textxpython

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

    if extension in (wb1, wb2, wb3, qpw):
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

    if extension in (vsd, vst, vsw, vss, vtx):
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

    if extension == vdx:
        return applicationvndmsvisioviewer

    # iana
    if extension == vds:
        return modelvndsapvds

    if extension == vdi:
        return applicationxvdidisk

    # iana
    if extension == vcx:
        return applicationvndvcx

    if extension in (vcs, ics, ifb, icalendar):
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
        return textvndtypst

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

    if extension in (tarrz, trz):
        return applicationxrzipcompressedtar

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
        return applicationxsylk

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

    if extension in (step, stp, stpnc, p21, _210):
        return modelstep

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
        return applicationxstarmath

    if extension == smd:
        return applicationxstarmail

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

    if extension == sgl:
        return applicationxstarwriterglobal

    if extension == sgi:
        return imagexsgi

    if extension == sgf:
        return applicationxgosgf

    if extension == sg:
        return applicationxsg1000rom

    # apache
    if extension == sfv:
        return textxsfv

    if extension in (sfs, sqfs, sqsh, squashfs):
        return applicationvndsquashfs

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

    if extension in (sdw, vor):
        return applicationxstarwriter

    if extension == sds:
        return applicationxstarchart

    if extension == sdp:
        return applicationvndstardivisionimpresspacked

    if extension == sdm:
        return applicationvndstardivisionmail

    # iana
    if extension in (sdkm, sdkd):
        return applicationvndsolentsdkm_xml

    if extension == sdd:
        return applicationxstarimpress

    if extension == sdc:
        return applicationxstarcalc

    if extension == sda:
        return applicationxstardraw

    # apache
    if extension == scurl:
        return textvndcurlscurl

    if extension == sct:
        return imagexsct

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

    if extension == rz:
        return applicationxrzip

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

    if extension in (qwd, qwt, qxb, qxd, qxl, qxp, qxt):
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

    if extension == qbrew:
        return applicationxqbrew

    # iana
    if extension == qbo:
        return applicationvndintuqbo

    # iana
    if extension == qam:
        return applicationvndepsonquickanime

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

    if extension == py2:
        return textxpython2

    if extension in (py, py3, pyi):
        return textxpython3

    if extension == pxr:
        return imagexpxr

    if extension in (pxd, pxi, pyx):
        return textxcython

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

    if extension == pkpasses:
        return applicationvndapplepkpasses

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

    if extension == phm:
        return imagexphm

    if extension in (pgp, gpg, asc):
        return applicationpgpencrypted

    if extension == pgn:
        return applicationvndchesspgn

    if extension == pgm:
        return imagexportablegraymap

    if extension == pfr:
        return applicationfonttdpfr

    if extension == pfm:
        return imagexpfm

    if extension in (pfa, pfb, gsf):
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

    if extension in (pct, pict, pict1, pict2):
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

    if extension in (pcapng, scap, ntar):
        return applicationxpcapng

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

    if extension == parquet:
        return applicationvndapacheparquet

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

    if extension == otm:
        return applicationvndoasisopendocumenttextmastertemplate

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
    if extension in (onetoc, onetoc2, onetmp, onepkg, one, onea):
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
        return applicationvndoasisopendocumentbase

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

    if extension == nix:
        return textxnix

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

    if extension == msu:
        return applicationmicrosoftupdate

    # iana
    if extension == msty:
        return applicationvndmuveestyle

    if extension == msp:
        return applicationmicrosoftpatch

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

    if extension in (mp4, m4v, f4v, lrv, lrf, mp4v):
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

    if extension in (mkd, markdown):
        return textmarkdown

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

    if extension in (m2t, m2ts, cpi, clpi, mpls, bdm, bdmv):
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

    if extension == lottie:
        return applicationzip_dotlottie

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

    # iana
    if extension == jais:
        return imagejais

    # iana
    if extension == jaii:
        return imagejaii

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

    if extension == hta:
        return applicationhta

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

    if extension in (hdr, pic, rgbe, xyze):
        return imagevndradiance

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

    if extension == gsite:
        return applicationvndgoogleappssite

    if extension == gsheet:
        return applicationvndgoogleappsspreadsheet

    if extension == gscript:
        return applicationvndgoogleappsscript

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

    if extension == gmap:
        return applicationvndgoogleappsmap

    if extension == gltf:
        return modelgltf_json

    if extension == glb:
        return modelgltfbinary

    if extension == glade:
        return applicationxglade

    if extension == gjam:
        return applicationvndgoogleappsjam

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
    if extension == ggs:
        return applicationvndgeogebraslides

    # iana
    if extension == ggb:
        return applicationvndgeogebrafile

    if extension == gg:
        return applicationxgamegearrom

    if extension == gform:
        return applicationvndgoogleappsform

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

    if extension in (gen, md, sgd):
        return applicationxgenesisrom

    if extension in (ged, gedcom):
        return textvndfamilysearchgedcom

    if extension == gdshader:
        return applicationxgodotshader

    if extension == gdraw:
        return applicationvndgoogleappsdrawing

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

    if extension == fbx:
        return applicationvndautodeskfbx

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

    if extension in (efi, ocx, sys):
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

    if extension == drm:
        return applicationvndprocreatedream

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

    if extension == dockerfile:
        return textxdockerfile

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

    # iana
    if extension == dcmp:
        return applicationvnddcmp_xml

    if extension == dcl:
        return textxdcl

    if extension in (dbk, docbook):
        return applicationdocbook_xml

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

    if extension in (cts, mts, ts):
        return applicationtypescript

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

    if extension in (cjs, js, jsm, mjs):
        return textjavascript

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

    if extension in (cel, kcf):
        return imagexkisscel

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

    if extension == bst:
        return applicationbuildstream_yaml

    # iana
    if extension == bsp:
        return modelvndvalvesourcecompiledmap

    if extension == bsdiff:
        return applicationxbsdiff

    if extension == brushset:
        return applicationvndprocratebrushset

    if extension == brush:
        return applicationvndprocreatebrush

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
    if extension in (bin, dms, mar, dist, distz, bpk, dump, elc, deploy, msm, buffer):
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

    # iana
    if extension == bdo:
        return applicationvndnatobindingdataobject_xml

    if extension == bdf:
        return applicationxfontbdf

    if extension == bcpio:
        return applicationxbcpio

    if extension == bat:
        return applicationxbat

    if extension == bas:
        return textxbasic

    # iana
    if extension == bary:
        return modelvndbary

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

    if extension in (asm, s):
        return textxasm

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

    if extension in (a, ar, lib):
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

    if mimeType == applicationvndgovskxmldatacontainer_xml:
        return [ "xdcf" ]

    if mimeType == applicationcalendar_xml:
        return [ "xcs" ]

    if mimeType == applicationxnintendoswitchxci:
        return [ "xci" ]

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

    if mimeType == textxpython:
        return [ "wsgi" ]

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
        return [ "wb1", "wb2", "wb3", "qpw" ]

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
        return [ "vsd", "vst", "vsw", "vss", "vtx" ]

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

    if mimeType == applicationvndmsvisioviewer:
        return [ "vdx" ]

    if mimeType == modelvndsapvds:
        return [ "vds" ]

    if mimeType == applicationxvdidisk:
        return [ "vdi" ]

    if mimeType == applicationvndvcx:
        return [ "vcx" ]

    if mimeType == textcalendar:
        return [ "vcs", "ics", "ifb", "icalendar" ]

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

    if mimeType == textvndtypst:
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

    if mimeType == applicationxrzipcompressedtar:
        return [ "tarrz", "trz" ]

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

    if mimeType == applicationxsylk:
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

    if mimeType == modelstep:
        return [ "step", "stp", "stpnc", "p21", "210" ]

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

    if mimeType == applicationxstarmath:
        return [ "smf" ]

    if mimeType == applicationxstarmail:
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

    if mimeType == applicationxstarwriterglobal:
        return [ "sgl" ]

    if mimeType == imagexsgi:
        return [ "sgi" ]

    if mimeType == applicationxgosgf:
        return [ "sgf" ]

    if mimeType == applicationxsg1000rom:
        return [ "sg" ]

    if mimeType == textxsfv:
        return [ "sfv" ]

    if mimeType == applicationvndsquashfs:
        return [ "sfs", "sqfs", "sqsh", "squashfs" ]

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

    if mimeType == applicationxstarwriter:
        return [ "sdw", "vor" ]

    if mimeType == applicationxstarchart:
        return [ "sds" ]

    if mimeType == applicationvndstardivisionimpresspacked:
        return [ "sdp" ]

    if mimeType == applicationvndstardivisionmail:
        return [ "sdm" ]

    if mimeType == applicationvndsolentsdkm_xml:
        return [ "sdkm", "sdkd" ]

    if mimeType == applicationxstarimpress:
        return [ "sdd" ]

    if mimeType == applicationxstarcalc:
        return [ "sdc" ]

    if mimeType == applicationxstardraw:
        return [ "sda" ]

    if mimeType == textvndcurlscurl:
        return [ "scurl" ]

    if mimeType == imagexsct:
        return [ "sct" ]

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

    if mimeType == applicationxrzip:
        return [ "rz" ]

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
        return [ "qwd", "qwt", "qxb", "qxd", "qxl", "qxp", "qxt" ]

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

    if mimeType == applicationxqbrew:
        return [ "qbrew" ]

    if mimeType == applicationvndintuqbo:
        return [ "qbo" ]

    if mimeType == applicationvndepsonquickanime:
        return [ "qam" ]

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

    if mimeType == textxpython2:
        return [ "py2" ]

    if mimeType == textxpython3:
        return [ "py", "py3", "pyi" ]

    if mimeType == imagexpxr:
        return [ "pxr" ]

    if mimeType == textxcython:
        return [ "pxd", "pxi", "pyx" ]

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

    if mimeType == applicationvndapplepkpasses:
        return [ "pkpasses" ]

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

    if mimeType == imagexphm:
        return [ "phm" ]

    if mimeType == applicationpgpencrypted:
        return [ "pgp", "gpg", "asc" ]

    if mimeType == applicationvndchesspgn:
        return [ "pgn" ]

    if mimeType == imagexportablegraymap:
        return [ "pgm" ]

    if mimeType == applicationfonttdpfr:
        return [ "pfr" ]

    if mimeType == imagexpfm:
        return [ "pfm" ]

    if mimeType == applicationxfonttype1:
        return [ "pfa", "pfb", "gsf" ]

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
        return [ "pct", "pict", "pict1", "pict2" ]

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

    if mimeType == applicationxpcapng:
        return [ "pcapng", "scap", "ntar" ]

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

    if mimeType == applicationvndapacheparquet:
        return [ "parquet" ]

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

    if mimeType == applicationvndoasisopendocumenttextmastertemplate:
        return [ "otm" ]

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
        return [ "onetoc", "onetoc2", "onetmp", "onepkg", "one", "onea" ]

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

    if mimeType == applicationvndoasisopendocumentbase:
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

    if mimeType == textxnix:
        return [ "nix" ]

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

    if mimeType == applicationmicrosoftupdate:
        return [ "msu" ]

    if mimeType == applicationvndmuveestyle:
        return [ "msty" ]

    if mimeType == applicationmicrosoftpatch:
        return [ "msp" ]

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
        return [ "mp4", "m4v", "f4v", "lrv", "lrf", "mp4v" ]

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

    if mimeType == textmarkdown:
        return [ "mkd", "markdown" ]

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
        return [ "m2t", "m2ts", "cpi", "clpi", "mpls", "bdm", "bdmv" ]

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

    if mimeType == applicationzip_dotlottie:
        return [ "lottie" ]

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

    if mimeType == imagejais:
        return [ "jais" ]

    if mimeType == imagejaii:
        return [ "jaii" ]

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

    if mimeType == applicationhta:
        return [ "hta" ]

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

    if mimeType == imagevndradiance:
        return [ "hdr", "pic", "rgbe", "xyze" ]

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

    if mimeType == applicationvndgoogleappssite:
        return [ "gsite" ]

    if mimeType == applicationvndgoogleappsspreadsheet:
        return [ "gsheet" ]

    if mimeType == applicationvndgoogleappsscript:
        return [ "gscript" ]

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

    if mimeType == applicationvndgoogleappsmap:
        return [ "gmap" ]

    if mimeType == modelgltf_json:
        return [ "gltf" ]

    if mimeType == modelgltfbinary:
        return [ "glb" ]

    if mimeType == applicationxglade:
        return [ "glade" ]

    if mimeType == applicationvndgoogleappsjam:
        return [ "gjam" ]

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

    if mimeType == applicationvndgeogebraslides:
        return [ "ggs" ]

    if mimeType == applicationvndgeogebrafile:
        return [ "ggb" ]

    if mimeType == applicationxgamegearrom:
        return [ "gg" ]

    if mimeType == applicationvndgoogleappsform:
        return [ "gform" ]

    if mimeType == applicationxtexgf:
        return [ "gf" ]

    if mimeType == applicationvndgeometryexplorer:
        return [ "gex", "gre" ]

    if mimeType == applicationgeo_json:
        return [ "geojson" ]

    if mimeType == applicationvnddynageo:
        return [ "geo" ]

    if mimeType == applicationxgenesisrom:
        return [ "gen", "md", "sgd" ]

    if mimeType == textvndfamilysearchgedcom:
        return [ "ged", "gedcom" ]

    if mimeType == applicationxgodotshader:
        return [ "gdshader" ]

    if mimeType == applicationvndgoogleappsdrawing:
        return [ "gdraw" ]

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

    if mimeType == applicationvndautodeskfbx:
        return [ "fbx" ]

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
        return [ "efi", "ocx", "sys" ]

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

    if mimeType == applicationvndprocreatedream:
        return [ "drm" ]

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

    if mimeType == textxdockerfile:
        return [ "dockerfile" ]

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

    if mimeType == applicationvnddcmp_xml:
        return [ "dcmp" ]

    if mimeType == textxdcl:
        return [ "dcl" ]

    if mimeType == applicationdocbook_xml:
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

    if mimeType == applicationtypescript:
        return [ "cts", "mts", "ts" ]

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

    if mimeType == textjavascript:
        return [ "cjs", "js", "jsm", "mjs" ]

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

    if mimeType == imagexkisscel:
        return [ "cel", "kcf" ]

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

    if mimeType == applicationbuildstream_yaml:
        return [ "bst" ]

    if mimeType == modelvndvalvesourcecompiledmap:
        return [ "bsp" ]

    if mimeType == applicationxbsdiff:
        return [ "bsdiff" ]

    if mimeType == applicationvndprocratebrushset:
        return [ "brushset" ]

    if mimeType == applicationvndprocreatebrush:
        return [ "brush" ]

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
        return [ "bin", "dms", "mar", "dist", "distz", "bpk", "dump", "elc", "deploy", "msm", "buffer" ]

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

    if mimeType == applicationvndnatobindingdataobject_xml:
        return [ "bdo" ]

    if mimeType == applicationxfontbdf:
        return [ "bdf" ]

    if mimeType == applicationxbcpio:
        return [ "bcpio" ]

    if mimeType == applicationxbat:
        return [ "bat" ]

    if mimeType == textxbasic:
        return [ "bas" ]

    if mimeType == modelvndbary:
        return [ "bary" ]

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

    if mimeType == textxasm:
        return [ "asm", "s" ]

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
        return [ "a", "ar", "lib" ]

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