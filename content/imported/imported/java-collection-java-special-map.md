---
title: Java Collection Tutorial - Java Special Maps
nav: Java Collection Tutorial -...
description: It sorts the map entries on keys based on the Comparable interface from the keys or a Comparator object.
section: Imported - java2s Archive
order: 50341
source: https://www.java2s.com/Tutorials/Java/Java_Collection/0200__Java_Special_Map.html
---
```java title=Example.java
```

## Sorted Maps

A sorted map keeps the map entries in order.

It sorts the map entries on keys based on the Comparable interface from the keys or a Comparator object.

If the keys implement the Comparable interface and you use a Comparator object, the Comparator object will do the sorting.

SortedMap interface inherits from the Map interface represented a sorted map.

Comparator comparator() returns the Comparator object used for custom sorting in the SortedMap.

K firstKey() returns the key of the first entry in the SortedMap. If the SortedMap is empty, it throws a NoSuchElementException.

SortedMap headMap(K toKey) returns a view of the SortedMap whose entries will have keys less than the specified toKey. The view is backed by the original SortedMap.

K lastKey() returns the key of the last entry in the SortedMap. If the SortedMap is empty, it throws a NoSuchElementException.

SortedMap subMap(K fromKey,K toKey) returns a view of the SortedMap whose entries will have keys ranging from the specified fromKey (inclusive) and toKey (exclusive).

SortedMap tailMap(K fromKey) returns a view of the SortedMap whose entries will have keys equal to or greater than the specified fromKey.

The TreeMap class is the implementation class for the SortedMap interface. The following code demonstrates how to use a SortedMap.

```java title=Example.java
import java.util.SortedMap;
import java.util.TreeMap;
//www.java2s.compublicclass Main {
  publicstaticvoid main(String[] args) {
    SortedMap<String, String> sMap = new TreeMap<>();
    sMap.put("CSS", "style");
    sMap.put("HTML", "mark up");
    sMap.put("Oracle", "database");
    sMap.put("XML", "data");
    SortedMap<String, String> subMap = sMap.subMap("CSS", "XML");
    System.out.println(subMap);
    // Get the first and last keys
    String firstKey = sMap.firstKey();
    String lastKey = sMap.lastKey();
    System.out.println("First Key:  " + firstKey);
    System.out.println("Last key:   " + lastKey);
  }
}
```

The code above generates the following result.

## SortedMap with Comparator

To use a Comparator object to sort the entries in a SortedMap, use the constructor of the TreeMap class that takes a Comparator as an argument.

The following code shows how to sort entries in a sorted map based on the length of their keys followed by the alphabetical order of the keys ignoring the case:

```java title=Example.java
import java.util.Comparator;
import java.util.SortedMap;
import java.util.TreeMap;
/*fromwww.java2s.com*/publicclass Main {
  publicstaticvoid main(String[] args) {
    Comparator<String> keyComparator  =
        Comparator.comparing(String::length).thenComparing(String::compareToIgnoreCase);
    SortedMap<String, String> sMap = new TreeMap<>(keyComparator);
    sMap.put("CSS", "style");
    sMap.put("HTML", "mark up");
    sMap.put("Oracle", "database");
    sMap.put("XML", "data");
    SortedMap<String, String> subMap = sMap.subMap("CSS", "XML");
    System.out.println(subMap);
    // Get the first and last keys
    String firstKey = sMap.firstKey();
    String lastKey = sMap.lastKey();
    System.out.println("First Key:  " + firstKey);
    System.out.println("Last key:   " + lastKey);
  }
}
```

The code above generates the following result.

A navigable map is represented by an instance of the NavigableMap interface.

It extends the SortedMap interface by adding methods to get the closest match for a key, get a view of the map in reverse order, etc.

The TreeMap class is the implementation class for the NavigableMap interface.

The following code shows how to use a NavigableMap.

```java title=Example.java
import java.util.Map.Entry;
import java.util.NavigableMap;
import java.util.TreeMap;
//fromwww.java2s.compublicclass Main {
  publicstaticvoid main(String[] args) {
    NavigableMap<String, String> nMap = new TreeMap<>();
    nMap.put("CSS", "style");
    nMap.put("HTML", "mark up");
    nMap.put("Oracle", "database");
    nMap.put("XML", "data");
    System.out.println("Navigable Map:" + nMap);
    Entry<String, String> lowerXML = nMap.lowerEntry("XML");
    Entry<String, String> floorXML = nMap.floorEntry("XML");
    Entry<String, String> higherXML = nMap.higherEntry("XML");
    Entry<String, String> ceilingXML = nMap.ceilingEntry("XML");
    System.out.println("Lower:" + lowerXML);
    System.out.println("Floor:" + floorXML);
    System.out.println("Higher:" + higherXML);
    System.out.println("Ceiling:" + ceilingXML);
    // Get the reverse order view of the map
    NavigableMap<String, String> reverseMap = nMap.descendingMap();
    System.out.println("Navigable Map(Reverse  Order):" + reverseMap);
  }
}
```

The code above generates the following result.

## Concurrent Maps

A ConcurrentMap allows us to perform concurrent operations without locking the map.

We can choose the level of concurrency when we create a concurrent map using its implementation class.

The ConcurrentHashMap class is an implementation class for the ConcurrentMap interface. Both of them are in the java.util.concurrent package.

```java title=Example.java
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.ConcurrentMap;
/*fromwww.java2s.com*/publicclass Main {
  publicstaticvoid main(String[] args) {
    ConcurrentMap<String, String> cMap = new ConcurrentHashMap<>();
    cMap.put("A", "A");
    System.out.println("Concurrent Map: " + cMap);
    System.out.println(cMap.putIfAbsent("A", "1"));
    System.out.println(cMap.putIfAbsent("B", "B"));
    System.out.println(cMap.remove("A", "B"));
    System.out.println(cMap.replace("A", "B"));
    System.out.println("Concurrent Map: " + cMap);
  }
}
```

The code above generates the following result.

- « Previous
