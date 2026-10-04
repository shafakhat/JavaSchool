---
title: Methods Accepting a Variable Number of objects
nav: Methods Accepting a Variab...
description: Imported from the java2s.com archive: Methods Accepting a Variable Number of objects
section: Imported - java2s Archive
order: 1230
source: https://web.archive.org/web/20140829083843/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/MethodsAcceptingaVariableNumberofobjects.htm
---
```java title=Example.java
public class MainClass {
  public static void main(String[] args) {
    printAll(2, "two", 4, "four", 4.5, "four point five");
    printAll();
    printAll(25, "Anything goes", true, 4E4, false);
  }
  public static void printAll(Object... args) {
    for (Object arg : args) {
      System.out.print("  " + arg);
    }
    System.out.println();
  }
}
java title=Example.java
2  two  4  four  4.5  four point five
25  Anything goes  true  40000.0  false
```
