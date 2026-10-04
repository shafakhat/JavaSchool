---
title: The continue statement
nav: The continue statement
description: Imported from the java2s.com archive: The continue statement
section: Imported - java2s Archive
order: 1053
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0080__Statement-Control/Thecontinuestatementskipsallorpartofaloopiteration.htm
---
```java title=Example.java
publicclass MainClass {
  publicstaticvoid main(String[] arg) {
    int limit = 10;
    int sum = 0;
    for (int i = 1; i <= limit; i++) {
      if (i % 3 == 0) {
        continue;
      }
      sum += i;
    }
    System.out.println(sum);
  }
}
java title=Example.java
37
```
