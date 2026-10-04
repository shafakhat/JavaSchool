---
title: Java Design Patterns Tutorial - Java Design Pattern - Singleton Pattern
nav: Java Design Patterns Tutor...
description: This pattern involves only a single class which is responsible to creates its own object.
section: Imported - java2s Archive
order: 50114
source: https://www.java2s.com/Tutorials/Java/Java_Design_Patterns/0030__Java_Singleton_Pattern.html
---
```java title=Example.java
« Previous
```

- Next »

Singleton pattern is a creational pattern.

This pattern involves only a single class which is responsible to creates its own object.

The class ensures that only single object get created.

This class provides a way to access its only object.

For example, when design a user interface, we may only have one main application windows. We can use the Singleton Pattern to ensure that there is only one instance of the MainApplicationWindow object.

## Example

The following code is going to create a MainWindow class.

MainWindow class have its constructor as private and have a static instance of itself.

MainWindow class provides a static method to get its static instance to outside world.

Main, our demo class will use MainWindow class to get a MainWindow object.

```java title=Example.java
class MainWindow {
   //create an object of MainWindow
   privatestatic MainWindow instance = new MainWindow();
   //make the constructor private so that this class cannot be
   //instantiated by other classprivate MainWindow(){}
   //Get the only object available
   publicstatic MainWindow getInstance(){
      return instance;
   }
   public void showMessage(){
      System.out.println("Hello World!");
   }
}
publicclass Main {
   publicstatic void main(String[] args) {
      //Get the only object available
      MainWindow object = MainWindow.getInstance();
      //show the message
      object.showMessage();
   }
}
```

The code above generates the following result.

- Next »
- « Previous
