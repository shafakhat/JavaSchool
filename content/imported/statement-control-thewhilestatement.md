---
title: The while Statement
nav: The while Statement
description: One way to create a loop is by using the while statement. Another way is to use the for statement
section: Imported - java2s Archive
order: 1176
source: https://web.archive.org/web/20140829081628/http://www.java2s.com/Tutorial/Java/0080__Statement-Control/ThewhileStatement.htm
---
One way to create a loop is by using the while statement. Another way is to use the for statement
The while statement has the following syntax.

```java title=Example.java
while (booleanExpression) {
    statement (s)
}
```

statement(s) will be executed as long as booleanExpression evaluates to true. If there is only a single statement inside the braces, you may omit the braces. For clarity, you should always use braces even when there is only one statement.
As an example of the while statement, the following code prints integer numbers that are less than three.

```java title=Example.java
public class MainClass {
  public static void main(String[] args) {
    int i = 0;
    while (i < 3) {
      System.out.println(i);
      i++;
    }
  }
}
```

To produce three beeps with an interval of 500 milliseconds, use this code:

```java title=Example.java
public class MainClass {
  public static void main(String[] args) {
    int j = 0;
    while (j < 3) {
      java.awt.Toolkit.getDefaultToolkit().beep();
      try {
        Thread.currentThread().sleep(500);
      } catch (Exception e) {
      }
      j++;
    }
  }
}
```

Sometimes, you use an expression that always evaluates to true (such as the boolean literal true) but relies on the break statement to escape from the loop.

```java title=Example.java
public class MainClass {
  public static void main(String[] args) {
    int k = 0;
    while (true) {
      System.out.println(k);
      k++;
      if (k > 2) {
        break;
      }
    }
  }
}
```
