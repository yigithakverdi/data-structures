class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.depth = None

    def __str__(self):
        