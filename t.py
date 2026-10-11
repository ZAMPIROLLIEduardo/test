
from typing import Mapping, Sequence

# ==============================================================================
# 1. THE MODERN WAY (Python 3.12+)
# ==============================================================================

# Generic Function: [T] declares the type parameter. 
# It ensures the return type matches the type inside the list.
def get_first_element[T](items: list[T]) -> T:
    """Returns the first element of a list while preserving its type."""
    return items[0]


# Generic Class: A reusable container wrapper.
class Storage[T]:
    """A generic box to store and retrieve a single item."""
    def __init__(self, item: T) -> None:
        self.item: T = item

    def get_item(self) -> T:
        return self.item


# Constrained Generics: Restricting types using a colon (:).
# This guarantees T must be an integer, float, or their subclasses.
def scale_value[T: (int, float)](value: T, factor: float) -> float:
    """Multiplies a numeric value by a float factor."""
    return value * factor


# Multiple Parameters: Useful for pairs, dictionaries, or mappings.
def create_pair[K, V](key: K, value: V) -> tuple[K, V]:
    """Creates a tuple pair using two distinct types."""
    return (key, value)


# ==============================================================================
# 2. RUNNING THE CODE (Type Inference & Validation)
# ==============================================================================
if __name__ == "__main__":
    print("--- 1. Testing Generic Function ---")
    number_list = [10, 20, 30]
    string_list = ["Python", "Generics", "Tutorial"]

    # The type checker automatically infers the types here
    first_num: int = get_first_element(number_list)
    first_str: str = get_first_element(string_list)
    
    print(f"First Number: {first_num} (Type: {type(first_num).__name__})")
    print(f"First String: '{first_str}' (Type: {type(first_str).__name__})")

    print("\n--- 2. Testing Generic Class ---")
    # You can be explicit, or let Python infer the type
    int_box = Storage[int](42)
    str_box = Storage("Hello World")

    print(f"Stored Box Int: {int_box.get_item()}")
    print(f"Stored Box Str: '{str_box.get_item()}'")

    print("\n--- 3. Testing Constraints ---")
    print(f"Scaled Int: {scale_value(10, 1.5)}")
    print(f"Scaled Float: {scale_value(5.5, 2.0)}")
    # scale_value("invalid", 2) -> Static type checkers (like Mypy) will flag this error!

    print("\n--- 4. Testing Multiple Parameters ---")
    pair = create_pair("user_id", 9402)
    print(f"Generated Pair: {pair} (Types: {type(pair[0]).__name__}, {type(pair[1]).__name__})")
