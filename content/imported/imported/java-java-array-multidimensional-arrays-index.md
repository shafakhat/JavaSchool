---
title: Java Array multidimensional Arrays index
nav: Java Array multidimensiona...
description: int sum = 0;/*fromwww.java2s.com*/for (int i = 0; i < array.length; i++)
section: Imported
order: 20002
source: http://www.java2s.com/ref/java/java-array-multidimensional-arrays-index.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Question

What is the output of the following code?

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String[] args) {
    int[][] array = { { 1, 2, 3, 4 },
                      { 5, 6, 7, 8 } /*www.java2s.com*/
                    };
    System.out.println(m1(array)[0]);
    System.out.println(m1(array)[1]);
  }

  publicstaticint[] m1(int[][] m) {
    int[] result = newint[2];
    result[0] = m.length;
    result[1] = m[0].length;
    return result;
  }
}
```

```java title=Example.java
2
4
```

## Question

What is the output of the following code?

```java title=Example.java
 Code:
 publicclass Main {
                                   //www.java2s.compublicstaticvoid main(String[] args) {
     int[][] array = { { 1, 2 }, { 3, 4 }, { 5, 6 } };
     for (int i = array.length - 1; i >= 0; i--) {
       for (int j = array[i].length - 1; j >= 0; j--)
         System.out.print(array[i][j] + " ");
       System.out.println();
     }
   }
 }
```

```java title=Example.java
6 5
4 3
2 1
```

## Question

What is the output of the following code?

```java title=Example.java
publicclass Main {

  publicstaticvoid main(String[] args) {
    int[][] array = { { 1, 2 }, { 3, 4 }, { 5, 6 } };
    int sum = 0;/*fromwww.java2s.com*/for (int i = 0; i < array.length; i++)
      sum += array[i][0];
    System.out.println(sum);
  }
}
```

```java title=Example.java
9
```

PreviousNext

## Related

- Java Array multidimensional Arrays declaration
- Java Array multidimensional Arrays initialize arrays with input values.
- Java Array multidimensional Arrays initialize arrays with random values
- Java Array multidimensional Arrays get the largest sum
- Java Array multidimensional Arrays print array
