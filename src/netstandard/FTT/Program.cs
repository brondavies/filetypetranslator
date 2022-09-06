using FTT.generators;
using System;

namespace FTT
{
    class Program
    {
        static void Main(string[] args)
        {
            try
            {
                Sources.Parse(
                    typeof(CsharpGenerator),
                    typeof(PythonGenerator)
                    );
            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
                Console.WriteLine(e.StackTrace);
                Environment.ExitCode = 1;
            }
        }
    }
}
