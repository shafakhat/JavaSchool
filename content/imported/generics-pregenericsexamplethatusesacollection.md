---
title: Pre generics example that uses a collection.
nav: Pre generics example that ...
description: String str = (String) itr.next(); // explicit cast needed here.
section: Imported - java2s Archive
order: 1045
source: https://web.archive.org/web/20090603082712/http://www.java2s.com:80/Code/Java/Generics/Pregenericsexamplethatusesacollection.htm
---
Pre generics example that uses a collection.

```java title=Example.java
/*
Java 2, v5.0 (Tiger) New Features
by Herbert Schildt
ISBN: 0072258543
Publisher: McGraw-Hill/Osborne, 2004
*/
import java.util.*;
public class OldStyle {
  public static void main(String args[]) {
    ArrayList list = new ArrayList();
    // These lines store strings, but any type of object
    // can be stored.  In old-style code, there is no
    // convenient way restrict the type of objects stored
    // in a collection
    list.add("one");
    list.add("two");
    list.add("three");
    list.add("four");
    Iterator itr = list.iterator();
    while(itr.hasNext()) {
      // To retrieve an element, an explicit type cast is needed
      // because the collection stores only Object.
      String str = (String) itr.next(); // explicit cast needed here.
      System.out.println(str + " is " + str.length() + " chars long.");
    }
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
11.  Data structure and collections: Modern, generics version.
12.  Java generic: Generics and arrays.
13.  Collections and Data structure: the generic way
14.  The GenStack Class
