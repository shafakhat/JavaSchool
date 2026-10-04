---
title: Java Algorithms How to - Create random name generator
nav: Java Algorithms How to - C...
description: result = Character.toString(firstname.charAt(0)); // First char
section: Imported - java2s Archive
order: 1024
source: https://web.archive.org/web/20160730032210/http://www.java2s.com:80/Tutorials/Java/Algorithms_How_to/Random/Create_random_name_generator.htm
---
## Question

We would like to know how to create random name generator.

## Answer

```java title=Example.java
import java.util.Random;
publicclass Main {
  publicstaticvoid main(String args[]) {
    Random rnd = new Random();
    String firstname = "James";
    String lastname = "Bond";
    String result;
    result = Character.toString(firstname.charAt(0)); // First char
if (lastname.length() > 5)
      result += lastname.substring(0, 5);
    else
      result += lastname;
    result += Integer.toString(rnd.nextInt(99));
    System.out.println(result);
  }
}
```

The code above generates the following result.
