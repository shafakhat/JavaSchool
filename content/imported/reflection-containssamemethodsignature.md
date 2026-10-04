---
title: Contains Same Method Signature
nav: Contains Same Method Signa...
description: //$Id: IntrospectionUtil.java 1540 2007-01-19 12:24:10Z janb $
section: Imported - java2s Archive
order: 2122
source: https://web.archive.org/web/20140829092259/http://www.java2s.com/Tutorial/Java/0125__Reflection/ContainsSameMethodSignature.htm
---
```java title=Example.java
//
//$Id: IntrospectionUtil.java 1540 2007-01-19 12:24:10Z janb $
//Copyright 2006 Mort Bay Consulting Pty. Ltd.
//------------------------------------------------------------------------
//Licensed under the Apache License, Version 2.0 (the "License");
//you may not use this file except in compliance with the License.
//You may obtain a copy of the License at
//http://www.apache.org/licenses/LICENSE-2.0
//Unless required by applicable law or agreed to in writing, software
//distributed under the License is distributed on an "AS IS" BASIS,
//WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
//See the License for the specific language governing permissions and
//limitations under the License.
//
import java.lang.reflect.Field;
import java.lang.reflect.Member;
import java.lang.reflect.Method;
import java.lang.reflect.Modifier;
import java.util.Arrays;
import java.util.List;
public class IntrospectionUtil {
  public static boolean containsSameMethodSignature(Method method, Class c, boolean checkPackage) {
    if (checkPackage) {
      if (!c.getPackage().equals(method.getDeclaringClass().getPackage()))
        return false;
    }
    boolean samesig = false;
    Method[] methods = c.getDeclaredMethods();
    for (int i = 0; i < methods.length && !samesig; i++) {
      if (IntrospectionUtil.isSameSignature(method, methods[i]))
        samesig = true;
    }
    return samesig;
  }
  public static boolean containsSameFieldName(Field field, Class c, boolean checkPackage) {
    if (checkPackage) {
      if (!c.getPackage().equals(field.getDeclaringClass().getPackage()))
        return false;
    }
    boolean sameName = false;
    Field[] fields = c.getDeclaredFields();
    for (int i = 0; i < fields.length && !sameName; i++) {
      if (fields[i].getName().equals(field.getName()))
        sameName = true;
    }
    return sameName;
  }
  public static boolean isInheritable(Package pack, Member member) {
    if (pack == null)
      return false;
    if (member == null)
      return false;
    int modifiers = member.getModifiers();
    if (Modifier.isPublic(modifiers))
      return true;
    if (Modifier.isProtected(modifiers))
      return true;
    if (!Modifier.isPrivate(modifiers) && pack.equals(member.getDeclaringClass().getPackage()))
      return true;
    return false;
  }
  public static boolean checkParams(Class[] formalParams, Class[] actualParams, boolean strict) {
    if (formalParams == null && actualParams == null)
      return true;
    if (formalParams == null && actualParams != null)
      return false;
    if (formalParams != null && actualParams == null)
      return false;
    if (formalParams.length != actualParams.length)
      return false;
    if (formalParams.length == 0)
      return true;
    int j = 0;
    if (strict) {
      while (j < formalParams.length && formalParams[j].equals(actualParams[j]))
        j++;
    } else {
      while ((j < formalParams.length) && (formalParams[j].isAssignableFrom(actualParams[j]))) {
        j++;
      }
    }
    if (j != formalParams.length) {
      return false;
    }
    return true;
  }
  public static boolean isSameSignature(Method methodA, Method methodB) {
    if (methodA == null)
      return false;
    if (methodB == null)
      return false;
    List parameterTypesA = Arrays.asList(methodA.getParameterTypes());
    List parameterTypesB = Arrays.asList(methodB.getParameterTypes());
    if (methodA.getName().equals(methodB.getName()) && parameterTypesA.containsAll(parameterTypesB))
      return true;
    return false;
  }
  public static boolean isTypeCompatible(Class formalType, Class actualType, boolean strict) {
    if (formalType == null && actualType != null)
      return false;
    if (formalType != null && actualType == null)
      return false;
    if (formalType == null && actualType == null)
      return true;
    if (strict)
      return formalType.equals(actualType);
    else
      return formalType.isAssignableFrom(actualType);
  }
  protected static Method findInheritedMethod(Package pack, Class clazz, String methodName,
      Class[] args, boolean strictArgs) throws NoSuchMethodException {
    if (clazz == null)
      throw new NoSuchMethodException("No class");
    if (methodName == null)
      throw new NoSuchMethodException("No method name");
    Method method = null;
    Method[] methods = clazz.getDeclaredMethods();
    for (int i = 0; i < methods.length && method == null; i++) {
      if (methods[i].getName().equals(methodName) && isInheritable(pack, methods[i])
          && checkParams(methods[i].getParameterTypes(), args, strictArgs))
        method = methods[i];
    }
    if (method != null) {
      return method;
    } else
      return findInheritedMethod(clazz.getPackage(), clazz.getSuperclass(), methodName, args,
          strictArgs);
  }
  protected static Field findInheritedField(Package pack, Class clazz, String fieldName,
      Class fieldType, boolean strictType) throws NoSuchFieldException {
    if (clazz == null)
      throw new NoSuchFieldException("No class");
    if (fieldName == null)
      throw new NoSuchFieldException("No field name");
    try {
      Field field = clazz.getDeclaredField(fieldName);
      if (isInheritable(pack, field) && isTypeCompatible(fieldType, field.getType(), strictType))
        return field;
      else
        return findInheritedField(clazz.getPackage(), clazz.getSuperclass(), fieldName, fieldType,
            strictType);
    } catch (NoSuchFieldException e) {
      return findInheritedField(clazz.getPackage(), clazz.getSuperclass(), fieldName, fieldType,
          strictType);
    }
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
