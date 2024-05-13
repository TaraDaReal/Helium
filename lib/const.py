class TokenType():
    STRING = "string"
    KEYWORD = "keyword"
    INTEGER = "integer"
    BOOLEAN = "bool"
    VARIABLE = "variable"
    ASSIGN = "assign"
    EQUALS = "equals"

    def __init__(self) -> None:
            pass
        
class BUILT_IN_KEYWORDS():
     LOG = "log"
     LOGLN = "logln"
     DEFINE = "define"

     def __init__(self) -> None:
          pass


class Token:

    def __init__(self, typ: TokenType, val) -> None:
        self.type = typ
        self.value = val

    def value_(self):
        return self.value
    
    def type_(self):
        return self.type

