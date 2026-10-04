---
title: Java Algorithms Convert number to English words example 3
nav: Java Algorithms Convert nu...
description: String string;//fromwww.java2s.comString st1[] = { "", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", };
section: Imported - java2s Archive
order: 1023
source: https://web.archive.org/web/20210102113325/http://www.java2s.com/ref/java/java-algorithms-convert-number-to-english-words-example-3.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Description

Java Algorithms Convert number to English words example 3

```java title=Example.java
import java.util.Scanner;

publicclass Main {
   String string;//fromwww.java2s.comString st1[] = { "", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", };
   String st2[] = { "hundred", "thousand", "lakh", "crore" };
   String st3[] = { "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen",
         "ninteen", };
   String st4[] = { "twenty", "thirty", "fourty", "fifty", "sixty", "seventy", "eighty", "ninety" };

   publicString convert(int number) {
      int n = 1;
      int word;
      string = "";
      while (number != 0) {
         switch (n) {
         case 1:
            word = number % 100;
            pass(word);
            if (number > 100 && number % 100 != 0) {
               show("and ");
               // System.out.print("ankit");
            }
            number /= 100;
            break;
         case 2:
            word = number % 10;
            if (word != 0) {
               show(" ");
               show(st2[0]);
               show(" ");
               pass(word);
            }
            number /= 10;
            break;
         case 3:
            word = number % 100;
            if (word != 0) {
               show(" ");
               show(st2[1]);
               show(" ");
               pass(word);
            }
            number /= 100;
            break;
         case 4:
            word = number % 100;
            if (word != 0) {
               show(" ");
               show(st2[2]);
               show(" ");
               pass(word);
            }
            number /= 100;
            break;
         case 5:
            word = number % 100;
            if (word != 0) {
               show(" ");
               show(st2[3]);
               show(" ");
               pass(word);
            }
            number /= 100;
            break;
         }
         n++;
      }
      return string;
   }

   publicvoid pass(int number) {
      int word, q;
      if (number < 10) {
         show(st1[number]);
      }
      if (number > 9 && number < 20) {
         show(st3[number - 10]);
      }
      if (number > 19) {
         word = number % 10;
         if (word == 0) {
            q = number / 10;
            show(st4[q - 2]);
         } else {
            q = number / 10;
            show(st1[word]);
            show(" ");
            show(st4[q - 2]);
         }
      }
   }

   publicvoid show(String s) {
      String st;
      st = string;
      string = s;
      string += st;
   }

   publicstaticvoid main(String[] args) {
      Main w = new Main();
      Scanner input = newScanner(System.in);
      System.out.print("Enter Number: ");
      int num = input.nextInt();
      String inwords = w.convert(num);
      System.out.println(inwords);
   }
}
```

PreviousNext

## Related

- Java Algorithms Convert infix expression to postfix expression
- Java Algorithms Convert number to English words
- Java Algorithms Convert number to English words example 2
- Java Algorithms Convert number to English words example 4
- Java Algorithms Convert number to French words
