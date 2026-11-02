# Tree

A tree is a **non-linear, hierarchical data structure**. It is made of nodes
connected by edges and has one starting node called the **root**. A node can
have child nodes; a node with no children is a **leaf**. Unlike a general graph,
a tree has no cycles, and there is exactly one path from the root to each node.

```text
        A          root
       / \
      B   C        children of A
     /
    D              leaf
```

## Tree types

- A **binary tree** allows each node to have at most two children, commonly
  called `left` and `right`.
- A **binary search tree (BST)** is a binary tree with an ordering rule: values
  in the left subtree are smaller than the node's value, and values in the
  right subtree are larger. A BST is not necessarily balanced.

Python does not have a built-in tree type. Trees are usually represented with
node objects that refer to their children.

## Traversal

Traversal means visiting the nodes in a particular order. For a binary tree:

- **Preorder:** node, left subtree, right subtree
- **Inorder:** left subtree, node, right subtree (visits BST values in sorted
  order)
- **Postorder:** left subtree, right subtree, node
- **Level order:** visit nodes level by level, usually with a queue

Visiting all `n` nodes takes **O(n)** time. Recursive depth-first traversals use
**O(h)** call-stack space, where `h` is the tree's height; level-order traversal
can use **O(w)** space, where `w` is the maximum width of the tree.

## BST search

Searching a BST takes **O(h)** time: **O(log n)** when the tree is balanced, but
**O(n)** in the worst case when it is skewed. A regular binary tree does not
automatically have the BST ordering rule, so searching it may require checking
every node.
