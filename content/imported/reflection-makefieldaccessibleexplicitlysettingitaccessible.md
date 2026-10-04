---
title: Make field accessible, explicitly setting it accessible
nav: Make field accessible, exp...
description: * Licensed under the Apache License, Version 2.0 (the "License");
section: Imported - java2s Archive
order: 2194
source: https://web.archive.org/web/20140829090641/http://www.java2s.com/Tutorial/Java/0125__Reflection/Makefieldaccessibleexplicitlysettingitaccessible.htm
---
```java title=Example.java
/*
 * Copyright 2002-2008 the original author or authors.
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
import java.lang.reflect.Field;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.lang.reflect.Modifier;
import java.sql.SQLException;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;
/**
 * Simple utility class for working with the reflection API and handling
 * reflection exceptions.
 *
 * Only intended for internal use.
 *
 * @author Juergen Hoeller
 * @author Rob Harrop
 * @author Rod Johnson
 * @author Costin Leau
 * @since 1.2.2
 */
public abstract class ReflectionUtils {
  /**
   * Make the given field accessible, explicitly setting it accessible if necessary.
   * The <code>setAccessible(true)</code> method is only called when actually necessary,
   * to avoid unnecessary conflicts with a JVM SecurityManager (if active).
   * @param field the field to make accessible
   * @see java.lang.reflect.Field#setAccessible
   */
  public static void makeAccessible(Field field) {
    if (!Modifier.isPublic(field.getModifiers()) ||
        !Modifier.isPublic(field.getDeclaringClass().getModifiers())) {
      field.setAccessible(true);
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
