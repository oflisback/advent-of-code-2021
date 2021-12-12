class Node():
    def __init__(self, name):
        self._name = name
        self._paths = []
        self._done = False

    def __repr__(self):
        return f"{self._name}: {self._paths}"

    @property
    def name(self):
        return self._name

    @property
    def small(self):
        return not self._name.isupper()

    @property
    def done(self):
        return self._done

    @done.setter
    def done(self, done):
        self._done = done

    @property
    def neighbours(self):
        return self._paths
 
    def add_path(self, node):
        self._paths.append(node)
