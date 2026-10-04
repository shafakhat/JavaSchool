---
title: Removes the first occurrence of the specified element from the specified array.
nav: Removes the first occurren...
description: * Licensed under the Apache License, Version 2.0 (the "License");
section: Imported - java2s Archive
order: 2356
source: https://web.archive.org/web/2014/http://www.java2s.com/Tutorial/Java/0140__Collections/Removesthefirstoccurrenceofthespecifiedelementfromthespecifiedarray.htm
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
 */import java.lang.reflect.Array;
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
 */public class Main {
  /**
   * Removes the first occurrence of the specified element from the
   * specified array. All subsequent elements are shifted to the left
   * (substracts one from their indices). If the array doesn't contains
   * such an element, no elements are removed from the array.
   *
   * This method returns a new array with the same elements of the input
   * array except the first occurrence of the specified element. The component
   * type of the returned array is always the same as that of the input
   * array.
   *
   * <pre>
   * ArrayUtils.removeElement(null, 1)      = null
   * ArrayUtils.removeElement([], 1)        = []
   * ArrayUtils.removeElement([1], 2)       = [1]
   * ArrayUtils.removeElement([1, 3], 1)    = [3]
   * ArrayUtils.removeElement([1, 3, 1], 1) = [3, 1]
   * </pre>
   *
   * @param array  the array to remove the element from, may be <code>null</code>
   * @param element  the element to be removed
   * @return A new array containing the existing elements except the first
   *         occurrence of the specified element.
   * @since 2.1
   */ public static short[] removeElement(short[] array, short element) {
      int index = indexOf(array, element);
      if (index == -1) {
          return clone(array);
      }
      return remove(array, index);
  }
  /**
   * Removes the element at the specified position from the specified array.
   * All subsequent elements are shifted to the left (substracts one from
   * their indices).
   *
   * This method returns a new array with the same elements of the input
   * array except the element on the specified position. The component
   * type of the returned array is always the same as that of the input
   * array.
   *
   * If the input array is <code>null</code>, an IndexOutOfBoundsException
   * will be thrown, because in that case no valid index can be specified.
   *
   * <pre>
   * ArrayUtils.remove([1], 0)         = []
   * ArrayUtils.remove([2, 6], 0)      = [6]
   * ArrayUtils.remove([2, 6], 1)      = [2]
   * ArrayUtils.remove([2, 6, 3], 1)   = [2, 3]
   * </pre>
   *
   * @param array  the array to remove the element from, may not be <code>null</code>
   * @param index  the position of the element to be removed
   * @return A new array containing the existing elements except the element
   *         at the specified position.
   * @throws IndexOutOfBoundsException if the index is out of range
   * (index < 0 || index >= array.length), or if the array is <code>null</code>.
   * @since 2.1
   */ public static short[] remove(short[] array, int index) {
      return (short[]) remove((Object) array, index);
  }
  /**
   * Removes the element at the specified position from the specified array.
   * All subsequent elements are shifted to the left (substracts one from
   * their indices).
   *
   * This method returns a new array with the same elements of the input
   * array except the element on the specified position. The component
   * type of the returned array is always the same as that of the input
   * array.
   *
   * If the input array is <code>null</code>, an IndexOutOfBoundsException
   * will be thrown, because in that case no valid index can be specified.
   *
   * @param array  the array to remove the element from, may not be <code>null</code>
   * @param index  the position of the element to be removed
   * @return A new array containing the existing elements except the element
   *         at the specified position.
   * @throws IndexOutOfBoundsException if the index is out of range
   * (index < 0 || index >= array.length), or if the array is <code>null</code>.
   * @since 2.1
   */ private static Object remove(Object array, int index) {
      int length = getLength(array);
      if (index < 0 || index >= length) {
          throw new IndexOutOfBoundsException("Index: " + index + ", Length: " + length);
      }
      Object result = Array.newInstance(array.getClass().getComponentType(), length - 1);
      System.arraycopy(array, 0, result, 0, index);
      if (index < length - 1) {
          System.arraycopy(array, index + 1, result, index, length - index - 1);
      }
      return result;
  }
  /**
   * Finds the index of the given value in the array starting at the given index.
   *
   * This method returns {@link #INDEX_NOT_FOUND} (<code>-1</code>) for a <code>null</code> input array.
   *
   * A negative startIndex is treated as zero. A startIndex larger than the array
   * length will return {@link #INDEX_NOT_FOUND} (<code>-1</code>).
   *
   * @param array  the array to search through for the object, may be <code>null</code>
   * @param valueToFind  the value to find
   * @param startIndex  the index to start searching at
   * @return the index of the value within the array,
   *  {@link #INDEX_NOT_FOUND} (<code>-1</code>) if not found or <code>null</code> array input
   */ public static int indexOf(short[] array, short valueToFind) {
      if (array == null) {
          return -1;
      }
      for (int i = 0; i < array.length; i++) {
          if (valueToFind == array[i]) {
              return i;
          }
      }
      return -1;
  }
  /**
   * Returns the length of the specified array.
   * This method can deal with <code>Object</code> arrays and with primitive arrays.
   *
   * If the input array is <code>null</code>, <code>0</code> is returned.
   *
   * <pre>
   * ArrayUtils.getLength(null)            = 0
   * ArrayUtils.getLength([])              = 0
   * ArrayUtils.getLength([null])          = 1
   * ArrayUtils.getLength([true, false])   = 2
   * ArrayUtils.getLength([1, 2, 3])       = 3
   * ArrayUtils.getLength(["a", "b", "c"]) = 3
   * </pre>
   *
   * @param array  the array to retrieve the length from, may be null
   * @return The length of the array, or <code>0</code> if the array is <code>null</code>
   * @throws IllegalArgumentException if the object arguement is not an array.
   * @since 2.1
   */ public static int getLength(Object array) {
      if (array == null) {
          return 0;
      }
      return Array.getLength(array);
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
   */ public static short[] clone(short[] array) {
      if (array == null) {
          return null;
      }
      return (short[]) array.clone();
  }
}
```

| 9.6.1. | Arrays of Objects |
|---|---|
| 9.6.2. | Arrays of Strings: using 'new' operator |
| 9.6.3. | Arrays of Strings: initial values determine the size of the array |
| 9.6.4. | Demonstrate String arrays. |
| 9.6.5. | Checks whether two arrays are the same length, treating null arrays as length 0. |
| 9.6.6. | Checks whether two arrays are the same type taking into account multi-dimensional arrays. |
| 9.6.7. | Turn an array of ints into a printable string. |
| 9.6.8. | Check if the given object is an array (primitve or native). |
| 9.6.9. | Reverses the order of the given long type value array. |
| 9.6.10. | Removes the first occurrence of the specified element from the specified array. |
| 9.6.11. | Removes the element at the specified position from the specified array. |
