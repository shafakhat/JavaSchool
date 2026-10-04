---
title: Get the short name of the specified class by striping off the package name.
nav: Get the short name of the ...
description: * Copyright 2005, JBoss Inc., and individual contributors as indicated
section: Imported - java2s Archive
order: 2130
source: https://web.archive.org/web/20140829080005/http://www.java2s.com/Tutorial/Java/0125__Reflection/Gettheshortnameofthespecifiedclassbystripingoffthepackagename.htm
---
```java title=Example.java
import java.lang.reflect.Method;
import java.net.URL;
import java.security.CodeSource;
import java.security.ProtectionDomain;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
/*
 * JBoss, Home of Professional Open Source
 * Copyright 2005, JBoss Inc., and individual contributors as indicated
 * by the @authors tag. See the copyright.txt in the distribution for a
 * full listing of individual contributors.
 *
 * This is free software; you can redistribute it and/or modify it
 * under the terms of the GNU Lesser General Public License as
 * published by the Free Software Foundation; either version 2.1 of
 * the License, or (at your option) any later version.
 *
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
 * Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public
 * License along with this software; if not, write to the Free
 * Software Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA
 * 02110-1301 USA, or see the FSF site: http://www.fsf.org.
 */
public class Main {
  /** The string used to separator packages */
  public static final String PACKAGE_SEPARATOR = ".";
  /**
   *
   * @param classname
   *          Class name.
   * @return Short class name.
   */
  public static String stripPackageName(final String classname) {
    int idx = classname.lastIndexOf(PACKAGE_SEPARATOR);
    if (idx != -1)
      return classname.substring(idx + 1, classname.length());
    return classname;
  }
}
```

| 7.6.1. | Demonstrate Package |
|---|---|
| 7.6.2. | Get full package name |
| 7.6.3. | Get package name of a class |
| 7.6.4. | getPackage() returns null for a class in the unnamed package |
| 7.6.5. | getPackage() returns null for a primitive type or array |
| 7.6.6. | Find the Package of an Object |
| 7.6.7. | Get the class name with or without the package |
| 7.6.8. | Detect if a package is available |
| 7.6.9. | Get the package name of the specified class. |
| 7.6.10. | Get the short name of the specified class by striping off the package name. |
| 7.6.11. | Get Package Names From Dir |
| 7.6.12. | Get non Package Qualified Name |
| 7.6.13. | Returns the package portion of the specified class |
