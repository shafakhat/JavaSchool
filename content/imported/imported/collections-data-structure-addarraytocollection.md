---
title: Add array to collection
nav: Add array to collection
description: public static <T> void addArrayToCollection(T[] array, Collection<T> collection)
section: Imported - java2s Archive
order: 1015
source: https://web.archive.org/web/20111115133938/http://www.java2s.com:80/Code/Java/Collections-Data-Structure/Addarraytocollection.htm
---
```java title=Example.java
import java.util.Arrays;
import java.util.Collection;
public class Util{
  public static <T> void addArrayToCollection(T[] array, Collection<T> collection)
  {
    collection.addAll(Arrays.asList(array));
  }
}
```

1.  Array Iterator
---  ---
2.  Array Map
3.  Array Set
4.  Array Int Set
5.  Remove duplicate element from array
6.  Convert an Array to a List
7.  Converting an Array to a Collection
8.  Converting a Collection of user objects to an Array
9.  Create an array containing the elements in a set
10.  Convert an array to a Map
11.  Converting a Collection of String to an Array
12.  Treating an Array as an Enumeration
13.  ArrayEnumeration class (implements Enumeration)
14.  Custom ArrayMap implementation (extends AbstractMap)
15.  Custom ArraySet implementation (extends AbstractSet)
16.  Converts array into a java.util.Map.
17.  Growable array of ints
18.  Growable array of floats.
19.  Acts like an java.util.ArrayList but for primitive int values
20.  Acts like an java.util.ArrayList but for primitive long values
