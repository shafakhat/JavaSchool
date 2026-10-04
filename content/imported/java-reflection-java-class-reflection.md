---
title: Java Reflection - Java Class Reflecting
nav: Java Reflection - Java Cla...
description: We can use Java reflection to get the information about a class, such as its package name, its access modifiers, etc.
section: Imported - java2s Archive
order: 50403
source: https://www.java2s.com/Tutorials/Java/Java_Reflection/0030__Java_Class_Reflection.html
---
```java title=Example.java
```

We can use Java reflection to get the information about a class, such as its package name, its access modifiers, etc.

To get the simple class name, use the getSimpleName() method from the Class.

```java title=Example.java
String simpleName = c.getSimpleName();
```

The modifiers of a class are the keywords before the keyword class in the class declaration, such as abstract, public.

The getModifiers() method from Class returns all modifiers for the class.

The getModifiers() method returns an integer. We have to call the java.lang.reflect.Modifier.toString(int modifiers) to get the textual form of the modifiers.

To get the name of the superclass, use the getSuperclass() method from Class.

If the getSuperclass() method is invoked on the Object class, it returns null since it has no super class.

To get the names of all interfaces implemented by a class, use the getInterfaces().

```java title=Example.java
Class[] interfaces = c.getInterfaces();
```

## Example

```java title=Example.java
import java.io.Serializable;
import java.lang.reflect.Modifier;
import java.lang.reflect.TypeVariable;
class MyClass<T> implements Cloneable, Serializable {
  privateint id = -1;
  private String name = "Unknown";
  public MyClass(int id, String name) {
    this.id = id;
    this.name = name;
  }
  public Object clone() {
    try {
      return super.clone();
    } catch (CloneNotSupportedException e) {
      thrownew RuntimeException(e.getMessage());
    }
  }
  public String toString() {
    return"MyClass: id=" + this.id + ", name=" + this.name;
  }
}
publicclass Main {
  publicstaticvoid main(String[] args) {
    // Print the class declaration for the Class class
    String classDesciption = getClassDescription(MyClass.class);
    System.out.println(classDesciption);
  }
  publicstatic String getClassDescription(Class c) {
    StringBuilder classDesc = new StringBuilder();
    int modifierBits = 0;
    String keyword = "";
    if (c.isInterface()) {
      modifierBits = c.getModifiers() & Modifier.interfaceModifiers();
      if (c.isAnnotation()) {
        keyword = "@interface";
      } else {
        keyword = "interface";
      }
    } elseif (c.isEnum()) {
      modifierBits = c.getModifiers() & Modifier.classModifiers();
      keyword = "enum";
    }
    modifierBits = c.getModifiers() & Modifier.classModifiers();
    keyword = "class";
    String modifiers = Modifier.toString(modifierBits);
    classDesc.append(modifiers);
    classDesc.append(" " + keyword);
    String simpleName = c.getSimpleName();
    classDesc.append(" " + simpleName);
    String genericParms = getGenericTypeParams(c);
    classDesc.append(genericParms);
    Class superClass = c.getSuperclass();
    if (superClass != null) {
      String superClassSimpleName = superClass.getSimpleName();
      classDesc.append("  extends " + superClassSimpleName);
    }
    String interfaces = Main.getClassInterfaces(c);
    if (interfaces != null) {
      classDesc.append("  implements " + interfaces);
    }
    return classDesc.toString();
  }
  publicstatic String getClassInterfaces(Class c) {
    Class[] interfaces = c.getInterfaces();
    String interfacesList = null;
    if (interfaces.length > 0) {
      String[] interfaceNames = new String[interfaces.length];
      for (int i = 0; i < interfaces.length; i++) {
        interfaceNames[i] = interfaces[i].getSimpleName();
      }
      interfacesList = String.join(", ", interfaceNames);
    }
    return interfacesList;
  }
  publicstatic String getGenericTypeParams(Class c) {
    StringBuilder sb = new StringBuilder();
    TypeVariable<?>[] typeParms = c.getTypeParameters();
    if (typeParms.length > 0) {
      String[] paramNames = new String[typeParms.length];
      for (int i = 0; i < typeParms.length; i++) {
        paramNames[i] = typeParms[i].getTypeName();
      }
      sb.append('<');
      String parmsList = String.join(",", paramNames);
      sb.append(parmsList);
      sb.append('>');
    }
    return sb.toString();
  }
}
```

The code above generates the following result.

```java title=Example.java
class MyClass<T>  extends Object  implements Cloneable, Serializable
```

The code above generates the following result.

- « Previous
