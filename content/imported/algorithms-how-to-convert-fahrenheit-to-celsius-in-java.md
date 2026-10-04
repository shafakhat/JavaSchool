---
title: How to Convert Fahrenheit to Celsius in Java
nav: How to Convert Fahrenheit ...
description: //from j a v a2s.com public static void main(String[] args) {
section: Imported - java2s Archive
order: 1082
source: https://web.archive.org/web/20140118015651/http://java2s.com/Tutorials/Java/Algorithms/How_to_Convert_Fahrenheit_to_Celsius_in_Java.htm
---
### Convert Fahrenheit to Celsius

To Convert Fahrenheit to Celsius:

- Take the temperature in Fahrenheit subtract 32.
- Divide by 1.8.
- The result is degrees Celsius.

```java title=Example.java
public class Main {
public static void main(String[] args) {
    for (int i=-40; i<=120; i+=10) {
      float c = (i-32)*(5f/9);
      System.out.println("fahrenheit "+i + " to celsius " + c);
    }
  }
}
```

The code above generates the following result.

To Convert Celsius to Fahrenheit

- Take the temperature in Celsius and multiply 1.8.
- Add 32 degrees.
- The result is degrees Fahrenheit.

#### Next chapter...

What you will learn in the next chapter:

- What is Java Format Class
- Syntax for format method
- Note for format method
- Example - format method
