from .nondeterministic_finite_automaton import NondeterministicFiniteAutomaton as nfa


class NonDisjointSets(object):
    def __init__(self, sub):
        self.sub = sub

    def __contains__(self, a_set):
        return a_set & self.sub
