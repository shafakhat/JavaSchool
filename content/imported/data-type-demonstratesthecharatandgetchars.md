---
title: Demonstrates the charAt and getChars
nav: Demonstrates the charAt an...
description: Imported from the java2s.com archive: Demonstrates the charAt and getChars
section: Imported - java2s Archive
order: 1097
source: https://web.archive.org/web/20140829081838/http://www.java2s.com/Tutorial/Java/0040__Data-Type/DemonstratesthecharAtandgetChars.htm
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
      // copy characters from string into charArray
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
