class StackItem(object):

    def __init__(self, x, minimum=None):
        """
        initialize your data structure here.
        """
        self.value = x
        # 0 is falsey in Python
        self.minimum = minimum if minimum != None else x


    def __repr__(self):
        return 'val: {}, min: {}'.format(self.value, self.minimum)


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        # Initialize head
        self.container = []


    def __getitem__(self, key):
        """
        support indexing this way.
        """
        # Silent error
        if key < len(self.container): return self.container[key]


    def isEmpty(self):
        """
        :rtype: bool
        """
        return len(self.container) == 0


    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        # Get the minimum
        minimum = None
        if not self.isEmpty():
            minimum = self.container[-1].minimum
            minimum = x if x < minimum else minimum
        self.container.append(StackItem(x, minimum))


    def pop(self):
        """
        :rtype: void
        """
        if not self.isEmpty(): del self.container[-1]


    def top(self):
        """
        :rtype: int, maybe?: None
        """
        if self.isEmpty(): return None
        return self.container[-1].value
        

    def getMin(self):
        """
        :rtype: int, maybe?: None
        """
        if self.isEmpty(): return None
        return self.container[-1].minimum
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

if __name__ == '__main__':
    a = MinStack()
    a.push(3)
    a.push(0)
    a.push(5)
    # a.push(-1)
    # a.push(10)
