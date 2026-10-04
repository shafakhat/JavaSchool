---
title: If the given objects are equal
nav: If the given objects are e...
description: * Licensed under the Apache License, Version 2.0 (the "License");
section: Imported - java2s Archive
order: 2378
source: https://web.archive.org/web/20140404050801/http://www.java2s.com/Tutorial/Java/0140__Collections/Ifthegivenobjectsareequal.htm
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
   * Determine if the given objects are equal, returning <code>true</code>
   * if both are <code>null</code> or <code>false</code> if only one is
   * <code>null</code>.
   * Compares arrays with <code>Arrays.equals</code>, performing an equality
   * check based on the array elements rather than the array reference.
   * @param o1 first Object to compare
   * @param o2 second Object to compare
   * @return whether the given objects are equal
   * @see java.util.Arrays#equals
   */
  public static boolean nullSafeEquals(Object o1, Object o2) {
    if (o1 == o2) {
      return true;
    }
    if (o1 == null || o2 == null) {
      return false;
    }
    if (o1.equals(o2)) {
      return true;
    }
    if (o1 instanceof Object[] && o2 instanceof Object[]) {
      return Arrays.equals((Object[]) o1, (Object[]) o2);
    }
    if (o1 instanceof boolean[] && o2 instanceof boolean[]) {
      return Arrays.equals((boolean[]) o1, (boolean[]) o2);
    }
    if (o1 instanceof byte[] && o2 instanceof byte[]) {
      return Arrays.equals((byte[]) o1, (byte[]) o2);
    }
    if (o1 instanceof char[] && o2 instanceof char[]) {
      return Arrays.equals((char[]) o1, (char[]) o2);
    }
    if (o1 instanceof double[] && o2 instanceof double[]) {
      return Arrays.equals((double[]) o1, (double[]) o2);
    }
    if (o1 instanceof float[] && o2 instanceof float[]) {
      return Arrays.equals((float[]) o1, (float[]) o2);
    }
    if (o1 instanceof int[] && o2 instanceof int[]) {
      return Arrays.equals((int[]) o1, (int[]) o2);
    }
    if (o1 instanceof long[] && o2 instanceof long[]) {
      return Arrays.equals((long[]) o1, (long[]) o2);
    }
    if (o1 instanceof short[] && o2 instanceof short[]) {
      return Arrays.equals((short[]) o1, (short[]) o2);
    }
    return false;
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
