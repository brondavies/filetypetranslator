using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Text.RegularExpressions;
using System.Xml.Serialization;

namespace FTT
{
    class Sources
    {
        const string freedesktopUrl = "https://gitlab.freedesktop.org/xdg/shared-mime-info/-/raw/master/data/freedesktop.org.xml.in";
        const string stdiconJsonUrl = "http://www.stdicon.com/mimetypes";
        const string mimedbJsonUrl = "https://cdn.rawgit.com/jshttp/mime-db/master/db.json";

        public static void Parse(params Type[] generators)
        {
            MimeInfo info = null;
            JsonDict stdicon = null;
            MimeDbInfoDict mimedb = null;
            using (WebClient client = new WebClient())
            {
                XmlSerializer serializer = new XmlSerializer(typeof(MimeInfo));
                info = (MimeInfo)serializer.Deserialize(client.OpenRead(freedesktopUrl));
                mimedb = JsonConvert.DeserializeObject<MimeDbInfoDict>(client.DownloadString(mimedbJsonUrl));
                // no longer exists :( 
                // stdicon = JsonConvert.DeserializeObject<JsonDict>(client.DownloadString(stdiconJsonUrl));
            }

            List<MimeType> mimetypes = new List<MimeType>();
            ParseMimeInfo(info, mimetypes);
            ParseMimeDbInfo(mimedb, mimetypes);
            if (stdicon != null)
            {
                ParseStdIcon(stdicon, mimetypes);
            }
            mimetypes = mimetypes.OrderBy(m => m.extensions.First()).ToList();

            foreach(var type in generators)
            {
                var generator = Activator.CreateInstance(type) as ICodeGenerator;
                generator.GenerateFileStart();
                generator.GenerateConstants(mimetypes);
                
                //GetMimeTypeInternal
                generator.GenerateBeginFunction();
                foreach (var mt in mimetypes)
                {
                    generator.GenerateFunctionBody(mt);
                }
                generator.GenerateEndFunction();
                
                // GetMimeTypeFileExtensionsInternal
                generator.GenerateBeginFunction2();
                foreach (MimeType mt in mimetypes)
                {
                    generator.GenerateFunctionBody2(mt);
                }
                generator.GenerateEndFunction2();
                generator.GenerateFileEnd();
                generator.Finish();
            }
        }

        private static void ParseStdIcon(JsonDict dict, List<MimeType> mimetypes)
        {
            foreach (var entry in dict)
            {
                string extension = CleanExtension(entry.Keys.First());
                string type = entry.Values.First().Trim();
                if (!string.IsNullOrEmpty(type) && !string.IsNullOrEmpty(extension))
                {
                    MimeType mimeType = mimetypes.Find(t => t.type == type) ?? new MimeType();

                    if (!mimetypes.Exists(m => m.extensions.Contains(extension)))
                    {
                        mimeType.extensions.Add(extension);
                        if (string.IsNullOrEmpty(mimeType.type))
                        {
                            mimeType.type = type;
                            mimetypes.Add(mimeType);
                        }
                    }
                }
            }
        }

        private static void ParseMimeInfo(MimeInfo info, List<MimeType> mimetypes)
        {
            foreach (mimeinfoMimetype item in info.Items)
            {
                if (item.glob != null && !string.IsNullOrEmpty(item.type))
                {
                    bool added = false;
                    item.type = item.type.ToLowerInvariant().Trim();
                    MimeType mimeType = mimetypes.Find(t => t.type == item.type) ?? new MimeType();
                    foreach (var glob in item.glob)
                    {
                        string extension = CleanExtension(glob.pattern);
                        if (!string.IsNullOrEmpty(extension) && !mimetypes.Exists(m => m.extensions.Contains(extension)) && !mimeType.extensions.Contains(extension))
                        {
                            added = mimeType.type == null;
                            mimeType.extensions.Add(extension);
                        }
                    }
                    if (added)
                    {
                        mimeType.type = item.type;
                        mimeType.comment = item._comment;
                        mimetypes.Add(mimeType);
                    }
                }
            }
        }

        private static void ParseMimeDbInfo(MimeDbInfoDict dict, List<MimeType> mimetypes)
        {
            foreach (var entry in dict)
            {
                bool added = false;
                var type = entry.Key;
                var item = entry.Value;
                type = type.ToLowerInvariant().Trim();
                MimeType mimeType = mimetypes.Find(t => t.type == type) ?? new MimeType();
                if (item.extensions != null)
                { 
                    foreach (var extension in item.extensions)
                    {
                        if (!string.IsNullOrEmpty(extension) && !mimetypes.Exists(m => m.extensions.Contains(extension)) && !mimeType.extensions.Contains(extension))
                        {
                            added = mimeType.type == null;
                            mimeType.extensions.Add(extension);
                        }
                    }
                    if (added)
                    {
                        mimeType.type = type;
                        mimeType.comment = item.source;
                        mimetypes.Add(mimeType);
                    }
                }
            }
        }

        static Regex cleanregex = new Regex("[^a-z0-9]");
        private static string CleanExtension(string ext)
        {
            return cleanregex.Replace(ext.ToLowerInvariant().Trim(), "");
        }
    }
}
