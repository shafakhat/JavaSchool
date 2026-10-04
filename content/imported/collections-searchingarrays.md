---
title: Searching Arrays
nav: Searching Arrays
description: private static void printArray(String message, int array[]) {
section: Imported - java2s Archive
order: 2342
source: https://web.archive.org/web/2014/http://www.java2s.com/Tutorial/Java/0140__Collections/SearchingArrays.htm
---
```java title=Example.java
public static int binarySearch(byte array[], byte key)
public static int binarySearch(char array[], char key)
public static int binarySearch(double array[], double key)
public static int binarySearch(float array[], float key)
public static int binarySearch(int array[], int key)
public static int binarySearch(long array[], long key)
public static int binarySearch(short array[], short key)
java title=Example.java
import java.util.Arrays;
public class MainClass {
  public static void main(String args[]) throws Exception {
    int array[] = { 2, 5, -2, 6, -3, 8, 0, -7, -9, 4 };
    Arrays.sort(array);
    printArray("Sorted array", array);
    int index = Arrays.binarySearch(array, 2);
    System.out.println("Found 2 @ " + index);
    index = Arrays.binarySearch(array, 1);
    System.out.println("Didn't find 1 @ " + index);
    int newIndex = -index - 1;
    array = insertElement(array, 1, newIndex);
    printArray("With 1 added", array);
  }
  private static void printArray(String message, int array[]) {
    System.out.println(message + ": [length: " + array.length + "]");
    for (int i = 0; i < array.length; i++) {
      if (i != 0)
        System.out.print(", ");
      System.out.print(array[i]);
    }
    System.out.println();
  }
  private static int[] insertElement(int original[], int element, int index) {
    int length = original.length;
    int destination[] = new int[length + 1];
    System.arraycopy(original, 0, destination, 0, index);
    destination[index] = element;
    System.arraycopy(original, index, destination, index + 1, length - index);
    return destination;
  }
}
java title=Example.java
Sorted array: [length: 10]
-9, -7, -3, -2, 0, 2, 4, 5, 6, 8
Found 2 @ 5
Didn't find 1 @ -6
With 1 added: [length: 11]
-9, -7, -3, -2, 0, 1, 2, 4, 5, 6, 8
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
