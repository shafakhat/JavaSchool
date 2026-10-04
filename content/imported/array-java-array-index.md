---
title: Java Array Index
nav: Java Array Index
description: We refer to the first element of the myIntArray array as myIntArray[0], and we reference the fifth element in the array as myIntArray[4].
section: Imported - java2s Archive
order: 1035
source: https://web.archive.org/web/20131221124759/http://www.java2s.com:80/Tutorials/Java/Array/Java_Array_Index.htm
---
In this chapter you will learn:

- Description for Java Array Index
- Example - ArrayIndexOutOfBoundsException
- Example - How to access array element by index

### Description

The Java array index starts at 0 or 1.

We refer to the first element of the myIntArray array as myIntArray[0], and we reference the fifth element in the array as myIntArray[4].

The maximum index value for an array is one less than the number of elements in the array.

Java checks that the index values you use are valid. If you use an index value that is less than 0, or greater than the index value for the last element in the array, an exception is thrown.

### Example

Array stores elements and we use index to reference a single value in an array. The starting value of the index is 0. If you try to reference elements with negative numbers or numbers greater than the array length, you will get a run-time error.

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String args[]) {
int days[] = {1, 2, 3,};
    System.out.println("days[2] is " + days[10]);
  }
}
```

It generates the following error.

### Example 2

We usually use a for loop to access each element in an array. The following code uses a one-dimensional array to find the average of a set of numbers.

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String args[]) {
    double nums[] = {10.1, 11.2, 12.3, 13.4, 14.5};
    double result = 0;
    int i;for (i = 0; i < 5; i++)
      result = result + nums[i];
    System.out.println("Average is " + result / 5);
  }
}
```

The output:

#### Next chapter...

What you will learn in the next chapter:

- How to use for each loop with Java array
- Syntax for array for each loop
- Example - Java array for each loop
