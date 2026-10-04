---
title: Java Algorithms Huffman code
nav: Java Algorithms Huffman code
description: // Count frequencyint[] counts = getCharacterFrequency("this is a test test test");
section: Imported - java2s Archive
order: 1027
source: https://web.archive.org/web/20210102113326/http://www.java2s.com/ref/java/java-algorithms-huffman-code.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Description

Java Algorithms Huffman code

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String[] args) {
    // Count frequencyint[] counts = getCharacterFrequency("this is a test test test");

    System.out.printf("%-15s%-15s%-15s%-15s\n", "ASCII Code", "Character", "Frequency", "Code");

    Tree tree = getHuffmanTree(counts); // Create a Huffman treeString[] codes = getCode(tree.root); // Get codesfor (int i = 0; i < codes.length; i++) {
      if (counts[i] != 0) {// (char)i is not in text if counts[i] is 0System.out.printf("%-15d%-15s%-15d%-15s\n", i, (char) i + "", counts[i], codes[i]);
      }/*fromwww.java2s.com*/
    }
  }
  /**
   * Get Huffman codes for the characters This method is called once after a
   * Huffman tree is built
   */publicstaticString[] getCode(Node root) {
    if (root == null)
      return null;
    String[] codes = newString[2 * 128];
    assignCode(root, codes);
    return codes;
  }
  /* Recursively get codes to the leaf node */privatestaticvoid assignCode(Node root, String[] codes) {
    if (root.left != null) {
      root.left.code = root.code + "0";
      assignCode(root.left, codes);

      root.right.code = root.code + "1";
      assignCode(root.right, codes);
    } else {
      codes[(int) root.element] = root.code;
    }
  }

  /** Get a Huffman tree from the codes */publicstatic Tree getHuffmanTree(int[] counts) {
    // Create a heap to hold trees
    Heap<Tree> heap = new Heap<>(); // Defined in Listing 24.10for (int i = 0; i < counts.length; i++) {
      if (counts[i] > 0)
        heap.add(new Tree(counts[i], (char) i)); // A leaf node tree
    }

    while (heap.getSize() > 1) {
      Tree t1 = heap.remove(); // Remove the smallest weight tree
      Tree t2 = heap.remove(); // Remove the next smallest weight
      heap.add(new Tree(t1, t2)); // Combine two trees
    }
    return heap.remove(); // The final tree
  }
  publicstaticint[] getCharacterFrequency(String text) {
    int[] counts = newint[256]; // 256 ASCII charactersfor (int i = 0; i < text.length(); i++)
      counts[(int) text.charAt(i)]++; // Count the character in textreturn counts;
  }
}

/** Huffman coding tree */class Tree implementsComparable<Tree> {
  Node root; // The root of the tree/** Create a tree with two subtrees */public Tree(Tree t1, Tree t2) {
    root = newNode();
    root.left = t1.root;
    root.right = t2.root;
    root.weight = t1.root.weight + t2.root.weight;
  }

  /** Create a tree containing a leaf node */public Tree(int weight, char element) {
    root = newNode(weight, element);
  }

  @Override/** Compare trees based on their weights */publicint compareTo(Tree t) {
    if (root.weight < t.root.weight) // Purposely reverse the orderreturn 1;
    elseif (root.weight == t.root.weight)
      return 0;
    elsereturn -1;
  }

}

classNode {
  char element; // Stores the character for a leaf nodeint weight; // weight of the subtree rooted at this nodeNode left; // Reference to the left subtreeNode right; // Reference to the right subtreeString code = ""; // The code of this node from the rootpublicNode() {
  }
  publicNode(int weight, char element) {
    this.weight = weight;
    this.element = element;
  }
}

class Heap<E extendsComparable> {
  private java.util.ArrayList<E> list = new java.util.ArrayList<E>();

  public Heap() {
  }

  public Heap(E[] objects) {
    for (int i = 0; i < objects.length; i++)
      add(objects[i]);
  }

  publicvoid add(E newObject) {
    list.add(newObject); // Append to the heapint currentIndex = list.size() - 1; // The index of the last nodewhile (currentIndex > 0) {
      int parentIndex = (currentIndex - 1) / 2;
      // Swap if the current object is greater than its parentif (list.get(currentIndex).compareTo(list.get(parentIndex)) > 0) {
        E temp = list.get(currentIndex);
        list.set(currentIndex, list.get(parentIndex));
        list.set(parentIndex, temp);
      } elsebreak; // the tree is a heap now

      currentIndex = parentIndex;
    }
  }

  public E remove() {
    if (list.size() == 0)
      return null;

    E removedObject = list.get(0);
    list.set(0, list.get(list.size() - 1));
    list.remove(list.size() - 1);

    int currentIndex = 0;
    while (currentIndex < list.size()) {
      int leftChildIndex = 2 * currentIndex + 1;
      int rightChildIndex = 2 * currentIndex + 2;

      // Find the maximum between two childrenif (leftChildIndex >= list.size())
        break; // The tree is a heapint maxIndex = leftChildIndex;
      if (rightChildIndex < list.size()) {
        if (list.get(maxIndex).compareTo(list.get(rightChildIndex)) < 0) {
          maxIndex = rightChildIndex;
        }
      }

      // Swap if the current node is less than the maximumif (list.get(currentIndex).compareTo(list.get(maxIndex)) < 0) {
        E temp = list.get(maxIndex);
        list.set(maxIndex, list.get(currentIndex));
        list.set(currentIndex, temp);
        currentIndex = maxIndex;
      } elsebreak; // The tree is a heap
    }

    return removedObject;
  }

  publicint getSize() {
    return list.size();
  }
}
```

PreviousNext

## Related

- Java Algorithms Convert number to English words example 3
- Java Algorithms Convert number to English words example 4
- Java Algorithms Convert number to French words
- Java Algorithms Move along circle
- Java Algorithms Parse postfix arithmetic expressions
