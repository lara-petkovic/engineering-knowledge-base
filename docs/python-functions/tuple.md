# `tuple`

A tuple is an ordered collection of values in Python.

```python
numbers = (1, 2, 3)
print(numbers)  # (1, 2, 3)
```

## What it does

A tuple stores multiple items in one variable. It is similar to a list, but tuples cannot be changed after creation.

```python
point = (10, 20)
print(point[0])  # 10
print(point[1])  # 20
```

## When to use it

Use a tuple when you want a fixed set of values that should not change:

- coordinates
- date and time values
- returning multiple values from a function
- values that should stay constant

## Things to remember

- tuples use parentheses: `()`
- they are ordered
- they are immutable (cannot be modified)
- they can contain different data types

```python
person = ("Ana", 25, "Beograd")
print(person)  # ('Ana', 25, 'Beograd')
```

## Tuple vs list

```python
my_list = [1, 2, 3]
my_list[0] = 10  # allowed

my_tuple = (1, 2, 3)
# my_tuple[0] = 10   # this raises an error
```

A list is mutable, while a tuple is immutable.
