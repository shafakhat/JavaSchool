---
title: the type argument for T must be either Number, or a class derived from Number.
nav: the type argument for T mu...
description: the type argument for T must be either Number, or a class derived from Number.
section: Imported - java2s Archive
order: 1051
source: https://web.archive.org/web/20081201185952/http://www.java2s.com:80/Code/Java/Generics/thetypeargumentforTmustbeeitherNumberoraclassderivedfromNumber.htm
---
the type argument for T must be either Number, or a class derived from Number.

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
class BoundsDemo {
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
2.  Java generic: Hierarchy argument
3.  Boxing Generic Example
4.  Demonstrate a raw generic type.
5.  T is a type parameter that will be replaced by a real type when an object of type Gen is created.
6.  Create a generic class that can compute the average of an array of numbers of any given type.
7.  Demonstrate a raw type.
8.  A subclass can add its own type parameters.
