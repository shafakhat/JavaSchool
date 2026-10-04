---
title: Java Tutorial - Java Break
nav: Java Tutorial - Java Break
description: When a break statement is encountered inside a loop, the loop is terminated and program control resumes at the next statement following the loop.
section: Imported - java2s Archive
order: 50436
source: https://www.java2s.com/Tutorials/Java/Java_Language/4050__Java_break.html
---
When a break statement is encountered inside a loop, the loop is terminated and program control resumes at the next statement following the loop.

Syntax for break statement

```java title=Example.java
break;
```

or

```java title=Example.java
break labelName;
```

Here is a simple example:

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String args[]) {
    for (int i = 0; i < 100; i++) {
      if (i == 10)
        break; // terminate loop if i is 10
      System.out.println("i: " + i);
    }
    System.out.println("Loop complete.");
  }
}
```

This program generates the following output:

## Example

The break statement can be used with while loop as well. For example, here is the preceding program coded by use of a while loop.

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String args[]) {
    int i = 0;while (i < 100) {
      if (i == 10)
        break; // terminate loop if i is 10
      System.out.println("i: " + i);
      i++;
    }
    System.out.println("Loop complete.");
  }
}
```

The output:

## Example 2

The break statement is useful to exit an infinite loop. In the following while loop the true value is hard coded in, therefore the while loop is an infinite loop. Then it uses an if statement combined with the break statement to exit the whole loop when i is 10.

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String args[]) {
    int i = 0;while (true) {
      if (i == 10){
        break; // terminate loop if i is 10
      }
      System.out.println("i: " + i);
      i++;
    }
    System.out.println("Loop complete.");
  }
}
```

The output:

## Example 3

When used inside a set of nested loops, the break statement will only break out of the inner-most loop. For example:

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String args[]) {
    for (int i = 0; i < 5; i++) {
      System.out.print("Pass " + i + ": ");
      for (int j = 0; j < 100; j++) {
        if (j == 10)
          break; // terminate loop if j is 10
        System.out.print(j + " ");
      }
      System.out.println();
    }
    System.out.println("Loops complete.");
  }
}
```

This program generates the following output:

## Example 4

The break that terminates a switch statement affects only that switch statement and not any enclosing loops.

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String args[]) {
    for (int i = 0; i < 6; i++)
      switch (i) {
        case 1:
          System.out.println("i is one.");
          for (int j = 0; j < 5; j++) {
            System.out.println("j is " + j);
          }
          break;
        case 2:
          System.out.println("i is two.");
          break;
        default:
          System.out.println("i is greater than 3.");
      }
  }
}
```

The output:

From the result we can see that the break statement only exit the switch statement.

## Example 5

We can specify a label for break statement and let the code logic exit to that point. The following code uses the label to make break statement exit two layers of the nested for loop.

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String args[]) {
    outer: for (int i = 0; i < 10; i++) {
      for (int j = 0; j < 10; j++) {
        if (j + 1 < i) {
          System.out.println();continue outer;
        }
        System.out.print(" " + (i * j));
      }
    }
    System.out.println();
  }
}
```

The output:

- « Previous
