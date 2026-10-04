---
title: Obtaining the Characters in a String as an Array of Bytes
nav: Obtaining the Characters i...
description: String text = "To be or not to be"; // Define a string
section: Imported - java2s Archive
order: 1161
source: https://web.archive.org/web/20070420005516/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/ObtainingtheCharactersinaStringasanArrayofBytes.htm
---
```java title=Example.java
public class MainClass {
  public static void main(String[] arg) {
    String text = "To be or not to be";        // Define a string
    byte[] textArray = text.getBytes();
    for(byte b: textArray){
      System.out.println(b);
    }
  }
}
```

```java title=Example.java

84
111
32
98
101
32
111
114
32
110
111
116
32
116
111
32
98
101
```
