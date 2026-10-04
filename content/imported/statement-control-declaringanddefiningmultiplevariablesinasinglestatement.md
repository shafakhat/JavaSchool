---
title: Declaring and defining multiple variables in a single statement
nav: Declaring and defining mul...
description: Imported from the java2s.com archive: Declaring and defining multiple variables in a single statement
section: Imported - java2s Archive
order: 1050
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0080__Statement-Control/Declaringanddefiningmultiplevariablesinasinglestatement.htm
---
A comma separates each variable.

```java title=Example.java
publicclass MainClass{
  publicstaticvoid main(String[] arg){
   long a = 999999999L, b = 100000000L;
   int c = 0, d = 0;
   System.out.println(a);
   System.out.println(b);
   System.out.println(c);
   System.out.println(d);
  }
}
java title=Example.java
999999999
100000000
0
0
```
