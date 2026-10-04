---
title: Data structure and collections
nav: Data structure and collect...
description: // The following statement will now cause a compile-time eror.
section: Imported - java2s Archive
order: 1019
source: https://web.archive.org/web/20090520050118/http://www.java2s.com:80/Code/Java/Generics/DatastructureandcollectionsModerngenericsversion.htm
---
Data structure and collections: Modern, generics version.

```java title=Example.java
/*
Java 2, v5.0 (Tiger) New Features
by Herbert Schildt
ISBN: 0072258543
Publisher: McGraw-Hill/Osborne, 2004
*/
import java.util.*;
public class NewStyle {
  public static void main(String args[]) {
    // Now, list holds references of type String.
    ArrayList<String> list = new ArrayList<String>();
    list.add("one");
    list.add("two");
    list.add("three");
    list.add("four");
    // Notice that Iterator is also generic.
    Iterator<String> itr = list.iterator();
    // The following statement will now cause a compile-time eror.
//    Iterator<Integer> itr = list.iterator(); // Error!
    while(itr.hasNext()) {
      String str = itr.next(); // no cast needed
      // Now, the following line is a compile-time,
      // rather than runtime, error.
//    Integer i = itr.next(); // this won't compile
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
11.  Pre generics example that uses a collection.
12.  Java generic: Generics and arrays.
13.  Collections and Data structure: the generic way
14.  The GenStack Class
