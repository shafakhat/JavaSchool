---
title: Java Algorithms Convert number to English words example 4
nav: Java Algorithms Convert nu...
description: publicstaticfinalString[] units = { "", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
section: Imported - java2s Archive
order: 1024
source: https://web.archive.org/web/20210102113326/http://www.java2s.com/ref/java/java-algorithms-convert-number-to-english-words-example-4.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Description

Java Algorithms Convert number to English words example 4

```java title=Example.java
publicclass Main {
   publicstaticfinalString[] units = { "", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
         "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen" };

   publicstaticfinalString[] tens = { "", // 0"", // 1"twenty", // 2"thirty", // 3"forty", // 4"fifty", // 5"sixty", // 6"seventy", // 7"eighty", // 8"ninety"// 9
   };//fromwww.java2s.compublicstaticString convert(finalint n) {
      if (n < 0) {
         return"minus " + convert(-n);
      }

      if (n < 20) {
         return units[n];
      }

      if (n < 100) {
         return tens[n / 10] + ((n % 10 != 0) ? " " : "") + units[n % 10];
      }

      if (n < 1000) {
         return units[n / 100] + " hundred" + ((n % 100 != 0) ? " " : "") + convert(n % 100);
      }

      if (n < 1000000) {
         return convert(n / 1000) + " thousand" + ((n % 1000 != 0) ? " " : "") + convert(n % 1000);
      }

      if (n < 1000000000) {
         return convert(n / 1000000) + " million" + ((n % 1000000 != 0) ? " " : "") + convert(n % 1000000);
      }

      return convert(n / 1000000000) + " billion" + ((n % 1000000000 != 0) ? " " : "") + convert(n % 1000000000);
   }

   publicstaticvoid main(finalString[] args) {
      int n = 1000;
      System.out.printf("%10d =  '%s'%n", n, convert(n));

      n = 11000;
      System.out.printf("%10d =  '%s'%n", n, convert(n));

      n = 999999999;
      System.out.printf("%10d =  '%s'%n", n, convert(n));

      n = Integer.MAX_VALUE;

      System.out.printf("%10d =  '%s'%n", n, convert(n));
   }
}
```

PreviousNext

## Related

- Java Algorithms Convert number to English words
- Java Algorithms Convert number to English words example 2
- Java Algorithms Convert number to English words example 3
- Java Algorithms Convert number to French words
- Java Algorithms Huffman code
