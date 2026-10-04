---
title: Adds all the elements of the given arrays into a new array.
nav: Adds all the elements of t...
description: Adds all the elements of the given arrays into a new array. : Auto Growth Array « Collections Data Structure « Java
section: Imported - java2s Archive
order: 1021
source: https://web.archive.org/web/20091117172534/http://www.java2s.com:80/Code/Java/Collections-Data-Structure/Addsalltheelementsofthegivenarraysintoanewarray.htm
---
Adds all the elements of the given arrays into a new array. : Auto Growth Array « Collections Data Structure « Java

```java title=Example.java
/*   Copyright 2004 The Apache Software Foundation
 *
 *   Licensed under the Apache License, Version 2.0 (the "License");
 *   you may not use this file except in compliance with the License.
 *   You may obtain a copy of the License at
 *
 *       http://www.apache.org/licenses/LICENSE-2.0
 *
 *   Unless required by applicable law or agreed to in writing, software
 *   distributed under the License is distributed on an "AS IS" BASIS,
 *   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 *   See the License for the specific language governing permissions and
 *  limitations under the License.
 */
import java.lang.reflect.Array;
/**
 * <p>Operations on arrays, primitive arrays (like <code>int[]</code>) and
 * primitive wrapper arrays (like <code>Integer[]</code>).</p>
 *
 * <p>This class tries to handle <code>null</code> input gracefully.
 * An exception will not be thrown for a <code>null</code>
 * array input. However, an Object array that contains a <code>null</code>
 * element may throw an exception. Each method documents its behaviour.</p>
 *
 * @author Stephen Colebourne
 * @author Moritz Petersen
 * @author <a href="mailto:fredrik@westermarck.com">Fredrik Westermarck</a>
 * @author Nikolay Metchev
 * @author Matthew Hawthorne
 * @author Tim O'Brien
 * @author Pete Gieser
 * @author Gary Gregory
 * @author <a href="mailto:equinus100@hotmail.com">Ashwin S</a>
 * @author Maarten Coene
 * @since 2.0
 * @version $Id: ArrayUtils.java 632503 2008-03-01 00:21:52Z ggregory $
 */
public class Main {
  /**
   * <p>Adds all the elements of the given arrays into a new array.</p>
   * <p>The new array contains all of the element of <code>array1</code> followed
   * by all of the elements <code>array2</code>. When an array is returned, it is always
   * a new array.</p>
   *
   * <pre>
   * ArrayUtils.addAll(null, null)     = null
   * ArrayUtils.addAll(array1, null)   = cloned copy of array1
   * ArrayUtils.addAll(null, array2)   = cloned copy of array2
   * ArrayUtils.addAll([], [])         = []
   * ArrayUtils.addAll([null], [null]) = [null, null]
   * ArrayUtils.addAll(["a", "b", "c"], ["1", "2", "3"]) = ["a", "b", "c", "1", "2", "3"]
   * </pre>
   *
   * @param array1  the first array whose elements are added to the new array, may be <code>null</code>
   * @param array2  the second array whose elements are added to the new array, may be <code>null</code>
   * @return The new array, <code>null</code> if <code>null</code> array inputs.
   *      The type of the new array is the type of the first array.
   * @since 2.1
   */
  public static Object[] addAll(Object[] array1, Object[] array2) {
      if (array1 == null) {
          return clone(array2);
      } else if (array2 == null) {
          return clone(array1);
      }
      Object[] joinedArray = (Object[]) Array.newInstance(array1.getClass().getComponentType(),
                                                          array1.length + array2.length);
      System.arraycopy(array1, 0, joinedArray, 0, array1.length);
      System.arraycopy(array2, 0, joinedArray, array1.length, array2.length);
      return joinedArray;
  }
  /**
   * <p>Shallow clones an array returning a typecast result and handling
   * <code>null</code>.</p>
   *
   * <p>The objects in the array are not cloned, thus there is no special
   * handling for multi-dimensional arrays.</p>
   *
   * <p>This method returns <code>null</code> for a <code>null</code> input array.</p>
   *
   * @param array  the array to shallow clone, may be <code>null</code>
   * @return the cloned array, <code>null</code> if <code>null</code> input
   */
  public static Object[] clone(Object[] array) {
      if (array == null) {
          return null;
      }
      return (Object[]) array.clone();
  }
}
```

1.  Growable int[]
---  ---
2.  Your own auto-growth Array
3.  Long Vector
4.  Int Vector (from java-objects-database)
5.  ArrayList of int primitives
6.  ArrayList of long primitives
7.  ArrayList of short primitives
8.  ArrayList of double primitives
9.  ArrayList of boolean primitives
10.  ArrayList of char primitives
11.  ArrayList of byte primitives
12.  Growable String array with type specific access methods.
13.  Auto Size Array
14.  Dynamic Int Array
15.  Dynamic Long Array
16.  Int Array
17.  Int Array List
18.  ArrayList of float primitives
19.  Fast Array
20.  Extensible vector of bytes
21.  Int Vector
22.  A two dimensional Vector
23.  Lazy List creation based on ArrayList
24.  Append the given Object to the given array
25.  Simple object pool
26.  A variable length Double Array: expanding and contracting its internal storage array as elements are added and removed.
