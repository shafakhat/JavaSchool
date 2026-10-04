---
title: Java Design Patterns Tutorial - Java Design Pattern - Mediator Pattern
nav: Java Design Patterns Tutor...
description: Mediator pattern reduces communication between multiple objects.
section: Imported - java2s Archive
order: 50128
source: https://www.java2s.com/Tutorials/Java/Java_Design_Patterns/0180__Java_Mediator_Pattern.html
---
```java title=Example.java
```

Mediator pattern reduces communication between multiple objects.

This pattern provides a mediator class which handles all the communications between different classes.

Mediator pattern falls under behavioral pattern category.

## Example

```java title=Example.java
class Printer {publicstaticvoid showMessage(Machine user, String message){
      System.out.println(new java.util.Date().toString()
         + " [" + user.getName() +"] : " + message);
   }
}
class Machine {
   private String name;
   public Machine(String name){
      this.name  = name;
   }
   public String getName() {
      return name;
   }
   publicvoid setName(String name) {
      this.name = name;
   }
   publicvoid sendMessage(String message){
      Printer.showMessage(this,message);
   }
}
class Main {
   publicstaticvoid main(String[] args) {
      Machine m1= new Machine("M1");
      Machine m2 = new Machine("M2");
      m1.sendMessage("Rebooting");
      m2.sendMessage("Computing");
   }
}
```

- « Previous
