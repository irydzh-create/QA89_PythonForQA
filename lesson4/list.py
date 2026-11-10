fruits = ["orange", "strawberry", "mango"]
fruits.append("orange")
print(fruits)

fruits.insert(1, "banana")
print(fruits)

fruits.index("banana")
print(fruits)

first_banana_index = fruits.index("mango")
print(f"The fruits was added to position {first_banana_index}")


fruits.remove("orange")
print(fruits)

fruits.pop(2)
print(fruits)

numbers=[10,20,30]
deleted=numbers.pop(1)# удали и возвращай то что удалил
print(numbers)
print(deleted)

numbers.clear()
print(numbers)