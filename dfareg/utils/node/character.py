from .fragment.nfa_fragment import NFAFragment
from .context import Context
from .node import Node


class Character(Node):
    def __init__(self, char):
        self.char = char

    def assemble(self, context):
        frag = NFAFragment()
        s1 = context.new_state()
        s2 = context.new_state()
        frag.connect(s1, self.char, s2)

        frag.start = s1
        frag.accepts = frozenset([s2])

        return frag
