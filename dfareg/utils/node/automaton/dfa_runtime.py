class DFARuntime(object):
    def __init__(self, DFA):
        self.DFA = DFA
        self.cur_state = self.DFA.start

    def do_transition(self, char):
        self.cur_state = self.DFA.transition(self.cur_state, char)

    def is_accept_state(self):
        return self.cur_state in self.DFA.accepts

    def does_accept(self, input):
        for alphabet in input:
            self.do_transition(alphabet)
        return self.is_accept_state()
