from lib.const import TokenType, BUILT_IN_KEYWORDS

class HParser:

    def __init__(self) -> None:
        self.variables = {}

    def parse(self, tokens, toklist):
        ln = len(tokens)
        i = 0

        def next(n=1): return tokens[i+n]

        while i < ln:
            tok = tokens[i]

            if tok.type == TokenType.KEYWORD:
                 
                match tok.value:
                    
                    case BUILT_IN_KEYWORDS.LOG:
                        try:
                            nt = tokens[i + 1]
                        except IndexError:
                            raise SyntaxError("Expected STRING, BOOL, VAR or INT after LOGLN, but got NOTHING")

                        isStr = nt.type == TokenType.STRING
                        isInt = nt.type == TokenType.INTEGER
                        isVar = nt.type == TokenType.VARIABLE
                        isBool = nt.type == TokenType.BOOLEAN

                        if not isStr and not isInt and not isVar and not isBool:
                            raise SyntaxError(f"Expected STRING, BOOL, VAR or INT after LOGLN, but got {nt.type.upper()}")

                        if not isVar:
                            print(nt.value, end='')
                        else:
                            print(self.variables[nt.value], end='')


                        i += 2

                    case BUILT_IN_KEYWORDS.LOGLN:
                        try:
                            nt = tokens[i + 1]
                        except IndexError:
                            raise SyntaxError("Expected STRING, BOOL, VAR or INT after LOGLN, but got NOTHING")

                        isStr = nt.type == TokenType.STRING
                        isInt = nt.type == TokenType.INTEGER
                        isVar = nt.type == TokenType.VARIABLE
                        isBool = nt.type == TokenType.BOOLEAN

                        if not isStr and not isInt and not isVar and not isBool:
                            raise SyntaxError(f"Expected STRING, BOOL, VAR or INT after LOGLN, but got {nt.type.upper()}")

                        if not isVar:
                            print(nt.value, end='\n')
                        else:
                            print(self.variables[nt.value], end='\n')


                        i += 2

                    case BUILT_IN_KEYWORDS.DEFINE:
                        try:
                            nt = tokens[i+1]
                        except IndexError:
                            raise SyntaxError("Expected VARIABLE NAME after DEFINE, but got NOTHING")
                        
                        isVar = nt.type == TokenType.VARIABLE

                        if not isVar:
                            raise SyntaxError(f"Expected VARIABLE NAME after DEFINE, but got {nt.type.upper()}")
                        
                        self.variables[nt.value] = None

                        i += 2

            elif tok.type == TokenType.VARIABLE:

                try:
                    nt = next()
                except IndexError:
                    raise SyntaxError(f"Expected ASSIGN (=) after VARIABLE, but got NOTHING")
                
                try:
                    nnt = next(2)
                except IndexError:
                    raise SyntaxError(f"Expected STRING or INT after VARIABLE ASSIGN, but got NOTHING")
                if nt.type == TokenType.ASSIGN and (nnt.type == TokenType.STRING or nnt.type == TokenType.INTEGER):
                    self.variables[tok.value] = nnt.value

                    i += 3
                        
            else:
                print(tok.type)
                print(toklist)
                raise SyntaxError(f"Unexpected token {tok.value}") 
