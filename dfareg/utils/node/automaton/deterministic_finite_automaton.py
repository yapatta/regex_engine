from .dfa_runtime import DFARuntime


class DeterministicFiniteAutomaton(object):
    def __init__(self,
                 transition,  # 遷移関数
                 start,  # 開始状態
                 accepts,  # 受理状態の集合
                 ):
        self.transition = transition
        self.start = start
        self.accepts = accepts

    def get_runtime(self):
        return DFARuntime(self)

    def transition(set_, alpha):
        ret = set()
        for elem in set_:
            ret |= nfa.transition(elem, alpha)
        return nfa.epsilon_expand(frozenset(ret))
