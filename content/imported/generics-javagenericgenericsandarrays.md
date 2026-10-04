---
title: Java generic
nav: Java generic
description: // Can't create an array of type-specific generic references.
section: Imported - java2s Archive
order: 1038
source: https://web.archive.org/web/20090603182351/http://www.java2s.com:80/Code/Java/Generics/JavagenericGenericsandarrays.htm
---
Java generic: Generics and arrays.

```java title=Example.java
class Gen<T extends Number> {
  T ob;
  T vals[];
  Gen(T o, T[] nums) {
    ob = o;
    vals = nums;
  }
}
public class GenArrays {
  public static void main(String args[]) {
    Integer n[] = { 1, 2, 3, 4, 5 };
    Gen<Integer> iOb = new Gen<Integer>(50, n);
    // Can't create an array of type-specific generic references.
    // Gen<Integer> gens[] = new Gen<Integer>[10]; // Wrong!
    Gen<?> gens[] = new Gen<?>[10]; // OK
  }
}
```

1.  Creating a Type-Specific List
---  ---
2.  A list declared to hold objects of a type T can also hold objects that extend from T.
3.  A value retrieved from a type-specific list does not need to be casted
4.  Generic ArrayList
5.  Generic Data Structure
6.  Unchecked Example
7.  Generic Stack
8.  Enum and Generic
9.  Generic HashMap
10.  Foreach and generic data structure
11.  Pre generics example that uses a collection.
12.  Data structure and collections: Modern, generics version.
13.  Collections and Data structure: the generic way
14.  The GenStack Class
