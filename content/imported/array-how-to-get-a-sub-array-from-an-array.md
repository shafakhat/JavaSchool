---
title: How to get a sub array from an array
nav: How to get a sub array fro...
description: public static int[] get(int[] array, int offset, int length) {
section: Imported - java2s Archive
order: 1131
source: https://web.archive.org/web/2018/http://java2s.com/Tutorials/Java/Array/How_to_get_a_sub_array_from_an_array.htm
---
In this chapter you will learn:

- Subarray from array that starts at offset

### Subarray from array that starts at offset

```java title=Example.java
import java.util.Arrays;
public class Main {
public static void main(String[] argv){
  int[] intArray = new int[]{1,2,3,4,5,6,7,8};
  int[] intSubArray = get(intArray,3,2);
  System.out.println(Arrays.toString(intSubArray));
}
  public static int[] get(int[] array, int offset, int length) {
    int[] result = new int[length];
    System.arraycopy(array, offset, result, 0, length);
    return result;
  }
}
```

The code above generates the following result.

#### Next chapter...

What you will learn in the next chapter:

- Get array upperbound
- Get the number of dimensions
