---
title: Make methods that have unspecified number of parameters
nav: Make methods that have uns...
description: myMethod(new Object[] { "value 1", new Integer(2), "value n" });
section: Imported - java2s Archive
order: 1210
source: https://web.archive.org/web/20140829084058/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/MakemethodsthathaveunspecifiednumberofparameterspassanarrayofObjects.htm
---
```java title=Example.java
public class Main {
  public static void main(String args[]) {
    myMethod(new Object[] { "value 1", new Integer(2), "value n" });
  }
  public static void myMethod(Object parms[]) {
    for (int i = 0; i < parms.length; i++)
      System.out.println(parms[i]);
  }
}
```

| 5.9.1. | Demonstrating variable-length arguments |
|---|---|
| 5.9.2. | Using varargs with standard arguments |
| 5.9.3. | Methods Accepting a Variable Number of objects |
| 5.9.4. | Limiting the object Types in a Variable Argument List |
| 5.9.5. | Demonstrate variable-length arguments. |
| 5.9.6. | Use varargs with standard arguments. |
| 5.9.7. | Overloading Vararg Methods |
| 5.9.8. | Make methods that have unspecified number of parameters:pass an array of Objects |
