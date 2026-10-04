---
title: Call all possible exceptions during method invocation with reflection
nav: Call all possible exceptio...
description: System.out.println("Invoked static method: " + args[1] + " of class: " + args[0]
section: Imported - java2s Archive
order: 2113
source: https://web.archive.org/web/20140829091917/http://www.java2s.com/Tutorial/Java/0125__Reflection/Callallpossibleexceptionsduringmethodinvocationwithreflection.htm
---
```java title=Example.java
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
public class Invoke {
  public static void main(String[] args) {
    try {
      Class c = Class.forName(args[0]);
      Method m = c.getMethod(args[1]);
      Object ret = m.invoke(null);
      System.out.println("Invoked static method: " + args[1] + " of class: " + args[0]
          + " with no args\nResults: " + ret);
    } catch (ClassNotFoundException e) {
      System.out.println(e);
    } catch (NoSuchMethodException e2) {
      System.out.println(e2);
    } catch (IllegalAccessException e3) {
      System.out.println(e3);
    } catch (InvocationTargetException e) {
      System.out.println(e);
      System.out.println("Method threw an: " + e.getTargetException());
    }
  }
}
```

| 7.5.1. | List methods of a class using Reflection |
|---|---|
| 7.5.2. | Design your own class loader |
| 7.5.3. | Get method my parameters |
| 7.5.4. | Show public methods. |
| 7.5.5. | Method Inspector |
| 7.5.6. | Invoke methods of an object using reflection |
| 7.5.7. | Call a member function to get the value |
| 7.5.8. | Prints out the declared methods on java.lang.Number |
| 7.5.9. | Demonstrates how to get simple method information |
| 7.5.10. | Prints out the declared methods on java.lang.Object |
| 7.5.11. | Demonstrates how to get specific method information |
| 7.5.12. | Get the current method name |
| 7.5.13. | Get the current method name With JDK1.5 |
| 7.5.14. | Get method from a class by name |
| 7.5.15. | Get super class and all its declared methods |
| 7.5.16. | Invoke a method with parameter |
| 7.5.17. | Call a class method with 2 arguments |
| 7.5.18. | Call all possible exceptions during method invocation with reflection |
| 7.5.19. | get Declared Method by name and parameter type |
| 7.5.20. | Getting the Methods of a Class Object: By obtaining a list of all declared methods |
| 7.5.21. | Getting the Methods of a Class Object: By obtaining a list of all public methods, both declared and inherited. |
| 7.5.22. | Getting the Methods of a Class Object: By obtaining a particular Method object. |
| 7.5.23. | Invoke method with wrong parameters |
| 7.5.24. | Checks whether the specified class contains a method matching the specified name. |
| 7.5.25. | Find method |
| 7.5.26. | Returns method with the specified name |
| 7.5.27. | Sorts methods according to their name, number of parameters, and parameter types. |
| 7.5.28. | Contains Same Method Signature |
