<h2><a href="https://leetcode.com/problems/maximum-frequency-stack">895. Maximum Frequency Stack</a></h2>

<p>Design a stack-like data structure to push elements to the stack and pop the most frequent element from the stack.</p>

<p>Implement the <code>FreqStack</code> class:</p>

<ul>
	<li><code>FreqStack()</code> constructs an empty frequency stack.</li>
	<li><code>void push(int val)</code> pushes an integer <code>val</code> onto the top of the stack.</li>
	<li><code>int pop()</code> removes and returns the most frequent element in the stack.
	<ul>
		<li>If there is a tie for the most frequent element, the element closest to the stack&#39;s top is removed and returned.</li>
	</ul>
	</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input</strong>
[&quot;FreqStack&quot;, &quot;push&quot;, &quot;push&quot;, &quot;push&quot;, &quot;push&quot;, &quot;push&quot;, &quot;push&quot;, &quot;pop&quot;, &quot;pop&quot;, &quot;pop&quot;, &quot;pop&quot;]
[[], [5], [7], [5], [7], [4], [5], [], [], [], []]
<strong>Output</strong>
[null, null, null, null, null, null, null, 5, 7, 5, 4]

<strong>Explanation</strong>
FreqStack freqStack = new FreqStack();
freqStack.push(5); // The stack is [5]
freqStack.push(7); // The stack is [5,7]
freqStack.push(5); // The stack is [5,7,5]
freqStack.push(7); // The stack is [5,7,5,7]
freqStack.push(4); // The stack is [5,7,5,7,4]
freqStack.push(5); // The stack is [5,7,5,7,4,5]
freqStack.pop();   // return 5, as 5 is the most frequent. The stack becomes [5,7,5,7,4].
freqStack.pop();   // return 7, as 5 and 7 is the most frequent, but 7 is closest to the top. The stack becomes [5,7,5,4].
freqStack.pop();   // return 5, as 5 is the most frequent. The stack becomes [5,7,4].
freqStack.pop();   // return 4, as 4, 5 and 7 is the most frequent, but 4 is closest to the top. The stack becomes [5,7].
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= val &lt;= 10<sup>9</sup></code></li>
	<li>At most <code>2 * 10<sup>4</sup></code> calls will be made to <code>push</code> and <code>pop</code>.</li>
	<li>It is guaranteed that there will be at least one element in the stack before calling <code>pop</code>.</li>
</ul>


---

# 🛍️ Maximum-Frequency-Stack | Explained

## Approach 1: Frequency Bucket Approach
### Intuition
The core idea behind this approach is to utilize a frequency map and a bucket system to efficiently store and retrieve elements based on their frequency. This approach works by maintaining a frequency count for each element and storing elements with the same frequency in the same bucket.

### Algorithm Visualized
```mermaid
graph LR
    A[FreqStack] -->|push|> B[Frequency Map]
    A -->|push|> C[Bucket System]
    A -->|pop|> D[Bucket System]
    D -->|get max frequency|> E[FreqStack]
    E -->|update frequency|> B
```

### Approach
The algorithmic logic can be broken down into two primary operations: push and pop. The push operation increases the frequency of the element and updates the bucket system accordingly. The pop operation retrieves the element with the maximum frequency and updates the frequency count.

### Detailed Code Analysis
The code utilizes a dictionary (`self.freq`) to store the frequency of each element and another dictionary (`self.bucket`) to store the elements based on their frequency. The `self.maxfreq` variable keeps track of the maximum frequency.

In the `push` method:
- Line 11: The frequency of the element is incremented using `self.freq.get(val, 0) + 1`. The `get` method returns the value for the given key if it exists; otherwise, it returns the default value (0).
- Line 12: The maximum frequency is updated if the new frequency is greater than the current maximum frequency.
- Lines 13-15: If the new frequency is not already a key in the `self.bucket` dictionary, a new list is created to store the elements with that frequency.
- Line 16: The element is appended to the list of elements with the same frequency.

In the `pop` method:
- Line 18: The element with the maximum frequency is retrieved from the corresponding bucket.
- Line 19: The frequency of the popped element is decremented.
- Lines 20-21: If the bucket for the maximum frequency becomes empty, the maximum frequency is decremented.

### Code
```python
class FreqStack:
    def __init__(self):
        self.freq = {}
        self.bucket = {}
        self.maxfreq = 0

    def push(self, val: int) -> None:
        self.freq[val] = self.freq.get(val, 0) + 1
        self.maxfreq = max(self.freq[val], self.maxfreq)
        if self.freq[val] not in self.bucket:
            self.bucket[self.freq[val]] = []
        self.bucket[self.freq[val]].append(val)

    def pop(self) -> int:
        popval = self.bucket[self.maxfreq].pop()
        self.freq[popval] = self.freq.get(popval, 0) - 1
        if self.bucket[self.maxfreq] == []:
            self.maxfreq -= 1
        return popval
```

### Complexity
- **Time:** 
  * The `push` operation has a time complexity of O(1) because dictionary lookups and updates are constant time operations. The `append` operation also has a time complexity of O(1) because lists in Python are implemented as dynamic arrays.
  * The `pop` operation has a time complexity of O(1) because list pops and dictionary lookups are constant time operations.
- **Space:** 
  * The space complexity is O(n) where n is the number of elements pushed onto the stack. This is because in the worst case, each element has a unique frequency, resulting in a separate list in the `self.bucket` dictionary.

## 🕵️‍♂️ Follow-up Questions (Optional)
What are the trade-offs between using a dictionary and a list to store the frequency of elements? 
Answer: Using a dictionary allows for constant time lookups and updates, while using a list would result in linear time complexity for these operations. However, the dictionary approach requires more memory to store the frequency count for each element.

How would you modify the implementation to handle duplicate pushes of the same element?
Answer: The current implementation already handles duplicate pushes by incrementing the frequency count for the element. No additional modifications are needed.