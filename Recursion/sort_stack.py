"""
Hypothesis: sort(4,3,6,2,1)  --> gives sorted stack --> 1,2,3,4,6
            pop top element and sort(4,3,6,2)    --> gives sorted stack --> 2,3,4,6
Induction: Insert the above popped element at correct position.  --> this also can be performed directly or using recursion
Base Condition: if n == 1 or n == 0, return stack[top]  where n is size of an array.

top elem = 1
Hypothesis for insertion:  insert([2,3,4,6], ele_to_insert)  --> insert 1 at correct position.
                      popped top element and call insert([2,3,4) , ele_to_insert)  --> insert 1 at correct position.
Induction:
Base condition for sort: if ele_to_insert >= stack[top] , insert at the top and return.
"""

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

    def sort(self):
        if(len(self.stack) in (1,0)):  ## Base condition
            return self.stack
        top_ele = self.pop()
        self.sort()
        self.insert(top_ele)    ## Insert at correct position --> implemented it recursively
        return self.stack


    def insert(self, ele_to_insert):
        if(len(self.stack) == 0 or (ele_to_insert > self.peek())):
            self.push(ele_to_insert)
            return self.stack

        top_ele = self.pop()
        self.insert(ele_to_insert)
        self.push(top_ele)

        return self.stack


st = Stack()
st.push(30)
st.push(40)
st.push(10)
st.push(80)
st.push(5)
print("After pushing elements on the stack: ", st.stack)
print("The popped element is :", st.pop())
print("After popping out element in the stack: ", st.stack)
print("The top element in the stack is : ", st.peek())

st.push(5)
print()
print("The stack before sorting:", st.stack)
st.sort()
print("The stack after sorting:", st.stack)



