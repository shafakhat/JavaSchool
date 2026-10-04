---
title: A bubble sort for Strings.
nav: A bubble sort for Strings.
description: Imported from the java2s.com archive: A bubble sort for Strings.
section: Imported - java2s Archive
order: 1008
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/AbubblesortforStrings.htm
---
```java title=Example.java
class SortString {
  static String arr[] = { "N", "i", "t", "t", "f", "a", "g" };

  publicstaticvoid main(String args[]) {
    for (int j = 0; j < arr.length; j++) {
      for (int i = j + 1; i < arr.length; i++) {
        if (arr[i].compareTo(arr[j]) < 0) {
          String t = arr[j];
          arr[j] = arr[i];
          arr[i] = t;
        }
      }
      System.out.println(arr[j]);
    }
  }
}
```
