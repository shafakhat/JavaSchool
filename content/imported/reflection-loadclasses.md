---
title: Load classes
nav: Load classes
description: * This library is free software; you can redistribute it and/or
section: Imported - java2s Archive
order: 2136
source: https://web.archive.org/web/20140829075302/http://www.java2s.com/Tutorial/Java/0125__Reflection/Loadclasses.htm
---
```java title=Example.java
/**
 * EasyBeans
 * Copyright (C) 2006 Bull S.A.S.
 * Contact: easybeans@ow2.org
 *
 * This library is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Lesser General Public
 * License as published by the Free Software Foundation; either
 * version 2.1 of the License, or any later version.
 *
 * This library is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public
 * License along with this library; if not, write to the Free Software
 * Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307
 * USA
 *
 * --------------------------------------------------------------------------
 * $Id: ClassUtils.java 3783 2008-07-30 13:44:06Z benoitf $
 * --------------------------------------------------------------------------
 */
/**
 * The <code>ClassUtils</code> class is the central point used to load classes.
 * @author Guillaume Sauthier
 */
public final class ClassUtils {
    /**
     * Default constructor.
     */
    private ClassUtils() {}
    /**
     * Look up the class in the Tread Context ClassLoader and in the "current" ClassLoader.
     * @param className The class name to load
     * @return the corresponding Class instance
     * @throws ClassNotFoundException if the Class was not found.
     */
    public static Class forName(final String className) throws ClassNotFoundException {
        // Load classes from different classloaders :
        // 1. Thread Context ClassLoader
        // 2. ClassUtils ClassLoader
        ClassLoader tccl = Thread.currentThread().getContextClassLoader();
        Class cls = null;
        try {
            // Try with TCCL
            cls = Class.forName(className, true, tccl);
        } catch (ClassNotFoundException cnfe) {
            // Try now with the classloader used to load ClassUtils
            ClassLoader current = ClassUtils.class.getClassLoader();
            try {
                cls = Class.forName(className, true, current);
            } catch (ClassNotFoundException cnfe2) {
                // If this is still unknown, throw an Exception
                throw cnfe2;
            }
        }
        return cls;
    }
    /**
     * Look up the class in the Tread Context ClassLoader and in the "current" ClassLoader.
     * @param className The class name to load
     * @param clazz a class used to get classloader
     * @return the corresponding Class instance
     * @throws ClassNotFoundException if the Class was not found.
     */
    public static Class forName(final String className, final Class clazz) throws ClassNotFoundException {
        // Load classes from different classloaders :
        // 1. Thread Context ClassLoader
        // 2. ClassUtils ClassLoader
        ClassLoader tccl = Thread.currentThread().getContextClassLoader();
        Class cls = null;
        try {
            // Try with TCCL
            cls = Class.forName(className, true, tccl);
        } catch (ClassNotFoundException cnfe) {
            // Try now with the classloader used to load ClassUtils
            ClassLoader current = clazz.getClassLoader();
            if (current != null) {
                try {
                    cls = Class.forName(className, true, current);
                } catch (ClassNotFoundException cnfe2) {
                    // If this is still unknown, throw an Exception
                    throw new ClassNotFoundException("Class Not found in current ThreadClassLoader '" + tccl + "' and in '" + current + "' classloaders.", cnfe2);
                }
            } else {
                // rethrow exception
                throw cnfe;
            }
        }
        return cls;
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
