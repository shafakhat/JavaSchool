---
title: A Map where keys are compared by object identity, rather than equals()
nav: A Map where keys are compa...
description: A Map where keys are compared by object identity, rather than equals()
section: Imported - java2s Archive
order: 1057
source: https://web.archive.org/web/20100213172019/http://java2s.com/Code/Java/Collections-Data-Structure/AMapwherekeysarecomparedbyobjectidentityratherthanequals.htm
---
A Map where keys are compared by object identity, rather than equals()

```java title=Example.java
/*
 * Hibernate, Relational Persistence for Idiomatic Java
 *
 * Copyright (c) 2008, Red Hat Middleware LLC or third-party contributors as
 * indicated by the @author tags or express copyright attribution
 * statements applied by the authors.  All third-party contributions are
 * distributed under license by Red Hat Middleware LLC.
 *
 * This copyrighted material is made available to anyone wishing to use, modify,
 * copy, or redistribute it subject to the terms and conditions of the GNU
 * Lesser General Public License, as published by the Free Software Foundation.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
 * or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License
 * for more details.
 *
 * You should have received a copy of the GNU Lesser General Public License
 * along with this distribution; if not, write to:
 * Free Software Foundation, Inc.
 * 51 Franklin Street, Fifth Floor
 * Boston, MA  02110-1301  USA
 *
 */
import java.io.Serializable;
import java.util.ArrayList;
import java.util.Collection;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Iterator;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;
/**
 * A <tt>Map</tt> where keys are compared by object identity,
 * rather than <tt>equals()</tt>.
 */
public final class IdentityMap implements Map {
  private final Map map;
  private transient Map.Entry[] entryArray = new Map.Entry[0];
  private transient boolean dirty = false;
  /**
   * Return a new instance of this class, with an undefined
   * iteration order.
   *
   * @param size The size of the map
   * @return Map
   */
  public static Map instantiate(int size) {
    return new IdentityMap( new HashMap( size ) );
  }
  /**
   * Return a new instance of this class, with iteration
   * order defined as the order in which entries were added
   *
   * @param size The size of the map to create
   * @return
   */
  public static Map instantiateSequenced(int size) {
    return new IdentityMap( new LinkedHashMap( size ) );
  }
  /**
   * Private ctor used in serialization.
   *
   * @param underlyingMap The delegate map.
   */
  private IdentityMap(Map underlyingMap) {
    map = underlyingMap;
    dirty = true;
  }
  /**
   * Return the map entries (as instances of <tt>Map.Entry</tt> in a collection that
   * is safe from concurrent modification). ie. we may safely add new instances to
   * the underlying <tt>Map</tt> during iteration of the <tt>entries()</tt>.
   *
   * @param map
   * @return Collection
   */
  public static Map.Entry[] concurrentEntries(Map map) {
    return ( (IdentityMap) map ).entryArray();
  }
  public static List entries(Map map) {
    return ( (IdentityMap) map ).entryList();
  }
  public static Iterator keyIterator(Map map) {
    return ( (IdentityMap) map ).keyIterator();
  }
  public Iterator keyIterator() {
    return new KeyIterator( map.keySet().iterator() );
  }
  public static final class IdentityMapEntry implements java.util.Map.Entry {
    IdentityMapEntry(Object key, Object value) {
      this.key=key;
      this.value=value;
    }
    private Object key;
    private Object value;
    public Object getKey() {
      return key;
    }
    public Object getValue() {
      return value;
    }
    public Object setValue(Object value) {
      Object result = this.value;
      this.value = value;
      return result;
    }
  }
  public static final class IdentityKey implements Serializable {
    private Object key;
    IdentityKey(Object key) {
      this.key=key;
    }
    public boolean equals(Object other) {
      return key == ( (IdentityKey) other ).key;
    }
    public int hashCode() {
      return System.identityHashCode(key);
    }
    public String toString() {
      return key.toString();
    }
    public Object getRealKey() {
      return key;
    }
  }
  public int size() {
    return map.size();
  }
  public boolean isEmpty() {
    return map.isEmpty();
  }
  public boolean containsKey(Object key) {
    IdentityKey k = new IdentityKey(key);
    return map.containsKey(k);
  }
  public boolean containsValue(Object val) {
    return map.containsValue(val);
  }
  public Object get(Object key) {
    IdentityKey k = new IdentityKey(key);
    return map.get(k);
  }
  public Object put(Object key, Object value) {
    dirty = true;
    return map.put( new IdentityKey(key), value );
  }
  public Object remove(Object key) {
    dirty = true;
    IdentityKey k = new IdentityKey(key);
    return map.remove(k);
  }
  public void putAll(Map otherMap) {
    Iterator iter = otherMap.entrySet().iterator();
    while ( iter.hasNext() ) {
      Map.Entry me = (Map.Entry) iter.next();
      put( me.getKey(), me.getValue() );
    }
  }
  public void clear() {
    dirty = true;
    entryArray = null;
    map.clear();
  }
  public Set keySet() {
    // would need an IdentitySet for this!
    throw new UnsupportedOperationException();
  }
  public Collection values() {
    return map.values();
  }
  public Set entrySet() {
    Set set = new HashSet( map.size() );
    Iterator iter = map.entrySet().iterator();
    while ( iter.hasNext() ) {
      Map.Entry me = (Map.Entry) iter.next();
      set.add( new IdentityMapEntry( ( (IdentityKey) me.getKey() ).key, me.getValue() ) );
    }
    return set;
  }
  public List entryList() {
    ArrayList list = new ArrayList( map.size() );
    Iterator iter = map.entrySet().iterator();
    while ( iter.hasNext() ) {
      Map.Entry me = (Map.Entry) iter.next();
      list.add( new IdentityMapEntry( ( (IdentityKey) me.getKey() ).key, me.getValue() ) );
    }
    return list;
  }
  public Map.Entry[] entryArray() {
    if (dirty) {
      entryArray = new Map.Entry[ map.size() ];
      Iterator iter = map.entrySet().iterator();
      int i=0;
      while ( iter.hasNext() ) {
        Map.Entry me = (Map.Entry) iter.next();
        entryArray[i++] = new IdentityMapEntry( ( (IdentityKey) me.getKey() ).key, me.getValue() );
      }
      dirty = false;
    }
    return entryArray;
  }
  /**
   * Workaround for a JDK 1.4.1 bug where <tt>IdentityHashMap</tt>s are not
   * correctly deserialized.
   *
   * @param map
   * @return Object
   */
  public static Object serialize(Map map) {
    return ( (IdentityMap) map ).map;
  }
  /**
   * Workaround for a JDK 1.4.1 bug where <tt>IdentityHashMap</tt>s are not
   * correctly deserialized.
   *
   * @param o
   * @return Map
   */
  public static Map deserialize(Object o) {
    return new IdentityMap( (Map) o );
  }
  public String toString() {
    return map.toString();
  }
  public static Map invert(Map map) {
    Map result = instantiate( map.size() );
    Iterator iter = map.entrySet().iterator();
    while ( iter.hasNext() ) {
      Map.Entry me = (Map.Entry) iter.next();
      result.put( me.getValue(), me.getKey() );
    }
    return result;
  }
  static final class KeyIterator implements Iterator {
    private KeyIterator(Iterator iter) {
      identityKeyIterator = iter;
    }
    private final Iterator identityKeyIterator;
    public boolean hasNext() {
      return identityKeyIterator.hasNext();
    }
    public Object next() {
      return ( (IdentityKey) identityKeyIterator.next() ).key;
    }
    public void remove() {
      throw new UnsupportedOperationException();
    }
  }
}
```

