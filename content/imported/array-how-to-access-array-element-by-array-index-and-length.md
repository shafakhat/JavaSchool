---
title: How to access array element by array index and length
nav: How to access array elemen...
description: Array stores elements and we use index to reference a single value in an array. The starting value of the index is 0. If you try to reference elements with negative numbe
section: Imported - java2s Archive
order: 1023
source: https://web.archive.org/web/20130905071317/http://java2s.com/Tutorials/Java/Array/How_to_access_array_element_by_array_index_and_length.htm
---
In this chapter you will learn:

- How to access array element by index
- How to get the array length

### Array Index

Array stores elements and we use index to reference a single value in an array. The starting value of the index is 0. If you try to reference elements with negative numbers or numbers greater than the array length, you will get a run-time error.

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String args[]) {
int days[] = {31, 28, 31,};
    System.out.println("days[2] is " + days[10]);
  }
}
```

It generates the following error.

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

### Arrays length

Array size, arrayName.length, holds its length. The following code outputs the length of each array by using its length property.

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String args[]) {
    int a1[] = newint[10];
    int a2[] = {1, 2, 3, 4, 5};
    int a3[] = {4, 3, 2, 1};
    System.out.println("length of a1 is " + a1.length);
    System.out.println("length of a2 is " + a2.length);
    System.out.println("length of a3 is " + a3.length);
  }
}
```

This program displays the following output:

#### Next chapter...

What you will learn in the next chapter:

- How is the multidimensional arrays stored
- How to create a three-dimensional array
- What are Jagged array
- How to initialize multidimensional arrays during declaration
