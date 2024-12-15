from lib.const import Token, TokenType, BUILT_IN_KEYWORDS
from lib.util import is_num
from lib.HError import *

class HLexer:

    def __init__(self, code) -> None:
        self.code = code
        
    def next(self, pos, n=1):
        return self.code[pos+n]

    def tokenize(self):
            

            keywords = [getattr(BUILT_IN_KEYWORDS, attr) for attr in dir(BUILT_IN_KEYWORDS) if not callable(getattr(BUILT_IN_KEYWORDS, attr)) and not attr.startswith("__")]
            LENGTH = len(self.code)

            pos = 0
            self.tokens = []
            self.vars = []

            VARCHARS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_.,'

            while pos < LENGTH:
                cc = self.code[pos]
                #if cc space or \n, continue
                if cc == " " or cc == "\n":
                    pos += 1
                elif cc == '"':
                    # string?
                    res = ""
                    pos += 1

                    #while nc(nextchar) not " or \n and not eof
                    while self.code[pos] != '"' and self.code[pos] != "\n" and pos < LENGTH:
                        res += self.code[pos]
                        pos += 1

                    if self.code[pos] != '"':
                        raise SyntaxError(f"Unterminated string at pos {pos}")
                    pos += 1
                    self.tokens.append(Token(TokenType.STRING, res))
                    continue
                elif is_num(self.code[pos]) or (cc == '.' and is_num(self.code[pos+1])):
                    # number
                    res = ""
        
                    while (is_num(self.code[pos]) or (self.code[pos] == "." and is_num(self.code[pos+1]))) and self.code[pos] != "\n" and pos < LENGTH:
                        res += str(self.code[pos])
                        pos += 1
                    pos += 1
                    self.tokens.append(Token(TokenType.INTEGER, float(res)))
                    continue
                elif cc == "=":
                    if self.next(pos) == '=':
                        self.tokens.append(Token(TokenType.EQUALS, '=='))
                        pos += 2
                    elif self.next(pos) == ' ' or self.next(pos) == '\n':
                        self.tokens.append(Token(TokenType.ASSIGN, '='))
                        pos += 1
                    continue

                elif cc in VARCHARS:
                    res = cc
                    pos += 1
                    
                    #while nc is in varchars and not eof
                    while self.code[pos] in VARCHARS and pos < LENGTH:
                        res += self.code[pos]
                        pos += 1

                    if not (res in keywords):
                        
                        if res == "True" or res == 'False':
                            self.tokens.append(Token(TokenType.BOOLEAN, res))
                            continue

                        if res in self.vars:
                            self.tokens.append(Token(TokenType.VARIABLE, res))
                            continue
                        if self.tokens[-1].type == TokenType.KEYWORD and self.tokens[-1].value == 'define':
                            self.tokens.append(Token(TokenType.VARIABLE, res))
                            self.vars.append(res)
                            continue
                        else:
                            HeliumUndefinedToken(res)
                    
                    self.tokens.append(Token(TokenType.KEYWORD, res))
                    continue
                else:
                    # Unexpected char
                    raise SyntaxError(f"Unexpected character {cc}")
  
            return self.tokens
        

    def assembleTokList(self, tokens):
        tl = []
        for tok in tokens:
            t = {'type:': tok.type, 'value': tok.value}
            tl.append(t)
            
        return tl

