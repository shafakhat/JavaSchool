---
title: Finds the index of the given object in the array starting at the given index.
nav: Finds the index of the giv...
description: * Licensed under the Apache License, Version 2.0 (the "License");
section: Imported - java2s Archive
order: 2336
source: https://web.archive.org/web/20140829083700/http://www.java2s.com/Tutorial/Java/0140__Collections/Findstheindexofthegivenobjectinthearraystartingatthegivenindex.htm
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
   * Finds the index of the given object in the array starting at the given index.
   *
   * This method returns {@link #INDEX_NOT_FOUND} (<code>-1</code>) for a <code>null</code> input array.
   *
   * A negative startIndex is treated as zero. A startIndex larger than the array
   * length will return {@link #INDEX_NOT_FOUND} (<code>-1</code>).
   *
   * @param array  the array to search through for the object, may be <code>null</code>
   * @param objectToFind  the object to find, may be <code>null</code>
   * @param startIndex  the index to start searching at
   * @return the index of the object within the array starting at the index,
   *  {@link #INDEX_NOT_FOUND} (<code>-1</code>) if not found or <code>null</code> array input
   */
  public static int indexOf(Object[] array, Object objectToFind, int startIndex) {
      if (array == null) {
          return -1;
      }
      if (startIndex < 0) {
          startIndex = 0;
      }
      if (objectToFind == null) {
          for (int i = startIndex; i < array.length; i++) {
              if (array[i] == null) {
                  return i;
              }
          }
      } else {
          for (int i = startIndex; i < array.length; i++) {
              if (objectToFind.equals(array[i])) {
                  return i;
              }
          }
      }
      return -1;
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
