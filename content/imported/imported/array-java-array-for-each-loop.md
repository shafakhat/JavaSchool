---
title: Java Array for each loop
nav: Java Array for each loop
description: We can use a collection-based for loop as an alternative to the numerical for loop when processing the values of all the elements in an array.
section: Imported - java2s Archive
order: 1034
source: https://web.archive.org/web/20131221124810/http://www.java2s.com:80/Tutorials/Java/Array/Java_Array_for_each_loop.htm
---
In this chapter you will learn:

- How to use for each loop with Java array
- Syntax for array for each loop
- Example - Java array for each loop

### Description

We can use a collection-based for loop as an alternative to the numerical for loop when processing the values of all the elements in an array.

### Syntax

The syntax of for each loop for an array is as follows.

```java title=Example.java
for(arrayType variableName: array){
  process each variableName
}
```

### Example

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String args[]) {
    int days[] = {1, 2, 3,};
    for(int i:days){
      System.out.println(i);/*fromjava2s.com*/
    }
  }
}
```

The code above generates the following result.

#### Next chapter...

What you will learn in the next chapter:

- How is the multidimensional arrays stored
- Syntax for Java Multidimensional Arrays
- Example - Java Multidimensional Arrays
- Example - How to create a three-dimensional array
- What are Jagged array
- Example - Jagged array
- How to initialize multidimensional arrays during declaration
