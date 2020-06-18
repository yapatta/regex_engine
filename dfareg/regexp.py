from .utils.lexer import Lexer
from .utils.parser import Parser
from .utils.node.automaton.deterministic_finite_automaton import DeterministicFiniteAutomaton
from .utils.node.automaton.nondisjoint_sets import NonDisjointSets


class Regexp(object):
    def __init__(self, regexp):
        self.regexp = regexp
        self.dfa = None
        self._compile()

    def _compile(self):
        # コンパイル
        lexer_ = Lexer(self.regexp)
        parser_ = Parser(lexer_)
        nfa = parser_.expression()
        # 部分集合構成法
        self.dfa = nfa2dfa(nfa)

    def matches(self, string):
        runtime = self.dfa.get_runtime()
        return runtime.does_accept(string)


def nfa2dfa(nfa):
    def transition(set_, alpha):
        ret = set()
        for elem in set_:
            ret |= nfa.transition(elem, alpha)
        return nfa.epsilon_expand(frozenset(ret))

    return DeterministicFiniteAutomaton(
        transition,
        nfa.epsilon_expand(frozenset([nfa.start])),
        NonDisjointSets(nfa.accepts)
    )
