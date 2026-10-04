---
title: Java Algorithms How to - Check if a word is a palindrome
nav: Java Algorithms How to - C...
description: We would like to know how to check if a word is a palindrome.
section: Imported - java2s Archive
order: 1015
source: https://web.archive.org/web/20160721075429/http://www.java2s.com:80/Tutorials/Java/Algorithms_How_to/String/Check_if_a_word_is_a_palindrome.htm
---
```java title=Example.java
Back to String  ↑
```

## Question

We would like to know how to check if a word is a palindrome.

## Answer

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String[] args) {
    String n = "level";
    boolean right = true;
    int f = n.length() - 1;
    for (int i = 0; i < n.length(); i++) {
      if (n.charAt(i) != n.charAt(f - i)) {
        right = false;
      }
    }
    System.out.println("The word is " + right);
  }
}
```

The code above generates the following result.

```java title=Example.java
Back to String  ↑
```
