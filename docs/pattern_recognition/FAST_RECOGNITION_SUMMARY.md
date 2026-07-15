# Fast Recognition Summary

> Publication note: reorganized as an educational template. Employer-specific details are removed; all scenarios, metrics, and identifiers are fictionalized placeholders and are not claims about the maintainer's employment.

Duplicate or lookup                  -> Hash Set / Hash Map
Frequency or grouping                -> Frequency Map
Contiguous subarray sum/count        -> Prefix Sum
Sorted pair/triplet                  -> Two Pointers
In-place array modification          -> Slow/Fast Pointers
[start, end] ranges                  -> Intervals
Sorted input                         -> Binary Search
Minimum feasible capacity/speed      -> Binary Search on Answer
Contiguous substring/subarray        -> Sliding Window
Next greater/smaller                 -> Monotonic Stack
Nested symbols or expression         -> Stack
Top K / kth largest / repeated min   -> Heap
Cycle in linked list                 -> Fast and Slow Pointers
Nth node from end                    -> Two Pointers With Gap
Tree depth/height/validation         -> DFS
Tree level-by-level                  -> BFS
Dependencies/prerequisites           -> Topological Sort
Grid connected components            -> DFS/BFS
Clone nodes with cycles              -> DFS/BFS + Hash Map

---
## PHASE 1 — HASHING, SETS, AND FREQUENCY MAPS
---

Recognition Clues:
- Need fast lookup or membership checking
- Need to detect duplicates
- Need to find a complement
- Need to count frequencies
- Need to group values by a shared signature
- Order is not the primary concern

---
[x] Contains Duplicate
---
Pattern:
Hash Set

Recognition Clue:
Check whether an element has already appeared.

Approach:
- Create a set
- Iterate through the array
- If the value already exists in the set, return True
- Otherwise, add it to the set

Time Complexity:
O(n)

Space Complexity:
O(n)

---
[x] Two Sum
---
Pattern:
Hash Map

Recognition Clue:
Find two numbers that add to a target.
For every number, search for its complement.

Complement:
target - current_number

Approach:
- Store each number and its index in a hash map
- For each number, calculate its complement
- If the complement is already in the map, return both indices

Time Complexity:
O(n)

Space Complexity:
O(n)

---
[x] Valid Anagram
---
Pattern:
Frequency Map

Recognition Clue:
Determine whether two strings contain exactly the same characters
with the same frequencies.

Approach:
- Count each character in both strings
- Compare the frequency maps

Time Complexity:
O(n)

Space Complexity:
O(1) for a fixed alphabet
O(n) for an unrestricted character set

---
[x] Group Anagrams
---
Pattern:
Hash Map + Character Signature

Recognition Clue:
Group words that contain the same characters with the same frequencies.

Approach:
- Build a signature for each word
- Use the signature as the hash-map key
- Append the word to the corresponding group

Count Signature Complexity:
Time: O(n x k)
Space: O(n x k)

Sorted Signature Complexity:
Time: O(n x k log k)
Space: O(n x k)

Where:
n = number of strings
k = maximum string length

---
[x] Top K Frequent Elements
---
Pattern:
Frequency Map + Bucket Sort

Recognition Clue:
Need the k values with the highest frequencies.

Approach:
- Count frequencies using a hash map
- Create buckets where index represents frequency
- Traverse buckets from highest frequency to lowest
- Stop after collecting k elements

Time Complexity:
O(n)

Space Complexity:
O(n)

Alternative Heap Approach:
Time: O(n log k)
Space: O(n)

---
[x] Top K Frequent Words
---
Pattern:
Frequency Map + Heap

Recognition Clue:
Need the k most frequent words with lexicographical tie-breaking.

Approach:
- Count word frequencies
- Maintain a heap of size k
- Compare first by frequency
- Compare lexicographically when frequencies are equal

Time Complexity:
O(n + m log k)

Space Complexity:
O(m + k)

Where:
n = total number of words
m = number of unique words

---
[x] Happy Number
---
Pattern:
Cycle Detection

Recognition Clue:
A repeated transformation may enter an infinite cycle.

Approach:
- Repeatedly replace the number with the sum of squares of its digits
- Detect whether the sequence reaches 1
- Otherwise detect a repeated number or cycle

Hash Set Complexity:
Time: O(log n)
Space: O(log n)

