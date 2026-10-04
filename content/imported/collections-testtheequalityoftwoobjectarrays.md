---
title: Test the equality of two object arrays
nav: Test the equality of two o...
description: * Copyright 2005, JBoss Inc., and individual contributors as indicated
section: Imported - java2s Archive
order: 2347
source: https://web.archive.org/web/20140829084752/http://www.java2s.com/Tutorial/Java/0140__Collections/Testtheequalityoftwoobjectarrays.htm
---
```java title=Example.java
import java.lang.reflect.Array;
/*
 * JBoss, Home of Professional Open Source
 * Copyright 2005, JBoss Inc., and individual contributors as indicated
 * by the @authors tag. See the copyright.txt in the distribution for a
 * full listing of individual contributors.
 *
 * This is free software; you can redistribute it and/or modify it
 * under the terms of the GNU Lesser General Public License as
 * published by the Free Software Foundation; either version 2.1 of
 * the License, or (at your option) any later version.
 *
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
 * Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public
 * License along with this software; if not, write to the Free
 * Software Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA
 * 02110-1301 USA, or see the FSF site: http://www.fsf.org.
 */
public class Main {
  /**
   *
   * @param a       The first array.
   * @param b       The second array.
   * @param deep    True to traverse elements which are arrays.
   * @return        True if arrays are equal.
   */
  public static boolean equals(final Object[] a, final Object[] b,
                               final boolean deep)
  {
     if (a == b) return true;
     if (a == null || b == null) return false;
     if (a.length != b.length) return false;
     for (int i=0; i<a.length; i++) {
        Object x = a[i];
        Object y = b[i];
        if (x != y) return false;
        if (x == null || y == null) return false;
        if (deep) {
           if (x instanceof Object[] && y instanceof Object[]) {
              if (! equals((Object[])x, (Object[])y, true)) return false;
           }
           else {
              return false;
           }
        }
        if (! x.equals(y)) return false;
     }
     return true;
  }
  /**
   *
   * @param a    The first array.
   * @param b    The second array.
   * @return     True if arrays are equal.
   */
  public static boolean equals(final Object[] a, final Object[] b) {
     return equals(a, b, true);
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
