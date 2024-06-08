class MinStack:

    def __init__(self):
        self.min_items = []
        self.items = []


    def push(self, val: int) -> None:
        self.items.append(val)

        size = self.getSize()

        if (size == 1) or (val <= self.min_items[-1]):
            self.min_items.append(val)

    def pop(self) -> None:
        removed_item = self.items.pop()

        if self.min_items[-1] == removed_item:
            self.min_items.pop()


    def top(self) -> int:
        return self.items[-1]

    def getMin(self) -> int:
        return self.min_items[-1]

    def getSize(self) -> int:
        return len(self.items)

    def __str__(self):
        return self.items.__str__()

# Explanation
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top();    // return 0
# minStack.getMin(); // return -2
min_stack = MinStack()
print(min_stack.push(-2), min_stack)
print(min_stack.push(0), min_stack)
print(min_stack.push(-3), min_stack)
print(min_stack.getMin(), min_stack)
print(min_stack.pop(), min_stack)
print(min_stack.top(), min_stack)
print(min_stack.getMin(), min_stack)
