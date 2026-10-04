---
title: How to Copy Java array faster
nav: How to Copy Java array fas...
description: Java System class has a method we can use to copy array faster.
section: Imported - java2s Archive
order: 1125
source: https://web.archive.org/web/2018/http://java2s.com/Tutorials/Java/Array/How_to_Copy_Java_array_faster.htm
---
In this chapter you will learn:

- Copy array
- Copy array

### Copy array

Java System class has a method we can use to copy array faster.

static void arraycopy(Object src, int srcPos, Object dest, int destPos, int length) Copies an array from the specified source array, beginning at the specified position, to the specified position of the destination array.

The arraycopy( ) method can be used to copy quickly an array of any type from one place to another.

```java title=Example.java
public class Main {
  static byte a[] = {65, 66, 67, 68, 69, 70, 71, 72, 73, 74};
  static byte b[] = {77, 77, 77, 77, 77, 77, 77, 77, 77, 77};
public static void main(String args[]) {
    System.out.println("a = " + new String(a));
    System.out.println("b = " + new String(b));
    System.arraycopy(a, 0, b, 0, a.length);
    System.out.println("a = " + new String(a));
    System.out.println("b = " + new String(b));
    System.arraycopy(a, 0, a, 1, a.length - 1);
    System.arraycopy(b, 1, b, 0, b.length - 1);
    System.out.println("a = " + new String(a));
    System.out.println("b = " + new String(b));
  }
}
```

The output:

### Copy array

```java title=Example.java
import java.util.Arrays;
public class Main
{
    public static void main(String args[])
    {
        int arrayOriginal[] = {42, 55, 21};
        int arrayNew[] = Arrays.copyOf(arrayOriginal, 3);
        printIntArray(arrayNew);
    }
    static void printIntArray(int arrayNew[])
    {
        for (int i : arrayNew)
        {
            System.out.print(i);
            System.out.print(' ');
        }
        System.out.println();
    }
}
```

#### Next chapter...

What you will learn in the next chapter:

- Compare two arrays
- Compare two two-dimensional array
- Compare two arrays by reference
