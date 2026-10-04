---
title: Read Integers from console and calculate
nav: Read Integers from console...
description: Imported from the java2s.com archive: Read Integers from console and calculate
section: Imported - java2s Archive
order: 1042
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/ReadIntegersfromconsoleandcalculate.htm
---
```java title=Example.java
import java.util.Scanner;
publicclass MainClass
{
   publicstaticvoid main( String args[] )
   {
      Scanner input = new Scanner( System.in );
      int x;
      int y;
      int z;
      int result;
      System.out.print( "Enter first integer: " );
      x = input.nextInt();
      System.out.print( "Enter second integer: " );
      y = input.nextInt();
      System.out.print( "Enter third integer: " );
      z = input.nextInt();
      result = x * y * z;
      System.out.printf( "Product is %d\n", result );
   }
}
java title=Example.java
Enter first integer: 1
Enter second integer: 2
Enter third integer: 3
Product is 6
```
