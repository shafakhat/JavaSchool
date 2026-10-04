---
title: Java Reflection Field Access
nav: Java Reflection Field Access
description: To access non-accessible fields, methods, and constructors of a class using reflection call setAccessible(boolean flag) method from AccessibleObject class.
section: Imported - java2s Archive
order: 50408
source: https://www.java2s.com/Tutorials/Java/Java_Reflection/0080__Java_Field_Access.html
---
We can get or set a field using reflection in two steps.

- get the reference of the field.
- To read the field's value, call the getXxx() method on the field, where Xxx is the data type of the field.
- To set the value of a field, you call the corresponding setXxx() method.

Static and instance fields are accessed the same way.

## Example

```java title=Example.java
import java.lang.reflect.Field;
class MyClass {
  public String name = "Unknown";
  public MyClass() {
  }
  public String toString() {
    return"name=" + this.name;
  }
}
publicclass Main {
  publicstaticvoid main(String[] args) {
    Class<MyClass> ppClass = MyClass.class;
    try {
      MyClass p = ppClass.newInstance();
      Field name = ppClass.getField("name");
      String nameValue = (String) name.get(p);
      System.out.println("Current name is " + nameValue);
      name.set(p, "abc");
      nameValue = (String) name.get(p);
      System.out.println("New  name is " + nameValue);
    } catch (InstantiationException | IllegalAccessException
        | NoSuchFieldException | SecurityException | IllegalArgumentException e) {
      System.out.println(e.getMessage());
    }
  }
}
```

The code above generates the following result.

## Bypassing Accessibility Check

To access non-accessible fields, methods, and constructors of a class using reflection call setAccessible(boolean flag) method from AccessibleObject class.

We need to call this method with a true argument to make that field, method, and constructor accessible.

```java title=Example.java
import java.lang.reflect.Field;
class MyClass {
  private String name = "Unknown";
  public MyClass() {
  }
  public String toString() {
    return"name=" + this.name;
  }
}
publicclass Main {
  publicstaticvoid main(String[] args) {
    Class<MyClass> my = MyClass.class;
    try {
      MyClass p = my.newInstance();
      Field nameField = my.getDeclaredField("name");
      nameField.setAccessible(true);
      String nameValue = (String) nameField.get(p);
      System.out.println("Current name is " + nameValue);
      nameField.set(p, "abc");
      nameValue = (String) nameField.get(p);
      System.out.println("New name is " + nameValue);
    } catch (InstantiationException | IllegalAccessException
        | NoSuchFieldException | SecurityException | IllegalArgumentException e) {
      System.out.println(e.getMessage());
    }
  }
}
```

The code above generates the following result.

- « Previous
