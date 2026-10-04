---
title: How to search an array
nav: How to search an array
description: publicstaticint indexOf(int[] array, int valueToFind, int startIndex) {
section: Imported - java2s Archive
order: 1031
source: https://web.archive.org/web/20130905095119/http://java2s.com/Tutorials/Java/Array/How_to_search_an_array.htm
---
In this chapter you will learn:

- Search an element in an array and return the index and last index
- Search a double type array

### Search an element in an array and return the index and last index

```java title=Example.java
import java.lang.reflect.Array;
publicclass Main {
  publicstaticfinalint INDEX_NOT_FOUND = -1;
  publicstaticint indexOf(int[] array, int valueToFind) {
      return indexOf(array, valueToFind, 0);
  }
  publicstaticint indexOf(int[] array, int valueToFind, int startIndex) {
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
  publicstaticint lastIndexOf(int[] array, int valueToFind) {
      return lastIndexOf(array, valueToFind, Integer.MAX_VALUE);
  }
  publicstaticint lastIndexOf(int[] array, int valueToFind, int startIndex) {
      if (array == null) {
          return INDEX_NOT_FOUND;
      }
      if (startIndex < 0) {
          return INDEX_NOT_FOUND;
      } elseif (startIndex >= array.length) {
          startIndex = array.length - 1;
      }
      for (int i = startIndex; i >= 0; i--) {
          if (valueToFind == array[i]) {
              return i;
          }
      }
      return INDEX_NOT_FOUND;
  }
  publicstaticboolean contains(int[] array, int valueToFind) {
      return indexOf(array, valueToFind) != INDEX_NOT_FOUND;
  }
}
```

### Search a double type array

```java title=Example.java
import java.lang.reflect.Array;
publicclass Main {
  publicstaticfinalint INDEX_NOT_FOUND = -1;
  publicstaticint indexOf(double[] array, double valueToFind) {
      return indexOf(array, valueToFind, 0);
  }publicstaticint indexOf(double[] array, double valueToFind, double tolerance) {
      return indexOf(array, valueToFind, 0, tolerance);
  }
  publicstaticint indexOf(double[] array, double valueToFind, int startIndex) {
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
  publicstaticint indexOf(double[] array, double valueToFind, int startIndex, double tolerance) {
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
  publicstaticint lastIndexOf(double[] array, double valueToFind) {
      return lastIndexOf(array, valueToFind, Integer.MAX_VALUE);
  }
  publicstaticint lastIndexOf(double[] array, double valueToFind, double tolerance) {
      return lastIndexOf(array, valueToFind, Integer.MAX_VALUE, tolerance);
  }
  publicstaticint lastIndexOf(double[] array, double valueToFind, int startIndex) {
      if (isEmpty(array)) {
          return INDEX_NOT_FOUND;
      }
      if (startIndex < 0) {
          return INDEX_NOT_FOUND;
      } elseif (startIndex >= array.length) {
          startIndex = array.length - 1;
      }
      for (int i = startIndex; i >= 0; i--) {
          if (valueToFind == array[i]) {
              return i;
          }
      }
      return INDEX_NOT_FOUND;
  }
  publicstaticint lastIndexOf(double[] array, double valueToFind, int startIndex, double tolerance) {
      if (isEmpty(array)) {
          return INDEX_NOT_FOUND;
      }
      if (startIndex < 0) {
          return INDEX_NOT_FOUND;
      } elseif (startIndex >= array.length) {
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
  publicstaticboolean contains(double[] array, double valueToFind) {
      return indexOf(array, valueToFind) != INDEX_NOT_FOUND;
  }
  publicstaticboolean contains(double[] array, double valueToFind, double tolerance) {
      return indexOf(array, valueToFind, 0, tolerance) != INDEX_NOT_FOUND;
  }
  publicstaticboolean isEmpty(double[] array) {
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
