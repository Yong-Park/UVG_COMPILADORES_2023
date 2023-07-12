import sys
from antlr4 import *
from YAPLLexer import YAPLLexer
from YAPLParser import YAPLParser

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = YAPLLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = YAPLParser(stream)
    tree = parser.startRule()
 
if __name__ == '__main__':
    main(sys.argv)
