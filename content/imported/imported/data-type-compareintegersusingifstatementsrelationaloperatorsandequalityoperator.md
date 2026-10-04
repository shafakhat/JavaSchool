---
title: Compare integers using if statements, relational operators and equality operators
nav: Compare integers using if ...
description: Imported from the java2s.com archive: Compare integers using if statements, relational operators and equality operators
section: Imported - java2s Archive
order: 1019
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Compareintegersusingifstatementsrelationaloperatorsandequalityoperators.htm
---
```java title=Example.java
import java.util.Scanner;

publicclass MainClass
{
   publicstaticvoid main( String args[] )
   {
      Scanner input = new Scanner( System.in );

      int number1;
      int number2;

      System.out.print( "Enter first integer: " ); // prompt
      number1 = input.nextInt(); // read first number from user

      System.out.print( "Enter second integer: " ); // prompt
      number2 = input.nextInt(); // read second number from user
if ( number1 == number2 )
         System.out.printf( "%d == %d\n", number1, number2 );

      if ( number1 != number2 )
         System.out.printf( "%d != %d\n", number1, number2 );

      if ( number1 < number2 )
         System.out.printf( "%d < %d\n", number1, number2 );

      if ( number1 > number2 )
         System.out.printf( "%d > %d\n", number1, number2 );

      if ( number1 <= number2 )
         System.out.printf( "%d <= %d\n", number1, number2 );

      if ( number1 >= number2 )
         System.out.printf( "%d >= %d\n", number1, number2 );

   }

}
```

```java title=Example.java
Enter first integer: 2
Enter second integer: 3
2 != 3
2 < 3
2 <= 3
```
