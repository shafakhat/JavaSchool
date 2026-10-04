---
title: How to create and use Single-Member Annotations in Java
nav: How to create and use Sing...
description: A single-member annotation contains only one member. It allows a shorthand form of specifying the value of the member.
section: Imported - java2s Archive
order: 1020
source: https://web.archive.org/web/20141115061926/http://www.java2s.com:80/Tutorials/Java/Annotations/How_to_create_and_use_Single_Member_Annotations_in_Java.htm
---
In this chapter you will learn:

- How to create and use single member annotation
- Example - Java Single-Member Annotations
- How to set a default value for a member in an annotation

### Description

A single-member annotation contains only one member. It allows a shorthand form of specifying the value of the member.

When only one member is present, you don't need to specify the name of the member.

### Example

In order to use this shorthand, the name of the member must be value. Here is an example that creates and uses a single-member annotation:

```java title=Example.java
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.reflect.Method;
//www.java2s.com

@Retention(RetentionPolicy.RUNTIME)
@interface MySingle {
  int value(); // this variable name must be value
}

publicclass Main {
  @MySingle(100)
  publicstaticvoid myMeth() {
    Main ob = new Main ();
    try {
      Method m = ob.getClass().getMethod("myMeth");
      MySingle anno = m.getAnnotation(MySingle.class);
      System.out.println(anno.value()); // displays 100
    } catch (NoSuchMethodException exc) {
      System.out.println("Method Not Found.");
    }
  }

  publicstaticvoid main(String args[]) {
    myMeth();
  }
}
```

The code above generates the following result.

### Example 2

You can use the single-value syntax when applying an annotation that has other members, but those other members must all have default values.

For example, here the value xyz is added, with a default value of zero:

```java title=Example.java

@interface SomeAnno {
    int value();
    int xyz() default 0;
}
```

You can apply @SomeAnno as ,

```java title=Example.java

@SomeAnno(1)
```

by specifying the value using the single-member syntax.

In this case, xyz defaults to zero, and value gets the value 1.

#### Next chapter...

What you will learn in the next chapter:

- What are built-in annotations
- @Retention
- @Documented
- @Target
- @Inherited
- @Override
- @Deprecated
- @SuppressWarnings
