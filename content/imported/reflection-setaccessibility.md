---
title: Set Accessibility
nav: Set Accessibility
description: // $Id: ReflectionHelper.java 16271 2009-04-07 20:20:12Z hardy.ferentschik $
section: Imported - java2s Archive
order: 2188
source: https://web.archive.org/web/20140829093206/http://www.java2s.com/Tutorial/Java/0125__Reflection/SetAccessibility.htm
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
  public static void setAccessibility(Member member) {
    if ( !Modifier.isPublic( member.getModifiers() ) ) {
      //Sun's ease of use, sigh...
      ( ( AccessibleObject ) member ).setAccessible( true );
    }
  }
}
```

| 7.12.1. | Return true if the integer argument includes the public modifier, false otherwise |
|---|---|
| 7.12.2. | Return true if the integer argument includes the private modifier, false otherwise. |
| 7.12.3. | Return true if the integer argument includes the protected modifier,false otherwise. |
| 7.12.4. | Return true if the integer argument includes the static modifier, false otherwise. |
| 7.12.5. | Return true if the integer argument includes the final modifier, false otherwise. |
| 7.12.6. | Return true if the integer argument includes the abstract modifier, false otherwise. |
| 7.12.7. | Get all object accessible public fields |
| 7.12.8. | Overriding Default Access |
| 7.12.9. | Listing the Modifiers of a Class Object |
| 7.12.10. | Listing the Modifiers of a Member Object: Field, Constructor, and Method are all subclasses of Member. |
| 7.12.11. | Set Accessibility |
| 7.12.12. | Make AccessibleObject Accessible |
| 7.12.13. | Make field accessible, explicitly setting it accessible |
| 7.12.14. | whether given field is a "public static final" constant |
| 7.12.15. | Gets a method and forces it to be accessible, even if it is not. |
| 7.12.16. | AccessController.doPrivileged(new PrivilegedAction() ) |
