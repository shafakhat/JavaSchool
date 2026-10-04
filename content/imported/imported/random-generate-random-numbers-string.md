---
title: Java Algorithms How to - Generate random numbers String
nav: Java Algorithms How to - G...
description: staticchar digits[] = { '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' };
section: Imported - java2s Archive
order: 1005
source: https://web.archive.org/web/20160730055234/http://www.java2s.com:80/Tutorials/Java/Algorithms_How_to/Random/Generate_random_numbers_String.htm
---
```java title=Example.java
Back to Random  ↑
```

## Question

We would like to know how to generate random numbers String.

## Answer

```java title=Example.java
//fromwww.java2s.compublicclass Main {
  staticchar digits[] = { '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' };

  publicstaticchar randomDecimalDigit() {
    return digits[(int) Math.floor(Math.random() * 10)];
  }

  publicstatic String randomDecimalString(int ndigits) {
    StringBuilder result = new StringBuilder();
    for (int i = 0; i < ndigits; i++) {
      result.append(randomDecimalDigit());
    }
    return result.toString();
  }

  publicstaticvoid main(String[] args) {
    System.out.println(randomDecimalString(24));
  }
}
```

The code above generates the following result.

```java title=Example.java
Back to Random  ↑
```
