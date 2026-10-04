---
title: Java Algorithms Binary Search Tree
nav: Java Algorithms Binary Sea...
description: tree.inorder();/*www.java2s.com*/System.out.print("\nPostorder: ");
section: Imported - java2s Archive
order: 1019
source: https://web.archive.org/web/20210102113324/http://www.java2s.com/ref/java/java-algorithms-binary-search-tree.html
---
## Description

```java title=Example.java
import java.util.Collection;
import java.util.List;
publicclass Main {
  publicstaticvoid main(String[] args) {
    // Create a BST
    BinarySearchTree<String> tree = new BinarySearchTree<>();
    tree.insert("A");
    tree.insert("M");
    tree.insert("T");
    tree.insert("J");
    tree.insert("G");
    tree.insert("X");
    tree.insert("P");
    tree.insert("D");
    System.out.print("Inorder (sorted): ");
    tree.inorder();System.out.print("\nPostorder: ");
    tree.postorder();
    System.out.print("\nPreorder: ");
    tree.preorder();
    System.out.print("\nThe number of nodes is " + tree.getSize());
    System.out.print("\nIs P in the tree? " + tree.search("P"));
    System.out.print("\nA path from the root to P is: ");
    List<TreeNode<String>> path = tree.path("P");
    for (int i = 0; path != null && i < path.size(); i++)
      System.out.print(path.get(i).element + " ");
    Integer[] numbers = { 2, 4, 3, 1, 8, 5, 6, 7 };
    BinarySearchTree<Integer> intTree = new BinarySearchTree<>(numbers);
    System.out.print("\nInorder (sorted): ");
    intTree.inorder();
    tree.delete("G");
    printTree(tree);
    System.out.println("\nAfter delete A:");
    tree.delete("A");
    printTree(tree);
    System.out.println("\nAfter delete M:");
    tree.delete("M");
    printTree(tree);
  }
  publicstaticvoid printTree(BinarySearchTree tree) {
    // Traverse treeSystem.out.print("Inorder (sorted): ");
    tree.inorder();
    System.out.print("\nPostorder: ");
    tree.postorder();
    System.out.print("\nPreorder: ");
    tree.preorder();
    System.out.print("\nThe number of nodes is " + tree.getSize());
    System.out.println();
  }
}
class BinarySearchTree<E extendsComparable<E>> implements Tree<E> {
  protectedTreeNode<E> root;
  protectedint size = 0;
  public BinarySearchTree() {
  }
  public BinarySearchTree(E[] objects) {
    for (int i = 0; i < objects.length; i++)
      add(objects[i]);
  }
  @Overridepublicboolean search(E e) {
    TreeNode<E> current = root; // Start from the rootwhile (current != null) {
      if (e.compareTo(current.element) < 0) {
        current = current.left;
      } elseif (e.compareTo(current.element) > 0) {
        current = current.right;
      } else// element matches current.elementreturn true; // Element is found
    }
    return false;
  }
  @Overridepublicboolean insert(E e) {
    if (root == null)
      root = createNewNode(e); // Create a new rootelse {
      // Locate the parent nodeTreeNode<E> parent = null;
      TreeNode<E> current = root;
      while (current != null)
        if (e.compareTo(current.element) < 0) {
          parent = current;
          current = current.left;
        } elseif (e.compareTo(current.element) > 0) {
          parent = current;
          current = current.right;
        } elsereturn false; // Duplicate node not inserted// Create the new node and attach it to the parent nodeif (e.compareTo(parent.element) < 0)
        parent.left = createNewNode(e);
      else
        parent.right = createNewNode(e);
    }
    size++;
    return true; // Element inserted successfully
  }
  protectedTreeNode<E> createNewNode(E e) {
    returnnewTreeNode<>(e);
  }
  @Override/** Inorder traversal from the root */publicvoid inorder() {
    inorder(root);
  }
  /** Inorder traversal from a subtree */protectedvoid inorder(TreeNode<E> root) {
    if (root == null)
      return;
    inorder(root.left);
    System.out.print(root.element + " ");
    inorder(root.right);
  }
  @Override/** Postorder traversal from the root */publicvoid postorder() {
    postorder(root);
  }
  /** Postorder traversal from a subtree */protectedvoid postorder(TreeNode<E> root) {
    if (root == null)
      return;
    postorder(root.left);
    postorder(root.right);
    System.out.print(root.element + " ");
  }
  @Override/** Preorder traversal from the root */publicvoid preorder() {
    preorder(root);
  }
  /** Preorder traversal from a subtree */protectedvoid preorder(TreeNode<E> root) {
    if (root == null)
      return;
    System.out.print(root.element + " ");
    preorder(root.left);
    preorder(root.right);
  }
  @Override/** Get the number of nodes in the tree */publicint getSize() {
    return size;
  }
  /** Returns the root of the tree */publicTreeNode<E> getRoot() {
    return root;
  }
  /** Returns a path from the root leading to the specified element */publicList<TreeNode<E>> path(E e) {
    List<TreeNode<E>> list = new java.util.ArrayList<>();
    TreeNode<E> current = root; // Start from the rootwhile (current != null) {
      list.add(current); // Add the node to the listif (e.compareTo(current.element) < 0) {
        current = current.left;
      } elseif (e.compareTo(current.element) > 0) {
        current = current.right;
      } elsebreak;
    }
    return list;
  }
  @Overridepublicboolean delete(E e) {
    TreeNode<E> parent = null;
    TreeNode<E> current = root;
    while (current != null) {
      if (e.compareTo(current.element) < 0) {
        parent = current;
        current = current.left;
      } elseif (e.compareTo(current.element) > 0) {
        parent = current;
        current = current.right;
      } elsebreak;
    }
    if (current == null)
      return false; // Element is not in the tree// Case 1: current has no left childif (current.left == null) {
      // Connect the parent with the right child of the current nodeif (parent == null) {
        root = current.right;
      } else {
        if (e.compareTo(parent.element) < 0)
          parent.left = current.right;
        else
          parent.right = current.right;
      }
    } else {
      // Case 2: The current node has a left child// Locate the rightmost node in the left subtree of// the current node and also its parentTreeNode<E> parentOfRightMost = current;
      TreeNode<E> rightMost = current.left;
      while (rightMost.right != null) {
        parentOfRightMost = rightMost;
        rightMost = rightMost.right; // Keep going to the right
      }
      // Replace the element in current by the element in rightMost
      current.element = rightMost.element;
      // Eliminate rightmost nodeif (parentOfRightMost.right == rightMost)
        parentOfRightMost.right = rightMost.left;
      else// Special case: parentOfRightMost == current
        parentOfRightMost.left = rightMost.left;
    }
    size--;
    return true; // Element deleted successfully
  }
  @Override/** Obtain an iterator. Use in order. */public java.util.Iterator<E> iterator() {
    returnnew InorderIterator();
  }
  // Inner class InorderIteratorprivateclass InorderIterator implements java.util.Iterator<E> {
    // Store the elements in a listprivate java.util.ArrayList<E> list = new java.util.ArrayList<>();
    privateint current = 0; // Point to the current element in listpublic InorderIterator() {
      inorder(); // Traverse binary tree and store elements in list
    }
    /** Inorder traversal from the root */privatevoid inorder() {
      inorder(root);
    }
    /** Inorder traversal from a subtree */privatevoid inorder(TreeNode<E> root) {
      if (root == null)
        return;
      inorder(root.left);
      list.add(root.element);
      inorder(root.right);
    }
    @Override/** More elements for traversing? */publicboolean hasNext() {
      if (current < list.size())
        return true;
      return false;
    }
    @Override/** Get the current element and move to the next */public E next() {
      return list.get(current++);
    }
    @Override// Remove the element returned by the last next()publicvoid remove() {
      if (current == 0) // next() has not been called yetthrownewIllegalStateException();
      delete(list.get(--current));
      list.clear(); // Clear the list
      inorder(); // Rebuild the list
    }
  }
  @Override/** Remove all elements from the tree */publicvoid clear() {
    root = null;
    size = 0;
  }
}
interface Tree<E> extendsCollection<E> {
  /** Return true if the element is in the tree */publicboolean search(E e);
  /**
   * Insert element e into the binary tree Return true if the element is inserted
   * successfully
   */publicboolean insert(E e);
  /**
   * Delete the specified element from the tree Return true if the element is
   * deleted successfully
   */publicboolean delete(E e);
  /** Get the number of elements in the tree */publicint getSize();
  /** Inorder traversal from the root */publicdefaultvoid inorder() {
  }
  /** Postorder traversal from the root */publicdefaultvoid postorder() {
  }
  /** Preorder traversal from the root */publicdefaultvoid preorder() {
  }
  @Override/** Return true if the tree is empty */publicdefaultboolean isEmpty() {
    returnthis.size() == 0;
  }
  @Overridepublicdefaultboolean contains(Object e) {
    return search((E) e);
  }
  @Overridepublicdefaultboolean add(E e) {
    return insert(e);
  }
  @Overridepublicdefaultboolean remove(Object e) {
    return delete((E) e);
  }
  @Overridepublicdefaultint size() {
    return getSize();
  }
  @Overridepublicdefaultboolean containsAll(Collection<?> c) {
    // Left as an exercisereturn false;
  }
  @Overridepublicdefaultboolean addAll(Collection<? extends E> c) {
    // Left as an exercisereturn false;
  }
  @Overridepublicdefaultboolean removeAll(Collection<?> c) {
    // Left as an exercisereturn false;
  }
  @Overridepublicdefaultboolean retainAll(Collection<?> c) {
    // Left as an exercisereturn false;
  }
  @OverridepublicdefaultObject[] toArray() {
    // Left as an exercisereturn null;
  }
  @Overridepublicdefault <T> T[] toArray(T[] array) {
    // Left as an exercisereturn null;
  }
}
classTreeNode<E> {
  public E element;
  publicTreeNode<E> left;
  publicTreeNode<E> right;
  publicTreeNode(E e) {
    element = e;
  }
}
```

PreviousNext

## Related

- Java Lambda Expression Predefined Functional Interfaces
- Java Lambda Expression Functional Interfaces mark with @FunctionalInterface
- Java static Import
