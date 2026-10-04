---
title: Appending Basic Types
nav: Appending Basic Types
description: Imported from the java2s.com archive: Appending Basic Types
section: Imported - java2s Archive
order: 1005
source: https://web.archive.org/web/20070329215747/http://www.java2s.com:80/Tutorial/Java/0120__Development/AppendingBasicTypeslongdouble.htm
---
```java title=Example.java
public class MainClass {
  public static void main(String[] arg) {
    StringBuffer buf = new StringBuffer("The number is ");
    long number = 999;
    buf.append(number);
    buf.append(12.34);
    System.out.println(buf);
  }
}
```

```java title=Example.java
The number is 99912.34
```
