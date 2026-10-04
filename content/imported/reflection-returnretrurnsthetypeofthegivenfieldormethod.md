---
title: Return Retrurns the Type of the given Field or Method
nav: Return Retrurns the Type o...
description: // $Id: ReflectionHelper.java 16271 2009-04-07 20:20:12Z hardy.ferentschik $
section: Imported - java2s Archive
order: 2092
source: https://web.archive.org/web/20140829083509/http://www.java2s.com/Tutorial/Java/0125__Reflection/ReturnRetrurnstheTypeofthegivenFieldorMethod.htm
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
   * @param member The <code>Member</code> instance for which to retrieve the type.
   *
   * @return Retrurns the <code>Type</code> of the given <code>Field</code> or <code>Method</code>.
   *
   * @throws IllegalArgumentException in case <code>member</code> is not a <code>Field</code> or <code>Method</code>.
   */
  public static Type typeOf(Member member) {
    if ( member instanceof Field ) {
      return ( ( Field ) member ).getGenericType();
    }
    if ( member instanceof Method ) {
      return ( ( Method ) member ).getGenericReturnType();
    }
    throw new IllegalArgumentException( "Member " + member + " is neither a field nor a method" );
  }
}
```

| 7.4.1. | Recursively get all fields for a hierarchical class tree |
|---|---|
| 7.4.2. | Reflect All |
| 7.4.3. | System class reflection |
| 7.4.4. | Get all declared fields from a class |
| 7.4.5. | Getting the Field Objects of a Class Object: By obtaining a list of all declared fields. |
| 7.4.6. | Getting the Field Objects of a Class Object: By obtaining a list of all public fields, both declared and inherited. |
| 7.4.7. | Getting the Field Objects of a Class Object: By obtaining a particular Field object. |
| 7.4.8. | Reflection, Introspection, and Naming |
| 7.4.9. | Get the name of a primitive type |
| 7.4.10. | Getting and Setting the Value of a Field (assumes that the field has the type int) |
| 7.4.11. | Retrieving a Predefined Color by Name |
| 7.4.12. | Get a variable value from the variable name |
| 7.4.13. | Return a list of all fields (whatever access status, and on whatever superclass they were defined) that can be found on this class. |
| 7.4.14. | Checks whether the specified class contains a field matching the specified name. |
| 7.4.15. | Return Retrurns the Type of the given Field or Method |
