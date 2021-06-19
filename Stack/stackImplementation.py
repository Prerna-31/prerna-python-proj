class MyStack(object):
    top = -1
    stck = []
    size = 5
    def isFull(self):
        return self.top == self.size -1

    def isEmpty(self):
        return(self.top == -1)

    def push(self, element):
        if(self.isFull()):
            print("The stack is full::")
            return
        self.top += 1
        self.stck.append(element)
        return("The element {} is inserted".format(element))

    def pop(self):
        if(self.isEmpty()):
            print("The Stack is already empty:")
            return
        ele = self.stck[self.top]
        self.stck.remove(ele)
        self.top -= 1
        return("The element {} is popped".format(ele))

    def peek(self):
        return(self.stck[self.top])

    def min(self):
        return(min(self.stck))       ## It seems that it might be slower for large data sets. so we can use dictionaries to store data and get the min and max which will be fast enough.

    def max(self):
        return(max(self.stck))       ## It seems that it might be slower for large data sets. so we can use dictionaries to store data

st = MyStack()
print("Creating stack:::::")
st.push(60)
st.push(30)
st.push(40)
print("Current stack after pushing elements: " , st.stck)
st.pop()
st.push(80)
print("Current stack after pushing another element : ", st.stck)
print("The next element to be deleted :",st.peek())
st.push(100)
st.push(120)
st.push(10)
print("Current stack after pushing elements : ", st.stck)
print("Minimum element in Stack :",st.min())
print("Maximum element in Stack :",st.max())
st.pop()
print("Current stack after popping elements : ", st.stck)
print("Minimum element in Stack :",st.min())
print("Maximum element in Stack :",st.max())
st.pop()
st.pop()
st.pop()
st.pop()
print("Current stack after popping elements : ", st.stck)
st.pop()
