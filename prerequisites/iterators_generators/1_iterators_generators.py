# judiciously use resources
price=[1,2,3,9,8]


# For any Iterator
# __iter__
# __next__

price_iter = price.__iter__()
print(price_iter.__next__())
print(price_iter.__next__())
print(price_iter.__next__())

while True:
    try:
        print(price_iter.__next__())
    except StopIteration:
        print("Got StopIteration Error")
        break

class InfiniteNaturalNumbers:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        num = self.num
        self.num +=1
        return num

values = iter(InfiniteNaturalNumbers())
print(next(values))
print(next(values))
print(next(values))

# Generator smart and intelligent way to create iterators

def return_values():
    yield 1
    yield 2
    yield "three"

value = return_values()
print(value.__next__())
print(value.__next__())
print(value.__next__())