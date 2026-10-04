---
title: How to append element to an array
nav: How to append element to a...
description: Class<?> clazz = obj != null ? obj.getClass() : array.getClass().getComponentType();
section: Imported - java2s Archive
order: 1120
source: https://web.archive.org/web/2016/http://java2s.com/Tutorials/Java/Array/How_to_append_element_to_an_array.htm
---
In this chapter you will learn:

- Append an object to an array.
- Append one array to another

### Append an object to an array.

```java title=Example.java
import java.lang.reflect.Array;
public class Main {
  public static <T> T[] add(T[] array, T obj) {
    if (array == null && obj == null) {
      return null;
    }
    Class<?> clazz = obj != null ? obj.getClass() : array.getClass().getComponentType();
    int length = array != null ? array.length : 0;
    T[] newArray = (T[]) Array.newInstance(clazz, length + 1);
    if (array != null) {
      System.arraycopy(array, 0, newArray, 0, length);
    }
    newArray[length] = obj;
    return newArray;
  }
}
```

### Append one array to another

```java title=Example.java
import java.lang.reflect.Array;
public class Util {
  /**
   * Returns a new array that is the concatenation of a1 and a2.
   *
   * @param a1
   * @param a2
   * @return
   */ public static int[] append(int[] a1, int[] a2) {
    int[] ret = new int[a1.length + a2.length];
    System.arraycopy(a1, 0, ret, 0, a1.length);
    System.arraycopy(a2, 0, ret, a1.length, a2.length);
    return ret;
  }
  /**
   * Returns a new array that is the concatenation of a1 and a2.
   *
   * @param a1
   * @param a2
   * @return
   */ public static double[] append(double[] a1, double[] a2) {
    double[] ret = new double[a1.length + a2.length];
    System.arraycopy(a1, 0, ret, 0, a1.length);
    System.arraycopy(a2, 0, ret, a1.length, a2.length);
    return ret;
  }
  /**
   * Returns a new array with a single element appended at the end. Use this
   * sparingly, for it will allocate a new array. You can easily turn a
   * linear-time algorithm to quadratic this way.
   *
   * @param v
   *            Original array
   * @param elem
   *            Element to add to end
   */ public static int[] append(int[] v, int elem) {
    int[] ret = new int[v.length + 1];
    System.arraycopy(v, 0, ret, 0, v.length);
    ret[v.length] = elem;
    return ret;
  }
  /**
   * Returns a new array with a single element appended at the end. Use this
   * sparingly, for it will allocate a new array. You can easily turn a
   * linear-time algorithm to quadratic this way.
   *
   * @param v
   *            Original array
   * @param elem
   *            Element to add to end
   */ public static boolean[] append(boolean[] v, boolean elem) {
    boolean[] ret = new boolean[v.length + 1];
    System.arraycopy(v, 0, ret, 0, v.length);
    ret[v.length] = elem;
    return ret;
  }
  /**
   * Returns a new array with a single element appended at the end. Use this
   * sparingly, for it will allocate a new array. You can easily turn a
   * linear-time algorithm to quadratic this way.
   *
   * @param v
   *            Original array
   * @param elem
   *            Element to add to end
   * @return Array with length v+1 that is (v0,v1,...,vn,elem). Runtime type
   *         will be same as he pased-in array.
   */ public static Object[] append(Object[] v, Object elem) {
    Object[] ret = (Object[]) Array.newInstance(v.getClass()
        .getComponentType(), v.length + 1);
    System.arraycopy(v, 0, ret, 0, v.length);
    ret[v.length] = elem;
    return ret;
  }
}
```

#### Next chapter...

What you will learn in the next chapter:

- Maximum value in a byte array
- Maximum value in a double-type array
- Returns the minimum value in a double-type array
