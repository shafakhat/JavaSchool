---
title: Get all methods including the inherited method. Using the getMethods(), we can only access public methods.
nav: Get all methods including ...
description: System.out.println("Method name = " + method.getName());
section: Imported - java2s Archive
order: 2200
source: https://web.archive.org/web/2018/http://www.java2s.com/Tutorial/Java/0125__Reflection/GetallmethodsincludingtheinheritedmethodUsingthegetMethodswecanonlyaccesspublicmethods.htm
---
```java title=Example.java
import java.lang.reflect.Method;
class GetMethods {
  public int add(int numberA, int numberB) {
    return numberA + numberB;
  }
  protected int multiply(int numberA, int numberB) {
    return numberA * numberB;
  }
  private double div(int numberA, int numberB) {
    return numberA / numberB;
  }
}
public class Main {
  public static void main(String[] args) throws Exception {
    GetMethods object = new GetMethods();
    Class clazz = object.getClass();
    Method[] methods = clazz.getMethods();
    for (Method method : methods) {
      System.out.println("Method name        = " + method.getName());
      System.out.println("Method return type = " + method.getReturnType().getName());
      Class[] paramTypes = method.getParameterTypes();
      for (Class c : paramTypes) {
        System.out.println("Param type         = " + c.getName());
      }
    }
    Method method = clazz.getMethod("add", new Class[] { int.class, int.class });
    System.out.println("Method name: " + method.getName());
  }
}
```

| 7.13.1. | Get super class of an object |
|---|---|
| 7.13.2. | Superclass of Object is null |
| 7.13.3. | Get all methods including the inherited method. Using the getMethods(), we can only access public methods. |
| 7.13.4. | The superclass of primitive types is always null |
| 7.13.5. | Getting the Superclass of an Object |
| 7.13.6. | Is Inheritable |
