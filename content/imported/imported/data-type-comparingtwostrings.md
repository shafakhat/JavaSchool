---
title: Comparing Two Strings
nav: Comparing Two Strings
description: In the following code, if s1 is null, the if statement will return false without evaluating the second expression.
section: Imported - java2s Archive
order: 1037
source: https://web.archive.org/web/20070525054836/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/ComparingTwoStrings.htm
---
```java title=Example.java
public class MainClass {
  public static void main(String[] args) {
    String s1 = "Java";
    String s2 = "Java";
    if (s1.equals(s2)) {
      System.out.println("==");
    }
  }
}
```

Sometimes you see this style.

```java title=Example.java
if ("Java".equals (s1))
```

In the following code, if s1 is null, the if statement will return false without evaluating the second expression.

```java title=Example.java
if (s1 != null && s1.equals("Java"))
```
