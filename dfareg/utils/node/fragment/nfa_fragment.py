import copy
from ..automaton import nondeterministic_finite_automaton as nfa


class NFAFragment(object):
    def __init__(self):
        self.start = None  # 整数型
        self.accepts = None  # frozenset型
        self.map = dict()

    def connect(self, from_, char, to):
        slot = self.map.setdefault((from_, char), set())
        slot.add(to)

    def new_skelton(self):
        # コピーして返す
        new_frag = NFAFragment()
        new_frag.map = copy.deepcopy(self.map)
        return new_frag

    def __or__(self, frag):
        new_frag = self.new_skelton()
        for k, v in frag.map.items():
            new_frag.map[k] = v.copy()

        return new_frag

    def build(self):
        map_ = self.map

        def transition(state, char):
            return frozenset(map_.get((state, char), []))

        return nfa.NondeterministicFiniteAutomaton(
            transition,
            self.start,
            self.accepts
        )
