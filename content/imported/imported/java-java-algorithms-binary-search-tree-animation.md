---
title: Java Algorithms Binary Search Tree Animation
nav: Java Algorithms Binary Sea...
description: private BinarySearchTree<Integer> tree = new BinarySearchTree<>();
section: Imported - java2s Archive
order: 1018
source: https://web.archive.org/web/20210102113325/http://www.java2s.com/ref/java/java-algorithms-binary-search-tree-animation.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Description

Java Algorithms Binary Search Tree Animation

```java title=Example.java
import java.util.Collection;
import java.util.List;

import javafx.application.Application;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.HBox;
import javafx.scene.layout.Pane;
import javafx.scene.paint.Color;
import javafx.scene.shape.Circle;
import javafx.scene.shape.Line;
import javafx.scene.text.Text;
import javafx.stage.Stage;

class BTView extends Pane {
  private BinarySearchTree<Integer> tree = new BinarySearchTree<>();
  privatedouble radius = 15; // Tree node radiusprivatedouble vGap = 50; // Gap between two levels in a tree

  BTView(BinarySearchTree<Integer> tree) {
    this.tree = tree;
    setStatus("Tree is empty");
  }/*www.java2s.com*/publicvoid setStatus(String msg) {
    getChildren().add(newText(20, 20, msg));
  }

  publicvoid displayTree() {
    this.getChildren().clear(); // Clear the paneif (tree.getRoot() != null) {
      // Display tree recursively
      displayTree(tree.getRoot(), getWidth() / 2, vGap, getWidth() / 4);
    }
  }

  /** Display a subtree rooted at position (x, y) */privatevoid displayTree(TreeNode<Integer> root, double x, double y, double hGap) {
    if (root.left != null) {
      // Draw a line to the left node
      getChildren().add(newLine(x - hGap, y + vGap, x, y));
      // Draw the left subtree recursively
      displayTree(root.left, x - hGap, y + vGap, hGap / 2);
    }

    if (root.right != null) {
      // Draw a line to the right node
      getChildren().add(newLine(x + hGap, y + vGap, x, y));
      // Draw the right subtree recursively
      displayTree(root.right, x + hGap, y + vGap, hGap / 2);
    }

    // Display a node
    Circle circle = new Circle(x, y, radius);
    circle.setFill(Color.WHITE);
    circle.setStroke(Color.BLACK);
    getChildren().addAll(circle, newText(x - 4, y + 4, root.element + ""));
  }
}

publicclass Main extends Application {
  @Overridepublicvoid start(Stage primaryStage) {
    BinarySearchTree<Integer> tree = new BinarySearchTree<>(); // Create a tree

    BorderPane pane = new BorderPane();
    BTView view = new BTView(tree); // Create a View
    pane.setCenter(view);

    TextField tfKey = newTextField();
    tfKey.setPrefColumnCount(3);
    tfKey.setAlignment(Pos.BASELINE_RIGHT);
    Button btInsert = newButton("Insert");
    Button btDelete = newButton("Delete");
    HBox hBox = new HBox(5);
    hBox.getChildren().addAll(newLabel("Enter a key: "), tfKey, btInsert, btDelete);
    hBox.setAlignment(Pos.CENTER);
    pane.setBottom(hBox);

    btInsert.setOnAction(e -> {
      int key = Integer.parseInt(tfKey.getText());
      if (tree.search(key)) { // key is in the tree already
        view.displayTree();
        view.setStatus(key + " is already in the tree");
      } else {
        tree.insert(key); // Insert a new key
        view.displayTree();
        view.setStatus(key + " is inserted in the tree");
      }
    });

    btDelete.setOnAction(e -> {
      int key = Integer.parseInt(tfKey.getText());
      if (!tree.search(key)) { // key is not in the tree
        view.displayTree();
        view.setStatus(key + " is not in the tree");
      } else {
        tree.delete(key); // Delete a key
        view.displayTree();
        view.setStatus(key + " is deleted from the tree");
      }
    });

    // Create a scene and place the pane in the stage
    Scene scene = new Scene(pane, 450, 250);
    primaryStage.setTitle("BSTAnimation");
    primaryStage.setScene(scene);
    primaryStage.show();
  }

  publicstaticvoid main(String[] args) {
    launch(args);
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

- Java Lambda Expression Functional Interfaces mark with @FunctionalInterface
- Java static Import
- Java Algorithms Binary Search Tree
- Java Algorithms Bracket Checker
- Java Algorithms Convert infix expression to postfix expression
