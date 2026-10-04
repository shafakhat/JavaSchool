---
title: Java Algorithms Convert number to English words example 2
nav: Java Algorithms Convert nu...
description: OneHundred, TwoHundred, ThreeHundred, FourHundred, FiveHundred, SixHundred, SevenHundred, EightHundred,
section: Imported - java2s Archive
order: 1022
source: https://web.archive.org/web/20210102113325/http://www.java2s.com/ref/java/java-algorithms-convert-number-to-english-words-example-2.html
---
## Description

```java title=Example.java
publicclass Main {
   publicenum hundreds {
      OneHundred, TwoHundred, ThreeHundred, FourHundred, FiveHundred, SixHundred, SevenHundred, EightHundred,
      NineHundred
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
