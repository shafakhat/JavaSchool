---
title: Java generic
nav: Java generic
description: 1. A simple generic class with two type parameters: T and V.
section: Imported - java2s Archive
order: 1039
source: https://web.archive.org/web/20100213125847/http://java2s.com/Code/Java/Generics/JavagenericHierarchyargument.htm
---
Java generic: Hierarchy argument

```java title=Example.java
class Stats<T extends Number> {
  T[] nums;
  Stats(T[] o) {
    nums = o;
  }
  double average() {
    double sum = 0.0;
    for (int i = 0; i < nums.length; i++)
      sum += nums[i].doubleValue();
    return sum / nums.length;
  }
}
public class BoundsDemo {
  public static void main(String args[]) {
    Integer inums[] = { 1, 2, 3, 4, 5 };
    Stats<Integer> iob = new Stats<Integer>(inums);
    double v = iob.average();
    System.out.println("iob average is " + v);
    Double dnums[] = { 1.1, 2.2, 3.3, 4.4, 5.5 };
    Stats<Double> dob = new Stats<Double>(dnums);
    double w = dob.average();
    System.out.println("dob average is " + w);
  }
}
```

1.  A simple generic class with two type parameters: T and V.
---  ---
2.  Boxing Generic Example
3.  Demonstrate a raw generic type.
4.  T is a type parameter that will be replaced by a real type when an object of type Gen is created.
5.  Create a generic class that can compute the average of an array of numbers of any given type.
6.  the type argument for T must be either Number, or a class derived from Number.
7.  Demonstrate a raw type.
8.  A subclass can add its own type parameters.
