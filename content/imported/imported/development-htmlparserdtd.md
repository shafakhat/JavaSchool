---
title: html parser DTD
nav: html parser DTD
description: Imported from java2s.com: html parser DTD
section: Imported
order: 20050
source: http://www.java2s.com:80/Tutorial/Java/0120__Development/htmlparserDTD.htm
---
```java title=Example.java
import java.io.IOException;
import javax.swing.text.html.parser.DTD;
public class MainClass {
  public static void main(String[] args) {
    try {
      DTD d1 = DTD.getDTD("html");
      for (int i = 0; i < 14; i++) {
        System.out.println(d1.getElement(i).getName());
      }
    } catch (IOException e) {
      System.err.println(e);
      e.printStackTrace();
    }
  }
}
```

```java title=Example.java

#pcdata
html
meta
base
isindex
head
body
applet
param
p
title
style
link
script
```
