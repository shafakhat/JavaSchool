---
title: Java Algorithms Convert number to English words
nav: Java Algorithms Convert nu...
description: privatestaticfinalString[] tensNames = { "", //" ten", //" twenty", //" thirty", //" forty", //" fifty", //" sixty", //" seventy", //" eighty", //" ninety"//
section: Imported - java2s Archive
order: 1025
source: https://web.archive.org/web/20210102113325/http://www.java2s.com/ref/java/java-algorithms-convert-number-to-english-words.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Description

Java Algorithms Convert number to English words

```java title=Example.java
import java.text.DecimalFormat;

publicclass Main {

   privatestaticfinalString[] tensNames = { "", //" ten", //" twenty", //" thirty", //" forty", //" fifty", //" sixty", //" seventy", //" eighty", //" ninety"//
   };//fromwww.java2s.comprivatestaticfinalString[] numNames = { "", //" one", //" two", //" three", //" four", //" five", //" six", //" seven", //" eight", //" nine", //" ten", //" eleven", //" twelve", //" thirteen", //" fourteen", //" fifteen", //" sixteen", //" seventeen", //" eighteen", //" nineteen"//
   };

   privatestaticString convertLessThanOneThousand(int number) {
      String soFar;

      if (number % 100 < 20) {
         soFar = numNames[number % 100];
         number /= 100;
      } else {
         soFar = numNames[number % 10];
         number /= 10;

         soFar = tensNames[number % 10] + soFar;
         number /= 10;
      }
      if (number == 0)
         return soFar;
      return numNames[number] + " hundred" + soFar;
   }

   publicstaticString convert(long number) {
      // 0 to 999 999 999 999if (number == 0) {
         return"zero";
      }

      String snumber = Long.toString(number);

      // pad with "0"String mask = "000000000000";
      DecimalFormat df = newDecimalFormat(mask);
      snumber = df.format(number);

      // XXXnnnnnnnnnint billions = Integer.parseInt(snumber.substring(0, 3));
      // nnnXXXnnnnnnint millions = Integer.parseInt(snumber.substring(3, 6));
      // nnnnnnXXXnnnint hundredThousands = Integer.parseInt(snumber.substring(6, 9));
      // nnnnnnnnnXXXint thousands = Integer.parseInt(snumber.substring(9, 12));

      String tradBillions;
      switch (billions) {
      case 0:
         tradBillions = "";
         break;
      case 1:
         tradBillions = convertLessThanOneThousand(billions) + " billion ";
         break;
      default:
         tradBillions = convertLessThanOneThousand(billions) + " billion ";

      }
      String result = tradBillions;

      String tradMillions;
      switch (millions) {
      case 0:
         tradMillions = "";
         break;
      case 1:
         tradMillions = convertLessThanOneThousand(millions) + " million ";
         break;
      default:
         tradMillions = convertLessThanOneThousand(millions) + " million ";
      }
      result = result + tradMillions;

      String tradHundredThousands;
      switch (hundredThousands) {
      case 0:
         tradHundredThousands = "";
         break;
      case 1:
         tradHundredThousands = "one thousand ";
         break;
      default:
         tradHundredThousands = convertLessThanOneThousand(hundredThousands) + " thousand ";
      }
      result = result + tradHundredThousands;

      String tradThousand;
      tradThousand = convertLessThanOneThousand(thousands);
      result = result + tradThousand;

      // remove extra spaces!return result.replaceAll("^\\s+", "").replaceAll("\\b\\s{2,}\\b", " ");
   }

   publicstaticvoid main(String[] args) {
      System.out.println(convert(0));
      System.out.println(convert(1));
      System.out.println(convert(16));
      System.out.println(convert(100));
      System.out.println(convert(1316));
      System.out.println(convert(1000000));
      System.out.println(convert(123456789));
      System.out.println(convert(2147483647));

   }
}
```

PreviousNext

## Related

- Java Algorithms Binary Search Tree Animation
- Java Algorithms Bracket Checker
- Java Algorithms Convert infix expression to postfix expression
- Java Algorithms Convert number to English words example 2
- Java Algorithms Convert number to English words example 3
