import { FTT } from '../dist/FTT.js';

let mimeType = FTT.getMimeType('Path/To/My/File.doc');
console.log(mimeType);

mimeType = FTT.getMimeType('Path/To/My/File.docx');
console.log(mimeType);

let extensions = FTT.getMimeTypeFileExtensions('text/csv');
console.log(extensions[0]);