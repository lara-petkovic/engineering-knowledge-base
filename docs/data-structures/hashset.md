# Hash Set (`set`)

I used a hash set to track unique values. Python stores references to elements
in a hash table, using their hashes to locate slots in memory.

```python
nums = [4, 2, 4, 7]
seen = set()

for number in nums:
    seen.add(number)

print(seen)  # Contains 2, 4, and 7; iteration order is not guaranteed.
print(4 in seen)  # True
```

## How it behaves in memory

In CPython, the set and its table live in heap memory. A hash determines a
starting slot; if another element occupies it, Python probes other slots and
compares elements. Matching hashes alone do not imply equal elements.

```text
set → table slot [hash + reference] → element object
```

An insertion normally uses a free slot in the existing table. When the table
needs to grow, Python allocates a larger table and rearranges the entries, not
the referenced objects. See the [CPython set implementation](https://github.com/python/cpython/blob/main/Objects/setobject.c).

## Time complexity

Let `k` be the number of stored elements. These costs assume constant-time
hashing and equality comparisons, as is usual for bounded-size integers.

| Operation | Average / amortized | Worst case |
| --- | --- | --- |
| Membership: `value in seen` | O(1) average | O(k) |
| Insert: `seen.add(value)` | O(1) amortized, expected | O(k) |
| Delete: `seen.remove(value)`, `seen.discard(value)` | O(1) average | O(k) |

`remove()` raises `KeyError` for a missing element; `discard()` does not.
Collisions can make operations linear, and one insertion can trigger a resize.
Building a set from `n` items takes O(n) expected time, but can take O(n²) under
pathological collisions. Hashing or comparing long strings or custom objects
can add further cost.

## Space complexity

- The set stores only unique values: four input elements above produce three
  entries. Adding a duplicate does not create another entry.
- In CPython, each occupied table slot stores a reference to an element and its
  hash. Adding an existing object does not copy the whole object into the set.
- The table also has unused slots to keep lookups efficient. It can grow by
  allocating a larger table, so memory usage is greater than just the references
  for the stored elements. Exact byte counts depend on the Python implementation
  and version.
- For `k` distinct integers, this set uses **O(k) extra space**. With `n` input
  elements, the worst case is **O(n)** because every value could be distinct.
  The input list already exists and is not counted as extra space.
- A set holding references to existing objects does not mean O(1) space: the
  number of table entries still grows with the number of unique elements.

For algorithm analysis, count how many entries the set can hold at its largest.
If measuring actual bytes, `sys.getsizeof(seen)` reports the set's own size,
including its table, but excludes the objects it references.

Deleting elements does not guarantee immediate shrinking: capacity may reflect
an earlier, larger set. Consider peak size when analyzing an algorithm. If the
algorithm creates new variable-sized element objects, count their memory too.

