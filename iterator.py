# a=["hello","I am","robot"]

# # for i in a:
# #     print(i)

# itr = iter(a)
# print(dir(iter))
# print(next(itr))
# itr=reversed(a)
# print(next(itr))


class RemotControl():
    def __init__(self):
        self.channels=["HBO","POGO","CN","ABC"]
        self.index=-1
    
    def __iter__(self):
        return self

    def __next__(self):
        self.index+=1

        if self.index ==  len(self.channels):
            raise StopIteration
        return self.channels[self.index]
    

r= RemotControl()
itr=iter(r)
print(next(itr))