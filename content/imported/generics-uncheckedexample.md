---
title: Unchecked Example
nav: Unchecked Example
description: 2. A list declared to hold objects of a type T can also hold objects that extend from T.
section: Imported - java2s Archive
order: 1053
source: https://web.archive.org/web/20090603133845/http://www.java2s.com:80/Code/Java/Generics/UncheckedExample.htm
---
Unchecked Example

```java title=Example.java
import java.util.*;
public class UncheckedExample {
    public void processIntVector(Vector<Integer> v)
    {
        // perform some processing on the vector
    }
    public static void main(String args[])
    {
        Vector<Integer> intVector = new Vector<Integer>();
        Vector oldVector = new Vector();
        UncheckedExample ue = new UncheckedExample();
        // This is permitted
        oldVector = intVector;
        // This causes an unchecked warning
        intVector = oldVector;
        // This is permitted
        ue.processIntVector(intVector);
        // This causes an unchecked warning
        ue.processIntVector(oldVector);
    }
}
```

1.  Creating a Type-Specific List
---  ---
2.  A list declared to hold objects of a type T can also hold objects that extend from T.
3.  A value retrieved from a type-specific list does not need to be casted
4.  Generic ArrayList
5.  Generic Data Structure
6.  Generic Stack
7.  Enum and Generic
8.  Generic HashMap
9.  Foreach and generic data structure
10.  Pre generics example that uses a collection.
11.  Data structure and collections: Modern, generics version.
12.  Java generic: Generics and arrays.
13.  Collections and Data structure: the generic way
14.  The GenStack Class
