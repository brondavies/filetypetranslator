using System.Collections.Generic;

namespace FTT
{
    interface ICodeGenerator
    {
        void GenerateFileStart();
        void GenerateConstants(List<MimeType> mimetypes);
        void GenerateBeginFunction();
        void GenerateFunctionBody(MimeType mimeType);
        void GenerateEndFunction();
        void GenerateBeginFunction2();
        void GenerateFunctionBody2(MimeType mimeType);
        void GenerateEndFunction2();
        void GenerateFileEnd();
        void Finish();
    }
}
