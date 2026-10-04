---
title: Copy characters from string into char Array
nav: Copy characters from strin...
description: Imported from the java2s.com archive: Copy characters from string into char Array
section: Imported - java2s Archive
order: 1001
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/CopycharactersfromstringintocharArray.htm
---
```java title=Example.java
public class MainClass
{
   public static void main( String args[] )
   {
      String s1 = "hello there";
      char charArray[] = new char[ 5 ];
      System.out.printf( "s1: %s", s1 );
      for ( int count = s1.length() - 1; count >= 0; count-- )
         System.out.printf( "%s ", s1.charAt( count ) );
      s1.getChars( 0, 5, charArray, 0 );
      System.out.print( "\nThe character array is: " );
      for ( char character : charArray )
         System.out.print( character );
   }
}
java title=Example.java
s1: hello theree r e h t   o l l e h
The character array is: hello
```
