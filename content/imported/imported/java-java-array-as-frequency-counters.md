---
title: Java Array as frequency counters
nav: Java Array as frequency co...
description: {//fromwww.java2s.comint[] responses = {1, 2, 5, 4, 3, 5, 2, 1,
section: Imported - java2s Archive
order: 1097
source: https://web.archive.org/web/20210102113249/http://www.java2s.com/ref/java/java-array-as-frequency-counters.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Description

Java Array as frequency counters

```java title=Example.java
publicclass Main
{
   publicstaticvoid main(String[] args)
   {//fromwww.java2s.comint[] responses = {1, 2, 5, 4, 3, 5, 2, 1,
          3, 3, 1, 4, 3, 3, 3, 2, 3, 3, 2,
          3, 3, 1, 4, 3, 3, 3, 2, 3, 3, 2,
          3, 3, 1, 4, 3, 3, 3, 2, 3, 3, 2,
          14};
      int[] frequency = newint[6]; // array of frequency countersfor (int answer = 0; answer < responses.length; answer++)
      {
         try
         {
            ++frequency[responses[answer]];
         }
         catch (ArrayIndexOutOfBoundsException e)
         {
            System.out.println(e); // invokes toString methodSystem.out.printf("   responses[%d] = %d%n%n",
               answer, responses[answer]);
         }
      }

      System.out.printf("%s%10s%n", "Rating", "Frequency");

      // output each array element's valuefor (int rating = 1; rating < frequency.length; rating++)
         System.out.printf("%6d%10d%n", rating, frequency[rating]);
   }
}
```

The following code uses the elements of an array as counters.

```java title=Example.java
import java.security.SecureRandom;

publicclass Main
{
   publicstaticvoid main(String[] args)
   {/*www.java2s.com*/SecureRandom randomNumbers = newSecureRandom();
      int[] frequency = newint[7]; // array of frequency counters// roll die 6,000,000 times; use die value as frequency indexfor (int roll = 1; roll <= 6000000; roll++)
         ++frequency[1 + randomNumbers.nextInt(6)];

      System.out.printf("%s%10s%n", "Face", "Frequency");

      // output each array element's valuefor (int face = 1; face < frequency.length; face++)
         System.out.printf("%4d%10d%n", face, frequency[face]);
   }
}
```

PreviousNext

## Related

- Java Array Type
- Java Array Initializer
- Java Array length property
- Java Array count occurrences of letter in char array
- Java Array display arrays
