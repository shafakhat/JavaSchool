---
title: The numerical for loop
nav: The numerical for loop
description: for (initialization_expression ; loop_condition ; increment_expression) {
section: Imported - java2s Archive
order: 1014
source: https://web.archive.org/web/20070716022406/http://www.java2s.com:80/Tutorial/Java/0080__Statement-Control/Thenumericalforloop.htm
---
```java title=Example.java
for (initialization_expression ; loop_condition ; increment_expression) {
  // statements
}
```

```java title=Example.java
public class MainClass {
  public static void main(String[] args) {
    int limit = 20; // Sum from 1 to this value
    int sum = 0;    // Accumulate sum in this variable
    for (int i = 1; i <= limit; i++) {
      sum = sum + i;
    }
    System.out.println("sum = " + sum);
  }
}
```

```java title=Example.java
sum = 210
```
