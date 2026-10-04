---
title: Java Object Oriented Design - Java Annotation Reflection
nav: Java Object Oriented Desig...
description: Program elements that let you access their annotations implement the java.lang.reflect.AnnotatedElement interface.
section: Imported - java2s Archive
order: 50197
source: https://www.java2s.com/Tutorials/Java/Java_Object_Oriented_Design/0760__Java_Annotation_Reflection.html
---
```java title=Example.java
```

Annotations on a program element are Java objects.

Program elements that let you access their annotations implement the java.lang.reflect.AnnotatedElement interface.

The following classes implement the AnnotatedElement interface:

Methods of the AnnotatedElement interface are used to access annotation on the following listed types of objects.

```java title=Example.java
java.lang.Class
java.lang.reflect.Executable
java.lang.reflect.Constructor
java.lang.reflect.Field
java.lang.reflect.Method
java.lang.reflect.Parameter
java.lang.Package
java.lang.reflect.AccessibleObject
```

An annotation type must be annotated with the Retention meta-annotation with the retention policy of runtime to access it at runtime.

## Example

Suppose you have a Test class and you want to print all its annotations. The following snippet of code will print all annotations on the class declaration of the Test class:

```java title=Example.java
import java.lang.annotation.Annotation;
@SuppressWarnings("unchecked")
@Deprecated
publicclass Main {
  publicstaticvoid main(String[] argv) {
    // Get the class object reference
    Class<Main> c = Main.class;
    // Get all annotations on the class declaration
    Annotation[] allAnns = c.getAnnotations();
    System.out.println("Annotation count: " + allAnns.length);
    // Print all annotations
for (Annotation ann : allAnns) {
      System.out.println(ann);
    }
  }
}
```

The toString() method of the Annotation interface returns the string representation of an annotation.

## Example 2

The following code shows how to get a specific annotation.

```java title=Example.java
import java.lang.annotation.Documented;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
@Retention(RetentionPolicy.RUNTIME)
@Documented
@interface Version {
  int major();
  int minor();
}
@Version(major=1,minor=2)
publicclass Main {
  publicstaticvoid main(String[] argv) {
    Class<Main> c = Main.class;
    Version v = c.getAnnotation(Version.class);
    if (v == null) {
      System.out.println("Version annotation is  not  present.");
    } else {
      int major = v.major();
      int minor = v.minor();
      System.out.println("Version: major=" + major + ", minor=" + minor);
    }
  }
}
```

The code above generates the following result.

## Example 3

The following code shows how to access annotation for methods.

```java title=Example.java
import java.lang.annotation.Annotation;
import java.lang.annotation.Documented;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.reflect.AnnotatedElement;
import java.lang.reflect.Method;
@Retention(RetentionPolicy.RUNTIME)
@interface Version {
  int major();
  int minor();
}
@Version(major = 1, minor = 0)
class AccessAnnotation {
  @Version(major = 1, minor = 1)
  publicvoid testMethod1() {
  }
  @Version(major = 1, minor = 2)
  @Deprecated
  publicvoid testMethod2() {
  }
}
publicclass Main {
  publicstaticvoid main(String[] args) {
    Class<AccessAnnotation> c = AccessAnnotation.class;
    System.out.println("Annotations for class:" + c.getName());
    printAnnotations(c);
    System.out.println("Method annotations:");
    Method[] m = c.getDeclaredMethods();
    for (int i = 0; i < m.length; i++) {
      System.out.println("Annotations for method:" + m[i].getName());
      printAnnotations(m[i]);
    }
  }
  publicstaticvoid printAnnotations(AnnotatedElement programElement) {
    Annotation[] annList = programElement.getAnnotations();
    for (int i = 0; i < annList.length; i++) {
      System.out.println(annList[i]);
      if (annList[i] instanceof Version) {
        Version v = (Version) annList[i];
        int major = v.major();
        int minor = v.minor();
        System.out.println("Found  Version annotation:  " + "major  =" + major
            + ", minor=" + minor);
      }
    }
  }
}
```

The code above generates the following result.

## Example 4

The following code shows how to access Instances of Repeatable Annotations at Runtime

```java title=Example.java
import java.lang.annotation.Repeatable;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
@Retention(RetentionPolicy.RUNTIME)
@interface LogHistory {
  Log[] value();
}
@Repeatable(LogHistory.class)
@interface Log {
  String date();
  String comments();
}
@Log(date = "02/01/2014", comments = "A")
@Log(date = "01/22/2014", comments = "B")
publicclass Main {
  publicstaticvoid main(String[] args) {
    Class<Main> mainClass = Main.class;
    Log[] annList = mainClass.getAnnotationsByType(Log.class);
    for (Log log : annList) {
      System.out.println("Date=" + log.date() + ", Comments=" + log.comments());
    }
    Class<LogHistory> containingAnnClass = LogHistory.class;
    LogHistory logs = mainClass.getAnnotation(containingAnnClass);
    for (Log log : logs.value()) {
      System.out.println("Date=" + log.date() + ", Comments=" + log.comments());
    }
  }
}
```

The code above generates the following result.

- « Previous
