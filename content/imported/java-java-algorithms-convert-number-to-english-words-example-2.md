---
title: Java Algorithms Convert number to English words example 2
nav: Java Algorithms Convert nu...
description: OneHundred, TwoHundred, ThreeHundred, FourHundred, FiveHundred, SixHundred, SevenHundred, EightHundred,
section: Imported - java2s Archive
order: 1001
source: https://web.archive.org/web/2016/http://www.java2s.com/ref/java/java-algorithms-convert-number-to-english-words-example-2.html
---
## Description

```java title=Example.java
public class Main {
   public enum hundreds {
      OneHundred, TwoHundred, ThreeHundred, FourHundred, FiveHundred, SixHundred, SevenHundred, EightHundred,
      NineHundred
   }
   public enum tens {
      Twenty, Thirty, Forty, Fifty, Sixty, Seventy, Eighty, Ninety
   }
   public enum ones {
      One, Two, Three, Four, Five, Six, Seven, Eight, Nine
   }
   public enum denom {
      Thousand, Million, Billion
   }
   public enum splNums {
      Ten, Eleven, Twelve, Thirteen, Fourteen, Fifteen, Sixteen, Seventeen, Eighteen, Nineteen
   }
   public static String text = "";
   public static void main(String[] args) {
      long num = 1234567;
      int rem = 0;
      int i = 0;
      while (num > 0) {
         if (i == 0) {
            rem = (int) (num % 1000);
            printText(rem);
            num = num / 1000;
            i++;
         } else if (num > 0) {
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
      else System.out.println("Zero");
   }
   public static void printText(int num) {
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
   public static void getSplNums(int num) {
      text = splNums.values()[num] + " " + text;
   }
   public static void getHundreds(int num) {
      text = hundreds.values()[num - 1] + " " + text;
   }
   public static void getTens(int num) {
      text = tens.values()[num - 2] + " " + text;
   }
   public static void getOnes(int num) {
      text = ones.values()[num - 1] + " " + text;
   }
}
```

PreviousNext

## Related
