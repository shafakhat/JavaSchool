---
title: Java Algorithms Convert number to English words example 4
nav: Java Algorithms Convert nu...
description: publicstaticfinalString[] units = { "", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
section: Imported - java2s Archive
order: 1024
source: https://web.archive.org/web/20210102113326/http://www.java2s.com/ref/java/java-algorithms-convert-number-to-english-words-example-4.html
---
## Description

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
