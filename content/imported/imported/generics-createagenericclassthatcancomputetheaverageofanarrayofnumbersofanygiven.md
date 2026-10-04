---
title: Create a generic class that can compute the average of an array of numbers of any given type.
nav: Create a generic class tha...
description: Create a generic class that can compute the average of an array of numbers of any given type.
section: Imported - java2s Archive
order: 1016
source: https://web.archive.org/web/20081201185941/http://www.java2s.com:80/Code/Java/Generics/Createagenericclassthatcancomputetheaverageofanarrayofnumbersofanygiventype.htm
---
```java title=Example.java
class Stats<T> {
  T[] nums;
  Stats(T[] o) {
    nums = o;
  }
  double average() {
    double sum = 0.0;
    for (int i = 0; i < nums.length; i++)
      sum += nums[i].doubleValue(); // Error!!!
    return sum / nums.length;
  }
}
```

1.  A simple generic class with two type parameters: T and V.
---  ---
2.  Java generic: Hierarchy argument
3.  Boxing Generic Example
4.  Demonstrate a raw generic type.
5.  T is a type parameter that will be replaced by a real type when an object of type Gen is created.
6.  the type argument for T must be either Number, or a class derived from Number.
7.  Demonstrate a raw type.
8.  A subclass can add its own type parameters.
