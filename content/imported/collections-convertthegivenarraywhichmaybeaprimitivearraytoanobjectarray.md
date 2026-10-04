---
title: Convert the given array (which may be a primitive array) to an object array
nav: Convert the given array (w...
description: * Licensed under the Apache License, Version 2.0 (the "License");
section: Imported - java2s Archive
order: 2380
source: https://web.archive.org/web/20140404050751/http://www.java2s.com/Tutorial/Java/0140__Collections/Convertthegivenarraywhichmaybeaprimitivearraytoanobjectarray.htm
---
```java title=Example.java
import java.lang.reflect.Array;
import java.util.Arrays;
/*
 * Copyright 2002-2007 the original author or authors.
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
//Revised from springframework
/**
 * Miscellaneous object utility methods. Mainly for internal use within the
 * framework; consider Jakarta's Commons Lang for a more comprehensive suite
 * of object utilities.
 *
 * @author Juergen Hoeller
 * @author Keith Donald
 * @author Rod Johnson
 * @author Rob Harrop
 * @author Alex Ruiz
 * @since 19.03.2004
 * @see org.apache.commons.lang.ObjectUtils
 */
abstract class ObjectUtils {
  private static final int INITIAL_HASH = 7;
  private static final int MULTIPLIER = 31;
  private static final String EMPTY_STRING = "";
  private static final String NULL_STRING = "null";
  private static final String ARRAY_START = "{";
  private static final String ARRAY_END = "}";
  private static final String EMPTY_ARRAY = ARRAY_START + ARRAY_END;
  private static final String ARRAY_ELEMENT_SEPARATOR = ", ";
  /**
   * Return whether the given array is empty: that is, <code>null</code>
   * or of zero length.
   * @param array the array to check
   * @return whether the given array is empty
   */
  public static boolean isEmpty(Object[] array) {
    return (array == null || array.length == 0);
  }
  /**
   * Append the given Object to the given array, returning a new array
   * consisting of the input array contents plus the given Object.
   * @param array the array to append to (can be <code>null</code>)
   * @param obj the Object to append
   * @return the new array (of the same component type; never <code>null</code>)
   */
  public static Object[] addObjectToArray(Object[] array, Object obj) {
    Class compType = Object.class;
    if (array != null) {
      compType = array.getClass().getComponentType();
    }
    else if (obj != null) {
      compType = obj.getClass();
    }
    int newArrLength = (array != null ? array.length + 1 : 1);
    Object[] newArr = (Object[]) Array.newInstance(compType, newArrLength);
    if (array != null) {
      System.arraycopy(array, 0, newArr, 0, array.length);
    }
    newArr[newArr.length - 1] = obj;
    return newArr;
  }
  /**
   * Convert the given array (which may be a primitive array) to an
   * object array (if necessary of primitive wrapper objects).
   * A <code>null</code> source value will be converted to an
   * empty Object array.
   * @param source the (potentially primitive) array
   * @return the corresponding object array (never <code>null</code>)
   * @throws IllegalArgumentException if the parameter is not an array
   */
  public static Object[] toObjectArray(Object source) {
    if (source instanceof Object[]) {
      return (Object[]) source;
    }
    if (source == null) {
      return new Object[0];
    }
    if (!source.getClass().isArray()) {
      throw new IllegalArgumentException("Source is not an array: " + source);
    }
    int length = Array.getLength(source);
    if (length == 0) {
      return new Object[0];
    }
    Class wrapperType = Array.get(source, 0).getClass();
    Object[] newArray = (Object[]) Array.newInstance(wrapperType, length);
    for (int i = 0; i < length; i++) {
      newArray[i] = Array.get(source, i);
    }
    return newArray;
  }
}
```

| 9.9.1. | How to sort an array |
|---|---|
| 9.9.2. | Sorting an Array in Descending (Reverse) Order |
| 9.9.3. | Shuffle elements of an array |
| 9.9.4. | Minimum and maximum number in array |
| 9.9.5. | Convert an Array to a List |
| 9.9.6. | Extend the size of an array |
| 9.9.7. | How to copy an array |
| 9.9.8. | Performing Binary Search on Java Array |
| 9.9.9. | Java Sort byte Array |
| 9.9.10. | Java Sort char Array |
| 9.9.11. | Java Sort double Array |
| 9.9.12. | Java Sort float Array |
| 9.9.13. | Sort an array: case-sensitive |
| 9.9.14. | Sort an array: case-insensitive |
| 9.9.15. | java.utils.Arrays provides ways to dump the content of an array. |
| 9.9.16. | Dump multi-dimensional arrays |
| 9.9.17. | Use java.util.Arrays.deepToString() to dump the multi-dimensional arrays |
| 9.9.18. | Shifting Elements in an Array: Shift all elements right by one |
| 9.9.19. | Shifting Elements in an Array: Shift all elements left by one |
| 9.9.20. | Compare two byte type arrays |
| 9.9.21. | Compare two char type arrays |
| 9.9.22. | Compare two short type arrays |
| 9.9.23. | Compare two int type arrays |
| 9.9.24. | Compare two long type arrays |
| 9.9.25. | Compare two float type arrays |
| 9.9.26. | Compare two double type arrays |
| 9.9.27. | Filling Elements in an Array |
| 9.9.28. | filling object arrays: |
| 9.9.29. | fill to a contiguous range of elements in an array |
| 9.9.30. | If the given objects are equal |
| 9.9.31. | Append the given Object to the given array |
| 9.9.32. | Array To String |
| 9.9.33. | Convert the given array (which may be a primitive array) to an object array |
| 9.9.34. | Gets the subarray from array that starts at offset. |
| 9.9.35. | Gets the subarray of length length from array that starts at offset. |
| 9.9.36. | Growable String array with type specific access methods. |
| 9.9.37. | Wrapper for arrays of ordered strings. This verifies the arrays and supports efficient lookups. |
| 9.9.38. | Reverses the order of the given object array. |
