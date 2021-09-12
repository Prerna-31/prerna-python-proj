"""
Hypothesis: reverse(4,3,6,2,1)  --> reverse the stack --> 1,2,6,3,4
            pop top element and reverse(4,3,6,2)    --> reverse the remaining stack-->2,6,3,4
Induction: push the above popped element into stack at 0th position --> recursion
Base Condition: if n == 1, return stack  where n is size of an array.

Hypothesis for insertion:  insert([2,6,3,4], poppedElement)   --> simply insert at 0th position.
                           pop top element and call insert([2,6,3],poppedElement)  --> simply insert at 0th position.
Induction step: push the above popped element into stack.
Base condition:  if (len(stack) == 1), simply push the element.
"""
import math as m
class Stack:
    def __init__(self):
        #self.stack = numpy.empty(5,'i')
        #self.stack.fill(0)
        self.stack= []
        self.top= -1
        self.size = 10 #len(self.stack)

    def push(self, data):
        if(self.top == self.size-1):
            print("Stack Overflow")
        self.top = self.top + 1
        self.stack.append(data)

    def pop(self):
        if(self.top == -1):
            print("Stack UnderFlow")

        ele = self.stack[self.top]
        self.stack.remove(self.peek())  #numpy.delete(self.stack, self.top)
        self.top -= 1
        return ele

    def peek(self):
        return self.stack[self.top]

    def reverse(self):
        if(len(self.stack) in (1,0)):
            return

        top_element = self.pop()
        self.reverse()
        self.insert(top_element)

    def insert(self, ele_to_insert):
        if(len(self.stack) == 0):
            self.push(ele_to_insert)
            return

        top_element = self.pop()
        self.insert(ele_to_insert)
        self.push(top_element)
        return


st = Stack()
st.push(30)
st.push(40)
st.push(10)
st.push(80)
st.push(5)
print("Stack before reverse:", st.stack)
st.reverse()
print("Stack after reverse:",st.stack)


