from typing import List, Optional, Callable

Image = List[List[int]]

def flatten_image(pic: Image)-> List[int]:
    flat_list = []
    for sublist in pic:
        for item in sublist:
            flat_list.append(item)
    return flat_list

image = [[1,2,3],[4,5,6]]

class Job:
    def __init__(self, title: str, description:Optional[str]):
        self.title = title
        self.description = description

    def __repr__(self):
        return self.title

job1: Job = Job(title="Team Lead", description="Leads Team")
job2: Job = Job(title="Senior Manager", description="Manages Team")

jobs:List[Job] = [job1, job2]

def smart_divide(func: Callable[[int, int],float]):
    def inner(a, b):
        if b==0:
            print("Whoops! Division by 0")
            return None

        return func(a,b)
    return inner

@smart_divide
def divide(a, b):
    print(a/b)

print(f"Division Result : {divide(9,0)}")