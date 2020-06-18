class Context(object):
    def __init__(self):
        self._state_count = 0

    def new_state(self):
        self._state_count += 1
        return self._state_count
