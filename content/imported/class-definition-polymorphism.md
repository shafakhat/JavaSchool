---
title: Polymorphism
nav: Polymorphism
description: It means the ability of a single variable of a given type to be used to reference objects of different types and to automatically call the method that is specific to the
section: Imported - java2s Archive
order: 1039
source: https://web.archive.org/web/20070421183242/http://www.java2s.com:80/Tutorial/Java/0100__Class-Definition/Polymorphism.htm
---
It means the ability of a single variable of a given type to be used to reference objects of different types and to automatically call the method that is specific to the type of object the variable references. (Ivor Horton's Beginning Java 2, JDK 5 Edition by Ivor Horton Wrox Press 2005 )

polymorphism works with derived class objects.

```java title=Example.java
import java.util.Random;
class Animal {
  public Animal(String aType) {
    type = new String(aType);
  }
  public String toString() {
    return "This is a " + type;
  }
  public void sound(){
    System.out.println("Sound for an animal");
  }
  private String type;
}
class Dog extends Animal {
  public Dog(String aType){
   super(aType);
  }
  public void sound() {
    System.out.println("Woof Woof");
  }
}
class Cat extends Animal {
  public Cat(String aName) {
    super("Cat");
    name = aName;
    breed = "Unknown";
  }
  public Cat(String aName, String aBreed) {
    super("Cat");
    name = aName;
    breed = aBreed;
  }
  public String toString() {
    return super.toString() + "\nIt's " + name + " the " + breed;
  }
  public void sound() {
    System.out.println("Miiaooww");
  }
  private String name;
  private String breed;
}
class Duck extends Animal {
  public Duck(String aName) {
    super("Duck");
    name = aName;
    breed = "Unknown";
  }
  public Duck(String aName, String aBreed) {
    super("Duck");
    name = aName;
    breed = aBreed;
  }
  public String toString() {
    return super.toString() + "\nIt's " + name + " the " + breed;
  }
  public void sound() {
    System.out.println("Quack quackquack");
  }
  private String name;
  private String breed;
}
public class MainClass {
  public static void main(String[] args) {
    Animal[] theAnimals = { new Dog("A"),
                            new Cat("C", "D"),
                            new Duck("E", "F") };
    Animal petChoice;
    Random select = new Random();
    for (int i = 0; i < 5; i++) {
      petChoice = theAnimals[select.nextInt(theAnimals.length)];
      System.out.println("\nYour choice:\n" + petChoice);
      petChoice.sound();
    }
  }
}
```

```java title=Example.java
Your choice:
This is a A
Woof Woof
Your choice:
This is a Duck
It's E the F
Quack quackquack
Your choice:
This is a Duck
It's E the F
Quack quackquack
Your choice:
This is a Duck
It's E the F
Quack quackquack
Your choice:
This is a Duck
It's E the F
Quack quackquack
```
