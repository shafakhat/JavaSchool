---
title: Java Algorithms How to - Generate Password
nav: Java Algorithms How to - G...
description: password.setCharAt(i, (char) (r[x.nextInt(256) % 8].nextInt(95) + 32));
section: Imported - java2s Archive
order: 1001
source: https://web.archive.org/web/20160730061630/http://www.java2s.com:80/Tutorials/Java/Algorithms_How_to/Random/Generate_Password.htm
---
```java title=Example.java
Back to Random  ↑
```

## Question

We would like to know how to generate Password.

## Answer

```java title=Example.java
import java.util.Random;
/*fromwww.java2s.com*/publicclass Main {
  publicstatic String generatePassword() {
    Random r[] = new Random[8];
    r[0] = new Random();
    r[1] = new Random();
    r[2] = new Random();
    r[3] = new Random();
    r[4] = new Random();
    r[5] = new Random();
    r[6] = new Random();
    r[7] = new Random();
    Random x = new Random();
    StringBuilder password = new StringBuilder();
    int length = 6;
    password.setLength(length);
    for (int i = 0; i < length; i++) {
      x.setSeed(r[i % 8].nextInt(500) * r[4].nextInt(900));
      password.setCharAt(i, (char) (r[x.nextInt(256) % 8].nextInt(95) + 32));
    }
    return password.toString();
  }
  publicstaticvoid main(String[] args) {
    System.out.println(generatePassword());
  }
}
```

The code above generates the following result.

```java title=Example.java
Back to Random  ↑
```
