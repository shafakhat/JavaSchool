---
title: How to binary search an Array in Java
nav: How to binary search an Ar...
description: System.out.println("Result of binary search of 2 is : " + intResult);
section: Imported - java2s Archive
order: 1127
source: https://web.archive.org/web/2020/http://java2s.com/Tutorials/Java/Array/How_to_binary_search_an_Array_in_Java.htm
---
In this chapter you will learn:

- Binary search an Array
- Binary Search on byte Array
- Insert an Element into a Sorted Array

### Binary search an Array

The following methods binary search array elements.

- static int binarySearch(byte[] a, byte key)
- static int binarySearch(byte[] a, int fromIndex, int toIndex, byte key)
- static int binarySearch(char[] a, char key)
- static int binarySearch(char[] a, int fromIndex, int toIndex, char key)
- static int binarySearch(double[] a, double key)
- static int binarySearch(double[] a, int fromIndex, int toIndex, double key)
- static int binarySearch(float[] a, float key)
- static int binarySearch(float[] a, int fromIndex, int toIndex, float key)
- static int binarySearch(int[] a, int key)
- static int binarySearch(int[] a, int fromIndex, int toIndex, int key)
- static int binarySearch(long[] a, int fromIndex, int toIndex, long key)
- static int binarySearch(long[] a, long key)
- static int binarySearch(Object[] a, int fromIndex, int toIndex, Object key)
- static int binarySearch(Object[] a, Object key)
- static int binarySearch(short[] a, int fromIndex, int toIndex, short key)
- static int binarySearch(short[] a, short key)
- static<T> int binarySearch(T[] a, int fromIndex, int toIndex, T key, Comparator<? super T> c)
- static<T> int binarySearch(T[] a, T key, Comparator<? super T> c)

```java title=Example.java
import java.util.Arrays;
public class Main{
  public static void main(String args[]) {
    int array[] = new int[10];
    for (int i = 0; i < 10; i++){
      array[i] = -3 * i;
    }
    System.out.print("Original contents: ");
    System.out.println(Arrays.toString(array));
    Arrays.sort(array);
    System.out.print("Sorted: ");
    System.out.println(Arrays.toString(array));
    System.out.print("The value -9 is at location ");
    int index = Arrays.binarySearch(array, -9);
    System.out.println(index);
  }
}
```

The output:

### Binary Search on byte Array

Performing Binary Search on byte Array

```java title=Example.java
import java.util.Arrays;
public class Main {
  public static void main(String[] args) {
    byte bArray[] = {1, 2, 3, 4, 5};
    Arrays.sort(bArray);
    byte searchValue = 2;
    int intResult = Arrays.binarySearch(bArray, searchValue);
    System.out.println("Result of binary search of 2 is : " + intResult);
    searchValue = 3;
    intResult = Arrays.binarySearch(bArray, searchValue);
    System.out.println("Result of binary search of 3 is : " + intResult);
  }
}
```

The output:

### Insert an Element into a Sorted Array

```java title=Example.java
import java.util.Arrays;
public class Main {
  public static void main(String[] argv) {
    String[] oldArray = new String[] { "a", "b", "c", "d" };
    int index = Arrays.binarySearch(oldArray, "e");
    if (index < 0) {
      int insertIndex = -index - 1;
      String[] newArray = new String[oldArray.length + 1];
      System.arraycopy(oldArray, 0, newArray, 0, insertIndex);
      System.arraycopy(oldArray, insertIndex, newArray, insertIndex + 1,
          oldArray.length - insertIndex);
      newArray[insertIndex] = "e";
      oldArray = newArray;
    }
    System.out.println(Arrays.toString(oldArray));
  }
}
```

The code above generates the following result.

#### Next chapter...

What you will learn in the next chapter:

- Search an element in an array and return the index and last index
- Search a double type array
