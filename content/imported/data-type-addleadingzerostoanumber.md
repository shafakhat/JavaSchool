---
title: Add leading zeros to a number
nav: Add leading zeros to a num...
description: System.out.println("Number with leading zeros: " + formatted);
section: Imported - java2s Archive
order: 1010
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Addleadingzerostoanumber.htm
---
```java title=Example.java
publicclass Main {
  publicstaticvoid main(String[] args) {
    int number = 1500;
    String formatted = String.format("%07d", number);
    System.out.println("Number with leading zeros: " + formatted);
  }
}
```
