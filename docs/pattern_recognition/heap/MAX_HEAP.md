# Max Heap

> Publication note: reorganized as an educational template. Employer-specific details are removed; all scenarios, metrics, and identifiers are fictionalized placeholders and are not claims about the maintainer's employment.

The Invariant (memorize this)

Just like we had:

* Stack → “What is the stack storing?”

For heaps, ask:
## What does my heap represent?

For Kth Largest:
The heap stores the largest K elements seen so far.

The root is always:
The Kth largest element.

Here's the rule I want you to remember forever.
Kth Largest
Keep the largest K elements.
Among those K, the one you're most willing to throw away is the smallest.
➡️ Use a Min Heap.

Kth Smallest
Keep the smallest K elements.
Among those K, the one you're most willing to throw away is the largest.
➡️ Use a Max Heap.

Implement a Max Heap in Python:
you negate the value and since the heap only contains min heap, negating the value will
keep the lowest value at the root thus by return the max value in python by reversing the negation.
largest = -heapq.heappop(heap)
