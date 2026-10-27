# `str.isalnum()`

Returns `True` if a string is nonempty and contains only letters or numeric
characters. Spaces and punctuation return `False`. Recognizes Unicode characters,
not just ASCII letters and digits.

```python
"a".isalnum()  # True
"7".isalnum()  # True
"abc123".isalnum()  # True
"č".isalnum()  # True
" ".isalnum()  # False
"!".isalnum()  # False
"".isalnum()  # False
```

## In Valid Palindrome

I used it to skip characters that are not letters or numbers:

```python
while left < right and not s[left].isalnum():
    left += 1
```

**Remember:** `isalnum()` only checks characters; it does not remove them or
change their case. Use `lower()` separately for case-insensitive comparisons.
