---
title: Java Reflection - Java Constructor Reflection
nav: Java Reflection - Java Con...
description: The following four methods from the Class class get information about the constructors:
section: Imported - java2s Archive
order: 50406
source: https://www.java2s.com/Tutorials/Java/Java_Reflection/0060__Java_Constructor_Reflection.html
---
```java title=Example.java
« Previous
```

- Next »

The following four methods from the Class class get information about the constructors:

```java title=Example.java

Constructor[] getConstructors()
Constructor[]  getDeclaredConstructors()
Constructor<T> getConstructor(Class...  parameterTypes)
Constructor<T> getDeclaredConstructor(Class...  parameterTypes)
```

The getConstructors() method returns all public constructors from current and super class.

The getDeclaredConstructors() method returns all declared constructors for current class.

The getConstructor(Class... parameterTypes) and getDeclaredConstructor(Class... parameterTypes) get the Constructor object by the parameter types.

## Example

The following code shows how to do reflection on constructors.

```java title=Example.java
import java.lang.reflect.Constructor;
import java.lang.reflect.Executable;
import java.lang.reflect.Method;
import java.lang.reflect.Modifier;
import java.lang.reflect.Parameter;
import java.util.ArrayList;
/*fromwww.java2s.com*/class MyClass<T> {
  public MyClass(int i, int j, String s) {
  }
  public MyClass(T t) {
  }
  publicint getInt(String a) {
    return 0;
  }
}
publicclass Main {
  publicstaticvoid main(String[] args) {
    Class<MyClass> c = MyClass.class;
    System.out.println("Constructors for " + c.getName());
    Constructor[] constructors = c.getConstructors();
    ArrayList<String> constructDescList = getConstructorsDesciption(constructors);
    for (String desc : constructDescList) {
      System.out.println(desc);
    }
  }
  publicstatic ArrayList<String> getConstructorsDesciption(
      Constructor[] constructors) {
    ArrayList<String> constructorList = new ArrayList<>();
    for (Constructor constructor : constructors) {
      String modifiers = getModifiers(constructor);
      String constructorName = constructor.getName();
      constructorList.add(modifiers + "  " + constructorName + "("
          + getParameters(constructor) + ") " + getExceptionList(constructor));
    }
    return constructorList;
  }
  publicstatic ArrayList<String> getParameters(Executable exec) {
    Parameter[] parms = exec.getParameters();
    ArrayList<String> parmList = new ArrayList<>();
    for (int i = 0; i < parms.length; i++) {
      int mod = parms[i].getModifiers() & Modifier.parameterModifiers();
      String modifiers = Modifier.toString(mod);
      String parmType = parms[i].getType().getSimpleName();
      String parmName = parms[i].getName();
      String temp = modifiers + "  " + parmType + "  " + parmName;
      if (temp.trim().length() == 0) {
        continue;
      }
      parmList.add(temp.trim());
    }
    return parmList;
  }
  publicstatic ArrayList<String> getExceptionList(Executable exec) {
    ArrayList<String> exceptionList = new ArrayList<>();
    for (Class<?> c : exec.getExceptionTypes()) {
      exceptionList.add(c.getSimpleName());
    }
    return exceptionList;
  }
  publicstatic String getModifiers(Executable exec) {
    int mod = exec.getModifiers();
    if (exec instanceof Method) {
      mod = mod & Modifier.methodModifiers();
    } elseif (exec instanceof Constructor) {
      mod = mod & Modifier.constructorModifiers();
    }
    return Modifier.toString(mod);
  }
}
```

The code above generates the following result.

- Next »
- « Previous
