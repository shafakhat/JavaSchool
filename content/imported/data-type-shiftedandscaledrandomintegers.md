---
title: Shifted and scaled random integers
nav: Shifted and scaled random ...
description: Random randomNumbers = new Random(); // random number generator
section: Imported - java2s Archive
order: 1024
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Shiftedandscaledrandomintegers.htm
---
```java title=Example.java
import java.util.Random;
public class MainClass
{
   public static void main( String args[] )
   {
      Random randomNumbers = new Random(); // random number generator
 int face; // stores each random integer generated
 for ( int i = 1; i <= 20; i++ )
      {
         // pick random integer from 1 to 6
         face = 1 + randomNumbers.nextInt( 6 );
         System.out.printf( "%d  ", face );
         // if i is divisible by 5, start a new line of output
 if ( i % 5 == 0 )
            System.out.println();
      }
   }
}
java title=Example.java
3  6  4  1  1
2  5  6  5  1
2  6  2  3  2
1  5  1  2  4
```
