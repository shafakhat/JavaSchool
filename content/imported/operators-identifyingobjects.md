---
title: Identifying Objects
nav: Identifying Objects
description: Imported from the java2s.com archive: Identifying Objects
section: Imported - java2s Archive
order: 1150
source: https://web.archive.org/web/20140215114433/http://www.java2s.com/Tutorial/Java/0060__Operators/IdentifyingObjects.htm
---
```java title=Example.java
class Animal {
  public String toString() {
    return "This is an animal ";
  }
}
class Dog extends Animal {
  public void sound() {
    System.out.println("Woof Woof");
  }
}
public class MainClass {
  public static void main(String[] a) {
    Dog aDog = new Dog();
    if (aDog instanceof Animal) {
      Animal ani = (Animal) aDog;
      System.out.println(ani);
    }
  }
}
java title=Example.java
This is an animal
```
