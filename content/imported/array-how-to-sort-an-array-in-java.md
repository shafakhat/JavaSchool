---
title: How to sort an array in Java
nav: How to sort an array in Java
description: The following methods sort the specified array into ascending numerical order.
section: Imported - java2s Archive
order: 1033
source: https://web.archive.org/web/20130905055437/http://java2s.com/Tutorials/Java/Array/How_to_sort_an_array_in_Java.htm
---
In this chapter you will learn:

- How to sort an array
- Sort string type array in case insensitive order and case sensitive order
- Sort an Array in Descending (Reverse) Order

### Sort an array

The following methods sort the specified array into ascending numerical order.

- static void sort(byte[] a)
- static void sort(byte[] a, int fromIndex, int toIndex)
- static void sort(char[] a)
- static void sort(char[] a, int fromIndex, int toIndex)
- static void sort(double[] a)
- static void sort(double[] a, int fromIndex, int toIndex)
- static void sort(float[] a)
- static void sort(float[] a, int fromIndex, int toIndex)
- static void sort(int[] a)
- static void sort(int[] a, int fromIndex, int toIndex)
- static void sort(long[] a)
- static void sort(long[] a, int fromIndex, int toIndex)
- static void sort(Object[] a)
- static void sort(Object[] a, int fromIndex, int toIndex)
- static void sort(short[] a)
- static void sort(short[] a, int fromIndex, int toIndex)
- static<T> void sort(T[] a, Comparator<? super T> c)
- static<T> void sort(T[] a, int fromIndex, int toIndex, Comparator<? super T> c)

```java title=Example.java
import java.util.Arrays;
publicclass Main{
  publicstaticvoid main(String args[]) {
    int array[] = newint[10];
    for (int i = 0; i < 10; i++){
      array[i] = -3 * i;
    }
    System.out.print("Original contents: ");
    System.out.println(Arrays.toString(array));
    Arrays.sort(array);
    System.out.print("Sorted: ");
    System.out.println(Arrays.toString(array));
  }
}
```

The output:

### Sort string type array in case insensitive order and case sensitive order

```java title=Example.java
import java.util.Arrays;
publicclass Main {
  publicstaticvoid main(String[] args) {
    String[] teams = new String[5];
    teams[0] = "M";
    teams[1] = "c";
    teams[2] = "A";
    teams[3] = "l";
    teams[4] = "E";
    Arrays.sort(teams);
    System.out.println(Arrays.toString(teams));
    Arrays.sort(teams, String.CASE_INSENSITIVE_ORDER);
    System.out.println(Arrays.toString(teams));
    Arrays.sort(teams);
    System.out.println(Arrays.toString(teams));
  }
}
```

The code above generates the following result.

### Sort an Array in Descending (Reverse) Order

```java title=Example.java
import java.util.Arrays;
import java.util.Collections;
publicclass Main {
    publicstaticvoid main(String[] args) {
        Integer[] arrayToSort = newInteger[] {
            newInteger(5),
            newInteger(89),
            newInteger(16),
            newInteger(2)
        };
        Arrays.sort(arrayToSort, Collections.reverseOrder());
        for (Integer i : arrayToSort) {
            System.out.println(i.intValue());
        }
    }
}
```

Output:

#### Next chapter...

What you will learn in the next chapter:

- Convert array to list
