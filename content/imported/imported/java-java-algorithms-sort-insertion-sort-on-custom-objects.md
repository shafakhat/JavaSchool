---
title: Java Algorithms Sort Insertion Sort on custom objects
nav: Java Algorithms Sort Inser...
description: in = out; // start shifting at outwhile (in > 0 && // until smaller one found,
section: Imported - java2s Archive
order: 1036
source: https://web.archive.org/web/20210102113327/http://www.java2s.com/ref/java/java-algorithms-sort-insertion-sort-on-custom-objects.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Description

Java Algorithms Sort Insertion Sort on custom objects

```java title=Example.java
class Person {/*fromwww.java2s.com*/privateString lastName;
   privateint age;

   public Person(String last, int a) { // constructor
      lastName = last;
      age = a;
   }

   publicvoid displayPerson() {
      System.out.print("   Last name: " + lastName);
      System.out.println(", Age: " + age);
   }

   publicString getLast() // get last name
   {
      return lastName;
   }
}

class MyArray {
   private Person[] a;
   privateint nElems;

   public MyArray(int max) {
      a = new Person[max];
      nElems = 0; // no items yet
   }

   publicvoid insert(String last, int age) {
      a[nElems] = new Person(last, age);
      nElems++; // increment size
   }

   publicvoid display() {
      for (int j = 0; j < nElems; j++) // for each element,
         a[j].displayPerson(); // display it
   }

   publicvoid insertionSort() {
      int in, out;

      for (out = 1; out < nElems; out++) {
         Person temp = a[out]; // out is dividing line
         in = out; // start shifting at outwhile (in > 0 && // until smaller one found,
               a[in - 1].getLast().compareTo(temp.getLast()) > 0) {
            a[in] = a[in - 1]; // shift item to the right
            --in; // go left one position
         }
         a[in] = temp; // insert marked item
      }
   }
}

publicclass Main {
   publicstaticvoid main(String[] args) {
      int maxSize = 100; // array size
      MyArray arr; // reference to array
      arr = new MyArray(maxSize); // create the array

      arr.insert("E", 24);
      arr.insert("G", 39);
      arr.insert("D", 37);
      arr.insert("S", 37);
      arr.insert("Y", 43);
      arr.insert("H", 21);
      arr.insert("S", 29);
      arr.insert("V", 42);
      arr.insert("V", 22);
      arr.insert("C", 18);

      System.out.println("Before sorting:");
      arr.display();

      arr.insertionSort(); // insertion-sort themSystem.out.println("After sorting:");
      arr.display();
   }
}
```

PreviousNext

## Related

- Java Algorithms Sort Bubble Sort
- Java Algorithms Sort Heap Sort
- Java Algorithms Sort Insertion Sort
- Java Algorithms Sort point along circle in clockwise order
- Java Algorithms Sort Selection Sort
