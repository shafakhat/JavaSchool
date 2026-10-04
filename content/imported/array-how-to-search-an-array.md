---
title: How to search an array
nav: How to search an array
description: public static int indexOf(int[] array, int valueToFind, int startIndex) {
section: Imported - java2s Archive
order: 1126
source: https://web.archive.org/web/2016/http://java2s.com/Tutorials/Java/Array/How_to_search_an_array.htm
---
In this chapter you will learn:

- Search an element in an array and return the index and last index
- Search a double type array

### Search an element in an array and return the index and last index

```java title=Example.java
import java.lang.reflect.Array;
public class Main {
  public static final int INDEX_NOT_FOUND = -1;
  public static int indexOf(int[] array, int valueToFind) {
      return indexOf(array, valueToFind, 0);
  }
  public static int indexOf(int[] array, int valueToFind, int startIndex) {
      if (array == null) {
          return INDEX_NOT_FOUND;
      }
      if (startIndex < 0) {
          startIndex = 0;
      }
      for (int i = startIndex; i < array.length; i++) {
          if (valueToFind == array[i]) {
              return i;
          }
      }
      return INDEX_NOT_FOUND;
  }
  public static int lastIndexOf(int[] array, int valueToFind) {
      return lastIndexOf(array, valueToFind, Integer.MAX_VALUE);
  }
  public static int lastIndexOf(int[] array, int valueToFind, int startIndex) {
      if (array == null) {
          return INDEX_NOT_FOUND;
      }
      if (startIndex < 0) {
          return INDEX_NOT_FOUND;
      } else if (startIndex >= array.length) {
          startIndex = array.length - 1;
      }
      for (int i = startIndex; i >= 0; i--) {
          if (valueToFind == array[i]) {
              return i;
          }
      }
      return INDEX_NOT_FOUND;
  }
  public static boolean contains(int[] array, int valueToFind) {
      return indexOf(array, valueToFind) != INDEX_NOT_FOUND;
  }
}
```

### Search a double type array

```java title=Example.java
import java.lang.reflect.Array;
public class Main {
  public static final int INDEX_NOT_FOUND = -1;
  public static int indexOf(double[] array, double valueToFind) {
      return indexOf(array, valueToFind, 0);
  } public static int indexOf(double[] array, double valueToFind, double tolerance) {
      return indexOf(array, valueToFind, 0, tolerance);
  }
  public static int indexOf(double[] array, double valueToFind, int startIndex) {
      if (isEmpty(array)) {
          return INDEX_NOT_FOUND;
      }
      if (startIndex < 0) {
          startIndex = 0;
      }
      for (int i = startIndex; i < array.length; i++) {
          if (valueToFind == array[i]) {
              return i;
          }
      }
      return INDEX_NOT_FOUND;
  }
  public static int indexOf(double[] array, double valueToFind, int startIndex, double tolerance) {
      if (isEmpty(array)) {
          return INDEX_NOT_FOUND;
      }
      if (startIndex < 0) {
          startIndex = 0;
      }
      double min = valueToFind - tolerance;
      double max = valueToFind + tolerance;
      for (int i = startIndex; i < array.length; i++) {
          if (array[i] >= min && array[i] <= max) {
              return i;
          }
      }
      return INDEX_NOT_FOUND;
  }
  public static int lastIndexOf(double[] array, double valueToFind) {
      return lastIndexOf(array, valueToFind, Integer.MAX_VALUE);
  }
  public static int lastIndexOf(double[] array, double valueToFind, double tolerance) {
      return lastIndexOf(array, valueToFind, Integer.MAX_VALUE, tolerance);
  }
  public static int lastIndexOf(double[] array, double valueToFind, int startIndex) {
      if (isEmpty(array)) {
          return INDEX_NOT_FOUND;
      }
      if (startIndex < 0) {
          return INDEX_NOT_FOUND;
      } else if (startIndex >= array.length) {
          startIndex = array.length - 1;
      }
      for (int i = startIndex; i >= 0; i--) {
          if (valueToFind == array[i]) {
              return i;
          }
      }
      return INDEX_NOT_FOUND;
  }
  public static int lastIndexOf(double[] array, double valueToFind, int startIndex, double tolerance) {
      if (isEmpty(array)) {
          return INDEX_NOT_FOUND;
      }
      if (startIndex < 0) {
          return INDEX_NOT_FOUND;
      } else if (startIndex >= array.length) {
          startIndex = array.length - 1;
      }
      double min = valueToFind - tolerance;
      double max = valueToFind + tolerance;
      for (int i = startIndex; i >= 0; i--) {
          if (array[i] >= min && array[i] <= max) {
              return i;
          }
      }
      return INDEX_NOT_FOUND;
  }
  public static boolean contains(double[] array, double valueToFind) {
      return indexOf(array, valueToFind) != INDEX_NOT_FOUND;
  }
  public static boolean contains(double[] array, double valueToFind, double tolerance) {
      return indexOf(array, valueToFind, 0, tolerance) != INDEX_NOT_FOUND;
  }
  public static boolean isEmpty(double[] array) {
      if (array == null || array.length == 0) {
          return true;
      }
      return false;
  }
}
```

#### Next chapter...

What you will learn in the next chapter:

- How to sort an array
- Sort string type array in case insensitive order and case sensitive order
- Sort an Array in Descending (Reverse) Order
