---
title: Pool container
nav: Pool container
description: * Licensed under the Apache License, Version 2.0 (the "License");
section: Imported - java2s Archive
order: 1044
source: https://web.archive.org/web/20111010003103/http://java2s.com:80/Code/Java/Generics/Poolcontainer.htm
---
```java title=Example.java
/*
 * Copyright 2008-2010 the T2 Project ant the Others.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
//package org.t2framework.commons.util;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Set;
import java.util.concurrent.CopyOnWriteArrayList;
import java.util.concurrent.CopyOnWriteArraySet;
public class Pool<T> {
  private static int DEFAULT_POOL_MAX = 10;
  private List<T> stock;
  private Set<T> havings;
  public static <T> Pool<T> create(T... stocks) {
    return new Pool<T>(Arrays.asList(stocks));
  }
  public static <T extends Cloneable> Pool<T> create(T origin) {
    return create(origin, DEFAULT_POOL_MAX);
  }
  public static <T extends Cloneable> Pool<T> create(T origin, int poolMax) {
    if (origin == null) {
      throw new IllegalArgumentException("origin: " + origin);
    }
    if (poolMax < 1) {
      throw new IllegalArgumentException("poolMax: " + poolMax);
    }
    List<T> copies = new ArrayList<T>();
    for (int i = 0; i < poolMax; i++) {
      try {
        @SuppressWarnings("unchecked")
        T copied = (T) origin.getClass().getMethod("clone").invoke(
            origin);
        copies.add(copied);
      } catch (Exception e) {
        throw new IllegalStateException(e);
      }
    }
    return new Pool<T>(copies);
  }
  private Pool(List<T> stocks) {
    if (stocks == null || stocks.size() == 0) {
      throw new IllegalArgumentException("stocks: " + stocks);
    }
    this.stock = new CopyOnWriteArrayList<T>();
    this.havings = new CopyOnWriteArraySet<T>();
    for (T stockItem : stocks) {
      stock.add(stockItem);
      havings.add(stockItem);
    }
  }
  public T borrowItem() {
    try {
      while (true) {
        if (0 < stock.size()) {
          return stock.remove(0);
        }
        Thread.sleep(10);
      }
    } catch (InterruptedException e) {
      throw new IllegalStateException(e);
    }
  }
  public void returnItem(T item) {
    if (havings.contains(item) == false) {
      throw new IllegalStateException("item is not mine");
    }
    stock.add(item);
  }
}
```

1.  Creating a Type-Specific List
---  ---
2.  A list declared to hold objects of a type T can also hold objects that extend from T.
3.  A value retrieved from a type-specific list does not need to be casted
4.  Generic ArrayList
5.  Generic Data Structure
6.  Unchecked Example
7.  Generic Stack
8.  Enum and Generic
9.  Generic HashMap
10.  Foreach and generic data structure
11.  Pre generics example that uses a collection.
12.  Data structure and collections: Modern, generics version.
13.  Java generic: Generics and arrays.
14.  Collections and Data structure: the generic way
15.  The GenStack Class
16.  Create a typesafe copy of a raw set.
17.  Create a typesafe copy of a raw list.
18.  Create a typesafe copy of a raw map.
19.  Create a typesafe filter of an unchecked iterator.
20.  Create a typesafe view over an underlying raw set.
21.  Create a typesafe view over an underlying raw map.
22.  Create a typesafe filter of an unchecked enumeration.
23.  Circular Object Buffer
24.  A collection that do not hold stored elements in memory, but serialize it into a file
25.  Generic Triple structure
26.  Generic Pair
27.  A generic bag of properties used to store properties that apply to a specific target.
