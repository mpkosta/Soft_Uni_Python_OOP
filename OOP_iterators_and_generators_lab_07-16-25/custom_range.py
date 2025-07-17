class custom_range:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = start - 1

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1
        if self.current > self.end:
            raise StopIteration
        return self.current


one_to_ten = custom_range(1, 10)
for number in one_to_ten:
    print(number)

