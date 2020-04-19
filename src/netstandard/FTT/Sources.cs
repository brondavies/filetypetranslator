using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Text;
using System.Text.RegularExpressions;
using System.Xml.Serialization;

namespace FTT
{
    class Sources
    {
        const string freedesktopUrl = "https://gitlab.freedesktop.org/xdg/shared-mime-info/-/raw/master/data/freedesktop.org.xml.in";
        const string stdiconJsonUrl = "http://www.stdicon.com/mimetypes";
        const string mimedbJsonUrl = "https://cdn.rawgit.com/jshttp/mime-db/master/db.json";

        const string indent = "                ";


        public static string Parse()
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

            StringBuilder format = new StringBuilder(GenerateFileStart());

            format.AppendLine(GenerateConstants(mimetypes));
            
            //GetMimeTypeInternal
            format.Append(GenerateBeginFunction());
            foreach (MimeType mt in mimetypes)
            {
                if (!string.IsNullOrEmpty(mt.comment))
                {
                    format.AppendLine(GenerateComment(mt.comment));
                }
                foreach (string extension in mt.extensions)
                {
                    format.AppendLine(GenerateCase(extension));
                }
                format.AppendLine(GenerateReturn(GetConstantFor(mt.type)));
            }
            format.Append(GenerateEndFunction());

            // GetMimeTypeFileExtensionsInternal
            format.Append(GenerateBeginFunction2());
            foreach (MimeType mt in mimetypes)
            {
                format.AppendLine(GenerateCase(mt.type));
                string extensions = @"new string[] { ";
                string strings = string.Join("\", \"", mt.extensions);
                if (strings.Length > 0)
                {
                    strings = quote(strings) + " ";
                }
                extensions += strings;
                extensions += "}";
                format.AppendLine(GenerateReturn(extensions));
            }

            format.Append(GenerateEndFunction2());
            format.Append(GenerateFileEnd());

            return format.ToString();
        }

        private static string GenerateConstants(List<MimeType> mimetypes)
        {
            StringBuilder result = new StringBuilder();
            foreach(var mimetype in mimetypes)
            {
                result.AppendLine(GenerateConstantFor(mimetype.type));
                foreach(string ext in mimetype.extensions)
                {
                    result.AppendLine(GenerateConstantFor(ext));
                }
            }
            return result.ToString();
        }

        static char[] numbers = new[] { '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' };
        private static string GenerateConstantFor(string type)
        {
            string name = GetConstantFor(type);
            return string.Format("        const string {0} = \"{1}\";", name, type);
        }

        private static string GetConstantFor(string type)
        {
            string name = CleanExtension(type);
            if (IsKeyword(name) || numbers.Contains(name.First()))
            {
                name = "_" + name;
            }
            return name;
        }

        private static bool IsKeyword(string name)
        {
            //this is not a comprehensive list, we just add to it as needed
            switch (name)
            {
                case "as":
                case "class":
                case "for":
                case "in":
                case "is":
                    return true;
            }
            return false;
        }

        private static string GenerateBeginFunction()
        {
            return @"
        private static string GetMimeTypeInternal(string extension)
        {
            switch (extension)
            {
";
        }

        private static string GenerateEndFunction2()
        {
            return @"            }

            return new string[] { };
        }";
        }

        private static string GenerateBeginFunction2()
        {
            return @"
        private static string[] GetMimeTypeFileExtensionsInternal(string mimeType)
        {
            switch(mimeType)
            {
";
        }

        private static string GenerateEndFunction()
        {
            return @"            }
            return """";
        }";
        }

        private static string quote(string value)
        {
            return string.Format("\"{0}\"", value);
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
            StringBuilder format = new StringBuilder(GenerateFileStart());
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

        private static string GenerateReturn(string type)
        {
            return string.Format("{0}    return {1};", indent, type);
        }

        private static string GenerateComment(string comment)
        {
            return string.Format("{0}// {1}", indent, comment);
        }

        private static string GenerateCase(string extension)
        {
            return string.Format("{0}case {1}:", indent, GetConstantFor(extension));
        }

        private static string GenerateFileStart()
        {
            return @"namespace FTTLib
{
    public partial class FTT
    {
";
        }

        private static string GenerateFileEnd()
        {
            return @"
    }
}";
        }

    }
}
