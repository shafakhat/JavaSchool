---
title: Check if a String is a valid date
nav: Check if a String is a val...
description: SimpleDateFormat dateFormat = new SimpleDateFormat("yyyy-MM-dd");
section: Imported - java2s Archive
order: 1016
source: https://web.archive.org/web/20100505182908/http://www.java2s.com:80/Tutorial/Java/0120__Development/CheckifaStringisavaliddate.htm
---
```java title=Example.java
import java.text.ParseException;
import java.text.SimpleDateFormat;
public class Main {
  public static boolean isValidDate(String inDate) {
    SimpleDateFormat dateFormat = new SimpleDateFormat("yyyy-MM-dd");
    dateFormat.setLenient(false);
    try {
      dateFormat.parse(inDate.trim());
    } catch (ParseException pe) {
      return false;
    }
    return true;
  }
  public static void main(String[] args) {
    System.out.println(isValidDate("2004-02-29"));
    System.out.println(isValidDate("2005-02-29"));
  }
}
/*
true
false
*/
```
