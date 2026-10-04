---
title: Simple object pool
nav: Simple object pool
description: * Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 2393
source: https://web.archive.org/web/20140216225544/http://www.java2s.com/Tutorial/Java/0140__Collections/Simpleobjectpool.htm
---
```java title=Example.java
/*
 *  Licensed to the Apache Software Foundation (ASF) under one or more
 *  contributor license agreements.  See the NOTICE file distributed with
 *  this work for additional information regarding copyright ownership.
 *  The ASF licenses this file to You under the Apache License, Version 2.0
 *  (the "License"); you may not use this file except in compliance with
 *  the License.  You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 *  Unless required by applicable law or agreed to in writing, software
 *  distributed under the License is distributed on an "AS IS" BASIS,
 *  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 *  See the License for the specific language governing permissions and
 *  limitations under the License.
 */
/**
 * Simple object pool. Based on ThreadPool and few other classes
 *
 * The pool will ignore overflow and return null if empty.
 *
 * @author Gal Shachor
 * @author Costin Manolache
 */
public final class SimplePool {
  /*
   * Where the threads are held.
   */
  private Object pool[];
  private int max;
  private int last;
  private int current = -1;
  private Object lock;
  public static final int DEFAULT_SIZE = 32;
  static final int debug = 0;
  public SimplePool() {
    this(DEFAULT_SIZE, DEFAULT_SIZE);
  }
  public SimplePool(int size) {
    this(size, size);
  }
  public SimplePool(int size, int max) {
    this.max = max;
    pool = new Object[size];
    this.last = size - 1;
    lock = new Object();
  }
  public void set(Object o) {
    put(o);
  }
  /**
   * Add the object to the pool, silent nothing if the pool is full
   */
  public void put(Object o) {
    synchronized (lock) {
      if (current < last) {
        current++;
        pool[current] = o;
      } else if (current < max) {
        // realocate
        int newSize = pool.length * 2;
        if (newSize > max)
          newSize = max + 1;
        Object tmp[] = new Object[newSize];
        last = newSize - 1;
        System.arraycopy(pool, 0, tmp, 0, pool.length);
        pool = tmp;
        current++;
        pool[current] = o;
      }
    }
  }
  /**
   * Get an object from the pool, null if the pool is empty.
   */
  public Object get() {
    Object item = null;
    synchronized (lock) {
      if (current >= 0) {
        item = pool[current];
        pool[current] = null;
        current -= 1;
      }
    }
    return item;
  }
  /**
   * Return the size of the pool
   */
  public int getMax() {
    return max;
  }
  /**
   * Number of object in the pool
   */
  public int getCount() {
    return current + 1;
  }
  public void shutdown() {
  }
}
```

| 9.10.1. | A variable length Double Array: expanding and contracting its internal storage array as elements are added and removed. |
|---|---|
| 9.10.2. | Simple object pool. Based on ThreadPool and few other classes |
| 9.10.3. | Your own auto-growth Array |
| 9.10.4. | The character array based string |
| 9.10.5. | ByteArray wraps java byte arrays (byte[]) to allow byte arrays to be used as keys in hashtables. |
| 9.10.6. | Adds all the elements of the given arrays into a new double-type array. |
| 9.10.7. | A writer for char strings |
| 9.10.8. | Array-List for integer objects. |
| 9.10.9. | Simple object pool |
| 9.10.10. | Concatenates two arrays of strings |
| 9.10.11. | Puts the entire source array in the target array at offset offset. |
| 9.10.12. | Lazy List creation |
| 9.10.13. | Stores a list of int |