Floyd Cycle Detection Complexity:
Time: O(log n)
Space: O(1)

---
[x] Difference of Two Arrays
---
Pattern:
Hash Sets

Recognition Clue:
Find values present in one array but absent from the other.

Approach:
- Convert both arrays into sets
- Compute values unique to each set

Time Complexity:
O(n + m)

Space Complexity:
O(n + m)

---
[x] Longest Consecutive Sequence
---
Pattern:
Hash Set

Recognition Clue:
Find the longest sequence of consecutive integers without sorting.

Approach:
- Add all values to a set
- Start counting only when number - 1 does not exist
- Expand forward while consecutive values exist

Time Complexity:
O(n)

Space Complexity:
O(n)

---
## PHASE 2 — PREFIX SUM
---

Recognition Clues:
- Problem asks about a contiguous subarray
- Need to count subarrays with a specific sum
- Need to detect equal counts of two categories
- Need divisibility by k
- Recalculating every subarray sum would be too expensive

Core Formula:
subarray_sum = current_prefix_sum - previous_prefix_sum

---
[x] Subarray Sum Equals K
---
Pattern:
Prefix Sum + Hash Map

Recognition Clue:
Count contiguous subarrays whose sum equals k.

Key Check:
current_prefix_sum - k

Approach:
- Track the running prefix sum
- Store how many times each prefix sum has appeared
- Add the count of prefix_sum - k to the answer

Important Initialization:
prefix_count[0] = 1

Time Complexity:
O(n)

Space Complexity:
O(n)

---
[x] Continuous Subarray Sum
---
Pattern:
Prefix Remainder + Hash Map

Recognition Clue:
Determine whether a subarray of length at least 2 has a sum divisible by k.

Key Idea:
If two prefix sums have the same remainder when divided by k,
the values between them have a sum divisible by k.

Approach:
- Track prefix_sum % k
- Store the earliest index for each remainder
- Check whether the index difference is at least 2

Time Complexity:
O(n)

Space Complexity:
O(n)

---
[x] Contiguous Array
---
Pattern:
Prefix Balance + Hash Map

Recognition Clue:
Find the longest contiguous subarray with equal numbers of 0 and 1.

Transformation:
0 becomes -1
1 remains +1

Approach:
- Track the running balance
- Store the earliest index where each balance appeared
- If the balance appears again, the values between the indices contain
  equal numbers of 0 and 1

Time Complexity:
O(n)

Space Complexity:
O(n)

---
## PHASE 3 — TWO POINTERS
---

Recognition Clues:
- Array is sorted
- Need a pair or triplet
- Need to compare values from both ends
- Need to modify an array in place
- Need one read pointer and one write pointer
- Ordering helps eliminate possibilities

---
[x] 3Sum
---
Pattern:
Sorting + Two Pointers

Recognition Clue:
Find unique triplets whose sum equals zero.

Approach:
- Sort the array
- Fix one number
- Use left and right pointers for the remaining two numbers
- Skip duplicates

Time Complexity:
O(n²)

Space Complexity:
O(1) excluding sorting and output

---
[x] Container With Most Water
---
Pattern:
Opposite-Direction Two Pointers

Recognition Clue:
Area depends on two boundaries, their distance, and the shorter height.

Formula:
area = width x min(left_height, right_height)

Approach:
- Start with pointers at both ends
- Calculate area
- Move the pointer with the shorter height

Time Complexity:
O(n)

Space Complexity:
## O(1)

---
[x] Merge Sorted Arrays
---
Pattern:
Backward Two Pointers

Recognition Clue:
Merge two sorted arrays in place without overwriting valid values.

Approach:
- Start pointers at the end of both valid arrays
- Write the larger value into the final position
- Move backward

Time Complexity:
O(m + n)

Space Complexity:
## O(1)

---
[x] Move Zeroes
---
Pattern:
Read and Write Pointers

Recognition Clue:
Move certain values while preserving the order of other values.

Approach:
- Use one pointer to scan
- Use another pointer to place nonzero values
- Fill remaining positions with zeroes

Time Complexity:
O(n)

Space Complexity:
## O(1)

---
[x] Remove Duplicates From Sorted Array
---
Pattern:
Slow and Fast Pointers

Recognition Clue:
Sorted duplicates are adjacent and the array must be modified in place.

