<h2><a href="https://leetcode.com/problems/contains-duplicate">217. Contains Duplicate</a></h2>

<p>Given an integer array <code>nums</code>, return <code>true</code> if any value appears <strong>at least twice</strong> in the array, and return <code>false</code> if every element is distinct.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,3,1]</span></p>

<p><strong>Output:</strong> <span class="example-io">true</span></p>

<p><strong>Explanation:</strong></p>

<p>The element 1 occurs at the indices 0 and 3.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,3,4]</span></p>

<p><strong>Output:</strong> <span class="example-io">false</span></p>

<p><strong>Explanation:</strong></p>

<p>All elements are distinct.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,1,1,3,3,4,3,2,4,2]</span></p>

<p><strong>Output:</strong> <span class="example-io">true</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>


---

# 🛍️ Contains-Duplicate | Explained

## Approach 1 (Sorting-Based)
### Intuition
The core idea behind this solution is to sort the input list and then scan for adjacent duplicates, leveraging the fact that identical elements will be placed next to each other after sorting. This strategy is akin to organizing a collection of items by their type to easily spot any duplicates.
### Approach
The algorithm works by first sorting the input list `nums` in ascending order. Then, it iterates through the sorted list, comparing each element with its predecessor. If it finds a pair of adjacent elements that are equal, it immediately returns `True`, indicating the presence of a duplicate. If the loop completes without finding any duplicates, the function returns `False`.
### Code
```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums = sorted(nums)
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False
```
### Complexity
- Time: O(n log n)
- Space: O(n)

## 👀 Detailed Explanation
1. **Core Intuition**: The algorithmic strategy used here is a sorting-based approach that relies on the property of sorted lists to have equal elements placed next to each other. This strategy facilitates the detection of duplicates by simplifying the comparison process.
2. **Complexity Analysis**:
   * Time: O(n log n) - This is due to the sorting operation, which dominates the time complexity. The subsequent for loop runs in O(n) time but is overshadowed by the sorting.
   * Space: O(n) - The space complexity is primarily influenced by the sorting operation, which in Python may require additional space depending on the sorting algorithm used (e.g., Timsort). The input list is modified in-place, but Python's sorting might still use extra space.
   * Justifications:
     + Time complexity is justified by the sorting operation, which has an average and worst-case time complexity of O(n log n).
     + Space complexity is justified by considering the potential for the sorting algorithm to use extra space, though the input list is sorted in-place.
3. **Critical Optimizations**: This sorting-based approach does not achieve optimal runtime boundaries for the problem, as more efficient solutions (like using a hash set) can solve it in O(n) time. However, it is straightforward and works well for smaller inputs or scenarios where simplicity is preferred over optimal performance. Microscopic micro-optimizations might include using a more space-efficient sorting algorithm if available, but the overall approach remains less efficient than other methods like hash-based solutions.

## 🕵️‍♂️ Follow-up Questions (Optional)
For this pattern, common interviewer follow-up questions might include:
- Can you optimize the solution to run in linear time (O(n))?
  Answer: Yes, by using a hash set to track unique elements encountered during a single pass through the input list.
- How would you adapt this solution for a streaming input (i.e., elements are provided one at a time)?
  Answer: By maintaining a hash set of seen elements and updating it as each new element arrives, similar to the optimized linear-time solution.