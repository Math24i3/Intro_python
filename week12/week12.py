class A:
    def __init__(self):
        self._name = 'Claus'

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if name in [str]:
            self._name = name
