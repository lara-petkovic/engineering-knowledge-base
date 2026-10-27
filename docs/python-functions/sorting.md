# `list.sort()` and `sorted()`

| | `list.sort()` | `sorted()` |
| --- | --- | --- |
| Input | A list | Any iterable |
| Result | Modifies the list; returns `None` | Returns a new sorted list |
| Original | Changed | Unchanged |

```python
nums = [3, 1, 2]
ordered = sorted(nums)  # [1, 2, 3]; nums stays [3, 1, 2]
nums.sort()  # nums becomes [1, 2, 3]
sorted("tea")  # ['a', 'e', 't']
```

Both accept `reverse=True` for descending order and `key=` for a sorting rule,
such as `sorted(words, key=len)` to sort by length. Equal sorting keys preserve
their original order (**stable sorting**).

## Algorithm and complexity

In CPython, both use **Timsort**, an adaptive merge-based algorithm that exploits
existing ordered runs. Modern CPython uses a **Powersort** merge strategy within
this sorting implementation.

For `n` elements, assuming O(1) comparisons:

| | Both operations |
| --- | --- |
| Best-case time (already ordered input) | O(n) |
| Average / worst-case time | O(n log n) |
| Worst-case sorting workspace | O(n) |

`sorted()` also allocates a new O(n) result list. **In-place does not mean O(1)
extra memory:** `sort()` can still need O(n) temporary workspace.

**Remember:** Use `nums.sort()` to change the list; use `sorted(nums)` to keep it.
Do not write `nums = nums.sort()` — that assigns `None`.

Sources: [Python sorting guide](https://docs.python.org/3/howto/sorting.html),
[CPython sorting design](https://github.com/python/cpython/blob/main/Objects/listsort.txt).
