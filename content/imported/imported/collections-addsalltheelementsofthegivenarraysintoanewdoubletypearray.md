---
title: Adds all the elements of the given arrays into a new double-type array.
nav: Adds all the elements of t...
description: * Licensed under the Apache License, Version 2.0 (the "License");
section: Imported - java2s Archive
order: 1029
source: https://web.archive.org/web/20100911233525/http://www.java2s.com:80/Tutorial/Java/0140__Collections/Addsalltheelementsofthegivenarraysintoanewdoubletypearray.htm
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
 * Operations on arrays, primitive arrays (like <code>int[]</code>) and
 * primitive wrapper arrays (like <code>Integer[]</code>).
 *
 * This class tries to handle <code>null</code> input gracefully.
 * An exception will not be thrown for a <code>null</code>
 * array input. However, an Object array that contains a <code>null</code>
 * element may throw an exception. Each method documents its behaviour.
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
   * Adds all the elements of the given arrays into a new array.
   * The new array contains all of the element of <code>array1</code> followed
   * by all of the elements <code>array2</code>. When an array is returned, it is always
   * a new array.
   *
   * <pre>
   * ArrayUtils.addAll(array1, null)   = cloned copy of array1
   * ArrayUtils.addAll(null, array2)   = cloned copy of array2
   * ArrayUtils.addAll([], [])         = []
   * </pre>
   *
   * @param array1  the first array whose elements are added to the new array.
   * @param array2  the second array whose elements are added to the new array.
   * @return The new double[] array.
   * @since 2.1
   */
  public static double[] addAll(double[] array1, double[] array2) {
      if (array1 == null) {
          return clone(array2);
      } else if (array2 == null) {
          return clone(array1);
      }
      double[] joinedArray = new double[array1.length + array2.length];
      System.arraycopy(array1, 0, joinedArray, 0, array1.length);
      System.arraycopy(array2, 0, joinedArray, array1.length, array2.length);
      return joinedArray;
  }
  /**
   * Shallow clones an array returning a typecast result and handling
   * <code>null</code>.
   *
   * The objects in the array are not cloned, thus there is no special
   * handling for multi-dimensional arrays.
   *
   * This method returns <code>null</code> for a <code>null</code> input array.
   *
   * @param array  the array to shallow clone, may be <code>null</code>
   * @return the cloned array, <code>null</code> if <code>null</code> input
   */
  public static double[] clone(double[] array) {
      if (array == null) {
          return null;
      }
      return (double[]) array.clone();
  }
}
```
