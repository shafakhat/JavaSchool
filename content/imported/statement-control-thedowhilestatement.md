---
title: The do-while Statement
nav: The do-while Statement
description: The do-while statement is like the while statement, except that the associated block always gets executed at least once.
section: Imported - java2s Archive
order: 1169
source: https://web.archive.org/web/20140829092125/http://www.java2s.com/Tutorial/Java/0080__Statement-Control/ThedowhileStatement.htm
---
The do-while statement is like the while statement, except that the associated block always gets executed at least once.
Its syntax is as follows:

```java title=Example.java
do {
    statement (s)
} while (booleanExpression);
```

Just like the while statement, you can omit the braces if there is only one statement within them. However, always use braces for the sake of clarity.

```java title=Example.java
public class MainClass {
  public static void main(String[] args) {
    int i = 0;
    do {
      System.out.println(i);
      i++;
    } while (i < 3);
  }
}
```

This prints the following to the console:

```java title=Example.java
0
1
2
```

The following do-while demonstrates that at least the code in the do block will be executed once even though the initial value of j used to test the expression j < 3 evaluates to false.

```java title=Example.java
public class MainClass {
  public static void main(String[] args) {
    int j = 4;
    do {
        System.out.println(j);
        j++;
    } while (j < 3);
  }
}
```

This prints the following on the console.

```java title=Example.java
4
```
