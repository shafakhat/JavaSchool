---
title: Convert byte[ ] array to String
nav: Convert byte[ ] array to S...
description: Imported from the java2s.com archive: Convert byte[ ] array to String
section: Imported - java2s Archive
order: 1028
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/ConvertbytearraytoString.htm
---
```java title=Example.java
public class Main {
    public static void main(String[] args) {
        byte[] byteArray = new byte[] {87, 79, 87, 46, 46, 46};
        String value = new String(byteArray);
        System.out.println(value);
    }
}
//WOW...
```
