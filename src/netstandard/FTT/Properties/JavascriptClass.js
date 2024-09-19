//constants

function __getExt(fileName) {
  if (fileName.indexOf('.') >= 0) return fileName.split('.')[1].toLowerCase();
  else return fileName.toLowerCase();
}

//Methods for translating between mime-types and file extensions
/**
 * Returns the mime type for the given file name
 * @param {String} fileName - A file name, file extension or file path specification
 */
function getMimeType(fileName) {
  let extension = __getExt(fileName)
  //getMimeType body
}
/**
 * Returns a list of possible file extensions for the given mime type
 * @param {String} mimeType - A mime Type
 * @returns
 */
function getMimeTypeFileExtensions(mimeType) {
  //getMimeTypeFileExtensions body

  return [];
}

/**
 * Returns a file category for the given file name
 * @param {String} fileName - A file name, file extension or file path specification
 * @returns
 */
function getFileCategory(fileName) {
  let extension = __getExt(fileName)
  if ([_7z, '7zip', ace, air, apk, appxbundle, arc, arj, 'asec', 'bar', bz2, 'bzip', cab, cso, deb, 'dlc', dmg, gz, 'gzip', hqx, 'inv', 'ipa', iso, 'isz', jar, msu, 'nbh', pak, rar, rpm, sis, sisx, sit, 'sitd', sitx, tar, targz, tgz, 'webarchive', xap, z, zip].includes(extension))
    return FileCategory.Archive

  if ([_3ga, aac, aiff, amr, ape, 'arf', asf, asx, 'cda', 'dvf', flac, 'gp4', 'gp5', gpx, 'logic', m4a, m4b, m4p, midi, mp3, ogg, 'pcm', 'rec', snd, 'sng', 'uax', wav, wma, wpl, 'zab'].includes(extension))
    return FileCategory.Audio

  if ([_as, asm, asp, 'aspx', bat, c, 'cp', cpp, cs, css, gradle, htm, 'inc', jad, java, js, json, 'jsp', lib, m, 'matlab', ml, o, perl, php, pl, ps1, py, rb, 'rc', rss, 'scpt', sh, sql, src, 'swift', vb, vbs, ws, xaml, 'xcodeproj', xml, xsd, xsl, xslt, yml].includes(extension))
    return FileCategory.Code

  if ([abw, 'aww', azw, azw3, 'azw4', cbr, cbz, chm, 'cnt', 'dbx', djvu, doc, docm, docx, dot, dotm, dotx, epub, fb2, 'iba', 'ibooks', 'ind', 'indd', 'lit', mht, mobi, mpp, odf, odt, ott, pages, pmd, 'prn', 'prproj', ps, pub, 'pwi', rep, rtf, sdd, sdw, 'shs', 'snp', sxw, tpl, vsd, 'wlmp', wpd, wps, wri].includes(extension))
    return FileCategory.Document

  if ([bmp, cpt, dds, dib, dng, 'dt2', emf, gif, ico, 'icon', icns, jpeg, jpg, pcx, pic, png, psd, 'psdx', raw, tga, 'thm', tif, tiff, wbmp, wdp, webp].includes(extension))
    return FileCategory.Image

  if ([oxps, pdf, xps].includes(extension))
    return FileCategory.PDF

  if ([key, 'keynote', pot, potx, pps, ppsx, ppt, pptm, pptx].includes(extension))
    return FileCategory.Presentation

  if ([ods, numbers, sdc, xls, xlsx, xlsb].includes(extension))
    return FileCategory.Spreadsheet

  if (['alx', application, csv, 'eng', html, log, 'lrc', 'lst', nfo, opml, 'plist', reg, srt, sub, 'tbl', text, txt].includes(extension))
    return FileCategory.Text

  if (['264', _3g2, _3gp, avi, bik, 'dash', 'dat', 'dvr', flv, h264, m2t, m2ts, m4v, mkv, mod, mov, mp4, mpeg, mpg, 'mswmm', mts, ogv, rmvb, swf, 'tod', 'tp', ts, vob, webm, wmv].includes(extension))
    return FileCategory.Video

  return FileCategory.Binary
}

const FTT = {
  getMimeType,
  getMimeTypeFileExtensions,
  getFileCategory,
}

const FileCategory = {
  /**
   * Any file that can be extracted into several files
   */
  Archive: 'Archive',
  /**
   * Any file that can only contain an audio stream
   */
  Audio: 'Audio',
  /**
   * Any file that is unclassified or does not have a text representation
   */
  Binary: 'Binary',
  /**
   * Any file that contains instructions that are compilable or machine-readable
   */
  Code: 'Code',
  /**
   * Any file that is designed for conveying structured information between people
   */
  Document: 'Document',
  /**
   * Any file that can only contain a single image or series of images
   */
  Image: 'Image',
  /**
   * Any file that is considered a document archive format
   */
  PDF: 'PDF',
  /**
   * Any file that is designed for electronic presentations consisting of a series of separate pages or slides
   */
  Presentation: 'Presentation',
  /**
   * Any file in which data is arranged in rows and columns and can be manipulated and used in calculations
   */
  Spreadsheet: 'Spreadsheet',
  /**
   * Any file that is not classified under another category and is not binary
   */
  Text: 'Text',
  /**
   * Any file that is designed to be a container for a video stream
   */
  Video: 'Video',
}

module.exports = { FileCategory, FTT };
exports.default = FTT; 
