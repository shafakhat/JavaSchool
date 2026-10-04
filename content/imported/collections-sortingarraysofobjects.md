---
title: Sorting arrays of objects
nav: Sorting arrays of objects
description: public static void sort(Object array[], int fromIndex, int toIndex)
section: Imported - java2s Archive
order: 2333
source: https://web.archive.org/web/20140829083211/http://www.java2s.com/Tutorial/Java/0140__Collections/Sortingarraysofobjects.htm
---
```java title=Example.java
public static void sort(Object array[])
public static void sort(Object array[], int fromIndex, int toIndex)
public static void sort(Object array[], Comparator c)
public static void sort(Object array[], int fromIndex, int toIndex, Comparator c)
java title=Example.java
import java.util.Arrays;
public class MainClass {
  public static void main(String args[]) throws Exception {
    String[] a = new String[] { "A", "C", "B" };
    Arrays.sort(a);
    for (int i = 0, n = a.length; i < n; i++) {
      System.out.println(a[i]);
    }
  }
}
java title=Example.java
A
B
C
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
