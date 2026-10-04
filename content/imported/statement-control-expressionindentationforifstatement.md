---
title: Expression indentation for if statement
nav: Expression indentation for...
description: If the expression is too long, you can use two units of indentation for subsequent lines.
section: Imported - java2s Archive
order: 1003
source: https://web.archive.org/web/20070714011448/http://www.java2s.com:80/Tutorial/Java/0080__Statement-Control/Expressionindentationforifstatement.htm
---
If the expression is too long, you can use two units of indentation for subsequent lines.

```java title=Example.java
public class MainClass {
  public static void main(String[] args) {
    int numberOfLoginAttempts = 10;
    int numberOfMinimumLoginAttempts = 12;
    int numberOfMaximumLoginAttempts = 13;
    int y = 3;
    if (numberOfLoginAttempts < numberOfMaximumLoginAttempts
        || numberOfMinimumLoginAttempts > y) {
      y++;
    }
  }
}
```
