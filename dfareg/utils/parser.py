from .token import Token
from .node.character import Character
from .node.concat import Concat
from .node.star import Star
from .node.union import Union
from .node.context import Context


class Parser(object):
    def __init__(self, lexer):
        self.lexer = lexer
        self.look = None
        # 最初の文字を読む
        self.move()

    def match(self, tag):
        if self.look.kind != tag:
            # 予期せぬトークンが来たら、エラーで終了
            raise Exception("syntax error")
        self.move()

    def move(self):
        self.look = self.lexer.scan()

    # factor -> '(' subexpr ')' | CHARACTER
    def factor(self):
        if self.look.kind == Token.LPAREN:
            self.match(Token.LPAREN)
            node = self.subexpr()
            self.match(Token.RPAREN)
            return node
        else:
            node = Character(self.look.value)
            self.match(Token.CHARACTER)
            return node

    # star -> factor '*' | factor
    def star(self):
        node = self.factor()
        if self.look.kind == Token.OPE_STAR:
            self.match(Token.OPE_STAR)
            node = Star(node)
        return node

    # seq -> subseq | ''
    def seq(self):
        if self.look.kind == Token.LPAREN or self.look.kind == Token.CHARACTER:
            return self.subseq()
        else:
            return Character("")

    # subseq -> star subseq | star
    def subseq(self):
        node1 = self.star()
        if self.look.kind == Token.LPAREN or self.look.kind == Token.CHARACTER:
            # subseq -> star subseq
            node2 = self.subseq()
            node = Concat(node1, node2)
            return node
        else:
            # subseq -> star
            return node1

    # subexpr -> seq '|' subexpr | seq
    def subexpr(self):
        # subexpr    -> seq '|' subexpr | seq
        node = self.seq()
        if self.look.kind == Token.OPE_UNION:
            self.match(Token.OPE_UNION)
            node2 = self.subexpr()
            node = Union(node, node2)
        return node

    # expression -> subexpr EOF
    def expression(self):
        # expression -> subexpr EOF
        node = self.subexpr()
        self.match(Token.EOF)

        # 構文木を実行し、NFAを作る
        context = Context()
        fragment = node.assemble(context)
        return fragment.build()