Approach:
- Fast pointer scans the array
- Slow pointer tracks the next unique position
- Write a value only when it differs from the previous unique value

Time Complexity:
O(n)

Space Complexity:
## O(1)

---
[x] Two Sum II
---
Pattern:
Opposite-Direction Two Pointers

Recognition Clue:
Find two values in a sorted array that equal a target.

Approach:
- Start left at the beginning
- Start right at the end
- If sum is too small, move left
- If sum is too large, move right

Time Complexity:
O(n)

Space Complexity:
## O(1)

---
## PHASE 4 — INTERVALS
---

Recognition Clues:
- Input contains start and end values
- Need to merge overlapping ranges
- Need to insert a new range
- Need intersections between two sorted interval lists
- Problem involves schedules, bookings, or time ranges

Overlap Condition:
max(start1, start2) <= min(end1, end2)

---
[x] Insert Interval
---
Pattern:
Interval Merge

Recognition Clue:
Insert a new interval into an already sorted, non-overlapping list.

Approach:
- Add intervals that end before the new interval
- Merge all overlapping intervals
- Add the merged interval
- Add remaining intervals

Time Complexity:
O(n)

Space Complexity:
O(n) for output

---
[x] Interval List Intersections
---
Pattern:
Intervals + Two Pointers

Recognition Clue:
Find overlaps between two independently sorted interval lists.

Intersection:
start = max(start1, start2)
end = min(end1, end2)

Approach:
- Compare one interval from each list
- Add the intersection when start <= end
- Move the pointer whose interval ends first

Time Complexity:
O(n + m)

Space Complexity:
O(1) excluding output

---
[x] Merge Intervals
---
Pattern:
Sorting + Interval Merge

Recognition Clue:
Combine all overlapping intervals.

Approach:
- Sort intervals by start
- Compare each interval with the last merged interval
- Merge when overlapping
- Otherwise append a new interval

Time Complexity:
O(n log n)

Space Complexity:
O(n) for output

---
## PHASE 5 — BINARY SEARCH
---

Recognition Clues:
- Input is sorted
- Search space is monotonic
- Need first or last valid position
- Need minimum feasible answer
- Need maximum allowed answer
- A condition changes from False to True

---
[x] Binary Search
---
Pattern:
Standard Binary Search

Recognition Clue:
Find a target in a sorted array.

Approach:
- Compare the target with the middle value
- Eliminate half of the search space each time

Time Complexity:
O(log n)

Space Complexity:
## O(1)

---
[x] Search Insert Position
---
Pattern:
Lower-Bound Binary Search

Recognition Clue:
Find the first position where the value is greater than or equal to target.

Time Complexity:
O(log n)

Space Complexity:
## O(1)

---
[x] First and Last Position of Element
---
Pattern:
Two Boundary Binary Searches

Recognition Clue:
Find both the first and last occurrence of a duplicate target.

Approach:
- Run binary search for the left boundary
- Run binary search for the right boundary

Time Complexity:
O(log n)

Space Complexity:
## O(1)

---
[x] Find Peak Element
---
Pattern:
Binary Search on Slope

Recognition Clue:
Need any local peak where neighboring values are smaller.

Approach:
- Compare nums[mid] with nums[mid + 1]
- If nums[mid] is smaller, a peak exists on the right
- Otherwise, a peak exists at mid or on the left

Time Complexity:
O(log n)

Space Complexity:
## O(1)

---
[x] Find Minimum in Rotated Sorted Array
---
Pattern:
Rotated Binary Search

Recognition Clue:
Sorted array was rotated and the minimum is at the rotation boundary.

Approach:
- Compare middle value with right value
- If middle is greater, minimum is on the right
- Otherwise, minimum is at middle or on the left

Time Complexity:
O(log n)

Space Complexity:
## O(1)

---
[x] First Bad Version
---
Pattern:
First-True Boundary Search

Recognition Clue:
Boolean values follow this structure:

False False False True True True

Need the first True.

Time Complexity:
O(log n)

Space Complexity:
## O(1)

---
[x] Search in Rotated Sorted Array
---
Pattern:
Rotated Binary Search

Recognition Clue:
One half of the array is always sorted.

Approach:
- Determine which half is sorted
- Check whether target lies inside that half
- Eliminate the other half

