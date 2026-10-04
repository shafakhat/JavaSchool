---
title: How to implement Insertion Sort in Java
nav: How to implement Insertion...
description: while (in > 0 && number[in - 1] >= temp) // until one is smaller,
section: Imported - java2s Archive
order: 1084
source: https://web.archive.org/web/20140713164802/http://java2s.com/Tutorials/Java/Algorithms/How_to_implement_Insertion_Sort_in_Java.htm
---
In this chapter you will learn:

- Insertion Sort Implementation
- Object Insertion Sort

### Insertion Sort Implementation

```java title=Example.java
public class Main {
  public static void main(String[] args) {
    int maxSize = 100; // array size
    InsertSort arr; // reference to array
    arr = new InsertSort(maxSize); // create the array
    arr.insert(47);
    arr.insert(99);
    arr.insert(44);
    arr.insert(35);
    arr.insert(22);
    arr.insert(88);
    arr.insert(41);
    arr.insert(00);
    arr.insert(16);
    arr.insert(33);
    arr.display();
    arr.insertionSort();
    arr.display();
  }
}
class InsertSort {
  private long[] number;
  private int nElems;
  public InsertSort(int max) {
    number = new long[max];
    nElems = 0;
  }
  public void insert(long value) {
    number[nElems] = value;
    nElems++;
  }
  public void display() {
    for (int j = 0; j < nElems; j++)
      System.out.print(number[j] + " ");
    System.out.println("");
  }
  public void insertionSort() {
    int in, out;
    // out is dividing line
 for (out = 1; out < nElems; out++) {
      long temp = number[out]; // remove marked item
      in = out; // start shifts at out
 while (in > 0 && number[in - 1] >= temp) // until one is smaller,
      {
        number[in] = number[in - 1]; // shift item to right
        --in; // go left one position
      }
      number[in] = temp; // insert marked item
    }
  }
}
```

The code above generates the following result.

### Object Insertion Sort

The following code shows how to do object Insertion Sort. It compares the person's last name.

```java title=Example.java
public class Main{
  public static void main(String[] args) {
    int maxSize = 100; // array size
    ObjectInsertSort arr = new ObjectInsertSort(maxSize); // create the array
    arr.insert("Jack", "James", 24);
    arr.insert("James", "Chen", 37);
    arr.insert("Chirs", "Paul", 37);
    arr.insert("Rob", "Tom", 43);
    arr.insert("Carlo", "Sato", 21);
    arr.insert("Al", "Henry", 29);
    arr.insert("Nancy", "Jose", 72);
    arr.insert("Vang", "Minh", 22);
    System.out.println("Before sorting:");
    arr.display(); // display items
    arr.insertionSort(); // insertion-sort them
    System.out.println("After sorting:");
    arr.display(); // display them again
  }
}
class ObjectInsertSort {
  private Person[] a;
  private int nElems;
  public ObjectInsertSort(int max) {
    a = new Person[max];
    nElems = 0;
  }
  // put person into array
 public void insert(String last, String first, int age) {
    a[nElems] = new Person(last, first, age);
    nElems++;
  }
  public void display() {
    for (int j = 0; j < nElems; j++)
      a[j].displayPerson();
  }
  public void insertionSort() {
    int in, out;
    for (out = 1; out < nElems; out++) {
      Person temp = a[out]; // out is dividing line
      in = out; // start shifting at out
 while (in > 0 && // until smaller one found,
          a[in - 1].getLast().compareTo(temp.getLast()) > 0) {
        a[in] = a[in - 1]; // shift item to the right
        --in; // go left one position
      }
      a[in] = temp; // insert marked item
    }
  }
}
class Person {
  private String lastName;
  private String firstName;
  private int age;
  public Person(String last, String first, int a) {
    lastName = last;
    firstName = first;
    age = a;
  }
  public void displayPerson() {
    System.out.print("   Last name: " + lastName);
    System.out.print(", First name: " + firstName);
    System.out.println(", Age: " + age);
  }
  public String getLast() {
    return lastName;
  }
}
```

The code above generates the following result.

#### Next chapter...

What you will learn in the next chapter:

- Selection sort implementation
