from .fragment.nfa_fragment import NFAFragment
from .node import Node
from .context import Context


class Union(Node):
    def __init__(self, operand1, operand2):
        self.operand1 = operand1
        self.operand2 = operand2

    def assemble(self, context):
        frag1 = self.operand1.assemble(context)
        frag2 = self.operand2.assemble(context)
        frag = frag1 | frag2

        s = context.new_state()
        frag.connect(s, "", frag1.start)
        frag.connect(s, "", frag2.start)

        frag.start = s
        frag.accepts = frag1.accepts | frag2.accepts

        return frag
