---
title: String.Replace
nav: String.Replace
description: System.out.printf( "s1 = %s\ns2 = %s\ns3 = %s\n\n", s1, s2, s3 );
section: Imported - java2s Archive
order: 1052
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/StringReplace.htm
---
```java title=Example.java
publicclass MainClass
{
   publicstaticvoid main( String args[] )
   {
      String s1 = new String( "hello" );
      String s2 = new String( "GOODBYE" );
      String s3 = new String( "   spaces   " );
      System.out.printf( "s1 = %s\ns2 = %s\ns3 = %s\n\n", s1, s2, s3 );
      // test method replace
      System.out.printf("Replace 'l' with 'L' in s1: %s\n\n", s1.replace( 'l', 'L' ) );
   } // end main
}
```

```java title=Example.java
s1 = hello
s2 = GOODBYE
s3 =    spaces
Replace 'l' with 'L' in s1: heLLo
```
