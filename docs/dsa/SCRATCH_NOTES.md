# Scratch Notes

> Publication note: reformatted from private study notes. Employer-specific personal details and confidential context have been removed or generalized.

Determine if any value appears at least twice.
nums = [1, 2, 3, 1]

Brute Force:
sorted(nums)

{
    "user1": AAPL:400, MSFT:50,
    "user2" : AAPL: 200
}

s = "abcabcbb"
right = 5, left = 3
right - left + 1 = 3
seen = {"a", "b", "c"}

left = 5
right = 6

max_len = 6-5+1 = 2
seen = {"b", "c"}

s = "abcabcbb"
def length_longest_substring(s):
     seen = set()
     left = 0
     max_len = 0

     for right in range(len(s)):
          char = s[right]
          while char in seen:
               seen.remove(s[left])
               left += 1
          seen.add(char)
          max_len = max(max_len, right - left + 1)
     return max_len

          3
         / \
        9   20
          /    \
         15     7
