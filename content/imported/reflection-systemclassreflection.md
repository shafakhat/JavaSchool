---
title: System class reflection
nav: System class reflection
description: Imported from the java2s.com archive: System class reflection
section: Imported - java2s Archive
order: 2081
source: https://web.archive.org/web/20140829085200/http://www.java2s.com/Tutorial/Java/0125__Reflection/Systemclassreflection.htm
---
```java title=Example.java
import java.lang.reflect.Constructor;
import java.lang.reflect.Field;
import java.lang.reflect.Method;
public class ReflectionDemo1 {
  public static void main(String args[]) {
    try {
      Class c = Class.forName("java.awt.Dimension");
      System.out.println("Constructors:");
      Constructor constructors[] = c.getConstructors();
      for (int i = 0; i < constructors.length; i++) {
        System.out.println(" " + constructors[i]);
      }
      System.out.println("Fields:");
      Field fields[] = c.getFields();
      for (int i = 0; i < fields.length; i++) {
        System.out.println(" " + fields[i]);
      }
      System.out.println("Methods:");
      Method methods[] = c.getMethods();
      for (int i = 0; i < methods.length; i++) {
        System.out.println(" " + methods[i]);
      }
    } catch (Exception e) {
      System.out.println("Exception: " + e);
    }
  }
}
```

| 7.4.1. | Recursively get all fields for a hierarchical class tree |
|---|---|
| 7.4.2. | Reflect All |
| 7.4.3. | System class reflection |
| 7.4.4. | Get all declared fields from a class |
| 7.4.5. | Getting the Field Objects of a Class Object: By obtaining a list of all declared fields. |
| 7.4.6. | Getting the Field Objects of a Class Object: By obtaining a list of all public fields, both declared and inherited. |
| 7.4.7. | Getting the Field Objects of a Class Object: By obtaining a particular Field object. |
| 7.4.8. | Reflection, Introspection, and Naming |
| 7.4.9. | Get the name of a primitive type |
| 7.4.10. | Getting and Setting the Value of a Field (assumes that the field has the type int) |
| 7.4.11. | Retrieving a Predefined Color by Name |
| 7.4.12. | Get a variable value from the variable name |
| 7.4.13. | Return a list of all fields (whatever access status, and on whatever superclass they were defined) that can be found on this class. |
| 7.4.14. | Checks whether the specified class contains a field matching the specified name. |
| 7.4.15. | Return Retrurns the Type of the given Field or Method |
