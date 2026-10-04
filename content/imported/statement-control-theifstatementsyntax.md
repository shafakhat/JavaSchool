---
title: The if statement syntax
nav: The if statement syntax
description: The if statement is a conditional branch statement. The syntax of the if statement is either one of these two:
section: Imported - java2s Archive
order: 1013
source: https://web.archive.org/web/20070525053932/http://www.java2s.com:80/Tutorial/Java/0080__Statement-Control/Theifstatementsyntax.htm
---
The if statement is a conditional branch statement. The syntax of the if statement is either one of these two:

```java title=Example.java
if (booleanExpression) {
    statement (s)
}
```

or

```java title=Example.java
if (booleanExpression) {
    statement (s)
} else {
    statement (s)
}
```

For example, in the following if statement, the if block will be executed if x is greater than 4.

```java title=Example.java
public class MainClass {
  public static void main(String[] args) {
    int x = 9;
    if (x > 4) {
      // statements
    }
  }
}
```

In the following example, the if block will be executed if a is greater than 3. Otherwise, the else block will be executed.

```java title=Example.java
public class MainClass {
  public static void main(String[] args) {
    int a = 3;
    if (a > 3) {
      // statements
    } else {
      // statements
    }
  }
}
```
