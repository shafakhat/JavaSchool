---
title: Using ++ and -- with floating-point variables
nav: Using ++ and -- with float...
description: Imported from the java2s.com archive: Using ++ and -- with floating-point variables
section: Imported - java2s Archive
order: 1019
source: https://web.archive.org/web/20070330085721/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/Usingandwithfloatingpointvariables.htm
---
```java title=Example.java
public class MainClass{
  public static void main(String[] arg){
     double a = 12.12;
     System.out.println( a-- );
     System.out.println( a++ );
     System.out.println( --a );
     System.out.println( ++a );
  }
}
```

```java title=Example.java

12.12
11.12
11.12
12.12
```
