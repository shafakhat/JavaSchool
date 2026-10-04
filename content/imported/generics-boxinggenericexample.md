---
title: Boxing Generic Example
nav: Boxing Generic Example
description: 1. A simple generic class with two type parameters: T and V.
section: Imported - java2s Archive
order: 1012
source: https://web.archive.org/web/20081201192136/http://www.java2s.com:80/Code/Java/Generics/BoxingGenericExample.htm
---
Boxing Generic Example

```java title=Example.java
import java.util.*;
public class BoxingGenericsExample {
    public static void main(String args[])
    {
        HashMap<String,Integer> hm = new HashMap<String,Integer>();
        hm.put("speed", 20);
    }
}
```

1.  A simple generic class with two type parameters: T and V.
---  ---
2.  Java generic: Hierarchy argument
3.  Demonstrate a raw generic type.
4.  T is a type parameter that will be replaced by a real type when an object of type Gen is created.
5.  Create a generic class that can compute the average of an array of numbers of any given type.
6.  the type argument for T must be either Number, or a class derived from Number.
7.  Demonstrate a raw type.
8.  A subclass can add its own type parameters.
