# A repository of leetcode easy solutions      

## TwoSum

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

## ReverseInteger

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:
Input: 123
Output: 321  

Example 2:
Input: -123
Output: -321

Example 3:
Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

## PalindromeNumber

Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:
Input: 121
Output: true

Example 2:
Input: -121
Output: false

Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: 10
Output: false

Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Follow up:

Coud you solve it without converting the integer to a string?

## RomanToInteger

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

Example 1:
Input: "III"
Output: 3  

Example 2:
Input: "IV"
Output: 4  

Example 3:
Input: "IX"
Output: 9  

Example 4:
Input: "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.  

Example 5:
Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.  

## LongestCommonPrefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: ["flower","flow","flight"]
Output: "fl"  

Example 2:
Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.  

Note:

All given inputs are in lowercase letters a-z.

## ValidParentheses ***(Learned about Stacks)***

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:
Input: "()"
Output: true  

Example 2:
Input: "()[]{}"
Output: true  

Example 3:
Input: "(]"
Output: false  

Example 4:
Input: "([)]"
Output: false  

Example 5:
Input: "{[]}"
Output: true  

## MergeTwoSortedListsUL & MergeTwoSortedListsLL (Have made a non linked and linked list version of the algorithm)

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:  
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

## RemoveDuplicatesFromSortedArray
### Problem here was list object cannot be interpreted as an integer

Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.  

Example 2:

Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

It doesn't matter what values are set beyond the returned length.  

Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.

Internally you can think of this:  

```
// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
```

## RemoveElement (First Algorithm in C++, required setting up vs code to build, compile, run c++)
### To get setup for C++  I used minGW and this tutorial https://www.youtube.com/watch?v=DIw02CaEusY  
### Still could not get it working after this, so I just ran a hello world c++ file from the command line using g++ helloworld.cpp and then running the a.exe file produced from it  
### Then decided to make a seperate repo for c++ algorithms as I think they were conflicting with the python files when running

Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example 1:  
Given nums = [3,2,2,3], val = 3,

Your function should return length = 2, with the first two elements of nums being 2.

It doesn't matter what you leave beyond the returned length.  

Example 2:  
Given nums = [0,1,2,2,3,0,4,2], val = 2,

Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4.

Note that the order of those five elements can be arbitrary.

It doesn't matter what values are set beyond the returned length.
  
Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.

Internally you can think of this:
```
// nums is passed in by reference. (i.e., without making a copy)
int len = removeElement(nums, val);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
```

## ImplementstrStr
Implement strStr().  
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "hello", needle = "ll"
Output: 2  

Example 2:
Input: haystack = "aaaaa", needle = "bba"
Output: -1  

Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.
For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

## SearchInsertPosition
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.  
You may assume no duplicates in the array.  
Example 1:  
Input: [1,3,5,6], 5
Output: 2
  
Example 2:  
Input: [1,3,5,6], 2
Output: 1

Example 3:  
Input: [1,3,5,6], 7
Output: 4

Example 4:  
Input: [1,3,5,6], 0
Output: 0

## CountAndSay
The count-and-say sequence is the sequence of integers with the first five terms as following:  

1.     1
2.     11
3.     21
4.     1211
5.     111221  

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.  
  
Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.  
  
Note: Each term of the sequence of integers will be represented as a string.  
  
Example 1:  
Input: 1
Output: "1"  

Example 2:  
Input: 4
Output: "1211"

## MaximumSubarray
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.  
Example:  
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6  

Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:
If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

## LengthLastWord

Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.  
If the last word does not exist, return 0.  
Note: A word is defined as a character sequence consists of non-space characters only.  
Example:  
Input: "Hello World"
Output: 5

## PlusOne
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.
You may assume the integer does not contain any leading zero, except the number 0 itself.  
Example 1:  
Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.  

Example 2:  
Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.

## AddBinary
Given two binary strings, return their sum (also a binary string).  
The input strings are both non-empty and contains only characters 1 or 0.  
Example 1:  
Input: a = "11", b = "1"  
Output: "100"  

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"

## SquareRoot
Implement int sqrt(int x).
Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.  
Example 1:  
Input: 4
Output: 2  
Example 2:  
Input: 8
Output: 2  

Explanation: The square root of 8 is 2.82842..., and since 
             the decimal part is truncated, 2 is returned.
             
### Solution relies heavily on newton raphson equation for finding square root
![img](https://user-images.githubusercontent.com/36263575/65521433-1f8f3e80-dee1-11e9-9754-d3bb1f98c4e2.png)


## ClimbingStairs
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1: 

Input: 2
Output: 2 
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps 

Example 2:

Input: 3
Output: 3 
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step 

**Note: we are only looking to return the number of ways it can be done, not an output of the alternative routes**

## LinkedList
A general class (not on leetcode) to learn how linkedlists work in python.
Useful resource: https://www.youtube.com/watch?v=Ast5sKQXxEU 

Creates Node and LinkedList classes to be instantiated. Fantastic tutorial on how these work.
