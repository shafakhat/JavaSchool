---
title: Add new value, which sets as the first value, to existing array.
nav: Add new value, which sets ...
description: Add new value, which sets as the first value, to existing array.
section: Imported - java2s Archive
order: 1018
source: https://web.archive.org/web/20111109105615/http://www.java2s.com:80/Code/Java/Collections-Data-Structure/Addnewvaluewhichsetsasthefirstvaluetoexistingarray.htm
---
```java title=Example.java
/*
 * Copyright 2008-2009 the T2 Project ant the Others.
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
import java.lang.reflect.Array;
/**
 * ArrayUtil is an utility class for processing array.
 *
 * @author shot
 */
public class ArrayUtil {
  /**
   *
   * @param <T>
   * @param current
   * @param value
   * @return
   */
  @SuppressWarnings("unchecked")
  public static <T> T[] addFirst(T[] current, T value) {
    T[] newone = (T[]) Array.newInstance(current.getClass()
        .getComponentType(), current.length + 1);
    copy(current, newone, 0, 1, current.length);
    newone[0] = value;
    return newone;
  }
  /**
   * Copy array with from and to position.
   *
   * @param <T>
   * @param from
   * @param to
   * @param fromPos
   * @param toPos
   * @param length
   * @return
   */
  public static <T> T[] copy(T[] from, T[] to, int fromPos, int toPos,
      int length) {
    System.arraycopy(from, fromPos, to, toPos, length);
    return to;
  }
}
```

1.  Adds all the elements of the given arrays into a new boolean-value array.
---  ---
2.  Adds all the elements of the given arrays into a new byte-type array.
3.  Adds all the elements of the given arrays into a new char-type array.
4.  Adds all the elements of the given arrays into a new double-type array.
5.  Adds all the elements of the given arrays into a new float-type array.
6.  Adds all the elements of the given arrays into a new int-type array.
7.  Adds all the elements of the given arrays into a new long-type array.
8.  Adds all the elements of the given arrays into a new short-type array.
9.  Copies the given array and adds the given element at the end of the new array. (char type value)
10.  Copies the given array and adds the given element at the end of the new array. (float type value)
11.  Copies the given array and adds the given element at the end of the new array. (long value type)
12.  Copies the given array and adds the given element at the end of the new array. (object value type)
13.  Copies the given array and adds the given element at the end of the new array.(boolean value type)
14.  Copies the given array and adds the given element at the end of the new array.(byte value type)
15.  Copies the given array and adds the given element at the end of the new array.(double type value)
16.  Copies the given array and adds the given element at the end of the new array.(int value type)
17.  Copies the given array and adds the given element at the end of the new array.(short type array)
18.  Inserts the specified element at the specified position in the array.
19.  Inserts the specified element at the specified position in the boolean-type-value array.
20.  Inserts the specified element at the specified position in the byte-type-value array.
21.  Inserts the specified element at the specified position in the char-type-value array.
22.  Inserts the specified element at the specified position in the double-type-value array.
23.  Inserts the specified element at the specified position in the float-value-type array.
24.  Inserts the specified element at the specified position in the int-type-value array.
25.  Inserts the specified element at the specified position in the long-type-value array.
26.  Inserts the specified element at the specified position in the short-value-type array.
27.  Removes the element at the specified position from the specified array.
28.  Removes the element at the specified position from the specified long type array.
29.  Removes the first occurrence of the specified element from the specified array.
30.  Removes the first occurrence of the specified element from the specified long value array.
31.  Insert value to array
32.  Array Copy Utilities
33.  Concatenate Java arrays
34.  This program demonstrates array manipulation.
35.  Appends an Object to an Object array.
36.  Appends an integer to an integer array.
37.  Inserts an Object into an Object array at the index position.
38.  Prepends an Object to an Object array.
39.  Removes an Object from an Object array.
40.  Removes duplicate elements from the array
41.  Creates a new subarray from a larger array.
42.  Append one array to another
43.  Array Expander
44.  Array Util: seach, insert, append, remove, copy, shuffle
45.  Add new value to exsisting array.The new value is indexed to the last.
46.  Add one array to another
47.  Concatenates all the passed arrays
48.  Returns a copy of the specified array of objects of the specified size.
49.  Pack chunks
50.  Removes an element from a an array yielding a new array with that data.
