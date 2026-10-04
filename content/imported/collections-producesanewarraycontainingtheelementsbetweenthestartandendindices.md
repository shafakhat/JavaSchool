---
title: Produces a new array containing the elements between the start and end indices.
nav: Produces a new array conta...
description: * Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 2346
source: https://web.archive.org/web/20140829083340/http://www.java2s.com/Tutorial/Java/0140__Collections/Producesanewarraycontainingtheelementsbetweenthestartandendindices.htm
---
```java title=Example.java
import java.lang.reflect.Array;
/*
 * Licensed to the Apache Software Foundation (ASF) under one or more
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
 *
 *
 */
/**
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
  // Subarrays
  //-----------------------------------------------------------------------
  /**
   * Produces a new array containing the elements between
   * the start and end indices.
   *
   * The start index is inclusive, the end index exclusive.
   * Null array input produces null output.
   *
   * The component type of the subarray is always the same as
   * that of the input array. Thus, if the input is an array of type
   * <code>Date</code>, the following usage is envisaged:
   *
   * <pre>
   * Date[] someDates = (Date[])ArrayUtils.subarray(allDates, 2, 5);
   * </pre>
   *
   * @param array  the array
   * @param startIndexInclusive  the starting index. Undervalue (&lt;0)
   *      is promoted to 0, overvalue (&gt;array.length) results
   *      in an empty array.
   * @param endIndexExclusive  elements up to endIndex-1 are present in the
   *      returned subarray. Undervalue (&lt; startIndex) produces
   *      empty array, overvalue (&gt;array.length) is demoted to
   *      array length.
   * @return a new array containing the elements between
   *      the start and end indices.
   * @since 2.1
   */
  public static Object[] subarray(Object[] array, int startIndexInclusive, int endIndexExclusive) {
      if (array == null) {
          return null;
      }
      if (startIndexInclusive < 0) {
          startIndexInclusive = 0;
      }
      if (endIndexExclusive > array.length) {
          endIndexExclusive = array.length;
      }
      int newSize = endIndexExclusive - startIndexInclusive;
      Class type = array.getClass().getComponentType();
      if (newSize <= 0) {
          return (Object[]) Array.newInstance(type, 0);
      }
      Object[] subarray = (Object[]) Array.newInstance(type, newSize);
      System.arraycopy(array, startIndexInclusive, subarray, 0, newSize);
      return subarray;
  }
}
```

| 9.8.1. | Sorting Arrays |
|---|---|
| 9.8.2. | Sorting a subset of array elements |
| 9.8.3. | Sorting arrays of objects |
| 9.8.4. | Object Arrays: Searching for elements in a sorted object array |
| 9.8.5. | Searching Arrays |
| 9.8.6. | Finds the index of the given object in the array starting at the given index. |
| 9.8.7. | Finds the index of the given object in the array. |
| 9.8.8. | Finds the last index of the given object in the array starting at the given index. |
| 9.8.9. | Finds the value in the range (start,limit) of the largest element (rank) where the count of all smaller elements in that range is less than or equals target. |
| 9.8.10. | Returns an index into arra (or -1) where the character is not in the charset byte array. |
| 9.8.11. | Returns an int[] array of length segments containing the distribution count of the elements in unsorted int[] array with values between min and max (range). |
| 9.8.12. | Returns the minimum value in an array. |
| 9.8.13. | Returns true if all the references in array1 are equal to all the references in array2 (two null references are considered equal for this test). |
| 9.8.14. | Get the element index or last index among a boolean type array |
| 9.8.15. | Produces a new array containing the elements between the start and end indices. |
| 9.8.16. | Test the equality of two object arrays |
| 9.8.17. | Get the index and last index of an int type value array |
| 9.8.18. | FastQSorts the [l,r] partition (inclusive) of the specfied array of Rows, using the comparator. |
| 9.8.19. | Sort array utilities |
