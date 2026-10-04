---
title: Class Object
nav: Class Object
description: All the classes defined are subclasses by default. Object is a superclass of every class. The inheritance happens automatically. Your classes will inherit members from th
section: Imported - java2s Archive
order: 1247
source: https://web.archive.org/web/20140829090226/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/ClassObject.htm
---
All the classes defined are subclasses by default. Object is a superclass of every class. The inheritance happens automatically. Your classes will inherit members from the class Object.
Method Purpose toString() returns a string describing the current object equals() compares two objects getClass() returns a Class that identifies the class of the current object. hashCode() calculates a hashcode for an object notify() wakes up a thread associated with the current object. notifyAll() wakes up all threads associated with the current object. wait() causes a thread to wait

```java title=Example.java
class Dog{
  public Dog(String aType){
  }
}
public class MainClass{
  public static void main(String[] a){
    Dog d = new Dog("a");
    Class objectType = d.getClass();
    System.out.println(objectType.getName());
  }
}
java title=Example.java
Dog
```
