---
title: Execute the same statements for several different case labels
nav: Execute the same statement...
description: Imported from the java2s.com archive: Execute the same statements for several different case labels
section: Imported - java2s Archive
order: 1002
source: https://web.archive.org/web/20070525055041/http://www.java2s.com:80/Tutorial/Java/0080__Statement-Control/Executethesamestatementsforseveraldifferentcaselabels.htm
---
```java title=Example.java
public class MainClass {
  public static void main(String[] args) {
    char yesNo = 'N';
    switch(yesNo) {
      case 'n': case 'N':
           System.out.println("No selected");
           break;
      case 'y': case 'Y':
           System.out.println("Yes selected");
           break;
    }
  }
}
java title=Example.java
No selected
```
