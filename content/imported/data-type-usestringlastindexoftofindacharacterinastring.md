---
title: Use String.lastIndexOf to find a character in a string
nav: Use String.lastIndexOf to ...
description: Imported from the java2s.com archive: Use String.lastIndexOf to find a character in a string
section: Imported - java2s Archive
order: 1171
source: https://web.archive.org/web/2018/http://www.java2s.com/Tutorial/Java/0040__Data-Type/UseStringlastIndexOftofindacharacterinastring.htm
---
```java title=Example.java
public class MainClass
{
   public static void main( String args[] )
   {
      String letters = "abcdefghijklmabcdefghijklm";
      System.out.printf( "Last 'c' is located at index %d\n",
          letters.lastIndexOf( 'c' ) );
       System.out.printf( "Last 'a' is located at index %d\n",
          letters.lastIndexOf( 'a', 25 ) );
       System.out.printf( "Last '$' is located at index %d\n\n",
          letters.lastIndexOf( '$' ) );
   }
}
java title=Example.java
Last 'c' is located at index 15
Last 'a' is located at index 13
Last '$' is located at index -1
```
