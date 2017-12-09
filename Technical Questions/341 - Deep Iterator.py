# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):
    """
    Questions I had:
    - If its a list, is it still index-able? i.e: nestedList[0] 
    - If its a list, can we know the length?
    """
    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack = [[nestedList, 0]]

    def next(self):
        """
        :rtype: int
        """
        # self.hasNext prepares the stack for us
        self.hasNext()
        nestedList, i = self.stack[-1]
        self.stack[-1][1] += 1
        return nestedList[i].getInteger()

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.stack:
            nestedList, i = self.stack[-1]
            # Get rid of "fully visited" nestedList
            if i == len(nestedList): self.stack.pop()
            else:
                # If its an integer, done
                x = nestedList[i]
                if x.isInteger():
                    return True
                # Adding new list to the stack, increment the previous' nestedList's counter
                self.stack[-1][1] += 1
                self.stack.append([x.getList(), 0])
        return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
