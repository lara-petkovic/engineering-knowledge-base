# `ord()`

Returns the Unicode code point of a single character.

```python
ord('A')   # 65
ord('a')   # 97
ord('0')   # 48
```

## What it does

`ord()` takes one character and returns its numeric Unicode value. It is the opposite of `chr()`, which converts a number back into a character.

```python
letter = 'A'
code = ord(letter)
print(code)   # 65
print(chr(code))   # A
```

## When to use it

Use `ord()` when you need to work with the numeric value of a character, for example:

- comparing letters by code value
- building custom encoding logic
- working with ASCII or Unicode-based problems
- checking character ranges

## Things to remember

- `ord()` accepts exactly one character
- if you pass a string with more than one character, Python raises an error
- `ord()` works with Unicode, not just ASCII

```python
ord('č')   # 269
```

## Example

```python
text = "ABC"
for ch in text:
    print(ch, ord(ch))
```

This prints:

```python
A 65
B 66
C 67
```
