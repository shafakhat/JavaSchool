---
title: Array copy method
nav: Array copy method
description: Copy the content of an array (source) to another array (destination), beginning at the specified position, to the specified position of the destination array.
section: Imported - java2s Archive
order: 1007
source: https://web.archive.org/web/20070716073548/http://www.java2s.com:80/Tutorial/Java/0120__Development/Arraycopymethod.htm
---
Copy the content of an array (source) to another array (destination), beginning at the specified position, to the specified position of the destination array.

```java title=Example.java
public static void arraycopy (Object source, int sourcePos, Object destination, int destPos, int length)
```

For example, the following code uses arraycopy to copy the contents of array1 to array2.

```java title=Example.java
public class MainClass {
  public static void main(String[] a) {
    int[] array1 = { 1, 2, 3, 4 };
    int[] array2 = new int[array1.length];
    System.arraycopy(array1, 0, array2, 0, array1.length);
    for(int i: array2){
      System.out.println(i);
    }
  }
}
java title=Example.java
1
2
3
4
```