Time Complexity:
O(log n)

Space Complexity:
## O(1)

---
[x] Single Element in a Sorted Array
---
Pattern:
Binary Search Using Pair Alignment

Recognition Clue:
Every value appears twice except one, and the array is sorted.

Approach:
- Force the midpoint to an even index
- Compare nums[mid] with nums[mid + 1]
- Correct pair alignment exists before the single value
- Alignment changes after the single value

Time Complexity:
O(log n)

Space Complexity:
## O(1)

---
[x] Capacity to Ship Packages Within D Days
---
Pattern:
Binary Search on Answer

Recognition Clue:
Find the minimum capacity that satisfies a deadline.

Search Space:
Maximum package weight to total package weight

Feasibility Check:
## Can all packages be shipped within D days using this capacity?

Time Complexity:
O(n log S)

Space Complexity:
## O(1)

Where:
S = sum(weights) - max(weights)

---
[x] Koko Eating Bananas
---
Pattern:
Binary Search on Answer

Recognition Clue:
Find the minimum speed that completes all work within a deadline.

Search Space:
1 to maximum pile size

Feasibility Check:
## Can Koko finish all piles within h hours at this speed?

Time Complexity:
O(n log M)

Space Complexity:
## O(1)

Where:
M = maximum pile size

---
[x] Split Array Largest Sum
---
Pattern:
Binary Search on Answer

Recognition Clue:
Minimize the largest sum among k contiguous partitions.

Search Space:
Maximum array value to total array sum

Feasibility Check:
Can the array be divided into at most k partitions where no partition
## exceeds the candidate maximum?

Time Complexity:
O(n log S)

Space Complexity:
## O(1)

---
## PHASE 6 — SLIDING WINDOW
---

Recognition Clues:
- Problem asks about a contiguous substring or subarray
- Need longest, shortest, maximum, or minimum valid window
- Right pointer expands the window
- Left pointer shrinks the window
- Need to maintain counts, sums, or distinct values

---
## PHASE 6A — FIXED-SIZE SLIDING WINDOW
---

Recognition Clues:
- Window size is provided
- Every candidate window has the same length
- Need maximum, average, permutation, or anagram

---
[x] Maximum Average Subarray I
---
Pattern:
Fixed-Size Sliding Window

Recognition Clue:
Find the maximum sum or average among all subarrays of size k.

Approach:
- Calculate the first window sum
- Add the incoming value
- Remove the outgoing value

Time Complexity:
O(n)

Space Complexity:
## O(1)

---
[x] Find All Anagrams in a String
---
Pattern:
Fixed Window + Frequency Map

Recognition Clue:
Every valid substring must have the same length and frequency counts
as the pattern.

Approach:
- Build the pattern frequency map
- Maintain a window of pattern length
- Compare or track matching frequencies

Time Complexity:
O(n + m)

Space Complexity:
O(1) for a fixed alphabet

---
[x] Permutation in String
---
Pattern:
Fixed Window + Frequency Map

Recognition Clue:
Determine whether any substring is a permutation of another string.

Approach:
- Window length equals the pattern length
- Track character frequencies inside the window
- Return True when all frequencies match

Time Complexity:
O(n + m)

Space Complexity:
O(1) for a fixed alphabet

---
## PHASE 6B — VARIABLE-SIZE SLIDING WINDOW
---

Recognition Clues:
- Need longest or shortest valid substring/subarray
- Window grows until invalid or valid
- Left pointer moves based on a condition
- Common wording includes:
  - without repeating
  - at most k
  - minimum length
  - minimum window

---
[x] Longest Substring Without Repeating Characters
---
Pattern:
Variable Sliding Window + Hash Set or Map

Recognition Clue:
Find the longest substring where every character is unique.

Approach:
- Expand right pointer
- When a duplicate appears, move left until the duplicate is removed
- Track maximum window length

Time Complexity:
O(n)

Space Complexity:
O(k)

Where:
k = number of unique characters in the window

---
[x] Longest Substring With At Most K Distinct Characters
---
Pattern:
Variable Sliding Window + Frequency Map

Recognition Clue:
Find the longest substring containing no more than k unique characters.

Approach:
- Expand the window
- Track character frequencies
- Shrink while distinct count exceeds k

Time Complexity:
O(n)

Space Complexity:
O(k)

