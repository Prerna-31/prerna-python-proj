"""
This solution will have o(2n) ~~ O(n) as space complexity. and O(1) as time complexity.
"""
class MyStack(object):
    top = -1
    stck = []
    size = 5
    min_max_dic = []
    first = True

    def isFull(self):
        return self.top == self.size -1

    def isEmpty(self):
        return(self.top == -1)

    def push(self, element):
        if(self.isFull()):
            print("The stack is full::")
            return
        if(self.first):
            self.min_max_dic.append({'min': element , 'max':element})
            first = False

        self.top += 1
        self.stck.append(element)

        if (element < self.min_max_dic[self.top]['min']):
            self.min_max_dic[self.top+1]['min'] = element  ## This is maintaining min and max values in  stack
        if(element > self.min_max_dic[self.top]['max']):
            self.min_max_dic[self.top+1]['max'] = element

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
        return(min(self.min_max_dic[self.top]['min']))

    def max(self):
        return(max(self.min_max_dic[self.top]['max']))

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