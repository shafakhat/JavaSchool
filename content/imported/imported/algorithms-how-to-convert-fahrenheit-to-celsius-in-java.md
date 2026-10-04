---
title: How to Convert Fahrenheit to Celsius in Java
nav: How to Convert Fahrenheit ...
description: Next »« PreviousHome » Java Tutorial » AlgorithmsBubble sortBinary SearchInsertion SortSelection sortShell sortHeap SortMerge SortQuick SortFibonacciHanoi puzzleFahrenhei
section: Imported - java2s Archive
order: 1001
source: https://web.archive.org/web/20130831232422/http://java2s.com/Tutorials/Java/Algorithms/How_to_Convert_Fahrenheit_to_Celsius_in_Java.htm
---
In this chapter you will learn:

- Convert Fahrenheit to Celsius

### Convert Fahrenheit to Celsius

To Convert Fahrenheit to Celsius:

- Take the temperature in Fahrenheit subtract 32.
- Divide by 1.8.
- The result is degrees Celsius.

```java title=Example.java
publicclass Main {
/*java2s.com*/publicstaticvoid main(String[] args) {
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

- A growable int array
