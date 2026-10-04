---
title: How to reverse elements in an array with Java
nav: How to reverse elements in...
description: Next »« PreviousHome » Java Tutorial » ArrayJava ArrayCreate an ArrayArray Index and lengthMultidimensional ArraysArray examplesArray copyArray compareArray Binary search
section: Imported - java2s Archive
order: 1111
source: https://web.archive.org/web/2016/http://java2s.com/Tutorials/Java/Array/How_to_reverse_elements_in_an_array_with_Java.htm
---
In this chapter you will learn:

- How to reverse elements in an array
- Reverses the order of the given long type value array

### Reverses the order of an array

```java title=Example.java
import java.util.Arrays;
public class Main {
  public static void reverse(byte[] array) {
    if (array == null) {
      return;
    }
    int i = 0;
    int j = array.length - 1;
    byte tmp;
    while (j > i) {
      tmp = array[j];
      array[j] = array[i];
      array[i] = tmp;
      j--;
      i++;
    }
  }
  public static void main(String[] args) {
    byte[] b1 = new byte[] { 3, 2, 5, 4, 1 };
    for (byte b : b1) {
      System.out.println(b);
    }
    reverse(b1);
    for (byte b : b1) {
      System.out.println(b);
    }
  }
}
```

Output:

### Reverses the order of the given long type value array

```java title=Example.java
public class Main {
  public static void reverse(long[] array) {
      if (array == null) {
          return;
      } int i = 0;
      int j = array.length - 1;
      long tmp;
      while (j > i) {
          tmp = array[j];
          array[j] = array[i];
          array[i] = tmp;
          j--;
          i++;
      }
  }
}
```

#### Next chapter...

What you will learn in the next chapter:

- How to remove duplicate element from array
- Remove the element at the specified position from the specified array.
