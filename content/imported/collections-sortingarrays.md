---
title: Sorting Arrays
nav: Sorting Arrays
description: public static void sort(byte array[], int fromIndex, int toIndex)
section: Imported - java2s Archive
order: 2332
source: https://web.archive.org/web/20140215115603/http://www.java2s.com/Tutorial/Java/0140__Collections/SortingArrays.htm
---
```java title=Example.java
public static void sort(byte array[])
public static void sort(byte array[], int fromIndex, int toIndex)
public static void sort(char array[])
public static void sort(char array[], int fromIndex, int toIndex)
public static void sort(double array[])
public static void sort(double array[], int fromIndex, int toIndex)
public static void sort(float array[])
public static void sort(float array[], int fromIndex, int toIndex)
public static void sort(int array[])
public static void sort(int array[], int fromIndex, int toIndex)
public static void sort(long array[])
public static void sort(long array[], int fromIndex, int toIndex)
public static void sort(short array[])
public static void sort(short array[], int fromIndex, int toIndex)
```

```java title=Example.java
import java.util.Arrays;
public class MainClass {
  public static void main(String[] a) {
    int array[] = { 2, 5, -2, 6, -3 };
    Arrays.sort(array);
    for (int i : array) {
      System.out.println(i);
    }
  }
}
```

```java title=Example.java
-3
-2
2
5
6
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