---
[x] Minimum Size Subarray Sum
---
Pattern:
Variable Sliding Window

Recognition Clue:
Find the shortest contiguous subarray whose sum is at least target.

Important Condition:
This standard sliding-window solution requires positive numbers.

Approach:
- Expand until sum reaches target
- Shrink while the window remains valid
- Track minimum length

Time Complexity:
O(n)

Space Complexity:
## O(1)

---
[x] Minimum Window Substring
---
Pattern:
Variable Sliding Window + Frequency Map

Recognition Clue:
Find the smallest substring containing all required characters,
including duplicates.

Approach:
- Track required character counts
- Expand until all requirements are satisfied
- Shrink while the window remains valid
- Track the smallest valid window

Time Complexity:
O(n + m)

Space Complexity:
O(k)

---
[x] Longest Substring Without Repeating
---
Pattern:
Variable Sliding Window + Hash Set or Map

Recognition Clue:
Same problem as Longest Substring Without Repeating Characters.

Time Complexity:
O(n)

Space Complexity:
O(k)

---
## PHASE 6C — SLIDING WINDOW + MONOTONIC DEQUE
---

---
[x] Sliding Window Maximum
---
Pattern:
Monotonic Deque

Recognition Clue:
Need the maximum value for every window of size k.

Approach:
- Store indices in decreasing order of value
- Remove indices outside the current window
- Remove smaller values from the back
- Front of deque is the current maximum

Time Complexity:
O(n)

Space Complexity:
O(k)

---
## PHASE 7 — STACK
---

Recognition Clues:
- Need last-in, first-out behavior
- Matching parentheses or nested structures
- Evaluating expressions
- Removing adjacent values
- Tracking unresolved elements

---
[x] Evaluate Reverse Polish Notation
---
Pattern:
Expression Stack

Recognition Clue:
Operators act on the two most recently processed operands.

Approach:
- Push numbers onto the stack
- For an operator, pop two operands
- Apply the operator
- Push the result

Time Complexity:
O(n)

Space Complexity:
O(n)

---
[x] Min Stack
---
Pattern:
Stack + Minimum Tracking

Recognition Clue:
Need push, pop, top, and getMin in constant time.

Approach:
- Store the current minimum with every value
or
- Maintain a separate minimum stack

Time Complexity:
O(1) per operation

Space Complexity:
O(n)

---
[x] Remove Adjacent Duplicates in a String
---
Pattern:
Stack

Recognition Clue:
The current character may cancel the previous character.

Approach:
- If current character equals stack top, pop
- Otherwise, push

Time Complexity:
O(n)

Space Complexity:
O(n)

---
[x] Valid Parentheses
---
Pattern:
Matching Stack

Recognition Clue:
Each closing bracket must match the most recent unmatched opening bracket.

Approach:
- Push opening brackets
- For a closing bracket, verify the stack top matches
- Stack must be empty at the end

Time Complexity:
O(n)

Space Complexity:
O(n)

---
## PHASE 7B — MONOTONIC STACK
---

Recognition Clues:
- Next greater element
- Next smaller element
- Previous greater or smaller element
- Number of steps until a larger value
- Elements remain unresolved until a future value appears

---
[x] Daily Temperatures
---
Pattern:
Decreasing Monotonic Stack

Recognition Clue:
For each day, find how many days until a warmer temperature.

Approach:
- Store unresolved indices
- When the current temperature is warmer than the stack top,
  resolve the previous index

Time Complexity:
O(n)

Space Complexity:
O(n)

---
[x] Next Greater Element I
---
Pattern:
Decreasing Monotonic Stack + Hash Map

Recognition Clue:
For every selected number, find the first greater value to its right.

Approach:
- Process the larger array using a monotonic stack
- Store each number’s next greater result in a map
- Look up answers for the requested values

Time Complexity:
O(n + m)

Space Complexity:
O(n)

---
## PHASE 8 — HEAP / PRIORITY QUEUE
---

Recognition Clues:
- Need top k values
- Need kth largest or kth smallest
- Repeatedly need the smallest or largest active item
- Need to merge sorted streams
- Data arrives continuously

---
[x] K Closest Points to Origin
---
Pattern:
Size-K Max Heap

Recognition Clue:
Keep the k smallest distances without sorting all points.

