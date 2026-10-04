---
title: String Concatenation
nav: String Concatenation
description: Imported from the java2s.com archive: String Concatenation
section: Imported - java2s Archive
order: 1124
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/StringConcatenation.htm
---
```java title=Example.java
public class MainClass
{
   public static void main( String args[] )
   {
      String s1 = new String( "Happy " );
      String s2 = new String( "Birthday" );
      System.out.printf( "s1 = %s\ns2 = %s\n\n",s1, s2 );
      System.out.printf(
         "Result of s1.concat( s2 ) = %s\n", s1.concat( s2 ) );
      System.out.printf( "s1 after concatenation = %s\n", s1 );
   } // end main
}
java title=Example.java
s1 = Happy
s2 = Birthday
Result of s1.concat( s2 ) = Happy Birthday
s1 after concatenation = Happy
```
