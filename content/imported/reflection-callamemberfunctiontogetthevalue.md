---
title: Call a member function to get the value
nav: Call a member function to ...
description: // $Id: ReflectionHelper.java 16271 2009-04-07 20:20:12Z hardy.ferentschik $
section: Imported - java2s Archive
order: 2099
source: https://web.archive.org/web/20140829092203/http://www.java2s.com/Tutorial/Java/0125__Reflection/Callamemberfunctiontogetthevalue.htm
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
  public static Object getValue(Member member, Object object) {
    Object value = null;
    if ( member instanceof Method ) {
      Method method = ( Method ) member;
      try {
        value = method.invoke( object );
      }
      catch ( IllegalAccessException e ) {
        throw new RuntimeException( "Unable to access " + method.getName(), e );
      }
      catch ( InvocationTargetException e ) {
        throw new RuntimeException( "Unable to access " + method.getName(), e );
      }
    }
    else if ( member instanceof Field ) {
      Field field = ( Field ) member;
      try {
        value = field.get( object );
      }
      catch ( IllegalAccessException e ) {
        throw new RuntimeException( "Unable to access " + field.getName(), e );
      }
    }
    return value;
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
