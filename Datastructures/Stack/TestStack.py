from Stack import Stack

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
