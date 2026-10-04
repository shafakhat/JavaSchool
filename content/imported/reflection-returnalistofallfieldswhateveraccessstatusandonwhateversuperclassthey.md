---
title: Return a list of all fields (whatever access status, and on whatever superclass they were defined) that can be found on this class.
nav: Return a list of all field...
description: * Licensed under the Apache License, Version 2.0 (the "License");
section: Imported - java2s Archive
order: 2102
source: https://web.archive.org/web/20140829082916/http://www.java2s.com/Tutorial/Java/0125__Reflection/Returnalistofallfieldswhateveraccessstatusandonwhateversuperclasstheyweredefinedthatcanbefoundonthisclass.htm
---
```java title=Example.java
import java.lang.reflect.Field;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Locale;
import java.util.Map;
import java.util.Set;
import javax.servlet.http.HttpServletResponse;
/*
 * Copyright 2005 Joe Walker
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
/**
 * @author Joe Walker [joe at getahead dot ltd dot uk]
 */
public class Main {
  /**
   * Return a list of all fields (whatever access status, and on whatever
   * superclass they were defined) that can be found on this class.
   * This is like a union of {@link Class#getDeclaredFields()} which
   * ignores and super-classes, and {@link Class#getFields()} which ignored
   * non-public fields
   * @param clazz The class to introspect
   * @return The complete list of fields
   */
  public static Field[] getAllFields(Class<?> clazz)
  {
      List<Class<?>> classes = getAllSuperclasses(clazz);
      classes.add(clazz);
      return getAllFields(classes);
  }
  /**
   * As {@link #getAllFields(Class)} but acts on a list of {@link Class}s and
   * uses only {@link Class#getDeclaredFields()}.
   * @param classes The list of classes to reflect on
   * @return The complete list of fields
   */
  private static Field[] getAllFields(List<Class<?>> classes)
  {
      Set<Field> fields = new HashSet<Field>();
      for (Class<?> clazz : classes)
      {
          fields.addAll(Arrays.asList(clazz.getDeclaredFields()));
      }
      return fields.toArray(new Field[fields.size()]);
  }
  /**
   * Return a List of super-classes for the given class.
   * @param clazz the class to look up
   * @return the List of super-classes in order going up from this one
   */
  public static List<Class<?>> getAllSuperclasses(Class<?> clazz)
  {
      List<Class<?>> classes = new ArrayList<Class<?>>();
      Class<?> superclass = clazz.getSuperclass();
      while (superclass != null)
      {
          classes.add(superclass);
          superclass = superclass.getSuperclass();
      }
      return classes;
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
