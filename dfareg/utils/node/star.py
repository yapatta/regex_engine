from .node import Node
from .context import Context


class Star(Node):
    def __init__(self, operand):
        self.operand = operand

    def assemble(self, context):
        frag_orig = self.operand.assemble(context)
        frag = frag_orig.new_skelton()

        for state in frag_orig.accepts:
            frag.connect(state, "", frag_orig.start)

        s = context.new_state()
        frag.connect(s, "", frag_orig.start)

        frag.start = s
        frag.accepts = frag_orig.accepts | frozenset([s])

        return frag
