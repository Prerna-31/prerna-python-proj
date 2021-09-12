"""
Hypothesis: delete(4,3,6,2,1 , midEle)  --> deletes mid element --> 4,3,2,1
            pop top element and delete(4,3,6,2,midEle)    --> deletes mid elemnt --> 4,3,2
Induction: push the above popped element into stack.
Base Condition: if top == mid or n == 1, return stack[top]  where n is size of an array.
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

    def delete_mid_element(self, mid_index):
        if(self.top == mid_index or self.top ==1):
            self.pop()
            return

        top_element = self.pop()
        self.delete_mid_element(mid_index)
        self.push(top_element)

        return


st = Stack()
st.push(30)
st.push(40)
st.push(10)
st.push(80)
st.push(5)
print("Stack before deleting mid element:", st.stack)
st.delete_mid_element(m.floor(st.top // 2) )
print("Stack afterdeleting mid element: ",st.stack)


