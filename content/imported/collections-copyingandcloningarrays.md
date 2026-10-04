---
title: Copying and Cloning Arrays
nav: Copying and Cloning Arrays
description: System.out.println("New size: " + doubleArray(array1).length);
section: Imported - java2s Archive
order: 2479
source: https://web.archive.org/web/20140829083516/http://www.java2s.com/Tutorial/Java/0140__Collections/CopyingandCloningArrays.htm
---
```java title=Example.java
public class MainClass {
  public static void main (String args[]) {
    int array1[] = {1, 2, 3, 4, 5};
    int array2[] = {1, 2, 3, 4, 5, 6, 7, 8, 9};
    System.out.println("Original size: " + array1.length);
    System.out.println("New size: " + doubleArray(array1).length);
    System.out.println("Original size: " + array2.length);
    System.out.println("New size: " + doubleArray(array2).length);
  }
  static int[] doubleArray(int original[]) {
    int length = original.length;
    int newArray[] = new int[length*2];
    System.arraycopy(original, 0, newArray, 0, length);
    return newArray;
  }
}
java title=Example.java
Original size: 5
New size: 10
Original size: 9
New size: 18
```

| 9.5.1. | use Arrays.copyOf to copy array |
|---|---|
| 9.5.2. | Copying and Cloning Arrays |
| 9.5.3. | Doubling the size of an array |
| 9.5.4. | Array clone |
| 9.5.5. | Copy some items of an array into another array |
| 9.5.6. | Using Arrays.copyOf to copy an array |
| 9.5.7. | Copies the given array and adds the given element at the end of the new array. (long value type) |
