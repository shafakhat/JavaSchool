---
title: Java Collection Tutorial - Java Maps
nav: Java Collection Tutorial -...
description: A map represents a collection that contains key-value mappings.
section: Imported - java2s Archive
order: 50339
source: https://www.java2s.com/Tutorials/Java/Java_Collection/0180__Java_Map.html
---
```java title=Example.java
```

A map represents a collection that contains key-value mappings.

Map is a collection in which each element represents a key-value pair as <key, value>. A <key, value> pair is also known as an entry in the map. The key and the value must be reference types.

A map is represented by an instance of the Map<K,V> interface, which is not inherited from the Collection interface.

A Map does not allow any duplicate keys. Each key is mapped to exactly one value. Values do not have to be unique. Two keys may map to the same value.

A Map allows for at most one null value as its key and multiple null values as its values.

The methods in the Map interface may be classified in the following four categories depending on the operations they perform:

- basic operations
- bulk operations
- view operations
- comparison operations

## basic operations

The basic methods perform basic operations on a Map,

- putting an entry into a Map
- getting the value for a specified key
- getting the number of entries
- removing an entry
- checking if the Map is empty.

Examples of methods in this category are as follows:

```java title=Example.java
int size()
boolean isEmpty()
boolean containsKey (Object key)
boolean containsValue (Object value)
V  get(Object  key)
V  getOrDefault(Object key, V  defaultValue)
V  put(K  key, V  value)
V  putIfAbsent(K key, V  value)
V  remove  (Object key)
boolean remove(Object key, Object value)
boolean replace(K key, V  oldValue, V  newValue)
```

## bulk operations

The Map bulk operations perform bulk operations on a Map such as copying entries to another Map or removing all entries from the Map.

Examples of methods in this category are as follows:

```java title=Example.java
void  clear()
void  putAll (Map<? extends K,  ?  extends V>  t)
void  replaceAll(BiFunction<? super K,?  super V,?  extends V>  function)
```

## View operations

The view operations contains three methods. We can view the following sets from a Map.

- all keys in a Map as a Set,
- all values as a Collection,
- all <key, value> pairs as a Set.

Examples of methods in this category are as follows:

```java title=Example.java
Set<K> keySet()
Collection<V> values()
Set<Map.  Entry<K,  V>>entrySet()
```

All keys and all <key, value> pairs are always unique in a Map and returned as Set views.

Since a Map may contain duplicate values, it returns a Collection view for the values.

## Comparison operations

The comparison operations methods deal with comparing two Maps for equality. Examples of methods in this category are as follows:

```java title=Example.java
boolean equals (Object o)
int hashCode()
```

## Implementation

The HashMap, LinkedHashMap, and WeakHashMap are three implementation classes for the Map interface.

The HashMap allows one null value as a key and multiple null values as the values.

The following code demonstrates how to create and use a Map interface from its implementation class HashMap. A HashMap does not guarantee any specific iteration order of entries in the Map.

The following code creates a Map from a HashMap

```java title=Example.java
// Create a  map using HashMap
Map<String, String>  map = new HashMap<>();
map.put("CSS", "style");
```

The LinkedHashMap is another implementation class for the Map interface. It stores entries in the Map using a doubly linked list and keeps the iteration ordering as the insertion order.

The following code demonstrates how to use a Map.

```java title=Example.java
import java.util.HashMap;
import java.util.Map;
publicclass Main {
  publicstaticvoid main(String[] args) {
    Map<String, String> map = new HashMap<>();
    map.put("CSS", "style");
    map.put("HTML", "mark up");
    map.put("Oracle", "database");
    map.put("XML", "data");
    printDetails(map);
    map.clear();
    printDetails(map);
  }
  publicstaticvoid printDetails(Map<String, String> map) {
    String usage = map.get("CSS");
    System.out.println("Map: " + map);
    System.out.println("Map Size:  " + map.size());
    System.out.println("Map is empty:  " + map.isEmpty());
    System.out.println("Map contains CSS key:   " + map.containsKey("CSS"));
    System.out.println("Usage:  " + usage);
    System.out.println("removed:  " + map.remove("CSS"));
  }
}
```

The code above generates the following result.

The WeakHashMap class is another implementation for the Map interface.

WeakHashMap class contains weak keys. When there is no reference to the key except in the map, keys are candidates for garbage collection.

If a key is garbage collected, its associated entry is removed from the WeakHashMap.

The WeakHashMap allows a null key and multiple null values.

- « Previous
