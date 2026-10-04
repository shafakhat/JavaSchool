---
title: Using the built-in enumeration methods
nav: Using the built-in enumera...
description: All enumerations automatically contain two predefined methods: values( ) and valueOf( ).
section: Imported - java2s Archive
order: 1050
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Usingthebuiltinenumerationmethodsvalues.htm
---
All enumerations automatically contain two predefined methods: values( ) and valueOf( ).

- public static enum-type[ ] values( )
- public static enum-type valueOf(String str)

The values( ) method returns an array that contains a list of the enumeration constants.

The valueOf( ) method returns the enumeration constant whose value corresponds to the string passed in str.

```java title=Example.java
enum Week {
  Monday, Tuesday, Wednesday, Thursday, Friday, Saturaday, Sunday
}
publicclass MainClass {
  publicstaticvoid main(String args[]) {
    System.out.println("Here are all Week constants");
    // use values()
    Week allWeek[] = Week.values();
    for (Week aday : allWeek) {
      System.out.println(aday);
    }
  }
}
java title=Example.java
Here are all Week constants
Monday
Tuesday
Wednesday
Thursday
Friday
Saturaday
Sunday
```
