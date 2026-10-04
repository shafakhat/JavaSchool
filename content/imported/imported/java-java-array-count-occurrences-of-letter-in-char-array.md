---
title: Java Array count occurrences of letter in char array
nav: Java Array count occurrenc...
description: // Count the occurrences of each letterint[] counts = countLetters(chars);
section: Imported - java2s Archive
order: 1102
source: https://web.archive.org/web/20210102113249/http://www.java2s.com/ref/java/java-array-count-occurrences-of-letter-in-char-array.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Description

Java Array count occurrences of letter in char array

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
