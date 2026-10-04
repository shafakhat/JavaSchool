---
title: Get the name of a class
nav: Get the name of a class
description: Imported from the java2s.com archive: Get the name of a class
section: Imported - java2s Archive
order: 2208
source: https://web.archive.org/web/20140829075200/http://www.java2s.com/Tutorial/Java/0125__Reflection/Getthenameofaclass.htm
---
```java title=Example.java
import java.util.Calendar;
import java.math.BigDecimal;
public class Main {
  public static void main(String[] args) {
    // Get the name of the classes below.
    Class clazz = String.class;
    System.out.println("Class Name: " + clazz.getName());
    clazz = Calendar.class;
    System.out.println("Class Name: " + clazz.getName());
    clazz = BigDecimal.class;
    System.out.println("Class Name: " + clazz.getName());
  }
}
```

| 7.14.1. | Getting the Name of a Member Object |
|---|---|
| 7.14.2. | Unqualified names |
| 7.14.3. | Get full class name |
| 7.14.4. | Get the name of a class |
| 7.14.5. | Get the name of an array |
| 7.14.6. | Get the name of void |
| 7.14.7. | Get the unqualified name of a class |
| 7.14.8. | Get the fully-qualified name of a class |
| 7.14.9. | Get the fully-qualified name of a inner class |
| 7.14.10. | Use Class.forName to load a class |
| 7.14.11. | Get the class name in a static method |
