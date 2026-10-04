---
title: Pass a string to the Integer class constructor and call the intValue()
nav: Pass a string to the Integ...
description: Imported from the java2s.com archive: Pass a string to the Integer class constructor and call the intValue()
section: Imported - java2s Archive
order: 1264
source: https://web.archive.org/web/20140620235359/http://www.java2s.com/Tutorial/Java/0040__Data-Type/PassastringtotheIntegerclassconstructorandcalltheintValue.htm
---
```java title=Example.java
public class Main {
  public static void main(String[] argv) {
    String sValue = "5";
    try {
      int iValue = new Integer(sValue).intValue();
    } catch (NumberFormatException ex) {
      ex.printStackTrace();
    }
  }
}
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
