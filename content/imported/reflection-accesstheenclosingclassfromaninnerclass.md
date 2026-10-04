---
title: Access the enclosing class from an inner class
nav: Access the enclosing class...
description: 6. This class shows using Reflection to get a field from another class
section: Imported - java2s Archive
order: 1004
source: https://web.archive.org/web/20090526045842/http://www.java2s.com:80/Code/Java/Reflection/Accesstheenclosingclassfromaninnerclass.htm
---
Access the enclosing class from an inner class

```java title=Example.java
public class Main {
  public static void main(String a[]){
     new TestIt().doit();
  }
  public void doit() {
      new InnerClass().sayHello();
  }
  public void enclosingClassMethod(){
      System.out.println("Hello world!");
  }
 class InnerClass {
   public void sayHello() {
     TestIt.this.enclosingClassMethod();
   }
 }
}
```

1.  Class Reflection: class modifier
---  ---
2.  Class Reflection: class name
3.  Class Reflection: name for super class
4.  Object Reflection: create new instance
5.  Class reflection
6.  This class shows using Reflection to get a field from another class
7.  Show the class keyword and getClass() method in action
8.  Simple Demonstration of a ClassLoader WILL NOT COMPILE OUT OF THE BOX
9.  Demonstrate classFor to create an instance of an object
10.  CrossRef prints a cross-reference about all classes named in argv
11.  Make up a compilable version of a given Sun or other API
12.  Show a couple of things you can do with a Class object
13.  Reflect1 shows the information about the class named in argv
14.  Show that you can, in fact, take the class of a primitive
15.  JavaP prints structural information about classes
16.  Object Inspector
17.  Provides a set of static methods that extend the Java metaobject
18.  Demonstration of speed of reflexive versus programatic invocation
19.  Use reflection to get console char set
20.  Load the class source location from Class.getResource()
21.  Use reflection to dynamically discover the capabilities of a class.
22.  Get the class By way of a string
23.  Get the class By way of .class
