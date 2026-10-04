---
title: A Map implementation that dumps its content when memory runs low.
nav: A Map implementation that ...
description: A Map implementation that dumps its content when memory runs low.
section: Imported - java2s Archive
order: 1051
source: https://web.archive.org/web/20111114172141/http://www.java2s.com:80/Code/Java/Collections-Data-Structure/AMapimplementationthatdumpsitscontentwhenmemoryrunslow.htm
---
```java title=Example.java
//     package com.croftsoft.core.util;
import java.lang.ref.Reference;
import java.lang.ref.ReferenceQueue;
import java.lang.ref.SoftReference;
import java.util.AbstractMap;
import java.util.HashSet;
import java.util.Set;
import java.util.WeakHashMap;
/*********************************************************************
 *
 * <P>
 *
 * Backed by a WeakHashMap. Note that an entry will not be garbage collected if
 * its key remains strongly reachable.
 *
 * <P>
 *
 * @see java.util.WeakHashMap
 * @see java.lang.ref.SoftReference
 *
 * @version 1999-04-20
 * @author <a href="http://www.CroftSoft.com/">David Wallace Croft</a>
 *********************************************************************/
public class SoftHashMap extends AbstractMap
// ////////////////////////////////////////////////////////////////////
// ////////////////////////////////////////////////////////////////////
{
  private WeakHashMap weakHashMap = new WeakHashMap();
  private ReferenceQueue referenceQueue = new ReferenceQueue();
  private Set softSet = new HashSet();
  // ////////////////////////////////////////////////////////////////////
  // ////////////////////////////////////////////////////////////////////
  public static void main(String[] args)
  // ////////////////////////////////////////////////////////////////////
  {
    System.out.println(test());
  }
  public static boolean test()
  // ////////////////////////////////////////////////////////////////////
  {
    try {
      SoftHashMap softHashMap = new SoftHashMap();
      softHashMap.put("key", "value");
      if (!softHashMap.remove("key").equals("value")
          || (softHashMap.size() > 0)) {
        return false;
      }
      Runtime runtime = Runtime.getRuntime();
      for (int i = 0; i < 1000000; i++) {
        if (i % 10000 == 0) {
          System.out.println(i + ":  " + softHashMap.size()
              + " entries, " + runtime.freeMemory() + " / "
              + runtime.totalMemory() + " memory usage");
        }
        Integer value = new Integer(i);
        softHashMap.put(value.toString(), value);
      }
    } catch (Throwable t) {
      t.printStackTrace();
      return false;
    }
    return true;
  }
  // ////////////////////////////////////////////////////////////////////
  // ////////////////////////////////////////////////////////////////////
  public Set entrySet()
  // ////////////////////////////////////////////////////////////////////
  {
    clearQueue();
    return weakHashMap.entrySet();
  }
  public Object put(Object key, Object value)
  // ////////////////////////////////////////////////////////////////////
  {
    clearQueue();
    softSet.add(new SoftReference(key, referenceQueue));
    return weakHashMap.put(key, value);
  }
  // ////////////////////////////////////////////////////////////////////
  // ////////////////////////////////////////////////////////////////////
  public void clearQueue()
  // ////////////////////////////////////////////////////////////////////
  {
    Reference reference = null;
    while ((reference = referenceQueue.poll()) != null) {
      softSet.remove(reference);
    }
  }
  // ////////////////////////////////////////////////////////////////////
  // ////////////////////////////////////////////////////////////////////
}
```

1.  Creating and storing arrays in a map
---  ---
2.  Sort based on the values
3.  Get a key from value with an HashMap
4.  Retrieve environment variables (JDK1.5)
5.  Creating a Type-Specific Map: creates a map whose keys are Integer objects and values are String objects.
6.  A map declared to hold objects of a type T can also hold objects that extend from T
7.  A value retrieved from a type-specific collection does not need to be casted
8.  Map techniques.
9.  Create an array containing the keys in a map
10.  Create an array containing the values in a map
11.  Creating a Hash Table
12.  Creating a Map That Retains Order-of-Insertion
13.  Automatically Removing an Unreferenced Element from a Hash Table
14.  Creating a Type-Specific Map [5.0]
15.  Use Iterator to loop through the HashMap class
16.  Create type specific collections
17.  Convert Properties into Map
18.  A java.util.Map implementation using reference values
19.  Utility method that return a String representation of a map. The elements will be represented as "key = value"
20.  Utility method that return a String representation of a map. The elements will be represented as "key = value" (tab)
21.  This program demonstrates the use of a map with key type String and value type Employee
22.  Format a Map
23.  A Map that stores the values in files within a directory.
24.  Map List
25.  Multi Value Map Array List
26.  Multi Value Map Linked HashSet
27.  An object that maps keys to values, and values back to keys.
28.  LRU Map
29.  A map acts like array.
30.  Order Retaining Map
31.  BinaryMap class implements a map from objects to integer objects where the only value is the integer with value 1.
32.  A space-optimized map for associating char keys with values.
33.  A Map implementation that grows to a fixed size and then retains only a fixed number of the highest (largest) keys.
34.  Class which creates mapping between keys and a list of values.
35.  A map of values by class.
36.  History Map
37.  Sorts map by values in ascending order.
38.  Map from a given key to a list of values
39.  Map from a given key to a set of values
40.  Class which keeps a set of values and assigns each value a unique positive index.
41.  Array Map
42.  Array map
43.  An ArrayMap is a very inefficient map type that is more robust in dealing with changes to its keys than other maps.
44.  This Map stores it's keys as strings in upper case, null and duplicate keys are not allowed
45.  Map to string
46.  A simple class that stores key Strings as char[]'s in a hash table.
