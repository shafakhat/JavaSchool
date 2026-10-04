---
title: Object Arrays
nav: Object Arrays
description: public static int binarySearch(Object array[], Object key, Comparator c)
section: Imported - java2s Archive
order: 2341
source: https://web.archive.org/web/2014/http://www.java2s.com/Tutorial/Java/0140__Collections/ObjectArraysSearchingforelementsinasortedobjectarray.htm
---
```java title=Example.java
public static int binarySearch(Object array[], Object key)
public static int binarySearch(Object array[], Object key, Comparator c)
java title=Example.java
import java.util.Arrays;
public class MainClass {
  public static void main(String[] a) {
    String str[] = { "B", "H", "L", "M", "I", "N", "R" };
    // Ensure list sorted
    Arrays.sort(str);
    for (String s : str) {
      System.out.println(s);
    }
    // Search for element in list
 int index = Arrays.binarySearch(str, "M");
    System.out.println("Found M @ " + index);
  }
}
java title=Example.java
B
H
I
L
M
N
R
Found M @ 4
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
