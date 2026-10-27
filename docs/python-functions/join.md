# `str.join()`

Joins strings from an iterable (such as a list) into one string, placing the
separator between elements. Call it on the separator: `separator.join(items)`.

```python
chars = ["a", "b", "c"]
"".join(chars)  # "abc"
"-".join(chars)  # "a-b-c"
" ".join(chars)  # "a b c"
```

## With sorting: Group Anagrams

```python
s = "tea"
sorted(s)  # ['a', 'e', 't']
"".join(sorted(s))  # "aet"
```

Anagrams such as `"tea"` and `"eat"` produce the same sorted string, which can
serve as a dictionary key for grouping them.

## Remember

- `sorted()` returns a new sorted **list**.
- `join()` combines strings into one **string**; every element must be a string,
  otherwise it raises `TypeError`.
- `split()` goes the other direction: `"a-b-c".split("-")` returns
  `["a", "b", "c"]`.
