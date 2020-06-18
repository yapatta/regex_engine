class Token(object):
    # トークンの種類
    CHARACTER = 0
    OPE_UNION = 1
    OPE_STAR = 2
    LPAREN = 3
    RPAREN = 4
    EOF = 5

    def __init__(self, value, kind):
        # このトークンが持つ値
        self.value = value
        # このトークンの種類
        self.kind = kind
