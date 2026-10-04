---
title: Automatic Type Promotion in Expressions
nav: Automatic Type Promotion i...
description: System.out.println((f * b) + " + " + (i / c) + " - " + (d * s));
section: Imported - java2s Archive
order: 1308
source: https://web.archive.org/web/20140829083432/http://www.java2s.com/Tutorial/Java/0040__Data-Type/AutomaticTypePromotioninExpressions.htm
---
```java title=Example.java
byte b = 50;
   b = (byte)(b * 2);
java title=Example.java
public class MainClass {
  public static void main(String args[]) {
    byte b = 42;
    char c = 'a';
    short s = 1024;
    int i = 50000;
    float f = 5.67f;
    double d = .1234;
    double result = (f * b) + (i / c) - (d * s);
    System.out.println((f * b) + " + " + (i / c) + " - " + (d * s));
    System.out.println("result = " + result);
  }
}
java title=Example.java
238.14 + 515 - 126.3616
result = 626.7784146484375
```

| 2.16.1. | The Widening Conversion |
|---|---|
| 2.16.2. | The Narrowing Conversion |
| 2.16.3. | Narrowing conversion with information loss |
| 2.16.4. | An automatic type conversion |
| 2.16.5. | Casting Incompatible Types |
| 2.16.6. | Pass a string to the Integer class constructor and call the intValue() |
| 2.16.7. | Use toString method of Integer class to conver Integer into String. |
| 2.16.8. | Declaring Checked Exceptions |
| 2.16.9. | Automatic Type Promotion in Expressions |
| 2.16.10. | Convert byte array to Integer and Long |
| 2.16.11. | Class with methods for type conversion |
| 2.16.12. | Data type conversion |
| 2.16.13. | Convert primitive back and forth |
