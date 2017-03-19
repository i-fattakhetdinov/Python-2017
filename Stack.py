#import sys


class Stack:
    def __init__(self, obj):
        self.len = 0
        self.items = []
        for i in obj:
            self.push(i)

    def push(self, item):
        self.len += 1
        self.items += [item]

    def pop(self):
        self.len -= 1
        return self.items.pop()

    def top(self):
        return self.items[self.len - 1]

    def __len__(self):
        return self.len

    def __str__(self):
        st = ''
        for i in self.items:
            st += str(i) + ' '
        return st.rstrip()

#exec(sys.stdin.read())
