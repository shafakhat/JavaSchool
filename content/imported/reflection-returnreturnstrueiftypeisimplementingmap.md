---
title: Return Returns true if type is implementing Map
nav: Return Returns true if typ...
description: // $Id: ReflectionHelper.java 16271 2009-04-07 20:20:12Z hardy.ferentschik $
section: Imported - java2s Archive
order: 2062
source: https://web.archive.org/web/20140104010613/http://www.java2s.com/Tutorial/Java/0125__Reflection/ReturnReturnstrueiftypeisimplementingMap.htm
---
```java title=Example.java
// $Id: ReflectionHelper.java 16271 2009-04-07 20:20:12Z hardy.ferentschik $
/*
* JBoss, Home of Professional Open Source
* Copyright 2008, Red Hat Middleware LLC, and individual contributors
* by the @authors tag. See the copyright.txt in the distribution for a
* full listing of individual contributors.
*
* Licensed under the Apache License, Version 2.0 (the "License");
* you may not use this file except in compliance with the License.
* You may obtain a copy of the License at
* http://www.apache.org/licenses/LICENSE-2.0
* Unless required by applicable law or agreed to in writing, software
* distributed under the License is distributed on an "AS IS" BASIS,
* WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
* See the License for the specific language governing permissions and
* limitations under the License.
*/
import java.beans.Introspector;
import java.lang.annotation.Annotation;
import java.lang.reflect.AccessibleObject;
import java.lang.reflect.Field;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Member;
import java.lang.reflect.Method;
import java.lang.reflect.Modifier;
import java.lang.reflect.ParameterizedType;
import java.lang.reflect.Type;
import java.lang.reflect.WildcardType;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Iterator;
import java.util.List;
import java.util.Map;
/**
 * Some reflection utility methods.
 *
 * @author Hardy Ferentschik
 */
public class ReflectionHelper {
  /**
   * @param type the type to check.
   *
   * @return Returns <code>true</code> if <code>type</code> is implementing <code>Map</code>, <code>false</code> otherwise.
   */
  public static boolean isMap(Type type) {
    if ( type instanceof Class && isMapClass( ( Class ) type ) ) {
      return true;
    }
    if ( type instanceof ParameterizedType ) {
      return isMap( ( ( ParameterizedType ) type ).getRawType() );
    }
    if ( type instanceof WildcardType ) {
      Type[] upperBounds = ( ( WildcardType ) type ).getUpperBounds();
      return upperBounds.length != 0 && isMap( upperBounds[0] );
    }
    return false;
  }
  /**
   * Checks whether the specified class parameter is an instance of a collection class.
   *
   * @param clazz <code>Class</code> to check.
   *
   * @return <code>true</code> is <code>clazz</code> is instance of a collection class, <code>false</code> otherwise.
   */
  private static boolean isMapClass(Class<?> clazz) {
    List<Class<?>> classes = new ArrayList<Class<?>>();
    computeClassHierarchy( clazz, classes );
    return classes.contains( Map.class );
  }
  /**
   * Get all superclasses and interfaces recursively.
   *
   * @param clazz The class to start the search with.
   * @param classes List of classes to which to add all found super classes and interfaces.
   */
  private static void computeClassHierarchy(Class<?> clazz, List<Class<?>> classes) {
    for ( Class current = clazz; current != null; current = current.getSuperclass() ) {
      if ( classes.contains( current ) ) {
        return;
      }
      classes.add( current );
      for ( Class currentInterface : current.getInterfaces() ) {
        computeClassHierarchy( currentInterface, classes );
      }
    }
  }
}
```

| 7.2.1. | The superclass of interfaces is always null |
|---|---|
| 7.2.2. | Listing the Interfaces That an Interface Extends |
| 7.2.3. | Checking whether String is an interface or class |
| 7.2.4. | If a class object is an interface or a class |
| 7.2.5. | Listing the Interfaces That a Class Implements |
| 7.2.6. | Although the type of o2 is an interface, getSuperclass() returns the object's superclass |
| 7.2.7. | The interfaces for a primitive type is an empty array |
| 7.2.8. | Return Returns true if type is implementing Map |
| 7.2.9. | Returns true if a class implements Serializable and false otherwise. |
| 7.2.10. | Get Super Interfaces |
| 7.2.11. | Get all interface and object classes that are generalizations of the provided class |
