---
title: Attempts to use string variable before it has been initialized
nav: Attempts to use string var...
description: Imported from the java2s.com archive: Attempts to use string variable before it has been initialized
section: Imported - java2s Archive
order: 1005
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Attemptstousestringvariablebeforeithasbeeninitialized.htm
---
```java title=Example.java
publicclass MainClass {
  publicstaticvoid main(String[] arg) {
    String s = null;
    System.out.println(s.length());
  }
}
```

```java title=Example.java
Exception in thread "main" java.lang.NullPointerException
	at MainClass.main(MainClass.java:6)
```
