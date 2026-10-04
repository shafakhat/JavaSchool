---
title: Convert string to an integer or number
nav: Convert string to an integ...
description: Imported from the java2s.com archive: Convert string to an integer or number
section: Imported - java2s Archive
order: 1046
source: https://web.archive.org/web/20140829082218/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Convertstringtoanintegerornumber.htm
---
```java title=Example.java
public class Main {
  public static void main(String[] args) {
    String myNumber = "13";
    Integer number = Integer.parseInt(myNumber);
    System.out.println("My lucky number is: " + number);
    number = Integer.parseInt(myNumber, 16);
    System.out.println("My lucky number is: " + number);
    number = Integer.parseInt(myNumber, 8);
    System.out.println("My lucky number is: " + number);
  }
}
```
