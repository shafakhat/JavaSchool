---
title: Java Array find array element above average
nav: Java Array find array elem...
description: The problem is to write a program that finds the number of items above the average of all items.
section: Imported - java2s Archive
order: 1107
source: https://web.archive.org/web/20210102113249/http://www.java2s.com/ref/java/java-array-find-array-element-above-average.html
---
## Question

The problem is to write a program that finds the number of items above the average of all items.

- read 100 numbers
- get the average of these numbers
- find the number of the items greater than the average.
- let the user enter the number of input

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String[] args) {
    java.util.Scanner input = new java.util.Scanner(System.in);
    System.out.print("Enter the number of items: ");
    int n = input.nextInt();
    double[] numbers = newdouble[n];
    double sum = 0;

    //your code here
  }/*fromwww.java2s.com*/
}
```

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String[] args) {
    java.util.Scanner input = new java.util.Scanner(System.in);
    System.out.print("Enter the number of items: ");
    int n = input.nextInt();
    double[] numbers = newdouble[n];
    double sum = 0;

    System.out.print("Enter the numbers: ");
    for (int i = 0; i < n; i++) {
      numbers[i] = input.nextDouble();
      sum += numbers[i];
    }

    double average = sum / n;

    int count = 0; // The numbers of elements above averagefor (int i = 0; i < n; i++)
      if (numbers[i] > average)
        count++;

    System.out.println("Average is " + average);
    System.out.println("Number of elements above the average is "
      + count);
  }
}
```

PreviousNext

## Related

- Java Array as frequency counters
- Java Array count occurrences of letter in char array
- Java Array display arrays
- Java Array find the largest element
- Java Array find the smallest index of the largest element
