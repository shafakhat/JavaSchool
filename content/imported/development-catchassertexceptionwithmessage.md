---
title: Catch assert exception with message
nav: Catch assert exception wit...
description: Imported from the java2s.com archive: Catch assert exception with message
section: Imported - java2s Archive
order: 1013
source: https://web.archive.org/web/20110418062656/http://www.java2s.com:80/Tutorial/Java/0120__Development/Catchassertexceptionwithmessage.htm
---
```java title=Example.java
public class Main {
  public static void main(String[] argv) throws Exception {
    try {
      assert argv.length > 0 : "my message";
    } catch (AssertionError e) {
      String message = e.getMessage();
      System.out.println(message);
    }
  }
}
```
