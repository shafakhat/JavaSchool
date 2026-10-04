---
title: Array Reallocation
nav: Array Reallocation
description: You can make a clone of an array and make the new array have a different size.
section: Imported - java2s Archive
order: 2301
source: https://web.archive.org/web/20140829091428/http://www.java2s.com/Tutorial/Java/0140__Collections/ArrayReallocation.htm
---
You can make a clone of an array and make the new array have a different size.

```java title=Example.java
public static boolean[] copyOf (boolean[] original, int newLength)
public static byte[] copyOf (byte[] original, int newLength)
public static char[] copyOf (char[] original, int newLength)
public static double[] copyOf (double[] original, int newLength)
public static float [] copyOf (float[] original, int newLength)
public static int[] copyOf (int[] original, int newLength)
public static long[] copyOf (long[] original, int newLength)
public static short[] copyOf (short[] original, int newLength)
public static <T> T[] copyOf (T[] original, int newLength)
public static <T,U> T[] copyOf (U[] original, int newLength,java.lang.Class<? extends T[]> newType)
```

| The last method allows you to upcast each element in the original array to a parent type. |
|---|
| Another method similar to copyOf that is also added to Arrays in Java 6 is copyOfRange. |
| copyOfRange copies a range of elements to a new array. |
| Like copyOf, copyOfRange also provides overrides for each Java data type. |
| Here are their signatures: |

```java title=Example.java
public static boolean[] copyOfRange (boolean[] original,int from, int to)
public static byte[] copyOfRange (byte[] original,int from, int to)
public static char[] copyOfRange (char[] original,int from, int to)
public static double[] copyOfRange (double[] original,int from, int to)
public static float[] copyOfRange (float[] original,int from, int to)
public static int[] copyOfRange (int[] original, int from, int to)
public static long[] copyOfRange (long[] original, int from, int to)
public static short[] copyOfRange (short[] original, int from, int to)
public static <T> T[] copyOfRange (T[] original, int from, int to)
public static <T,U> T[] copyOfRange (U[] original, int from,int to, java.lang.Class<? extends T[]> newType)
```

Array reallocation example

```java title=Example.java
import java.util.Arrays;
public class ArrayReallocationDemo {
  public static void main(String[] args) {
    int[] data1 = new int[] { 1, 3, 5, 7, 9 };
    printArray(data1);
    int[] data2 = Arrays.copyOf(data1, 6);
    data2[5] = 11;
    printArray(data2);
    int[] data3 = Arrays.copyOfRange(data1, 2, 10);
    printArray(data3);
  }
  // print array elements
  private static void printArray(int[] data) {
    StringBuilder stringBuilder = new StringBuilder("[");
    for (int i = 0; i < data.length; i++) {
      stringBuilder.append(data[i]);
      if (i < data.length - 1)
        stringBuilder.append(", ");
    }
    stringBuilder.append("]");
    System.out.println(stringBuilder);
  }
}
java title=Example.java
[1, 3, 5, 7, 9]
[1, 3, 5, 7, 9, 11]
[5, 7, 9, 0, 0, 0, 0, 0]
```

| 9.3.1. | How to define an Array |
|---|---|
| 9.3.2. | Initializing array elements by index |
| 9.3.3. | Alternative Array Declaration Syntax |
| 9.3.4. | Anonymous arrays are declared similarly to regular arrays |
| 9.3.5. | An array is a Java object |
| 9.3.6. | To reference the components of an array |
| 9.3.7. | The Length of an Array |
| 9.3.8. | Initializing Arrays |
| 9.3.9. | Using a for loop to iterate over all the elements and set the values |
| 9.3.10. | Arrays of Characters |
| 9.3.11. | Using the Collection-Based for Loop with an Array |
| 9.3.12. | Changing Array Size |
| 9.3.13. | Array Reallocation |
| 9.3.14. | Use System.arraycopy to duplicate array |
| 9.3.15. | Minimum and maximum number in array |
| 9.3.16. | Shuffle elements of an array |
| 9.3.17. | Merge (or add) two arrays into one |
| 9.3.18. | Circular Buffer |
