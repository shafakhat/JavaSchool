---
title: Reflect All
nav: Reflect All
description: static void describeClassOrInterface(Class className, String name) {
section: Imported - java2s Archive
order: 2079
source: https://web.archive.org/web/20140829082739/http://www.java2s.com/Tutorial/Java/0125__Reflection/ReflectAll.htm
---
```java title=Example.java
import java.lang.reflect.Constructor;
import java.lang.reflect.Field;
import java.lang.reflect.Method;
import java.lang.reflect.Modifier;
public class ReflectApp {
  public static void main(String args[]) {
    String parm = args[0];
    Class className = void.class;
    try {
      className = Class.forName(parm);
    } catch (ClassNotFoundException ex) {
      System.out.println("Not a class or interface.");
      System.exit(0);
    }
    describeClassOrInterface(className, parm);
  }
  static void describeClassOrInterface(Class className, String name) {
    displayModifiers(className.getModifiers());
    displayFields(className.getDeclaredFields());
    displayMethods(className.getDeclaredMethods());
    if (className.isInterface()) {
      System.out.println("Interface: " + name);
    } else {
      System.out.println("Class: " + name);
      displayInterfaces(className.getInterfaces());
      displayConstructors(className.getDeclaredConstructors());
    }
  }
  static void displayModifiers(int m) {
    System.out.println("Modifiers: " + Modifier.toString(m));
  }
  static void displayInterfaces(Class[] interfaces) {
    if (interfaces.length > 0) {
      System.out.println("Interfaces: ");
      for (int i = 0; i < interfaces.length; ++i)
        System.out.println(interfaces[i].getName());
    }
  }
  static void displayFields(Field[] fields) {
    if (fields.length > 0) {
      System.out.println("Fields: ");
      for (int i = 0; i < fields.length; ++i)
        System.out.println(fields[i].toString());
    }
  }
  static void displayConstructors(Constructor[] constructors) {
    if (constructors.length > 0) {
      System.out.println("Constructors: ");
      for (int i = 0; i < constructors.length; ++i)
        System.out.println(constructors[i].toString());
    }
  }
  static void displayMethods(Method[] methods) {
    if (methods.length > 0) {
      System.out.println("Methods: ");
      for (int i = 0; i < methods.length; ++i)
        System.out.println(methods[i].toString());
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
