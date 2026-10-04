---
title: Analyze ClassLoader hierarchy for any given object or class loader
nav: Analyze ClassLoader hierar...
description: * Licensed under the Apache License, Version 2.0 (the "License");
section: Imported - java2s Archive
order: 2151
source: https://web.archive.org/web/20140829075532/http://www.java2s.com/Tutorial/Java/0125__Reflection/AnalyzeClassLoaderhierarchyforanygivenobjectorclassloader.htm
---
```java title=Example.java
/*
 * Copyright 2002-2005 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
/**
 * Utility class for diagnostic purposes, to analyze the
 * ClassLoader hierarchy for any given object or class loader.
 *
 * @author Rod Johnson
 * @author Juergen Hoeller
 * @since 02 April 2001
 * @see java.lang.ClassLoader
 */
public abstract class ClassLoaderUtils {
  /**
   * Show the class loader hierarchy for this class.
   * Uses default line break and tab text characters.
   * @param obj object to analyze loader hierarchy for
   * @param role a description of the role of this class in the application
   * (e.g., "servlet" or "EJB reference")
   * @return a String showing the class loader hierarchy for this class
   */
  public static String showClassLoaderHierarchy(Object obj, String role) {
    return showClassLoaderHierarchy(obj, role, "\n", "\t");
  }
  /**
   * Show the class loader hierarchy for this class.
   * @param obj object to analyze loader hierarchy for
   * @param role a description of the role of this class in the application
   * (e.g., "servlet" or "EJB reference")
   * @param lineBreak line break
   * @param tabText text to use to set tabs
   * @return a String showing the class loader hierarchy for this class
   */
  public static String showClassLoaderHierarchy(Object obj, String role, String lineBreak, String tabText) {
    String s = "object of " + obj.getClass() + ": role is " + role + lineBreak;
    return s + showClassLoaderHierarchy(obj.getClass().getClassLoader(), lineBreak, tabText, 0);
  }
  /**
   * Show the class loader hierarchy for the given class loader.
   * Uses default line break and tab text characters.
   * @param cl class loader to analyze hierarchy for
   * @return a String showing the class loader hierarchy for this class
   */
  public static String showClassLoaderHierarchy(ClassLoader cl) {
    return showClassLoaderHierarchy(cl, "\n", "\t");
  }
  /**
   * Show the class loader hierarchy for the given class loader.
   * @param cl class loader to analyze hierarchy for
   * @param lineBreak line break
   * @param tabText text to use to set tabs
   * @return a String showing the class loader hierarchy for this class
   */
  public static String showClassLoaderHierarchy(ClassLoader cl, String lineBreak, String tabText) {
    return showClassLoaderHierarchy(cl, lineBreak, tabText, 0);
  }
  /**
   * Show the class loader hierarchy for the given class loader.
   * @param cl class loader to analyze hierarchy for
   * @param lineBreak line break
   * @param tabText text to use to set tabs
   * @param indent nesting level (from 0) of this loader; used in pretty printing
   * @return a String showing the class loader hierarchy for this class
   */
  private static String showClassLoaderHierarchy(ClassLoader cl, String lineBreak, String tabText, int indent) {
    if (cl == null) {
      ClassLoader ccl = Thread.currentThread().getContextClassLoader();
      return "context class loader=[" + ccl + "] hashCode=" + ccl.hashCode();
    }
    StringBuffer buf = new StringBuffer();
    for (int i = 0; i < indent; i++) {
      buf.append(tabText);
    }
    buf.append("[").append(cl).append("] hashCode=").append(cl.hashCode()).append(lineBreak);
    ClassLoader parent = cl.getParent();
    return buf.toString() + showClassLoaderHierarchy(parent, lineBreak, tabText, indent + 1);
  }
}
```

| 7.7.1. | URL class loader |
|---|---|
| 7.7.2. | extends URLClassLoader |
| 7.7.3. | Load classes |
| 7.7.4. | how to use reflection to print the names and values of all nonstatic fields of an object |
| 7.7.5. | Runs a jar application from any url |
| 7.7.6. | BufferedReader reflection |
| 7.7.7. | Get the class By way of an object |
| 7.7.8. | Get the class By way of a string |
| 7.7.9. | Get the class By way of .class |
| 7.7.10. | Catch InvocationTargetException |
| 7.7.11. | Determining from Where a Class Was Loaded |
| 7.7.12. | Dynamically Reloading a Modified Class |
| 7.7.13. | Creating an Object Using a Constructor Object |
| 7.7.14. | Create an object from a string |
| 7.7.15. | Using the forName() method |
| 7.7.16. | Context ClassLoader |
| 7.7.17. | A tree structure that maps inheritance hierarchies of classes |
| 7.7.18. | Analyze ClassLoader hierarchy for any given object or class loader |
| 7.7.19. | Instantiate unknown class at runtime and call the object's methods |
| 7.7.20. | Load Class |
