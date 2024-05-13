from lib import HLexer as HLexer, HParser as HParser
import argparse

class Helium():
    def __init__(self, code) -> None:
        self.code = code
        self.lexer = HLexer.HLexer(self.code)
        self.parser = HParser.HParser()

    

    def run(self):
        self.tokens = self.lexer.tokenize()
        toklist = self.lexer.assembleTokList(self.tokens)
        self.parser.parse(self.tokens, toklist)
        
        



argparser = argparse.ArgumentParser(
    prog="helium.py",
    description="Interpret a Helium programming language source file"
)

argparser.add_argument('filename')
args = argparser.parse_args()

code = ""

try:
    with open(str(args.filename), 'r') as f: 
        code = f.read()
        code += "\n"
except FileNotFoundError:
    print(f"File {args.filename} not found!")

helium = Helium(code)
helium.run()