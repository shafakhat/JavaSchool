---
title: You don't have to place class variable declarations at the beginning of a class.
nav: You don't have to place cl...
description: Imported from the java2s.com archive: You don't have to place class variable declarations at the beginning of a class.
section: Imported - java2s Archive
order: 1008
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0020__Language/Youdonthavetoplaceclassvariabledeclarationsatthebeginningofaclass.htm
---
```java title=Example.java
publicclass MainClass
{
    publicstaticvoid main(String[] args)
    {
        helloMessage = "Hello, World!";
        System.out.println(helloMessage);
    }
    static String helloMessage;
}
```
