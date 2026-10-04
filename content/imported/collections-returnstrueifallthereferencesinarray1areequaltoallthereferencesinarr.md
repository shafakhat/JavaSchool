---
title: Returns true if all the references in array1 are equal to all the references in array2 (two null references are considered equal for this test).
nav: Returns true if all the re...
description: * JCommon : a free general purpose class library for the Java(tm) platform
section: Imported - java2s Archive
order: 2343
source: https://web.archive.org/web/20140829083540/http://www.java2s.com/Tutorial/Java/0140__Collections/Returnstrueifallthereferencesinarray1areequaltoallthereferencesinarray2twonullreferencesareconsideredequalforthistest.htm
---
```java title=Example.java
/*
 * JCommon : a free general purpose class library for the Java(tm) platform
 *
 *
 * (C) Copyright 2000-2005, by Object Refinery Limited and Contributors.
 *
 * Project Info:  http://www.jfree.org/jcommon/index.html
 *
 * This library is free software; you can redistribute it and/or modify it
 * under the terms of the GNU Lesser General Public License as published by
 * the Free Software Foundation; either version 2.1 of the License, or
 * (at your option) any later version.
 *
 * This library is distributed in the hope that it will be useful, but
 * WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
 * or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public
 * License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public
 * License along with this library; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301,
 * USA.
 *
 * [Java is a trademark or registered trademark of Sun Microsystems, Inc.
 * in the United States and other countries.]
 *
 * -------------------
 * ArrayUtilities.java
 * -------------------
 * (C) Copyright 2003-2005, by Object Refinery Limited.
 *
 * Original Author:  David Gilbert (for Object Refinery Limited);
 * Contributor(s):   -;
 *
 * $Id: ArrayUtilities.java,v 1.7 2008/09/10 09:21:30 mungady Exp $
 *
 * Changes
 * -------
 * 21-Aug-2003 : Version 1 (DG);
 * 04-Oct-2004 : Renamed ArrayUtils --> ArrayUtilities (DG);
 *
 */
public class Main {
  /**
   * Returns <code>true</code> if all the references in <code>array1</code>
   * are equal to all the references in <code>array2</code> (two
   * <code>null</code> references are considered equal for this test).
   *
   * @param array1  the first array (<code>null</code> permitted).
   * @param array2  the second array (<code>null</code> permitted).
   *
   * @return A boolean.
   */
  public static boolean equalReferencesInArrays(final Object[] array1,
                                                final Object[] array2) {
      if (array1 == null) {
          return (array2 == null);
      }
      if (array2 == null) {
          return false;
      }
      if (array1.length != array2.length) {
          return false;
      }
      for (int i = 0; i < array1.length; i++) {
          if (array1[i] == null) {
              if (array2[i] != null) {
                  return false;
              }
          }
          if (array2[i] == null) {
              if (array1[i] != null) {
                  return false;
              }
          }
          if (array1[i] != array2[i]) {
              return false;
          }
      }
      return true;
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
