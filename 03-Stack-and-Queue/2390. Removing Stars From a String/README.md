<h2><a href="https://leetcode.com/problems/removing-stars-from-a-string">2390. Removing Stars From a String</a></h2>

<p>You are given a string <code>s</code>, which contains stars <code>*</code>.</p>

<p>In one operation, you can:</p>

<ul>
	<li>Choose a star in <code>s</code>.</li>
	<li>Remove the closest <strong>non-star</strong> character to its <strong>left</strong>, as well as remove the star itself.</li>
</ul>

<p>Return <em>the string after <strong>all</strong> stars have been removed</em>.</p>

<p><strong>Note:</strong></p>

<ul>
	<li>The input will be generated such that the operation is always possible.</li>
	<li>It can be shown that the resulting string will always be unique.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> s = "leet**cod*e"
<strong>Output:</strong> "lecoe"
<strong>Explanation:</strong> Performing the removals from left to right:
- The closest character to the 1<sup>st</sup> star is 't' in "lee<strong><u>t</u></strong>**cod*e". s becomes "lee*cod*e".
- The closest character to the 2<sup>nd</sup> star is 'e' in "le<strong><u>e</u></strong>*cod*e". s becomes "lecod*e".
- The closest character to the 3<sup>rd</sup> star is 'd' in "leco<strong><u>d</u></strong>*e". s becomes "lecoe".
There are no more stars, so we return "lecoe".</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> s = "erase*****"
<strong>Output:</strong> ""
<strong>Explanation:</strong> The entire string is removed, so we return an empty string.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> consists of lowercase English letters and stars <code>*</code>.</li>
	<li>The operation above can be performed on <code>s</code>.</li>
</ul>


---

# 🛍️ Removing-Stars-From-a-String | Explained

## Approach 1 (Stack-based)
### Intuition
The core idea is to utilize a stack data structure to keep track of characters that are not removed by the asterisk (\*) symbol, effectively treating the string as a stack where asterisks pop the top element off the stack. This approach works by iteratively scanning the string and appending characters to the stack unless an asterisk is encountered, at which point the top character is removed from the stack.
### Approach
The algorithm iterates through the input string character by character. When a non-asterisk character is encountered, it is pushed onto the stack. When an asterisk is encountered and the stack is not empty, the top character is popped off the stack, effectively removing it from the resulting string.
### Detailed Code Analysis
Let's break down the provided code:
- `stack=[]`: Initializes an empty list (acting as a stack) to store characters that are not removed.
- `for ele in s`: Iterates over each character `ele` in the input string `s`.
- `if ele=='*' and stack`: Checks if the current character is an asterisk and if the stack is not empty. If both conditions are true, it pops the top character off the stack (`stack.pop()`), effectively removing the character preceding the asterisk.
- `else: stack.append(ele)`: If the current character is not an asterisk or the stack is empty (in which case the asterisk has no effect), the character is appended to the stack.
- `return ''.join(stack)`: Finally, all characters remaining in the stack (which represent the characters not removed by any asterisks) are joined together into a single string and returned as the result.

### Code
```python
class Solution:
    def removeStars(self, s: str) -> str:
        stack=[]
        for ele in s:
            if ele=='*' and stack:
                stack.pop()
            else:
                stack.append(ele)
        return ''.join(stack)
```
### Complexity
- Time: O(n), where n is the length of the string `s`, because each character in the string is processed once.
- Space: O(n), because in the worst-case scenario (when there are no asterisks in the string), the stack will store all characters of the string.

## 🕵️‍♂️ Follow-up Questions (Optional)
1. **Handling Edge Cases**: How would you handle the case where the input string contains only asterisks, or where the string starts with an asterisk? Answer: The provided solution already handles these cases correctly by checking if the stack is not empty before popping an element, thus preventing index errors.
2. **Optimizations**: Are there any further optimizations that could be applied to this solution? Answer: The current solution has a time complexity of O(n) and a space complexity of O(n), which is optimal for this problem since we must at least read the input string once. Thus, no significant optimizations are possible beyond the current implementation. 

**Core Intuition**: This algorithm leverages a stack to efficiently remove characters marked by asterisks, providing a straightforward and effective solution. The strategy hinges on the Last-In-First-Out (LIFO) nature of stacks, perfectly suited for this problem's requirements.

**Complexity Analysis**:
- Time: O(n)
  * Justification: The algorithm iterates over the string once, performing a constant amount of work for each character.
- Space: O(n)
  * Justification: The space used is proportional to the size of the input string in the worst-case scenario, where all characters are stored in the stack.

**Critical Optimizations**: The provided solution achieves optimal runtime and space boundaries for the given problem. No further microscopic optimizations can significantly improve its performance, as the algorithm's efficiency is already maximized given the constraints of the problem.