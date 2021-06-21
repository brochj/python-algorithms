# Binary Tree

A binary tree is a recursive data structure where each node can have 2 children at most.

A common type of binary tree is a binary search tree, in which every node has a value that is greater than or equal to the node values in the left sub-tree, and less than or equal to the node values in the right sub-tree.

## Why is look-up faster for a Binary Tree than a Linked List?

In a binary tree, every time you decide to take one of the two ‘next’ branches, you have eliminated half of the tree at that level. A node that doesn’t have to be searched at all is not going to add any time to your look up.

Of course the data has to be structured in a sensible way, which is why you are using a binary tree in the first place.

Imagine you have a list of words, and you want to know whether a given word is in the list or not.

In a linked list, you would look at each entry one after the other. Once you find the word, you can stop. But if the word isn’t in the list, you’d have to look at every element and still come up empty-handed.

If the words are organised into a binary tree based on the alphabet, things are much better. At the top level, we have a two-way split. All words starting with a-l are in one branch, the words starting with m-z are in the other. If we are testing a word that starts with ‘g’ for example, we know we don’t need to even look at the second branch, ever. We have cut the number of entries to search in half.

The next level repeats the process for the second letter (eliminating a further quarter), the third level for the third letter (eliminating another eighth) and so on. Pretty quickly we can determine whether our word is in the tree or not, and we have only searched one branch. (**Note this is a contrived example - binary trees are not usually used for word lists for other reasons**).

## References
[java-binary-tree](https://www.baeldung.com/java-binary-tree)
