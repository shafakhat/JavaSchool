---
title: Stats attempts (unsuccessfully) to create a generic class
nav: Stats attempts (unsuccessf...
description: // Stats attempts (unsuccessfully) to create a generic class that can compute
section: Imported - java2s Archive
order: 1049
source: https://web.archive.org/web/20090416234441/http://www.java2s.com:80/Code/Java/Generics/Statsattemptsunsuccessfullytocreateagenericclass.htm
---
```java title=Example.java
/*
Java 2, v5.0 (Tiger) New Features
by Herbert Schildt
ISBN: 0072258543
Publisher: McGraw-Hill/Osborne, 2004
*/
// Stats attempts (unsuccessfully) to create a generic class that can compute
// the average of an array of numbers of any given type.
// The class contains an error!
public class Stats<T> {
  T[] nums; // nums is an array of type T
  // Pass the constructor a reference to
  // an array of type T.
  Stats(T[] o) {
    nums = o;
  }
  // Return type double in all cases.
  double average() {
    double sum = 0.0;
    for(int i=0; i < nums.length; i++)
      sum += nums[i].doubleValue(); // Error!!!
    return sum / nums.length;
  }
}
```

1.  A simple generic class.
---  ---
2.  Demonstrate the non generic class
3.  A simple generic class heirarchy.
4.  A nongeneric class can be the superclass of a generic subclass.
5.  Use the instanceof operator with a generic class hierarchy.
6.  Java hierarchy generic class
7.  Custom Generic Object Tester