Approach:
- Calculate each point’s squared distance
- Maintain a max heap of size k
- Remove the farthest point when heap exceeds k

Time Complexity:
O(n log k)

Space Complexity:
O(k)

Alternative Sorting:
Time: O(n log n)
Space: Depends on sorting implementation

---
[x] Kth Largest Element in an Array
---
Pattern:
Size-K Min Heap

Recognition Clue:
Need only the kth largest value, not a fully sorted array.

Approach:
- Maintain a min heap of size k
- Remove the smallest when heap exceeds k
- Heap root is the kth largest

Time Complexity:
O(n log k)

Space Complexity:
O(k)

Quickselect Alternative:
Average Time: O(n)
Worst Time: O(n²)

---
[x] Kth Largest Element in a Stream
---
Pattern:
Persistent Size-K Min Heap

Recognition Clue:
Values arrive continuously and kth largest must be returned after each insertion.

Approach:
- Maintain a min heap of size k
- Add incoming value
- Remove smallest if size exceeds k
- Return heap root

Initialization Time:
O(n log k)

Add Operation:
O(log k)

Space Complexity:
O(k)

---
[x] Merge K Sorted Lists
---
Pattern:
Min Heap + Linked Lists

Recognition Clue:
Repeatedly select the smallest current node among k sorted lists.

Approach:
- Add each non-empty list head to the heap
- Pop the smallest node
- Append it to the result
- Add that node’s next node to the heap

Time Complexity:
O(N log k)

Space Complexity:
O(k)

Where:
N = total number of nodes
k = number of lists

---
[x] Top K Frequent Elements
---
Pattern:
Frequency Map + Bucket Sort or Heap

Recognition Clue:
Need the k values with the highest occurrence counts.

Bucket Sort Complexity:
Time: O(n)
Space: O(n)

Heap Complexity:
Time: O(n log k)
Space: O(n)

---
## PHASE 9 — LINKED LISTS
---

Recognition Clues:
- Need to reverse pointer direction
- Need cycle detection
- Need node relative to the end
- Need to merge sorted node sequences
- Need O(1) extra-space pointer manipulation

---
[x] Linked List Cycle
---
Pattern:
Fast and Slow Pointers

Recognition Clue:
Determine whether following next pointers eventually repeats a node.

Approach:
- Slow moves one step
- Fast moves two steps
- If they meet, a cycle exists

Time Complexity:
O(n)

Space Complexity:
## O(1)

---
[x] Merge Two Sorted Lists
---
Pattern:
Linked-List Two Pointers

Recognition Clue:
Merge two sorted node sequences.

Approach:
- Compare the current node from each list
- Attach the smaller node
- Advance that list pointer

Time Complexity:
O(n + m)

Space Complexity:
## O(1)

---
[x] Remove Nth Node From End of List
---
Pattern:
Two Pointers With a Fixed Gap

Recognition Clue:
Need a node based on its distance from the end.

Approach:
- Use a dummy node
- Move fast pointer n steps ahead
- Move both pointers until fast reaches the end
- Slow will be before the node to remove

Time Complexity:
O(n)

Space Complexity:
## O(1)

---
[x] Reverse Linked List
---
Pattern:
Pointer Reversal

Recognition Clue:
Reverse the direction of every next pointer.

Required Variables:
previous
current
next_node

Time Complexity:
O(n)

Space Complexity:
## O(1)

---
## PHASE 10 — BINARY TREES
---

Recognition Clues:
- Need depth, height, or balance
- Need to compare tree structures
- Need information from both child subtrees
- Need recursive divide-and-combine processing
- Need level-by-level traversal

---
[x] Balanced Binary Tree
---
Pattern:
Postorder DFS

Recognition Clue:
A node is balanced only after the heights of both child subtrees are known.

Approach:
- Recursively calculate left and right heights
- If height difference exceeds 1, mark unbalanced
- Return height to the parent

Time Complexity:
O(n)

Space Complexity:
O(h)

Worst Case:
O(n) for a skewed tree

Balanced Tree:
O(log n)

---
[x] Maximum Depth of a Binary Tree
---
Pattern:
## Dfs

Recognition Clue:
Depth is derived from the maximum child depth.

Formula:
1 + max(left_depth, right_depth)

Time Complexity:
O(n)

Space Complexity:
O(h)

---
[x] Same Tree
---
Pattern:
Parallel DFS

