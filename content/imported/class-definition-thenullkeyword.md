---
title: The null Keyword
nav: The null Keyword
description: You can test if a reference variable is null by using the == operator. For instance.
section: Imported - java2s Archive
order: 1221
source: https://web.archive.org/web/2016/http://www.java2s.com:80/Tutorial/Java/0100__Class-Definition/ThenullKeyword.htm
---
You can test if a reference variable is null by using the == operator. For instance.

```java title=Example.java
public class MainClass {
  public static void main(String[] args) {
    String book = null;
    if (book == null) {
        book = new String();
    }
  }
}
```

5.21.1.  The null Keyword
