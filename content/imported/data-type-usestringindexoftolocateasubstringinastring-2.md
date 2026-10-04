---
title: Use String.indexOf to locate a substring in a string
nav: Use String.indexOf to loca...
description: Imported from the java2s.com archive: Use String.indexOf to locate a substring in a string
section: Imported - java2s Archive
order: 1017
source: https://web.archive.org/web/20070620173353/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/UseStringindexOftolocateasubstringinastring.htm
---
```java title=Example.java
public class MainClass
{
   public static void main( String args[] )
   {
      String letters = "abcdefghijklmabcdefghijklm";
      System.out.printf( "\"def\" is located at index %d\n",
          letters.indexOf( "def" ) );
       System.out.printf( "\"def\" is located at index %d\n",
          letters.indexOf( "def", 7 ) );
       System.out.printf( "\"hello\" is located at index %d\n\n",
          letters.indexOf( "hello" ) );
   }
}
```

```java title=Example.java

"def" is located at index 3
"def" is located at index 16
"hello" is located at index -1
```
