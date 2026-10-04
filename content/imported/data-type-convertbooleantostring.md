---
title: Convert Boolean to String
nav: Convert Boolean to String
description: Imported from the java2s.com archive: Convert Boolean to String
section: Imported - java2s Archive
order: 1013
source: https://web.archive.org/web/2018/http://www.java2s.com/Tutorial/Java/0040__Data-Type/ConvertBooleantoString.htm
---
```java title=Example.java
public class Main {
    public static void main(String[] args) {
        boolean theValue = true;
        //boolean to String conversion
        String theValueAsString = new Boolean(theValue).toString();
        System.out.println(theValueAsString);
    }
}
//true
```
