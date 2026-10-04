---
title: Arrays are automatically cloneable
nav: Arrays are automatically c...
description: Imported from the java2s.com archive: Arrays are automatically cloneable
section: Imported - java2s Archive
order: 1003
source: https://web.archive.org/web/20101107122917/http://www.java2s.com:80/Tutorial/Java/0100__Class-Definition/Arraysareautomaticallycloneable.htm
---
```java title=Example.java
public class Main {
  public static void main(String[] argv) throws Exception {
    int[] ints = new int[] { 123, 234 };
    int[] intsClone = (int[]) ints.clone();
  }
}
```
