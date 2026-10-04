---
title: Checking whether the object referenced was of type String
nav: Checking whether the objec...
description: Imported from the java2s.com archive: Checking whether the object referenced was of type String
section: Imported - java2s Archive
order: 1005
source: https://web.archive.org/web/20070328232927/http://www.java2s.com:80/Tutorial/Java/0100__Class-Definition/CheckingwhethertheobjectreferencedwasoftypeString.htm
---
```java title=Example.java
class Animal {
  public Animal(String aType) {
    type = aType;
  }
  public String toString() {
    return "This is a " + type;
  }
  private String type;
}
public class MainClass {
  public static void main(String[] a) {
    Animal pet = new Animal("a");
    if (pet.getClass() == Animal.class) {
      System.out.println("it is an animal!");
    }
  }
}
java title=Example.java
it is an animal!
```
