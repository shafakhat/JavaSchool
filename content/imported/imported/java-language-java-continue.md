---
title: Java Tutorial - Java Continue
nav: Java Tutorial - Java Conti...
description: continue statement forces an early iteration of a loop. In while and do-while loops, a continue statement causes control to be transferred to the conditional expression t
section: Imported - java2s Archive
order: 50437
source: https://www.java2s.com/Tutorials/Java/Java_Language/4060__Java_Continue.html
---
```java title=Example.java
« Previous
```

- Next »

continue statement forces an early iteration of a loop. In while and do-while loops, a continue statement causes control to be transferred to the conditional expression that controls the loop. In a for loop, control goes first to the iteration portion of the for statement and then to the conditional expression.

## Java continue statement

Syntax for Java continue statement

```java title=Example.java
continue;
```

or

```java title=Example.java
continue labelName;
```

The following code shows how to use a continue statement.

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String[] argv) {
    for (int i = 0; i < 10; i++) {
      System.out.print(i + " ");
      if (i % 2 == 0)
        continue;
      System.out.println("");
    }/*www.java2s.com*/
  }
}
```

The code above generates the following result.

## Example

continue may specify a label to describe which enclosing loop to continue.

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String args[]) {
    outer: for (int i = 0; i < 10; i++) {
      for (int j = 0; j < 10; j++) {
        if (j > i) {
          System.out.println();/*www.java2s.com*/continue outer;
        }
        System.out.print(" " + (i * j));
      }
    }
    System.out.println();
  }
}
```

Here is the output of this program:

## Example 2

The following code shows how to use labeled while loop.

```java title=Example.java
//www.java2s.compublicclass Main {
  publicstaticvoid main(String[] args) {
    int i = 0;
    outer: while (true) {
      System.out.println("Outer while loop");
      while (true) {
        i++;
        System.out.println("i = " + i);
        if (i == 1) {
          System.out.println("continue");
          continue;
        }
        if (i == 3) {
          System.out.println("continue outer");
          continue outer;
        }
        if (i == 5) {
          System.out.println("break");
          break;
        }
        if (i == 7) {
          System.out.println("break outer");
          break outer;
        }
      }
    }
  }
}
```

The code above generates the following result.

## Example 3

The following code shows how to calculate Primes with continue statement and label.

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String[] args) {
    int nValues = 50;
//fromwww.java2s.com
    OuterLoop: for (int i = 2; i <= nValues; i++) {
      for (int j = 2; j < i; j++) {
        if (i % j == 0) {
          continue OuterLoop;
        }
      }
      System.out.println(i);
    }
  }
}
```

The code above generates the following result.

## Example 4

The following code shows how to use Labeled continue statement to calculate factorial numbers.

```java title=Example.java
/*www.java2s.com*/publicclass Main {
  publicstaticvoid main(String[] args) {
    int limit = 20;
    int factorial = 1;
    OuterLoop: for (int i = 1; i <= limit; i++) {
      factorial = 1;
      for (int j = 2; j <= i; j++) {
        if (i > 10 && i % 2 == 1) {
          continue OuterLoop;
        }
        factorial *= j;
      }
      System.out.println(i + "! is " + factorial);
    }
  }
}
```

The code above generates the following result.

- Next »
- « Previous
