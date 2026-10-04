---
title: Simple object pool. Based on ThreadPool and few other classes
nav: Simple object pool. Based ...
description: * or more contributor license agreements. See the NOTICE file
section: Imported - java2s Archive
order: 2387
source: https://web.archive.org/web/20140829080019/http://www.java2s.com/Tutorial/Java/0140__Collections/SimpleobjectpoolBasedonThreadPoolandfewotherclasses.htm
---
```java title=Example.java
/*
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied.  See the License for the
 * specific language governing permissions and limitations
 * under the License.
 */
/**
 *
 * The pool will ignore overflow and return null if empty.
 *
 * @author Gal Shachor
 * @author Costin
 * @author <a href="mailto:geirm@optonline.net">Geir Magnusson Jr.</a>
 * @version $Id: SimplePool.java 463298 2006-10-12 16:10:32Z henning $
 */
public final class SimplePool {
  /*
   * Where the objects are held.
   */
  private Object pool[];
  /**
   * max amount of objects to be managed set via CTOR
   */
  private int max;
  /**
   * index of previous to next free slot
   */
  private int current = -1;
  /**
   * @param max
   */
  public SimplePool(int max) {
    this.max = max;
    pool = new Object[max];
  }
  /**
   * Add the object to the pool, silent nothing if the pool is full
   *
   * @param o
   */
  public void put(Object o) {
    int idx = -1;
    synchronized (this) {
      /*
       * if we aren't full
       */
      if (current < max - 1) {
        /*
         * then increment the current index.
         */
        idx = ++current;
      }
      if (idx >= 0) {
        pool[idx] = o;
      }
    }
  }
  /**
   * Get an object from the pool, null if the pool is empty.
   *
   * @return The object from the pool.
   */
  public Object get() {
    synchronized (this) {
      /*
       * if we have any in the pool
       */
      if (current >= 0) {
        /*
         * remove the current one
         */
        Object o = pool[current];
        pool[current] = null;
        current--;
        return o;
      }
    }
    return null;
  }
  /**
   * Return the size of the pool
   *
   * @return The pool size.
   */
  public int getMax() {
    return max;
  }
  /**
   * for testing purposes, so we can examine the pool
   *
   * @return Array of Objects in the pool.
   */
  Object[] getPool() {
    return pool;
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
