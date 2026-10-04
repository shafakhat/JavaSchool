---
title: Comparing Enumeration Values
nav: Comparing Enumeration Values
description: Imported from the java2s.com archive: Comparing Enumeration Values
section: Imported - java2s Archive
order: 1374
source: https://web.archive.org/web/20140829075435/http://www.java2s.com/Tutorial/Java/0040__Data-Type/ComparingEnumerationValues.htm
---
```java title=Example.java
public class MainClass {
  enum Season {
    spring, summer, fall, winter
  };
  public static void main(String[] arg) {
    Season season = Season.summer;
    if (season.equals(Season.spring)) {
      System.out.println("It is Spring.");
    } else {
      System.out.println("It isn\'t Spring!");
    }
  }
}
java title=Example.java
It isn't Spring!
```

| 2.43.1. | Enumeration Fundamentals |
|---|---|
| 2.43.2. | How to define an enumeration |
| 2.43.3. | Enums in a Class |
| 2.43.4. | equals and = operator for enum data type |
| 2.43.5. | Comparing Enumeration Values |
| 2.43.6. | Two enumeration constants can be compared for equality by using the == relational operator |
| 2.43.7. | uses an enum, rather than interface variables, to represent the answers. |
| 2.43.8. | enum type with its own method |
| 2.43.9. | Enum type field |
| 2.43.10. | enum with switch |
