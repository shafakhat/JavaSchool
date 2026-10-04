---
title: Use Short constructor to convert short primitive type to Short object
nav: Use Short constructor to c...
description: Imported from the java2s.com archive: Use Short constructor to convert short primitive type to Short object
section: Imported - java2s Archive
order: 1140
source: https://web.archive.org/web/20101020202407/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/UseShortconstructortoconvertshortprimitivetypetoShortobject.htm
---
```java title=Example.java
public class Main {
  public static void main(String[] args) {
    short s = 10;
    Short sObj = new Short(s);
    System.out.println(sObj);
  }
}
```
