from typing import List, Tuple, Dict, Union

## Python 3.9 onwards
price: List[int] = [12, 23, 4, 5]
price: Tuple[int, int, int] = (1,2,5)
price: Dict[str, int] = {
    "item1": 23,
    "item2": 45,
    "item3":50
}


# Python 3.10 onwards
price: list[int] = [12,23]
price: tuple[int,int] = (1,2)
price: dict[str, int] = {
    "item1": 23,
    "item2": 45,
    "item3": 50
}

x:List[Union[int, float]] = [1, 2.5, 3.4]
y:List[Union[int | float]] = [1, 2.5, 3.4]

def inr_to_usd(value: float) -> Union[float, None]:
    try:
        conversion_factor = 75
        value = value/conversion_factor
        return value
    except TypeError:
        return None

# prerequisites\type_hinting\1_advance_type_hinting.py:33: error: Argument 1 to "inr_to_usd" has incompatible type "str"; expected "float"  [arg-type]
# Found 6 errors in 1 file (checked 1 source file)
inr_to_usd('23')

