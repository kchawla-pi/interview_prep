# Technical Interview Notes


## Arrays and Strings

#### Array
**Topics:**
-   Sizing
    -   In more statically typed languages, you have to worry about the size of an array.
    -   In its most basic implementation, arrays store data sequentially with **fixed** space.  If you want to use an array that can be resized, you must implement a solution to allow it to grow in size.
    -   The most common resizing method is to create a new array with double the size of the first array, then copy the elements of the first array to the new array.
    -   In Python, lists are implemented as resizeable arrays, so thankfully, you do not have to worry about this.
-   Optimization
    -   If an array is sorted, you can think about doing optimized search methods, like with a binary search.

**Big O efficiency:**
-   Indexing: O(1)
-   Search: O(n)
-   Insertion: O(n)
-   Optimized Search: O(log n)


#### Hash Tables / Maps
**Topics:**
-   Hashing
    -   A hash table is a structure that stores arbitrary data.  In Python, sets are a hash table.  It need not be a storage of key-value pairs.
    -   A hash map is a hash table, but with a collection of key-value pairs.
    -   The relationship between a pair is based on a hash function.
    -   When you provide a hash table with a new key, a hash function takes the key and generates a hash value.
    -   The data structure underlying a hash table/map need not be thought of as an array.  You could implement the back-end of a hash table to be a balanced binary search tree, and the hash value result from the hash algorithm would point you to where in the tree your value is.  A BST hash table would have O(logN) lookup, but would potentially use less space.

-   Collisions
    -   Two distinct pieces of data have the same hash value
    -   Put more simply, if you have two keys, 'a' and 'b' and in the hash map, the hash algorithm generates the exact same hash value, we have a collision.
    -   To handle collisions, two common ways would be to run the hash algorithm on the result recursively until you reach an unused hash value. Other ways would be to look around from the collision to find a new hash value.
    -   If the number of collisions is very high, the worst case runtime to retrieve an element starts to approach O(N).

**Big O efficiency:**
-   Indexing: O(1)
-   Search: O(1)
-   Insertion:  O(1)

### Array and String Methods
1.  isUnique()
    -   Determine if a string or list has all unique elements. Attempt to do so without any additional data structures.
2.  checkPermutation()
    -   Given two strings, determine if one is a permutation of the other.
3.  URLify()
    -   Write a method to replace all spaces in a string with '%20'. Trim any spaces on the end.
4.  palindromePermutation()
    -   Given one string, determine if it is a permutation of a palindrome.
5.  oneAway()
    -   There are three possible edits to a string: insert a character, remove a character, or replace a character.  Given two strings, write a function to check whether they are one edit or zero edits away.
6.  stringCompression()
    -   Implement a method to perform basic string compression using the counts of repeated characters, i.e. 'aabcccccaaa' --> 'a2b1c5a3'
7.  rotateMatrix()
    -   Given a 2D array of NxN size, rotate the array 90 degrees **in place**.
8.  zeroMatrix()
    -   Given a 2D array of MxN size, if an element is 0, its entire row and column are set to 0.
9.  stringRotation()
    -   Assume you have a method isSubstring() which checks if one word is a substring of another.  Given two strings s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring().