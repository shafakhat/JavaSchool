---
title: For statement in detail
nav: For statement in detail
description: It is common to declare a variable and assign a value to it in the initialization part. The variable declared will be visible to the expression and update parts as well a
section: Imported - java2s Archive
order: 1004
source: https://web.archive.org/web/20070612200430/http://www.java2s.com:80/Tutorial/Java/0080__Statement-Control/Forstatementindetail.htm
---
It is common to declare a variable and assign a value to it in the initialization part. The variable declared will be visible to the expression and update parts as well as to the statement block.

For example, the following for statement loops five times and each time prints the value of i. Note that the variable i is not visible anywhere else since it is declared within the for loop.

```java title=Example.java
public class MainClass {
  public static void main(String[] args) {
    for (int i = 0; i < 5; i++) {
        System.out.println(i + " ");
    }
  }
}
```

The initialization part of the for statement is optional.

```java title=Example.java
public class MainClass {
  public static void main(String[] args) {
    int j = 0;
    for (; j < 3; j++) {
      System.out.println(j);
    }
    // j is visible here
  }
}
```

The update statement is optional.

```java title=Example.java
public class MainClass {
  public static void main(String[] args) {
    int k = 0;
    for (; k < 3;) {
      System.out.println(k);
      k++;
    }
  }
}
```

You can even omit the booleanExpression part.

```java title=Example.java
public class MainClass {
  public static void main(String[] args) {
    int m = 0;
    for (;;) {
      System.out.println(m);
      m++;
      if (m > 4) {
        break;
      }
    }
  }
}
```

If you compare for and while, you'll see that you can always replace the while statement with for. This is to say that

```java title=Example.java
while (expression) {
    ...
}
can always be written as
for ( ; expression; ) {
    ...
}
```
