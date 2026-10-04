---
title: initialization_expression
nav: initialization_expression
description: Imported from the java2s.com archive: initialization_expression
section: Imported - java2s Archive
order: 1005
source: https://web.archive.org/web/20070716023453/http://www.java2s.com:80/Tutorial/Java/0080__Statement-Control/initializationexpressiondefinetwovariablesinforloop.htm
---
```java title=Example.java
public class MainClass {
  public static void main(String[] arg) {
    int limit = 10;
    int sum = 0;
    for (int i = 1, j = 0; i <= limit; i++, j++) {
      sum += i * j;
    }
    System.out.println(sum);
  }
}
```

```java title=Example.java
330
```
