class Python:
    def __init__(self) -> None:
        self.is_cool = True

class FastAPIDemo(Python):
    pass

f = FastAPIDemo()
print(f.is_cool)

class Pydantic:
    def is_valid(self, text):
        if "admin" in text:
            return False
        return True

class Starlette:
    def is_valid(self, text):
        return True

class FastAPI(Pydantic, Starlette):
    pass

f = FastAPI()
print(f.is_valid("admin tried to signin"))
## Print MRO
print(FastAPI.__mro__)