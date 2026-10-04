---
title: Context ClassLoader
nav: Context ClassLoader
description: /**************************************************************************************
section: Imported - java2s Archive
order: 2158
source: https://web.archive.org/web/2014/http://www.java2s.com/Tutorial/Java/0125__Reflection/ContextClassLoader.htm
---
```java title=Example.java
/**************************************************************************************
 * Copyright (c) Jonas BonŽr, Alexandre Vasseur. All rights reserved.                 *
 * http://aspectwerkz.codehaus.org                                                    *
 * ---------------------------------------------------------------------------------- *
 * The software in this package is published under the terms of the LGPL license      *
 * a copy of which has been included with this distribution in the license.txt file.  *
 **************************************************************************************/
import java.io.InputStream;
import java.net.URL;
/**
 * Utility methods dealing with the context class loader. Fail-over is provided to the default class loader.
 *
 * @author <a href="mailto:jboner@codehaus.org">Jonas BonŽr </a>
 */
public final class ContextClassLoader {
    /**
     * Loads a class starting from the given class loader (can be null, then use default class loader)
     *
     * @param loader
     * @param name   of class to load
     * @return
     * @throws ClassNotFoundException
     */
    public static Class forName(final ClassLoader loader, final String name) throws ClassNotFoundException {
        Class klass = null;
        if (loader != null) {
            klass = Class.forName(name, false, loader);
        } else {
            klass = Class.forName(name, false, ClassLoader.getSystemClassLoader());
        }
        return klass;
    }
    /**
     * Loads a class from the context class loader or, if that fails, from the default class loader.
     *
     * @param name is the name of the class to load.
     * @return a <code>Class</code> object.
     * @throws ClassNotFoundException if the class was not found.
     */
    public static Class forName(final String name) throws ClassNotFoundException {
        Class cls = null;
        try {
            cls = Class.forName(name, false, Thread.currentThread().getContextClassLoader());
        } catch (Exception e) {
            cls = Class.forName(name);
        }
        return cls;
    }
    /**
     * Loads a resource from the context class loader or, if that fails, from the default class loader.
     *
     * @param name is the name of the resource to load.
     * @return a <code>URL</code> object.
     */
    public static URL loadResource(final String name) {
        try {
            return Thread.currentThread().getContextClassLoader().getResource(name);
        } catch (Exception e) {
            return ClassLoader.class.getClassLoader().getResource(name);
        }
    }
//    /**
//     * Loads a resource from the context class loader or, if that fails, from the default class loader, as stream
//     *
//     * @param name is the name of the resource to load.
//     * @return a <code>InputStream</code> object.
//     */
//    public static InputStream getResourceAsStream(final String name) {
//        InputStream stream = null;
//        ClassLoader contextClassLoader = Thread.currentThread().getContextClassLoader();
//        if (contextClassLoader != null) {
//            stream = contextClassLoader.getResourceAsStream(name);
//        }
//        if (stream == null) {
//            ClassLoader classLoader = ClassLoader.class.getClassLoader();
//            if (classLoader != null) {
//                stream = classLoader.getResourceAsStream(name);
//            }
//        }
//        return stream;
//    }
    /**
     * Returns the context class loader.
     *
     * @return the context class loader
     */
    public static ClassLoader getLoader() {
        ClassLoader loader = Thread.currentThread().getContextClassLoader();
        if (loader == null) {
            loader = ClassLoader.class.getClassLoader();
        }
        return loader;
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
