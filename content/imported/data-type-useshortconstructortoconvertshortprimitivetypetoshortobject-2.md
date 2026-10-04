---
title: Use Short constructor to convert short primitive type to Short object
nav: Use Short constructor to c...
description: Imported from the java2s.com archive: Use Short constructor to convert short primitive type to Short object
section: Imported - java2s Archive
order: 1041
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/UseShortconstructortoconvertshortprimitivetypetoShortobject.htm
---
```java title=Example.java
publicclass Main {
  publicstaticvoid main(String[] args) {
    short s = 10;
    Short sObj = new Short(s);
    System.out.println(sObj);
  }
}
```
