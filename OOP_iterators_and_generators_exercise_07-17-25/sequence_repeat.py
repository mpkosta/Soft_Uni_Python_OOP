class sequence_repeat():
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.number:
            i = self.i % len(self.sequence) 
            self.i += 1 #this is inclemented for the next iteration to be used
            return self.sequence[i] #we need it to be at index i to know when to stop when index divides by itself and returns 0
        else:
            raise StopIteration

result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')

print("\n----")
result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end='')