Recognition Clue:
Compare two trees node by node at matching positions.

Approach:
- Both nodes null means equal
- One node null means unequal
- Different values mean unequal
- Recursively compare left and right children

Time Complexity:
O(n)

Space Complexity:
O(h)

---
[x] Lowest Common Ancestor of a Binary Tree
---
Pattern:
Recursive DFS

Recognition Clue:
Find the lowest node whose subtree contains both target nodes.

Approach:
- Return current node if it is null, p, or q
- Search left and right subtrees
- If both return non-null, current node is the LCA
- Otherwise return the non-null side

Time Complexity:
O(n)

Space Complexity:
O(h)

---
[x] Construct Binary Tree From Preorder and Inorder Traversal
---
Pattern:
Recursion + Hash Map

Recognition Clue:
Preorder identifies the root.
Inorder separates the left and right subtrees.

Approach:
- First preorder value is the root
- Find the root index in inorder
- Recursively build left and right subtrees
- Use a hash map for inorder indices

Time Complexity:
O(n)

Space Complexity:
O(n)

---
[x] Binary Tree Level Order Traversal
---
Pattern:
BFS + Queue

Recognition Clue:
Process nodes one tree level at a time.

Approach:
- Add root to queue
- Process exactly the current queue size for each level
- Add child nodes for the next level

Time Complexity:
O(n)

Space Complexity:
O(w)

Where:
w = maximum tree width

---
[x] Binary Tree Reverse Level Order Traversal
---
Pattern:
BFS + Reverse Result

Recognition Clue:
Return tree levels from bottom to top.

Approach:
- Perform normal BFS
- Reverse the level results
or
- Insert completed levels at the front

Time Complexity:
O(n)

Space Complexity:
O(n)

---
## PHASE 10B — BINARY SEARCH TREES
---

Recognition Clues:
- Left subtree values are smaller
- Right subtree values are larger
- Need ordered-tree validation
- Need to eliminate an entire subtree based on value

---
[x] Validate Binary Search Tree
---
Pattern:
DFS With Lower and Upper Bounds

Recognition Clue:
Every node must satisfy constraints created by all of its ancestors.

Condition:
lower_bound < node.value < upper_bound

Important:
Checking only immediate children is not sufficient.

Time Complexity:
O(n)

Space Complexity:
O(h)

---
[x] Lowest Common Ancestor of a BST
---
Pattern:
BST Property

Recognition Clue:
Both target values determine whether to move left or right.

Approach:
- If both values are smaller, move left
- If both values are larger, move right
- Otherwise, current node is the LCA

Time Complexity:
O(h)

Space Complexity:
O(1) iterative

---
## PHASE 11 — GRAPHS
---

Recognition Clues:
- Entities are connected by edges
- Need to visit reachable nodes
- Need connected components
- Need cycle detection
- Need dependency ordering
- Need to copy a network while preserving relationships

---
[x] Clone Graph
---
Pattern:
DFS or BFS + Hash Map

Recognition Clue:
Copy every node and edge while preventing duplicate copies and infinite cycles.

Required Mapping:
original_node -> cloned_node

Approach:
- Create a clone when first visiting a node
- Store it in the map
- Recursively or iteratively clone its neighbors

Time Complexity:
## O(V + E)

Space Complexity:
## O(V)

---
[x] Course Schedule
---
Pattern:
Topological Sort or Directed Cycle Detection

Recognition Clue:
Prerequisites form directed dependencies.
Need to determine whether all tasks can be completed.

Kahn’s Algorithm:
- Build adjacency list
- Calculate indegrees
- Add zero-indegree nodes to queue
- Remove completed dependencies
- Verify all nodes were processed

DFS Alternative:
- Unvisited
- Visiting
- Visited
- Encountering a visiting node means a cycle

Time Complexity:
## O(V + E)

Space Complexity:
## O(V + E)

---
[x] Number of Islands
---
Pattern:
Grid DFS or BFS

Recognition Clue:
Count connected components in a two-dimensional grid.

Approach:
- Scan every cell
- When land is found, increase island count
- Traverse all connected land cells
- Mark them as visited

Time Complexity:
O(rows x columns)

Space Complexity:
O(rows x columns) worst case

Possible Space Sources:
- DFS recursion stack
- BFS queue
- Visited set
