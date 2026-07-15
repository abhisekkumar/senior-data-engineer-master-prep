# Heap Functions

> Publication note: reorganized as an educational template. Employer-specific details are removed; all scenarios, metrics, and identifiers are fictionalized placeholders and are not claims about the maintainer's employment.

## Two Rules to Memorize Forever

heappush()
New element goes to the end.
Then:Bubble DownBubble Up

heappop()
Remove the root.
Move the last element to the root.
Then: Bubble Down

Push
Add to end
↑
Bubble Up

Pop
Remove root
↓
Move last element to root
↓
Bubble Down

               1
          /         \
         2           3
      /    \      /    \
     4      5    6      7
    / \    /
   8   9  10

One comparison per level.
Level 0           1

Level 1        2     3

Level 2       4 5   6 7

Level 3      8 9 10

Maximum Comparisons:
Level 3
↓
Level 2
↓
Level 1
↓
Level 0

General Case
If the heap has n elements
The height of complete binary tree is O(log n)

So the worst-case bubble-up path is:
Leaf
↓
Parent
↓
Grandparent
↓
...
↓
Root

Insertion = O(log n)

## Why is a heap O(log n)?
Because during insertion or removal, an element only travels along one root-to-leaf path.
A complete binary tree has a height of O(log n), so the maximum number of comparisons is
proportional to the tree height, not the total number of nodes.
