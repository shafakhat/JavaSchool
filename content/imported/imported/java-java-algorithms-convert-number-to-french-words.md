---
title: Java Algorithms Convert number to French words
nav: Java Algorithms Convert nu...
description: privatestaticfinalString[] dizaineNames = { "", //"", //"vingt", //"trente", //"quarante", //"cinquante", //"soixante", //"soixante", //"quatre-vingt", //"quatre-vingt"//
section: Imported - java2s Archive
order: 1026
source: https://web.archive.org/web/20210102113326/http://www.java2s.com/ref/java/java-algorithms-convert-number-to-french-words.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Description

Java Algorithms Convert number to French words

```java title=Example.java
import java.text.DecimalFormat;

publicclass Main {
   privatestaticfinalString[] dizaineNames = { "", //"", //"vingt", //"trente", //"quarante", //"cinquante", //"soixante", //"soixante", //"quatre-vingt", //"quatre-vingt"//
   };//fromwww.java2s.comprivatestaticfinalString[] uniteNames1 = { "", //"un", //"deux", //"trois", //"quatre", //"cinq", //"six", //"sept", //"huit", //"neuf", //"dix", //"onze", //"douze", //"treize", //"quatorze", //"quinze", //"seize", //"dix-sept", //"dix-huit", //"dix-neuf"//
   };

   privatestaticfinalString[] uniteNames2 = { "", //"", //"deux", //"trois", //"quatre", //"cinq", //"six", //"sept", //"huit", //"neuf", //"dix"//
   };

   private Main() {
   }

   privatestaticString convertZeroToHundred(int number) {

      int laDizaine = number / 10;
      int lUnite = number % 10;
      String resultat = "";

      switch (laDizaine) {
      case 1:
      case 7:
      case 9:
         lUnite = lUnite + 10;
         break;
      default:
      }

      String laLiaison = "";
      if (laDizaine > 1) {
         laLiaison = "-";
      }
      switch (lUnite) {
      case 0:
         laLiaison = "";
         break;
      case 1:
         if (laDizaine == 8) {
            laLiaison = "-";
         } else {
            laLiaison = " et ";
         }
         break;
      case 11:
         if (laDizaine == 7) {
            laLiaison = " et ";
         }
         break;
      default:
      }

      // dizaines en lettresswitch (laDizaine) {
      case 0:
         resultat = uniteNames1[lUnite];
         break;
      case 8:
         if (lUnite == 0) {
            resultat = dizaineNames[laDizaine];
         } else {
            resultat = dizaineNames[laDizaine] + laLiaison + uniteNames1[lUnite];
         }
         break;
      default:
         resultat = dizaineNames[laDizaine] + laLiaison + uniteNames1[lUnite];
      }
      return resultat;
   }

   privatestaticString convertLessThanOneThousand(int number) {

      int lesCentaines = number / 100;
      int leReste = number % 100;
      String sReste = convertZeroToHundred(leReste);

      String resultat;
      switch (lesCentaines) {
      case 0:
         resultat = sReste;
         break;
      case 1:
         if (leReste > 0) {
            resultat = "cent " + sReste;
         } else {
            resultat = "cent";
         }
         break;
      default:
         if (leReste > 0) {
            resultat = uniteNames2[lesCentaines] + " cent " + sReste;
         } else {
            resultat = uniteNames2[lesCentaines] + " cents";
         }
      }
      return resultat;
   }

   publicstaticString convert(long number) {
      if (number == 0) {
         return"zero";
      }

      String snumber = Long.toString(number);
      String mask = "000000000000";
      DecimalFormat df = newDecimalFormat(mask);
      snumber = df.format(number);

      int lesMilliards = Integer.parseInt(snumber.substring(0, 3));
      int lesMillions = Integer.parseInt(snumber.substring(3, 6));
      int lesCentMille = Integer.parseInt(snumber.substring(6, 9));
      int lesMille = Integer.parseInt(snumber.substring(9, 12));

      String tradMilliards;
      switch (lesMilliards) {
      case 0:
         tradMilliards = "";
         break;
      case 1:
         tradMilliards = convertLessThanOneThousand(lesMilliards) + " milliard ";
         break;
      default:
         tradMilliards = convertLessThanOneThousand(lesMilliards) + " milliards ";
      }
      String resultat = tradMilliards;

      String tradMillions;
      switch (lesMillions) {
      case 0:
         tradMillions = "";
         break;
      case 1:
         tradMillions = convertLessThanOneThousand(lesMillions) + " million ";
         break;
      default:
         tradMillions = convertLessThanOneThousand(lesMillions) + " millions ";
      }
      resultat = resultat + tradMillions;

      String tradCentMille;
      switch (lesCentMille) {
      case 0:
         tradCentMille = "";
         break;
      case 1:
         tradCentMille = "mille ";
         break;
      default:
         tradCentMille = convertLessThanOneThousand(lesCentMille) + " mille ";
      }
      resultat = resultat + tradCentMille;

      String tradMille;
      tradMille = convertLessThanOneThousand(lesMille);
      resultat = resultat + tradMille;

      return resultat;
   }

   publicstaticvoid main(String[] args) {
      System.out.println(convert(0));
      System.out.println(convert(9));
      System.out.println(convert(19));
      System.out.println(convert(21));
      System.out.println(convert(97));
      System.out.println(convert(100));
      System.out.println(convert(101));
      System.out.println(convert(201));
      System.out.println(convert(232));
      System.out.println(convert(999));
      System.out.println(convert(1000));
      System.out.println(convert(10001));
      System.out.println(convert(100000));
      System.out.println(convert(2000000));
      System.out.println(convert(3000000000L));
      System.out.println(convert(2147483647));
   }
}
```

PreviousNext

## Related

- Java Algorithms Convert number to English words example 2
- Java Algorithms Convert number to English words example 3
- Java Algorithms Convert number to English words example 4
- Java Algorithms Huffman code
- Java Algorithms Move along circle
