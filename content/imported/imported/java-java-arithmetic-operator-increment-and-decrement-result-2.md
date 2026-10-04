---
title: Java Arithmetic Operator increment and decrement result 2
nav: Java Arithmetic Operator i...
description: The prefixed operator causes the value of the x variable to be changed before the expression is evaluated.
section: Imported - java2s Archive
order: 1075
source: https://web.archive.org/web/20210102113217/http://www.java2s.com/ref/java/java-arithmetic-operator-increment-and-decrement-result-2.html
---
## Question

What is the output of the following code?

```java title=Example.java
int x = 3;
int answer = ++x * 10;
```

```java title=Example.java
40
```

## Note

The prefixed operator causes the value of the x variable to be changed before the expression is evaluated.

The statement int?answer = ++x * 10 does the same thing, in order, as these statements:

```java title=Example.java

x++;
int answer = x * 10;
```

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String args[]) {
    int x = 3;//www.java2s.comint answer = ++x * 10;
    System.out.println(answer);

  }
}
```

PreviousNext

## Related

- Java Arithmetic Operator divisible by 3
- Java Arithmetic Operator find the number of years
- Java Arithmetic Operator increment and decrement result 1
- Java Arithmetic Operator Integer division
- Java Arithmetic Operator Question 1
