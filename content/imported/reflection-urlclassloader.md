---
title: URL class loader
nav: URL class loader
description: Imported from the java2s.com archive: URL class loader
section: Imported - java2s Archive
order: 2134
source: https://web.archive.org/web/20140829075500/http://www.java2s.com/Tutorial/Java/0125__Reflection/URLclassloader.htm
---
```java title=Example.java
import java.lang.reflect.Method;
import java.net.URL;
import java.net.URLClassLoader;
public class MainClass {
  static public void main(String args[]) throws Exception {
    URL myurl[] = { new URL("file:///C:/CH3/ClassLoader/web/"),
        new URL("http://www.java2s.edu/~xyx/test/") };
    URLClassLoader x = new URLClassLoader(myurl);
    Class c = x.loadClass("TestURL");
    Class getArg1[] = { (new String[1]).getClass() };
    Method m = c.getMethod("main", getArg1);
    String[] my1 = { "arg1 passed", "arg2 passed" };
    Object myarg1[] = { my1 };
    m.invoke(null, myarg1);
    Object ob = c.newInstance();
    Class arg2[] = {};
    Method m2 = c.getMethod("tt", arg2);
    m2.invoke(ob, null);
    Class arg3[] = { (new String()).getClass(), int.class };
    Method m3 = c.getMethod("tt", arg3);
    Object myarg2[] = { "Arg1", new Integer(100) };
    m3.invoke(ob, myarg2);
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