1.  Ordered Map
---  ---
2.  Case Insensitive Map
3.  A Map collection with real-time behavior
4.  Cache Map
5.  Map implementation Optimized for Strings keys
6.  An integer hashmap
7.  An IdentityMap that uses reference-equality instead of object-equality
8.  Int Object HashMap
9.  Concurrent Skip List Map
10.  A hash map that uses primitive ints for the key rather than objects.
11.  Integer Map
12.  Copy On Write Map
13.  Expiring Map
14.  Array Map
15.  Int Object HashMap (from CERN)
16.  Int HashMap from jodd.org
17.  String Map
18.  List Map
19.  Map using Locale objects as keys
20.  Map with keys iterated in insertion order
21.  Most Recently Used Map
22.  Multi Map
23.  MultiMap is a Java version of the C++ STL class std::multimap
24.  Object Int Map
25.  Sequenced HashMap
26.  Int Int Map
27.  Int Object Map
28.  Identity HashMap
29.  A java.util.Map interface which can only hold a single object
30.  A multi valued Map
31.  A simple hashmap from keys to integers
32.  A memory-efficient hash map.
33.  An implementation of the java.util.Map interface which can only hold a single object.
34.  Utility methods for operating on memory-efficient maps.
35.  CaseBlindHashMap - a HashMap extension, using Strings as key values.
36.  A fixed size map implementation.
37.  Int HashMap
38.  IntMap provides a simple hashmap from keys to integers
39.  Complex Key HashMap
40.  A Map with multiple values for a key
41.  A Map that accepts int or Integer keys only
42.  Type-safe Map, from char array to String value
43.  A hashtable-based Map implementation with soft keys
44.  List ordered map
45.  Hash map using String values as keys mapped to primitive int values.
46.  Lookup table that stores a list of strings
47.  HashNMap stores multiple values by a single key value. Values can be retrieved using a direct query or by creating an enumeration over the stored elements.
48.  Combines multiple values to form a single composite key. MultiKey can often be used as an alternative to nested maps.
