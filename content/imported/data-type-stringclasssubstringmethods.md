---
title: String class substring methods
nav: String class substring met...
description: System.out.printf( "Substring from index 20 to end is \"%s\"\n",
section: Imported - java2s Archive
order: 1012
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Stringclasssubstringmethods.htm
---
```java title=Example.java
public class MainClass
{
   public static void main( String args[] )
   {
      String letters = "abcdefghijklmabcdefghijklm";
      // test substring methods
      System.out.printf( "Substring from index 20 to end is \"%s\"\n",
         letters.substring( 20 ) );
      System.out.printf( "%s \"%s\"\n",
         "Substring from index 3 up to, but not including 6 is",
         letters.substring( 3, 6 ) );
   } // end main
}
java title=Example.java
Substring from index 20 to end is "hijklm"
Substring from index 3 up to, but not including 6 is "def"
```
