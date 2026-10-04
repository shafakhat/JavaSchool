---
title: Java Array count occurrences of letter in char array
nav: Java Array count occurrenc...
description: // Count the occurrences of each letterint[] counts = countLetters(chars);
section: Imported - java2s Archive
order: 1102
source: https://web.archive.org/web/20210102113249/http://www.java2s.com/ref/java/java-array-count-occurrences-of-letter-in-char-array.html
---
## Description

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String[] args) {
    char[] chars = "demoscomtesttest".toCharArray();

    // Count the occurrences of each letterint[] counts = countLetters(chars);

    System.out.println("The occurrences of each letter are:");
    displayCounts(counts);//fromwww.java2s.com
  }
  /** Count the occurrences of each letter */publicstaticint[] countLetters(char[] chars) {
    // Declare and create an array of 26 intint[] counts = newint[26];

    // For each lowercase letter in the array, count itfor (int i = 0; i < chars.length; i++)
      counts[chars[i] - 'a']++;

    return counts;
  }

  /** Display counts */publicstaticvoid displayCounts(int[] counts) {
    for (int i = 0; i < counts.length; i++) {
      if(counts[i] > 0) {
        System.out.println((char)(i + 'a') +" " + counts[i] );
      }
    }
  }
}
```

PreviousNext

## Related

- Java Array Initializer
- Java Array length property
- Java Array as frequency counters
- Java Array display arrays
- Java Array find array element above average
