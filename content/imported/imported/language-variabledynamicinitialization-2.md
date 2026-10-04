---
title: Variable Dynamic Initialization
nav: Variable Dynamic Initializ...
description: Imported from the java2s.com archive: Variable Dynamic Initialization
section: Imported - java2s Archive
order: 1005
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0020__Language/VariableDynamicInitialization.htm
---
```java title=Example.java
publicclass MainClass {
  publicstaticvoid main(String args[]) {
    double a = 3.0, b = 4.0;

    // c is dynamically initialized
double c = Math.sqrt(a * a + b * b);

    System.out.println("Hypotenuse is " + c);
  }
}
```

```java title=Example.java
Hypotenuse is 5.0
```
