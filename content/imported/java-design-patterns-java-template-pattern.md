---
title: Java Design Patterns Tutorial - Java Design Pattern - Template Pattern
nav: Java Design Patterns Tutor...
description: In Template pattern, a parent abstract class expose several abstract methods for the subclass to implement. In the parent abstract class there is another method or severa
section: Imported - java2s Archive
order: 50133
source: https://www.java2s.com/Tutorials/Java/Java_Design_Patterns/0260__Java_Template_Pattern.html
---
```java title=Example.java
```

In Template pattern, a parent abstract class expose several abstract methods for the subclass to implement. In the parent abstract class there is another method or several methods which uses the abstract methods to achieve business logics.

The abstract methods usually are for each step required by the parent class.

For example, in order to use a new software we need to download, install, configuration, and run. If we are going to use template pattern to code the logic we would create a parent class as follows.

```java title=Example.java
abstractclass UseSoftware{
   abstract void download();
   abstract void install();
   abstract void configuration();
   abstract void run();
   public void useNewSoftware(){
     download();
     install();
     configuration();
     run();
   }
}
```

For using different software we just need to inherit from the abstract class above and provide the detailed implementation.

Template pattern is a behavior pattern.

## Example

```java title=Example.java
abstractclass Software {
   abstractvoid initialize();
   abstractvoid start();
   abstractvoid end();
   //template methodpublicfinalvoid play(){
      //initialize
      initialize();
      //start
      start();
      //end
      end();
   }
}
class Browser extends Software {
   @Override
   void end() {
      System.out.println("Browser Finished!");
   }
   @Override
   void initialize() {
      System.out.println("Browser Initialized!.");
   }
   @Override
   void start() {
      System.out.println("Browser Started.");
   }
}
class Editor extends Software {
   @Override
   void end() {
      System.out.println("Editor Finished!");
   }
   @Override
   void initialize() {
      System.out.println("Editor Initialized!");
   }
   @Override
   void start() {
      System.out.println("Editor Started!");
   }
}
publicclass Main {
   publicstaticvoid main(String[] args) {
      Software s1 = new Browser();
      s1.play();
      s1 = new Editor();
      s1.play();
   }
}
```

The code above generates the following result.

- « Previous
