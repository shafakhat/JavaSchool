---
title: Java Tutorial - What is a generic type in Java
nav: Java Tutorial - What is a ...
description: The term generics means parameterized types. Using generics, it is possible to create a single class that works with different types of data. A class, interface, or metho
section: Imported - java2s Archive
order: 50457
source: https://www.java2s.com/Tutorials/Java/Java_Language/8000__Java_Generic_introduction.html
---
```java title=Example.java
```

The term generics means parameterized types. Using generics, it is possible to create a single class that works with different types of data. A class, interface, or method that operates on a parameterized type is called generic.

## Syntax

Here is the syntax for declaring a generic class:

```java title=Example.java
class className<type-param-list> {}
```

Here is the syntax for declaring a reference to a generic class:

## Example

A Simple Generics Example

```java title=Example.java
// T is a type parameter that will be replaced by a real type
// when an object of type Gen is created.
class Gen<T> {
  T ob; // declare an object of type T
  Gen(T o) {
    ob = o;
  }
  // Return ob.
  T getob() {
    return ob;
  }
  // Show type of T.
void showType() {
    System.out.println("Type of T is " + ob.getClass().getName());
  }
}
publicclass Main {
  publicstaticvoid main(String args[]) {
    Gen<Integer> iOb = new Gen<Integer>(88);
    iOb.showType();
    int v = iOb.getob();
    System.out.println("value: " + v);
    Gen<String> strOb = new Gen<String>("Generics Test");
    strOb.showType();
    String str = strOb.getob();
    System.out.println("value: " + str);
  }
}
```

T is the name of a type parameter. T is used to declare an object. Generics work only with objects Generic types differ based on their type arguments

The code above generates the following result.

## Example 2

You can declare more than one type parameter in a generic type.

```java title=Example.java
// A simple generic class with two type parameters: T and V.
class TwoGen<T, V> {
  T ob1;
  V ob2;
  TwoGen(T o1, V o2) {
    ob1 = o1;
    ob2 = o2;
  }
  void showTypes() {
    System.out.println("Type of T is " + ob1.getClass().getName());
    System.out.println("Type of V is " + ob2.getClass().getName());
  }
  T getob1() {
    return ob1;
  }
  V getob2() {
    return ob2;
  }
}
publicclass Main {
  publicstaticvoid main(String args[]) {
    TwoGen<Integer, String> tgObj = new TwoGen<Integer, String>(88, "Generics");
    tgObj.showTypes();
    int v = tgObj.getob1();
    System.out.println("value: " + v);
    String str = tgObj.getob2();
    System.out.println("value: " + str);
  }
}
```

The code above generates the following result.

## Example 3

The following code declares and uses a Queue<E> generic type.

```java title=Example.java
class Queue<E> {
  private E[] elements;
  privateint head=0, tail=0;
  Queue(int size) {
    elements = (E[]) new Object[size];
  }
  void insert(E element) throws QueueFullException {
    if (isFull())
      thrownew QueueFullException();
    elements[tail] = element;
    tail = (tail + 1) % elements.length;
  }
  E remove() throws QueueEmptyException {
    if (isEmpty()){
      thrownew QueueEmptyException();
    }
    E element = elements[head];
    head = (head + 1) % elements.length;
    return element;
  }
  boolean isEmpty() {
    return head == tail;
  }
  boolean isFull() {
    return (tail + 1) % elements.length == head;
  }
}
class QueueEmptyException extends Exception {
}
class QueueFullException extends Exception {
}
publicclass Main{
  publicstaticvoid main(String[] args)
      throws QueueFullException, QueueEmptyException {
    Queue<String> queue = new Queue<String>(6);
    System.out.println("Empty: " + queue.isEmpty());
    System.out.println("Full: " + queue.isFull());
    queue.insert("A");
    queue.insert("B");
    queue.insert("C");
    queue.insert("D");
    queue.insert("E");
    System.out.println("Empty: " + queue.isEmpty());
    System.out.println("Full: " + queue.isFull());
    System.out.println("Removing " + queue.remove());
    System.out.println("Empty: " + queue.isEmpty());
    System.out.println("Full: " + queue.isFull());
    System.out.println("Adding F");
    queue.insert("F");
    while (!queue.isEmpty()){
      System.out.println("Removing " + queue.remove());
    }
    System.out.println("Empty: " + queue.isEmpty());
    System.out.println("Full: " + queue.isFull());
  }
}
```

Output:

## Deal with legacy code

To handle the transition to generics, Java allows a generic class to be used without any type arguments.

Here is an example that shows a raw type in action:

```java title=Example.java
class MyClass<T> {
  T ob;
  MyClass(T o) {
    ob = o;
  }
  T getob() {
    return ob;
  }
}
publicclass Main {
  publicstaticvoid main(String args[]) {
    MyClass raw = new MyClass(new Double(98.6));
    double d = (Double) raw.getob();
    System.out.println("value: " + d);
  }
}
```

Output:

- « Previous
