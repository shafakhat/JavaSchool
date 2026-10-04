---
title: Using braces makes your 'if' statement clearer
nav: Using braces makes your 'i...
description: If there is only one statement in an if or else block, the braces are optional.
section: Imported - java2s Archive
order: 1017
source: https://web.archive.org/web/20070714012641/http://www.java2s.com:80/Tutorial/Java/0080__Statement-Control/Usingbracesmakesyourifstatementclearer.htm
---
If there is only one statement in an if or else block, the braces are optional.

```java title=Example.java
public class MainClass {
  public static void main(String[] args) {
    int a = 3;
    if (a > 3)
      a++;
    else
      a = 3;
  }
}
```

Consider the following example:

```java title=Example.java
public class MainClass {
  public static void main(String[] args) {
    int a = 3, b = 1;
    if (a > 0 || b < 5)
      if (a > 2)
        System.out.println("a > 2");
      else
        System.out.println("a < 2");
  }
}
```

- It is hard to tell which if statement the else statement is associated with.
- Actually, An else statement is always associated with the immediately preceding if.

Using braces makes your code clearer.

```java title=Example.java
public class MainClass {
  public static void main(String[] args) {
    int a = 3, b = 1;
    if (a > 0 || b < 5) {
      if (a > 2) {
        System.out.println("a > 2");
      } else {
        System.out.println("a < 2");
      }
    }
  }
}
```
