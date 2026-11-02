# Copying a list with `[:]`

I learned from the [Subsets example](../../algorithms/backtracking/subsets.py)
that `[:]` makes a copy of a list:

```python
sol = [1, 2]
snapshot = sol[:]

sol.append(3)
print(snapshot)  # [1, 2]
```

In the example, `res.append(sol[:])` saves the current subset. If it appended
`sol` directly, every result would refer to the same list, which keeps changing
during backtracking.

This is a **shallow copy**: the outer list is new, but nested mutable objects
inside it are still shared.
