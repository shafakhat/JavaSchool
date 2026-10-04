---
title: A map declared to hold objects of a type T can also hold objects that extend from T
nav: A map declared to hold obj...
description: A map declared to hold objects of a type T can also hold objects that extend from T
section: Imported - java2s Archive
order: 1050
source: https://web.archive.org/web/20090602102412/http://www.java2s.com:80/Code/Java/Collections-Data-Structure/AmapdeclaredtoholdobjectsofatypeTcanalsoholdobjectsthatextendfromT.htm
---
A map declared to hold objects of a type T can also hold objects that extend from T

```java title=Example.java
import java.util.HashMap;
import java.util.Map;
public class Main {
  public static void main(String[] argv) {
    Map<Number, String> numMap = new HashMap<Number, String>();
    numMap.put(.5, "half");
    numMap.put(1, "first");
  }
}
```

1.  Creating and storing arrays in a map
---  ---
2.  Sort based on the values
3.  Get a key from value with an HashMap
4.  Retrieve environment variables (JDK1.5)
5.  Creating a Type-Specific Map: creates a map whose keys are Integer objects and values are String objects.
6.  A value retrieved from a type-specific collection does not need to be casted
7.  Map techniques.
8.  Create an array containing the keys in a map
9.  Create an array containing the values in a map
10.  Creating a Hash Table
11.  Creating a Map That Retains Order-of-Insertion
12.  Automatically Removing an Unreferenced Element from a Hash Table
13.  Creating a Type-Specific Map [5.0]
14.  Use Iterator to loop through the HashMap class
15.  Create type specific collections
16.  Convert Properties into Map
