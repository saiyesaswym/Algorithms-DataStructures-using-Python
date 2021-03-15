class Stack:
    def __init__(self):
        self.items=[]

    def push(self,item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def isEmpty(self):
        return len(self.items)==0

    def size(self):
        return len(self.items)


s = Stack()
print(s.isEmpty())
s.push(8)
s.push("hello")
print(s.peek())
s.push(True)
print(s.size())
print(s.isEmpty())
s.pop()
print(s.size())
