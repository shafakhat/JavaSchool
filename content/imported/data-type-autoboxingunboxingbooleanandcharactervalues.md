---
title: Autoboxing/Unboxing Boolean and Character Values
nav: Autoboxing/Unboxing Boolea...
description: Imported from the java2s.com archive: Autoboxing/Unboxing Boolean and Character Values
section: Imported - java2s Archive
order: 1310
source: https://web.archive.org/web/20140829091949/http://www.java2s.com/Tutorial/Java/0040__Data-Type/AutoboxingUnboxingBooleanandCharacterValues.htm
---
```java title=Example.java
public class MainClass {
  public static void main(String args[]) {
    Boolean booleanObject = true;
    if (booleanObject){
      System.out.println("b is true");
    }
    Character ch = 'x'; // box a char
    char ch2 = ch; // unbox a char
    System.out.println("ch2 is " + ch2);
  }
}
java title=Example.java
b is true
ch2 is x
```

| 2.18.1. | Type conversion (JDK1.5 Autoboxing/Unboxing) |
|---|---|
| 2.18.2. | Boxing and Unboxing |
| 2.18.3. | Autoboxing and Auto-Unboxing |
| 2.18.4. | Manually boxes the value 100 into an Integer |
| 2.18.5. | The modern way to construct an Integer object that has the value 100 |
| 2.18.6. | To unbox an object |
| 2.18.7. | Autoboxing/unboxing: an argument passed to a method or returned from a method |
| 2.18.8. | Autoboxing/unboxing occurs inside expressions |
| 2.18.9. | Auto-unboxing: mix different types of numeric objects in an expression. |
| 2.18.10. | Using an integer object to control a switch statement |
| 2.18.11. | Autoboxing/Unboxing Boolean and Character Values |
| 2.18.12. | Autoboxing/unboxing takes place with method parameters and return values. |
| 2.18.13. | Auto-unboxing allows you to mix different types of numeric objects in an expression. |
