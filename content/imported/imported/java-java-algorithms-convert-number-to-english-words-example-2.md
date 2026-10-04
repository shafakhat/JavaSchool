---
title: Java Algorithms Convert number to English words example 2
nav: Java Algorithms Convert nu...
description: OneHundred, TwoHundred, ThreeHundred, FourHundred, FiveHundred, SixHundred, SevenHundred, EightHundred,
section: Imported - java2s Archive
order: 1022
source: https://web.archive.org/web/20210102113325/http://www.java2s.com/ref/java/java-algorithms-convert-number-to-english-words-example-2.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Description

Java Algorithms Convert number to English words example 2

```java title=Example.java
publicclass Main {

   publicenum hundreds {
      OneHundred, TwoHundred, ThreeHundred, FourHundred, FiveHundred, SixHundred, SevenHundred, EightHundred,
      NineHundred/*fromwww.java2s.com*/
   }

   publicenum tens {
      Twenty, Thirty, Forty, Fifty, Sixty, Seventy, Eighty, Ninety
   }

   publicenum ones {
      One, Two, Three, Four, Five, Six, Seven, Eight, Nine
   }

   publicenum denom {
      Thousand, Million, Billion
   }

   publicenum splNums {
      Ten, Eleven, Twelve, Thirteen, Fourteen, Fifteen, Sixteen, Seventeen, Eighteen, Nineteen
   }

   publicstaticString text = "";

   publicstaticvoid main(String[] args) {
      long num = 1234567;
      int rem = 0;
      int i = 0;
      while (num > 0) {
         if (i == 0) {
            rem = (int) (num % 1000);
            printText(rem);
            num = num / 1000;
            i++;
         } elseif (num > 0) {
            rem = (int) (num % 100);
            if (rem > 0)
               text = denom.values()[i - 1] + " " + text;
            printText(rem);
            num = num / 100;
            i++;
         }
      }
      if (i > 0)
         System.out.println(text);
      elseSystem.out.println("Zero");
   }

   publicstaticvoid printText(int num) {
      if (!(num > 9 && num < 19)) {
         if (num % 10 > 0)
            getOnes(num % 10);
         num = num / 10;
         if (num % 10 > 0)
            getTens(num % 10);

         num = num / 10;
         if (num > 0)
            getHundreds(num);
      } else {
         getSplNums(num % 10);
      }
   }

   publicstaticvoid getSplNums(int num) {
      text = splNums.values()[num] + " " + text;
   }

   publicstaticvoid getHundreds(int num) {
      text = hundreds.values()[num - 1] + " " + text;
   }

   publicstaticvoid getTens(int num) {
      text = tens.values()[num - 2] + " " + text;
   }

   publicstaticvoid getOnes(int num) {
      text = ones.values()[num - 1] + " " + text;
   }
}
```

PreviousNext

## Related

- Java Algorithms Bracket Checker
- Java Algorithms Convert infix expression to postfix expression
- Java Algorithms Convert number to English words
- Java Algorithms Convert number to English words example 3
- Java Algorithms Convert number to English words example 4
