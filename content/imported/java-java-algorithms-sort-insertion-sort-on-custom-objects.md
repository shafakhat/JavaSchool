---
title: Java Algorithms Sort Insertion Sort on custom objects
nav: Java Algorithms Sort Inser...
description: in = out; // start shifting at outwhile (in > 0 && // until smaller one found,
section: Imported - java2s Archive
order: 1036
source: https://web.archive.org/web/20210102113327/http://www.java2s.com/ref/java/java-algorithms-sort-insertion-sort-on-custom-objects.html
---
## Description

```java title=Example.java
class Person {privateString lastName;
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
