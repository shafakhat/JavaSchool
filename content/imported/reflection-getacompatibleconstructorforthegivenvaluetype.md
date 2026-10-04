---
title: Get a compatible constructor for the given value type
nav: Get a compatible construct...
description: * Copyright 2005, JBoss Inc., and individual contributors as indicated
section: Imported - java2s Archive
order: 2076
source: https://web.archive.org/web/2014/http://www.java2s.com/Tutorial/Java/0125__Reflection/Getacompatibleconstructorforthegivenvaluetype.htm
---
```java title=Example.java
import java.lang.reflect.Array;
import java.lang.reflect.Constructor;
import java.lang.reflect.Method;
import java.lang.reflect.Modifier;
import java.net.URL;
import java.security.AccessController;
import java.security.CodeSource;
import java.security.PrivilegedAction;
import java.security.ProtectionDomain;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
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
 */public class Main {
  /////////////////////////////////////////////////////////////////////////
 //                           Coercion Methods                          //
 /////////////////////////////////////////////////////////////////////////
 /**
   *
   * @param type       Class to look for constructor in
   * @param valueType  Argument type for constructor
   * @return           Constructor or null
   */ public static Constructor getCompatibleConstructor(final Class type,
                                                     final Class valueType)
  {
     // first try and find a constructor with the exact argument type
 try {
        return type.getConstructor(new Class[] { valueType });
     }
     catch (Exception ignore) {
        // if the above failed, then try and find a constructor with
 // an compatible argument type
 // get an array of compatible types
        Class[] types = type.getClasses();
        for (int i=0; i<types.length; i++) {
           try {
              return type.getConstructor(new Class[] { types[i] });
           }
           catch (Exception ignore2) {}
        }
     }
     // if we get this far, then we can't find a compatible constructor
 return null;
  }
}
```
