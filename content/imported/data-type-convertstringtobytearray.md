---
title: Convert String to byte array
nav: Convert String to byte array
description: Imported from the java2s.com archive: Convert String to byte array
section: Imported - java2s Archive
order: 1014
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/ConvertStringtobytearray.htm
---
```java title=Example.java
publicclass Main {
    publicstaticvoid main(String[] args) {
        String stringToConvert = "this is a test";
        byte[] theByteArray = stringToConvert.getBytes();
        System.out.println(theByteArray.length);
    }
}
//14
```
