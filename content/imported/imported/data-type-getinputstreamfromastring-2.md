---
title: Get InputStream from a String
nav: Get InputStream from a Str...
description: Imported from the java2s.com archive: Get InputStream from a String
section: Imported - java2s Archive
order: 1016
source: https://web.archive.org/web/20100713111353/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/GetInputStreamfromaString.htm
---
```java title=Example.java
import java.io.ByteArrayInputStream;
public class Main {
  public static void main(String[] argv) throws Exception {
    byte[] bytes = "asdf".getBytes("UTF8");
    new ByteArrayInputStream(bytes);
  }
}
```
