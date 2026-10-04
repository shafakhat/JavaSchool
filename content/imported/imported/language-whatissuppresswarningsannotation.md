---
title: What is SuppressWarnings annotation?
nav: What is SuppressWarnings a...
description: Imported from the java2s.com archive: What is SuppressWarnings annotation?
section: Imported - java2s Archive
order: 1018
source: https://web.archive.org/web/20090901173712/http://www.java2s.com:80/Tutorial/Java/0020__Language/WhatisSuppressWarningsannotation.htm
---
```java title=Example.java
import java.util.Date;
public class Main {
    @SuppressWarnings(value={"deprecation"})
    public static void main(String[] args) {
        Date date = new Date(2009, 9, 30);
        System.out.println("date = " + date);
    }
}
```
