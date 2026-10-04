---
title: Java Reflection - Java Method Reflection
nav: Java Reflection - Java Met...
description: An instance of the java.lang.reflect.Method class represents a method. An instance of the java.lang.reflect.Constructor class represents a constructor.
section: Imported - java2s Archive
order: 50405
source: https://www.java2s.com/Tutorials/Java/Java_Reflection/0050__Java_Method_Reflection.html
---
```java title=Example.java
« Previous
```

- Next »

An instance of the java.lang.reflect.Method class represents a method. An instance of the java.lang.reflect.Constructor class represents a constructor.

Method and Constructor inherit from a common abstract superclass Executable.

A parameter in an Executable is represented by an object of the Parameter class

The getParameters() method in the Executable class gets all parameters as an array of Parameter.

By default, the parameter names are not stored in the class files. The name of the parameter class would be like arg0, arg1, etc. We can keep the actual parameter names in class files by compiling the source code using the -parameters option with the javac compiler.

The getExceptionTypes() method from Executable class returns an array of exceptions thrown by the Executable.

The getModifiers() method from Executable class returns the modifiers as an int.

The getTypeParameters() method from the Executable class returns an array of TypeVariable that represents the type parameters for generic methods or constructors.

## Example

```java title=Example.java
import java.lang.reflect.Constructor;
import java.lang.reflect.Executable;
import java.lang.reflect.Method;
import java.lang.reflect.Modifier;
import java.lang.reflect.Parameter;
import java.util.ArrayList;
//www.java2s.comclass MyClass<T> {
  public MyClass(int i, int j, String s){
  }
  public MyClass(T t){
  }
  publicint getInt(String a){
    return 0;
  }
}
publicclass Main {
  publicstaticvoid main(String[] argv){
    Class<MyClass> cls = MyClass.class;
    for(Method m:cls.getMethods()){
      System.out.println(m.getName());
      System.out.println(getModifiers(m));
      System.out.println(getParameters(m) );
      System.out.println(getExceptionList(m));
    }
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
      if(temp.trim().length() == 0){
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

## Reflecting on Methods

The following four methods in the Class class returns information about the methods of a class:

```java title=Example.java

Method[]  getMethods()
Method[]  getDeclaredMethods()
Method getMethod(String name,  Class...  parameterTypes)
Method getDeclaredMethod(String name,  Class...  parameterTypes)
```

The getMethods() method returns all the accessible public methods of the class both from in the class and inherited from the superclass.

The getDeclaredMethods() method returns all the methods declared only in the class (not include methods inherited from the superclass).

getMethod(String name, Class... parameterTypes) and getDeclaredMethod(String name, Class... parameterTypes) get the Method object by the method name and parameter types.

The getReturnType() method from the Method class returns the Class object containing information about the return type.

```java title=Example.java
import java.lang.reflect.Constructor;
import java.lang.reflect.Executable;
import java.lang.reflect.Method;
import java.lang.reflect.Modifier;
import java.lang.reflect.Parameter;
import java.util.ArrayList;
//fromwww.java2s.comclass MyClass<T> {
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
    ArrayList<String> methodsDesciption = getDeclaredMethodsList(c);
    System.out.println("Declared Methods  for " + c.getName());
    for (String desc : methodsDesciption) {
      System.out.println(desc);
    }
    methodsDesciption = getMethodsList(c);
    System.out.println("\nMethods for  " + c.getName());
    for (String desc : methodsDesciption) {
      System.out.println(desc);
    }
  }
  publicstatic ArrayList<String> getMethodsList(Class c) {
    Method[] methods = c.getMethods();
    ArrayList<String> methodsList = getMethodsDesciption(methods);
    return methodsList;
  }
  publicstatic ArrayList<String> getDeclaredMethodsList(Class c) {
    Method[] methods = c.getDeclaredMethods();
    ArrayList<String> methodsList = getMethodsDesciption(methods);
    return methodsList;
  }
  publicstatic ArrayList<String> getMethodsDesciption(Method[] methods) {
    ArrayList<String> methodList = new ArrayList<>();
    for (Method m : methods) {
      String modifiers = getModifiers(m);
      Class returnType = m.getReturnType();
      String returnTypeName = returnType.getSimpleName();
      String methodName = m.getName();
      String params = getParameters(m).toString();
      String throwsClause = getExceptionList(m).toString();
      methodList.add(modifiers + "  " + returnTypeName + "  " + methodName
          + "(" + params + ") " + throwsClause);
    }
    return methodList;
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
