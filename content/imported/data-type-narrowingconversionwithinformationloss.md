---
title: Narrowing conversion with information loss
nav: Narrowing conversion with ...
description: Narrowing conversion may incur information loss, if the converted value is larger than the capacity of the target type.
section: Imported - java2s Archive
order: 1078
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Narrowingconversionwithinformationloss.htm
---
Narrowing conversion may incur information loss, if the converted value is larger than the capacity of the target type.

In the following conversion, there is some information loss because 9876543210L is too big for an int.

```java title=Example.java
public class MainClass {
  public static void main(String[] args) {
    long a = 9876543210L;
    int b = (int) a;
    System.out.println(b);
  }
}
java title=Example.java
1286608618
```
