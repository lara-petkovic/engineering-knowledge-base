# `deque`

`deque` (double-ended queue) supports fast insertion and removal of items
at both ends. Import it from the `collections` module.

```python
from collections import deque

queue = deque([2, 3])
queue.append(4)      # Adds to the right: deque([2, 3, 4])
queue.appendleft(1)  # Adds to the left: deque([1, 2, 3, 4])

last = queue.pop()        # Returns and removes 4; leaves deque([1, 2, 3])
first = queue.popleft()   # Returns and removes 1; leaves deque([2, 3])
```

All four operations take **O(1)** time. With a regular list,
`pop(0)` takes **O(n)** because the remaining items must be shifted.
Calling `pop()` or `popleft()` on an empty deque raises `IndexError`.

Other useful methods and operations:

```python
queue = deque([1, 2])
queue.extend([3, 4])      # Adds multiple items to the right: [1, 2, 3, 4]
queue.extendleft([0, -1]) # Adds each item to the left: [-1, 0, 1, 2, 3, 4]
# extendleft reverses the order of the added items!

queue.rotate(1)   # Moves the last item to the front: [4, -1, 0, 1, 2, 3]
queue.rotate(-1)  # Moves the first item to the back: [-1, 0, 1, 2, 3, 4]

print(len(queue))  # 6
print(queue[0])    # -1 (first item, without removing it)
print(queue[-1])   # 4 (last item, without removing it)
queue.clear()     # Removes all items
```

For level-order tree traversal (BFS), use `append()` to add children
and `popleft()` to retrieve the next node: **first in, first out (FIFO)**.
See [Level Order Traversal](../../algorithms/trees/binary_tree_level_order_traversal.py).
