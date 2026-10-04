---
title: Roll a six-sided die 6000 times
nav: Roll a six-sided die 6000 ...
description: Random randomNumbers = new Random(); // random number generator
section: Imported - java2s Archive
order: 1860
source: https://web.archive.org/web/20140301114317/http://www.java2s.com/Tutorial/Java/0120__Development/Rollasixsideddie6000times.htm
---
```java title=Example.java
import java.util.Random;
public class MainClass
{
   public static void main( String args[] )
   {
      Random randomNumbers = new Random(); // random number generator
      int frequency1 = 0; // count of 1s rolled
      int frequency2 = 0; // count of 2s rolled
      int frequency3 = 0; // count of 3s rolled
      int frequency4 = 0; // count of 4s rolled
      int frequency5 = 0; // count of 5s rolled
      int frequency6 = 0; // count of 6s rolled
      int face; // stores most recently rolled value
      // summarize results of 6000 rolls of a die
      for ( int roll = 1; roll <= 6000; roll++ )
      {
         face = 1 + randomNumbers.nextInt( 6 ); // number from 1 to 6
         // determine roll value 1-6 and increment appropriate counter
         switch ( face )
         {
            case 1:
               ++frequency1; // increment the 1s counter
               break;
            case 2:
               ++frequency2; // increment the 2s counter
               break;
            case 3:
               ++frequency3; // increment the 3s counter
               break;
            case 4:
               ++frequency4; // increment the 4s counter
               break;
            case 5:
               ++frequency5; // increment the 5s counter
               break;
            case 6:
               ++frequency6; // increment the 6s counter
               break; // optional at end of switch
         }
      }
      System.out.println( "Face\tFrequency" ); // output headers
      System.out.printf( "1\t%d\n2\t%d\n3\t%d\n4\t%d\n5\t%d\n6\t%d\n",
         frequency1, frequency2, frequency3, frequency4,
         frequency5, frequency6 );
   }
}
java title=Example.java
Face  Frequency
1 1005
2 1028
3 1027
4 989
5 994
6 957
```

| 6.37.1. | Generating Random integer Numbers |
|---|---|
| 6.37.2. | Roll a six-sided die 6000 times |
| 6.37.3. | Random integers that range from from 0 to n |
| 6.37.4. | Random bytes |
| 6.37.5. | Random boolean |
| 6.37.6. | Random long type number |
| 6.37.7. | Random float type number |
| 6.37.8. | Random double type number |
| 6.37.9. | Create two random number generators with the same seed |
| 6.37.10. | Random number between 0 AND 10 |
| 6.37.11. | Random numbers between 0.0 and 1.0 |
| 6.37.12. | Random.nextInt(n) returns a distributed int value between 0 (inclusive) and n (exclusive). |
| 6.37.13. | Generate a random array of numbers |
| 6.37.14. | Random Gaussian values. |
| 6.37.15. | Operations for random Strings |
