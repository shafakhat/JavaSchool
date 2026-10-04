---
title: toLowerCase and toUpperCase
nav: toLowerCase and toUpperCase
description: System.out.printf( "s1 = %s\ns2 = %s\ns3 = %s\n\n", s1, s2, s3 );
section: Imported - java2s Archive
order: 1067
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/toLowerCaseandtoUpperCase.htm
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
      // test toLowerCase and toUpperCase
      System.out.printf( "s1.toUpperCase() = %s\n", s1.toUpperCase() );
      System.out.printf( "s2.toLowerCase() = %s\n\n", s2.toLowerCase() );
   }
}
java title=Example.java
s1 = hello
s2 = GOODBYE
s3 =    spaces
s1.toUpperCase() = HELLO
s2.toLowerCase() = goodbye
```
