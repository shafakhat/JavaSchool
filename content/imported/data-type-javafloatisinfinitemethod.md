---
title: Java Float isInfinite Method
nav: Java Float isInfinite Method
description: Imported from the java2s.com archive: Java Float isInfinite Method
section: Imported - java2s Archive
order: 1203
source: https://web.archive.org/web/20140829080150/http://www.java2s.com/Tutorial/Java/0040__Data-Type/JavaFloatisInfiniteMethod.htm
---
```java title=Example.java
public class Main {
  public static void main(String[] args) {
    float f = (float) 1 / 0;
    boolean b1 = Float.isInfinite(f);
    System.out.println(b1);
    Float fObj = new Float(f);
    boolean b2 = fObj.isInfinite();
    System.out.println(b2);
  }
}
```

| 2.11.1. | Java float is 32 bit single precision type and used when fractional precision calculation is required. |
|---|---|
| 2.11.2. | Floating­Point Types |
| 2.11.3. | Min and Max values of data type float |
| 2.11.4. | Use Float constructor to convert float primitive type to a Float object. |
| 2.11.5. | Java Float Comparison |
| 2.11.6. | Java Float isInfinite Method |
| 2.11.7. | Java Float isNaN Method |
| 2.11.8. | Java Float Wrapper Class |
| 2.11.9. | Pass floats as string literals to a method |
| 2.11.10. | Check if a string is a valid number |
| 2.11.11. | Use toString method of Float class to convert Float into String. |
| 2.11.12. | Declaring a variable of type float |
| 2.11.13. | Declaring more than one float variable in a single statement |
| 2.11.14. | Use Float.valueOf to convert string value to float |
| 2.11.15. | Convert Java Float to Numeric Primitive Data Types |
| 2.11.16. | Convert Java String to Float Object |
| 2.11.17. | Convert from float to String |
| 2.11.18. | Convert from String to float |
| 2.11.19. | Converting a String to a float type Number |
| 2.11.20. | Compare Two Java float Arrays |
| 2.11.21. | Compares two floats for order. |
| 2.11.22. | For a float value x, this method returns +1.0F if x >= 0 and -1.0F if x < 0. Returns NaN if x is NaN. |
| 2.11.23. | Tests two float arrays for equality. |
| 2.11.24. | Use System.out.printf to format float point number |
