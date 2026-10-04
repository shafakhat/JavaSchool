---
title: Creating a Type-Specific List
nav: Creating a Type-Specific L...
description: 1. A list declared to hold objects of a type T can also hold objects that extend from T.
section: Imported - java2s Archive
order: 1017
source: https://web.archive.org/web/20090603182345/http://www.java2s.com:80/Code/Java/Generics/CreatingaTypeSpecificList.htm
---
```java title=Example.java
import java.util.ArrayList;
import java.util.List;
public class Main {
  public static void main(String[] argv) {
    List<Integer> intlist = new ArrayList<Integer>();
    intlist.add(new Integer(123));
  }
}
```

1.  A list declared to hold objects of a type T can also hold objects that extend from T.
---  ---
2.  A value retrieved from a type-specific list does not need to be casted
3.  Generic ArrayList
4.  Generic Data Structure
5.  Unchecked Example
6.  Generic Stack
7.  Enum and Generic
8.  Generic HashMap
9.  Foreach and generic data structure
10.  Pre generics example that uses a collection.
11.  Data structure and collections: Modern, generics version.
12.  Java generic: Generics and arrays.
13.  Collections and Data structure: the generic way
14.  The GenStack Class
