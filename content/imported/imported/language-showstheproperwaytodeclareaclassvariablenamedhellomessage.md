---
title: shows the proper way to declare a class variable named helloMessage
nav: shows the proper way to de...
description: Imported from the java2s.com archive: shows the proper way to declare a class variable named helloMessage
section: Imported - java2s Archive
order: 1006
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0020__Language/showstheproperwaytodeclareaclassvariablenamedhelloMessage.htm
---
```java title=Example.java
publicclass MainClass
{
    static String helloMessage;

    publicstaticvoid main(String[] args)
    {
        helloMessage = "Hello, World!";
        System.out.println(helloMessage);
    }
}
```
