<h2><a href="https://leetcode.com/problems/verifying-an-alien-dictionary">953. Verifying an Alien Dictionary</a></h2>

<p>In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different <code>order</code>. The <code>order</code> of the alphabet is some permutation of lowercase letters.</p>

<p>Given a sequence of <code>words</code> written in the alien language, and the <code>order</code> of the alphabet, return <code>true</code> if and only if the given <code>words</code> are sorted lexicographically in this alien language.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
<strong>Output:</strong> true
<strong>Explanation: </strong>As 'h' comes before 'l' in this language, then the sequence is sorted.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
<strong>Output:</strong> false
<strong>Explanation: </strong>As 'd' comes after 'l' in this language, then words[0] &gt; words[1], hence the sequence is unsorted.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
<strong>Output:</strong> false
<strong>Explanation: </strong>The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" &gt; "app", because 'l' &gt; '∅', where '∅' is defined as the blank character which is less than any other character (<a href="https://en.wikipedia.org/wiki/Lexicographical_order" target="_blank">More info</a>).
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 100</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 20</code></li>
	<li><code>order.length == 26</code></li>
	<li>All characters in <code>words[i]</code> and <code>order</code> are English lowercase letters.</li>
</ul>


---

# 🛍️ Verifying-an-Alien-Dictionary | Explained

## Approach 1: Alien Dictionary Verification
### Intuition
The core idea behind this solution is to create a mapping of the alien dictionary order and then compare each pair of adjacent words in the given list based on this order. This approach is similar to how we would compare words in a standard dictionary, but with a custom order.
### Approach
The algorithm works by first creating a dictionary `alphabets` that maps each character in the alien dictionary order to its corresponding index. Then, it iterates over each pair of adjacent words in the list, comparing them character by character based on the alien dictionary order. If a word is found to be out of order, the function immediately returns `False`. If all pairs of words are found to be in order, the function returns `True`.
### Code
```python
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alphabets={}
        for i in range(len(order)):
            alphabets[order[i]]=i
        
        for j in range(1,len(words)):
            for i in range(len(max(words[j-1:j+1]))):
                if len(words[j-1])==i:
                    break
                if len(words[j])==i:
                    return False

                if alphabets[words[j-1][i]]>alphabets[words[j][i]]:
                    return False
                
                if alphabets[words[j-1][i]]<alphabets[words[j][i]]:
                    break
        
        return True
```
### Complexity
- Time: O(N * M)
  * N is the number of words in the list
  * M is the maximum length of a word
- Space: O(1)
  * The space complexity is constant because the size of the `alphabets` dictionary is determined by the length of the `order` string, which is fixed at 26 characters (one for each letter of the alphabet).

## 🕵️‍♂️ Follow-up Questions (Optional)
Some potential follow-up questions for this problem include:
1. How would you modify the solution to handle cases where the input words contain characters not found in the `order` string?
2. How would you optimize the solution for very large input lists, where the current approach may be too slow?

## 📊 Solution Analysis
1. **Core Intuition**: This solution works by creating a custom dictionary order mapping and then comparing each pair of adjacent words based on this order. It's a simple yet effective approach that takes advantage of the fact that the input words only contain characters found in the `order` string.
2. **Complexity Analysis**:
   * Time complexity: O(N * M), where N is the number of words and M is the maximum word length. This is because we're iterating over each pair of adjacent words and comparing them character by character.
   * Space complexity: O(1), because the size of the `alphabets` dictionary is constant.
3. **Critical Optimizations**: The current approach achieves optimal runtime boundaries, with a time complexity of O(N * M) that is typical for string comparison problems. However, some minor optimizations could include using a more efficient data structure for the `alphabets` dictionary, such as an array of size 26, or using a different comparison algorithm that takes advantage of the fact that the input words are in a specific order.