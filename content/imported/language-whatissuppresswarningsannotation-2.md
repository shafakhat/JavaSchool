---
title: What is SuppressWarnings annotation?
nav: What is SuppressWarnings a...
description: Imported from the java2s.com archive: What is SuppressWarnings annotation?
section: Imported - java2s Archive
order: 1008
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0020__Language/WhatisSuppressWarningsannotation.htm
---
```java title=Example.java
import java.util.Date;
publicclass Main {
    @SuppressWarnings(value={"deprecation"})
    publicstaticvoid main(String[] args) {
        Date date = new Date(2009, 9, 30);
        System.out.println("date = " + date);
    }
}
```
