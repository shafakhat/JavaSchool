---
title: Adds all the elements of the given arrays into a new char-type array.
nav: Adds all the elements of t...
description: Adds all the elements of the given arrays into a new char-type array.
section: Imported - java2s Archive
order: 1024
source: https://web.archive.org/web/20100201075550/http://java2s.com/Code/Java/Collections-Data-Structure/Addsalltheelementsofthegivenarraysintoanewchartypearray.htm
---
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
   * ArrayUtils.addAll(array1, null)   = cloned copy of array1
   * ArrayUtils.addAll(null, array2)   = cloned copy of array2
   * ArrayUtils.addAll([], [])         = []
   * </pre>
   *
   * @param array1  the first array whose elements are added to the new array.
   * @param array2  the second array whose elements are added to the new array.
   * @return The new char[] array.
   * @since 2.1
   */
  public static char[] addAll(char[] array1, char[] array2) {
      if (array1 == null) {
          return clone(array2);
      } else if (array2 == null) {
          return clone(array1);
      }
      char[] joinedArray = new char[array1.length + array2.length];
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
  public static char[] clone(char[] array) {
      if (array == null) {
          return null;
      }
      return (char[]) array.clone();
  }
}
```

1.  Adds all the elements of the given arrays into a new boolean-value array.
---  ---
2.  Adds all the elements of the given arrays into a new byte-type array.
3.  Adds all the elements of the given arrays into a new double-type array.
4.  Adds all the elements of the given arrays into a new float-type array.
5.  Adds all the elements of the given arrays into a new int-type array.
6.  Adds all the elements of the given arrays into a new long-type array.
7.  Adds all the elements of the given arrays into a new short-type array.
8.  Copies the given array and adds the given element at the end of the new array. (char type value)
9.  Copies the given array and adds the given element at the end of the new array. (float type value)
10.  Copies the given array and adds the given element at the end of the new array. (long value type)
11.  Copies the given array and adds the given element at the end of the new array. (object value type)
12.  Copies the given array and adds the given element at the end of the new array.(boolean value type)
13.  Copies the given array and adds the given element at the end of the new array.(byte value type)
14.  Copies the given array and adds the given element at the end of the new array.(double type value)
15.  Copies the given array and adds the given element at the end of the new array.(int value type)
16.  Copies the given array and adds the given element at the end of the new array.(short type array)
17.  Inserts the specified element at the specified position in the array.
18.  Inserts the specified element at the specified position in the boolean-type-value array.
19.  Inserts the specified element at the specified position in the byte-type-value array.
20.  Inserts the specified element at the specified position in the char-type-value array.
21.  Inserts the specified element at the specified position in the double-type-value array.
22.  Inserts the specified element at the specified position in the float-value-type array.
23.  Inserts the specified element at the specified position in the int-type-value array.
24.  Inserts the specified element at the specified position in the long-type-value array.
25.  Inserts the specified element at the specified position in the short-value-type array.
26.  Removes the element at the specified position from the specified array.
27.  Removes the element at the specified position from the specified long type array.
28.  Removes the first occurrence of the specified element from the specified array.
29.  Removes the first occurrence of the specified element from the specified long value array.
30.  Insert value to array
31.  Array Copy Utilities
32.  Concatenate Java arrays
