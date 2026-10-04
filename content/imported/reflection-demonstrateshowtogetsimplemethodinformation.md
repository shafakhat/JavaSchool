---
title: Demonstrates how to get simple method information
nav: Demonstrates how to get si...
description: * This software is granted under the terms of the Common Public License,
section: Imported - java2s Archive
order: 2101
source: https://web.archive.org/web/20140829092040/http://www.java2s.com/Tutorial/Java/0125__Reflection/Demonstrateshowtogetsimplemethodinformation.htm
---
```java title=Example.java
/*
 *     file: MethodInfoDemo.java
 *  package: oreilly.hcj.reflection
 *
 * This software is granted under the terms of the Common Public License,
 * CPL, which may be found at the following URL:
 * http://www-124.ibm.com/developerworks/oss/CPLv1.0.htm
 *
 * Copyright(c) 2003-2005 by the authors indicated in the @author tags.
 * All Rights are Reserved by the various authors.
 *
 ########## DO NOT EDIT ABOVE THIS LINE ########## */
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
/**
 *
 * @author <a href=mailto:kraythe@arcor.de>Robert Simmons jr. (kraythe)</a>
 * @version $Revision: 1.3 $
 */
public class MethodInfoDemo {
  /**
   * __UNDOCUMENTED__
   *
   * @param obj
   *          __UNDOCUMENTED__
   *
   * @throws IllegalAccessException
   *           __UNDOCUMENTED__
   * @throws InvocationTargetException
   *           __UNDOCUMENTED__
   */
  public static void emptyStrings(final Object obj) throws IllegalAccessException,
      InvocationTargetException {
    final String PREFIX = "set"; //$NON-NLS-1$
    Method[] methods = obj.getClass().getMethods();
    for (int idx = 0; idx < methods.length; idx++) {
      if (methods[idx].getName().startsWith(PREFIX)) {
        if (methods[idx].getParameterTypes()[0] == String.class) {
          methods[idx].invoke(obj, new Object[] { new String() });
        }
      }
    }
  }
  /**
   * Demo method.
   *
   * @param args
   *          Command line arguments.
   */
  public static void main(final String[] args) {
    String s = "";
    printMethodInfo(s);
    try {
      emptyStrings(s);
    } catch (final Exception ex) {
      ex.printStackTrace();
    }
  }
  /**
   * __UNDOCUMENTED__
   *
   * @param obj
   *          __UNDOCUMENTED__
   */
  public static void printMethodInfo(final Object obj) {
    Class type = obj.getClass();
    final Method[] methods = type.getMethods();
    for (int idx = 0; idx < methods.length; idx++) {
      System.out.println(methods[idx]);
    }
  }
}
/* ########## End of File ########## */
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
