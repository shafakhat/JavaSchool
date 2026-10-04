---
title: A java.util.Map interface which can only hold a single object
nav: A java.util.Map interface ...
description: A java.util.Map interface which can only hold a single object
section: Imported - java2s Archive
order: 1043
source: https://web.archive.org/web/20100213172746/http://java2s.com/Code/Java/Collections-Data-Structure/AjavautilMapinterfacewhichcanonlyholdasingleobject.htm
---
A java.util.Map interface which can only hold a single object

```java title=Example.java
/*
 * $Id: MicroMap.java 458489 2006-01-04 09:28:14Z ivaynberg $ $Revision:
 * 1.4 $ $Date: 2006-01-04 10:28:14 +0100 (Wed, 04 Jan 2006) $
 *
 *
 * Licensed under the Apache License, Version 2.0 (the "License"); you may not
 * use this file except in compliance with the License. You may obtain a copy of
 * the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
 * WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
 * License for the specific language governing permissions and limitations under
 * the License.
 */
import java.io.Serializable;
import java.util.AbstractList;
import java.util.AbstractSet;
import java.util.Collection;
import java.util.Iterator;
import java.util.Map;
import java.util.Set;
/**
 * An implementation of the java.util.Map interface which can only hold a single
 * object. This is particularly useful to control memory usage in Wicket because
 * many containers hold only a single component.
 *
 * @author Jonathan Locke
 */
public final class MicroMap implements Map, Serializable
{
  private static final long serialVersionUID = 1L;
  /** The maximum number of entries this map supports. */
  public static final int MAX_ENTRIES = 1;
  /** The one and only key in this tiny map */
  private Object key;
  /** The value for the only key in this tiny map */
  private Object value;
  /**
   * Constructor
   */
  public MicroMap()
  {
  }
  /**
   * Constructs map with a single key and value pair.
   *
   * @param key
   *            The key
   * @param value
   *            The value
   */
  public MicroMap(final Object key, final Object value)
  {
    put(key, value);
  }
  /**
   * @return True if this MicroMap is full
   */
  public boolean isFull()
  {
    return size() == MAX_ENTRIES;
  }
  /**
   * @see java.util.Map#size()
   */
  public int size()
  {
    return (key != null) ? 1 : 0;
  }
  /**
   * @see java.util.Map#isEmpty()
   */
  public boolean isEmpty()
  {
    return size() == 0;
  }
  /**
   * @see java.util.Map#containsKey(java.lang.Object)
   */
  public boolean containsKey(final Object key)
  {
    return key.equals(this.key);
  }
  /**
   * @see java.util.Map#containsValue(java.lang.Object)
   */
  public boolean containsValue(final Object value)
  {
    return value.equals(this.value);
  }
  /**
   * @see java.util.Map#get(java.lang.Object)
   */
  public Object get(final Object key)
  {
    if (key.equals(this.key))
    {
      return value;
    }
    return null;
  }
  /**
   * @see java.util.Map#put(java.lang.Object, java.lang.Object)
   */
  public Object put(final Object key, final Object value)
  {
    // Replace?
    if (key.equals(this.key))
    {
      final Object oldValue = this.value;
      this.value = value;
      return oldValue;
    }
    else
    {
      // Is there room for a new entry?
      if (size() < MAX_ENTRIES)
      {
        // Store
        this.key = key;
        this.value = value;
        return null;
      }
      else
      {
        throw new IllegalStateException("Map full");
      }
    }
  }
  /**
   * @see java.util.Map#remove(java.lang.Object)
   */
  public Object remove(final Object key)
  {
    if (key.equals(this.key))
    {
      final Object oldValue = this.value;
      this.key = null;
      this.value = null;
      return oldValue;
    }
    return null;
  }
  /**
   * @see java.util.Map#putAll(java.util.Map)
   */
  public void putAll(final Map map)
  {
    if (map.size() <= MAX_ENTRIES)
    {
      final Map.Entry e = (Map.Entry)map.entrySet().iterator().next();
      put(e.getKey(), e.getValue());
    }
    else
    {
      throw new IllegalStateException("Map full.  Cannot add " + map.size() + " entries");
    }
  }
  /**
   * @see java.util.Map#clear()
   */
  public void clear()
  {
    key = null;
    value = null;
  }
  /**
   * @see java.util.Map#keySet()
   */
  public Set keySet()
  {
    return new AbstractSet()
    {
      public Iterator iterator()
      {
        return new Iterator()
        {
          public boolean hasNext()
          {
            return index < MicroMap.this.size();
          }
          public Object next()
          {
            index++;
            return key;
          }
          public void remove()
          {
            MicroMap.this.clear();
          }
          int index;
        };
      }
      public int size()
      {
        return MicroMap.this.size();
      }
    };
  }
  /**
   * @see java.util.Map#values()
   */
  public Collection values()
  {
    return new AbstractList()
    {
      public Object get(final int index)
      {
        return value;
      }
      public int size()
      {
        return MicroMap.this.size();
      }
    };
  }
  /**
   * @see java.util.Map#entrySet()
   */
  public Set entrySet()
  {
    return new AbstractSet()
    {
      public Iterator iterator()
      {
        return new Iterator()
        {
          public boolean hasNext()
          {
            return index < MicroMap.this.size();
          }
          public Object next()
          {
            index++;
            return new Map.Entry()
            {
              public Object getKey()
              {
                return key;
              }
              public Object getValue()
              {
                return value;
              }
              public Object setValue(final Object value)
              {
                final Object oldValue = MicroMap.this.value;
                MicroMap.this.value = value;
                return oldValue;
              }
            };
          }
          public void remove()
          {
            clear();
          }
          int index = 0;
        };
      }
      public int size()
      {
        return MicroMap.this.size();
      }
    };
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
29.  A multi valued Map
30.  A simple hashmap from keys to integers
31.  A memory-efficient hash map.
32.  An implementation of the java.util.Map interface which can only hold a single object.
33.  Utility methods for operating on memory-efficient maps.
34.  CaseBlindHashMap - a HashMap extension, using Strings as key values.
35.  A fixed size map implementation.
36.  Int HashMap
37.  IntMap provides a simple hashmap from keys to integers
38.  Complex Key HashMap
39.  A Map with multiple values for a key
40.  A Map that accepts int or Integer keys only
41.  A Map where keys are compared by object identity, rather than equals()
42.  Type-safe Map, from char array to String value
43.  A hashtable-based Map implementation with soft keys
44.  List ordered map
45.  Hash map using String values as keys mapped to primitive int values.
46.  Lookup table that stores a list of strings
47.  HashNMap stores multiple values by a single key value. Values can be retrieved using a direct query or by creating an enumeration over the stored elements.
48.  Combines multiple values to form a single composite key. MultiKey can often be used as an alternative to nested maps.
