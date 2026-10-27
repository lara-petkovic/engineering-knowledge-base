# Hash Map (`dict`) - Python

- **Implementation:** A hash table. Internal details below describe CPython.
- **Memory:** An index table points to entries containing references to key and value objects in heap memory. Existing objects are not deep-copied.
- **Hash function:** `hash(key)` produces an integer hash value.
- **Indexing:** The initial slot is calculated using `hash & (capacity - 1)`; the index table points to the corresponding entry.
- **Collisions:** Different keys can target the same slot. Open addressing probes other slots; key comparisons distinguish matching keys from collisions.
- **Lookup:** Hash the key, locate candidate entries, and compare keys to find the associated value. It usually avoids scanning all entries.
- **Resizing:** When capacity becomes insufficient, Python grows the table and rebuilds its indices. Referenced objects do not need to move.
- **Keys:** Must be hashable, with a stable hash while stored. Equal keys must have equal hashes. Updating an existing key replaces its value.
- **Order:** Preserves insertion order; keys are not automatically sorted.

## Time complexity

Here, `n` is the number of stored keys. Hashing and equality comparisons are assumed to take O(1); long strings and custom objects can add cost.

| Operation | Average | Worst case |
| --- | --- | --- |
| Lookup: `d[key]` | O(1) | O(n) |
| Insert/update: `d[key] = value` | O(1)* | O(n) |
| Delete: `del d[key]` | O(1) | O(n) |
| Membership: `key in d` | O(1) | O(n) |

*Insertion is expected amortized O(1); an occasional resize costs O(n). Pathological collisions can also make operations O(n).

## Space complexity

- **O(n)** for the dictionary's table and entries, including spare capacity.
- References do not copy objects, but newly created keys/values consume memory too. Count variable-sized objects separately when relevant.
- Deletion does not necessarily shrink the table immediately; analyze peak size.

## Lookup step by step

```python
person = {"name": "Lara", "age": 25, "city": "Novi Sad"}
print(person["age"])  # 25
```

`key -> hash -> index -> slot -> entry -> key comparison -> value reference`

1. **Hash:** Obtain `hash("age")`. A hash is an integer, not an index or a memory address. String hashes are normally randomized between program runs, but remain stable within a run.
2. **Index:** Calculate the initial slot with `hash_value & (capacity - 1)`. For an illustrative hash of `123456789` and capacity `8`, the index is `5`.
3. **Slot and entry:** Access slot `5` directly, without scanning slots `0` through `4`. In CPython, the slot contains an index pointing to an entry with key/value references, not the key itself.
4. **Key comparison:** Confirm that the entry's key matches `"age"`. Different keys can target the same slot, even with different hashes. If it does not match, probe other candidate slots. CPython can use object identity before an equality comparison.
5. **Value:** Return the entry's value reference, which points to the Python object `25`.

The hash and slot numbers above are illustrative, not the actual layout of this dictionary. A missing key eventually reaches an unused slot; `person[key]` then raises `KeyError`.

**Interview takeaway:** With few collisions, lookup needs only a small number of probes, giving expected **O(1)** time. Many collisions can make it **O(n)**. The hash tells Python where to start searching; comparing keys confirms the match.

Reference: [CPython dictionary implementation](https://github.com/python/cpython/blob/main/Objects/dictobject.c).
