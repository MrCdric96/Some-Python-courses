# Node Class
class Node:

    def __init__(self, d, n=None, p=None):
        self.data  = d
        self.next_node = n
        self.pev_node = p

    def __str__(self):
        return ("(" + str(self.data) + ")")