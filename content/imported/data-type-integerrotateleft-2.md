---
title: Integer
nav: Integer
description: Imported from the java2s.com archive: Integer
section: Imported - java2s Archive
order: 1135
source: https://web.archive.org/web/20070319212133/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/IntegerrotateLeft.htm
---
```java title=Example.java
public class MainClass {
  public static void main(String args[]) {
    int n = 1;
    for (int i = 0; i < 16; i++) {
      n = Integer.rotateLeft(n, 1);
      System.out.println(n);
    }
  }
}
```

```java title=Example.java

2
4
8
16
32
64
128
256
512
1024
2048
4096
8192
16384
32768
65536
```
