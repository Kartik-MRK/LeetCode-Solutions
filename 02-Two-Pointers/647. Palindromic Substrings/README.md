<h2><a href="https://leetcode.com/problems/palindromic-substrings">647. Palindromic Substrings</a></h2>

<p>Given a string <code>s</code>, return <em>the number of <strong>palindromic substrings</strong> in it</em>.</p>

<p>A string is a <strong>palindrome</strong> when it reads the same backward as forward.</p>

<p>A <strong>substring</strong> is a contiguous sequence of characters within the string.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> s = "abc"
<strong>Output:</strong> 3
<strong>Explanation:</strong> Three palindromic strings: "a", "b", "c".
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> s = "aaa"
<strong>Output:</strong> 6
<strong>Explanation:</strong> Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 1000</code></li>
	<li><code>s</code> consists of lowercase English letters.</li>
</ul>


---

# 🛍️ Palindromic-Substrings | Explained

## Approach 1: Expand Around Center
### Intuition
The core intuition behind this approach is to treat each character in the string as the center of a potential palindrome and then expand outwards to find all possible palindromic substrings. This strategy works because it systematically explores all possible palindromes by considering both even-length and odd-length palindromes centered at each character.

### Approach
The algorithm iterates through the string, treating each character as the center of a potential palindrome. It then expands outwards from this center, checking if the characters on either side are equal. If they are, it increments the count of palindromic substrings and continues to expand. This process is repeated for both odd-length and even-length palindromes.

### Detailed Code Analysis
The provided code implements the expand around center approach. Here's a line-by-line breakdown:

- Lines 1-3 define the class and method for the solution.
- Line 4 initializes a variable `count` to keep track of the number of palindromic substrings.
- The first loop (lines 5-15) treats each character as the center of an odd-length palindrome. It initializes `left` to the character before the center and `right` to the character after the center. The while loop then expands outwards, checking if the characters at `left` and `right` are equal and incrementing `count` if they are.
- The second loop (lines 16-26) treats each pair of adjacent characters as the center of an even-length palindrome. It initializes `left` to the first character and `right` to the second character. The while loop then expands outwards, checking if the characters at `left` and `right` are equal and incrementing `count` if they are.

### Code
```python
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        for i in range(n):
            count += 1
            left = i - 1
            right = i + 1
            while left >= 0 and right < n:
                if s[left] == s[right]:
                    count += 1
                    left -= 1
                    right += 1
                else:
                    break
        for i in range(n - 1):
            left = i
            right = i + 1
            while left >= 0 and right < n:
                if s[left] == s[right]:
                    count += 1
                    left -= 1
                    right += 1
                else:
                    break
        return count
```

### Complexity
- **Time:** O(n^2) because in the worst case, for each character in the string, we might end up checking every other character. 
  * Justification:
    + The outer loop runs n times, where n is the length of the string.
    + The inner while loops potentially run n times in the worst case (when the string is filled with the same character).
- **Space:** O(1) because we only use a constant amount of space to store the count and the indices.
  * Justification:
    + We do not use any data structures that scale with the input size.
    + The space used does not grow with the size of the input string.

## Approach 2: None Detected

No other approaches were detected in the provided code. The given solution implements a single approach, namely the expand around center strategy for finding palindromic substrings. 

## 🕵️‍♂️ Follow-up Questions (Optional)
1. What if the input string is empty? The algorithm correctly handles this case, returning 0 because there are no substrings.
2. How would you optimize this solution for very large strings? To optimize, you could consider using a more efficient data structure or algorithm, but given the nature of the problem, the current solution is already quite efficient with a time complexity of O(n^2).