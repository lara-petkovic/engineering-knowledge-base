# Building a string in a loop

Strings are immutable, so `result += part` creates a new string each time. In a
loop, repeatedly copying the accumulated result can take O(n²) time and extra
memory allocations.

Collect parts in a list, then join them once:

```python
parts = []
for word in words:
    parts.append(convert(word))

result = "".join(parts)
```

List appends are amortized O(1), and `join()` builds the final string in one
pass. This takes O(n) time for n output characters and O(n) space for the
result. Use `separator.join(parts)` when a separator is needed, for example
`", ".join(parts)`.
