<h2><a href="https://leetcode.com/problems/search-in-rotated-sorted-array-ii">81. Search in Rotated Sorted Array II</a></h2>

<p>There is an integer array <code>nums</code> sorted in non-decreasing order (not necessarily with <strong>distinct</strong> values).</p>

<p>Before being passed to your function, <code>nums</code> is <strong>rotated</strong> at an unknown pivot index <code>k</code> (<code>0 &lt;= k &lt; nums.length</code>) such that the resulting array is <code>[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]</code> (<strong>0-indexed</strong>). For example, <code>[0,1,2,4,4,4,5,6,6,7]</code> might be rotated at pivot index <code>5</code> and become <code>[4,5,6,6,7,0,1,2,4,4]</code>.</p>

<p>Given the array <code>nums</code> <strong>after</strong> the rotation and an integer <code>target</code>, return <code>true</code><em> if </em><code>target</code><em> is in </em><code>nums</code><em>, or </em><code>false</code><em> if it is not in </em><code>nums</code><em>.</em></p>

<p>You must decrease the overall operation steps as much as possible.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [2,5,6,0,0,1,2], target = 0
<strong>Output:</strong> true
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [2,5,6,0,0,1,2], target = 3
<strong>Output:</strong> false
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 5000</code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
	<li><code>nums</code> is guaranteed to be rotated at some pivot.</li>
	<li><code>-10<sup>4</sup> &lt;= target &lt;= 10<sup>4</sup></code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> This problem is similar to&nbsp;<a href="/problems/search-in-rotated-sorted-array/description/" target="_blank">Search in Rotated Sorted Array</a>, but&nbsp;<code>nums</code> may contain <strong>duplicates</strong>. Would this affect the runtime complexity? How and why?</p>


---

# 🛍️ Search-in-Rotated-Sorted-Array-II | Explained

## Approach 1 (Optimized)
### Intuition
The core idea behind this solution is to utilize a modified binary search algorithm to efficiently search for a target element in a rotated sorted array, where the array may contain duplicate elements. This approach works by iteratively dividing the search space in half and adjusting the search boundaries based on the comparison of the middle element with the target and the rightmost element.

### Approach
The algorithm starts by initializing two pointers, `left` and `right`, to the beginning and end of the array, respectively. It then enters a loop that continues until `left` is greater than `right`. In each iteration, the algorithm calculates the middle index `mid` and compares the middle element `nums[mid]` with the target. If they match, the algorithm returns `True`. Otherwise, it adjusts the search boundaries based on the comparison of `nums[mid]` with `nums[right]` and the target.

### Detailed Code Analysis
Let's dive into the code:
```python
1class Solution:
2    def search(self, nums: List[int], target: int) -> bool:
3        n=len(nums)
4        left=0
5        right=n-1
```
Here, we initialize the length of the array `n`, and the `left` and `right` pointers to the beginning and end of the array, respectively.
```python
6        while left<=right:
7            mid=(left+right)//2
```
This loop continues until `left` is greater than `right`. In each iteration, we calculate the middle index `mid` using integer division.
```python
8            if nums[mid]==target:
9                return True
```
If the middle element `nums[mid]` matches the target, we immediately return `True`.
```python
10            if nums[mid]<nums[right]:
11                if nums[mid]<target<=nums[right]:
12                    left=mid+1
13                else:
14                    right=mid-1
```
If the middle element is less than the rightmost element, we know that the right half of the array is sorted. We then check if the target is within the range `[nums[mid], nums[right]]`. If it is, we adjust the `left` pointer to `mid + 1`. Otherwise, we adjust the `right` pointer to `mid - 1`.
```python
15            elif nums[right]<nums[mid]:
16                if nums[left]<=target<nums[mid]:
17                    right=mid-1
18                else:
19                    left=mid+1
```
If the rightmost element is less than the middle element, we know that the left half of the array is sorted. We then check if the target is within the range `[nums[left], nums[mid]]`. If it is, we adjust the `right` pointer to `mid - 1`. Otherwise, we adjust the `left` pointer to `mid + 1`.
```python
20            else:
21                right-=1
```
If the middle element is equal to the rightmost element, we cannot determine which half of the array is sorted. In this case, we simply decrement the `right` pointer by 1.
```python
22
23        return False
24        
```
If the loop completes without finding the target, we return `False`.

### Code
```python
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n=len(nums)
        left=0
        right=n-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                return True
            if nums[mid]<nums[right]:
                if nums[mid]<target<=nums[right]:
                    left=mid+1
                else:
                    right=mid-1
            elif nums[right]<nums[mid]:
                if nums[left]<=target<nums[mid]:
                    right=mid-1
                else:
                    left=mid+1
            else:
                right-=1
        return False
```

### Complexity
- Time: O(n) in the worst case, where n is the length of the array. This is because in the presence of duplicates, we may need to decrement the `right` pointer by 1 in each iteration, resulting in a linear time complexity. However, in the average case, the time complexity is O(log n) due to the binary search nature of the algorithm.
- Space: O(1), as we only use a constant amount of space to store the `left`, `right`, and `mid` indices.

## 🕵️‍♂️ Follow-up Questions (Optional)
Some potential follow-up questions for this problem include:
* How would you optimize the algorithm if the input array is extremely large and does not fit into memory?
* How would you modify the algorithm to search for a target element in a rotated sorted array with multiple rotations?

**Core Intuition:** 
The solution uses a modified binary search algorithm to efficiently search for a target element in a rotated sorted array, handling duplicate elements by adjusting the search boundaries based on comparisons with the middle and rightmost elements. 

**Complexity Analysis:**
* Time Complexity: O(n) 
    * Justification:
        + The algorithm iterates through the array, with a worst-case scenario of decrementing the right pointer by 1 in each iteration, resulting in linear time complexity.
        + In the average case, the time complexity is O(log n) due to the binary search nature of the algorithm.
* Space Complexity: O(1)
    * Justification: 
        + The algorithm uses a constant amount of space to store the left, right, and mid indices.

**Critical Optimizations:**
The algorithm achieves optimal runtime boundaries for searching in a rotated sorted array with duplicates, as it handles the worst-case scenario of linear time complexity. However, microscopic micro-optimizations could include using a more efficient data structure, such as a hash table, to store the elements of the array, allowing for constant-time lookups. Nevertheless, this would come at the cost of increased space complexity.