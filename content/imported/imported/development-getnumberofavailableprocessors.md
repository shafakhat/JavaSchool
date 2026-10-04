---
title: Get Number of Available Processors
nav: Get Number of Available Pr...
description: System.out.println("Number of processors available to the Java Virtual Machine: "
section: Imported
order: 20029
source: http://www.java2s.com:80/Tutorial/Java/0120__Development/GetNumberofAvailableProcessors.htm
---
```java title=Example.java
public class Main {
  public static void main(String[] args) {
    Runtime runtime = Runtime.getRuntime();
    int nrOfProcessors = runtime.availableProcessors();
    System.out.println("Number of processors available to the Java Virtual Machine: "
        + nrOfProcessors);
  }
}
// Number of processors available to the Java Virtual Machine: 2
```
