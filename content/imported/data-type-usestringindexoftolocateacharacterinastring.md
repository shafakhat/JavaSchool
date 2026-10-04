---
title: Use String.indexOf to locate a character in a string
nav: Use String.indexOf to loca...
description: Imported from the java2s.com archive: Use String.indexOf to locate a character in a string
section: Imported - java2s Archive
order: 1100
source: https://web.archive.org/web/20140829090618/http://www.java2s.com/Tutorial/Java/0040__Data-Type/UseStringindexOftolocateacharacterinastring.htm
---
```java title=Example.java
public class MainClass
{
   public static void main( String args[] )
   {
      String letters = "abcdefghijklmabcdefghijklm";
      System.out.printf(
         "'c' is located at index %d\n", letters.indexOf( 'c' ) );
      System.out.printf(
         "'a' is located at index %d\n", letters.indexOf( 'a', 1 ) );
      System.out.printf(
         "'$' is located at index %d\n\n", letters.indexOf( '$' ) );
   }
}
java title=Example.java
'c' is located at index 2
'a' is located at index 13
'$' is located at index -1
```
