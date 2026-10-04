---
title: Use lastIndexOf to find a substring in a string
nav: Use lastIndexOf to find a ...
description: System.out.printf( "Last \"hello\" is located at index %d\n",
section: Imported - java2s Archive
order: 1103
source: https://web.archive.org/web/20140829090815/http://www.java2s.com/Tutorial/Java/0040__Data-Type/UselastIndexOftofindasubstringinastring.htm
---
```java title=Example.java
public class MainClass
{
   public static void main( String args[] )
   {
      String letters = "abcdefghijklmabcdefghijklm";
      System.out.printf( "Last \"def\" is located at index %d\n",
          letters.lastIndexOf( "def" ) );
       System.out.printf( "Last \"def\" is located at index %d\n",
          letters.lastIndexOf( "def", 25 ) );
       System.out.printf( "Last \"hello\" is located at index %d\n",
          letters.lastIndexOf( "hello" ) );
   }
}
java title=Example.java
Last "def" is located at index 16
Last "def" is located at index 16
Last "hello" is located at index -1
```
