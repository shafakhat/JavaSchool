---
title: Java Design Patterns Tutorial - Java Design Pattern - Observer Pattern
nav: Java Design Patterns Tutor...
description: Observer pattern is used to notify its depenedent objects if one object is modified,.
section: Imported - java2s Archive
order: 50127
source: https://www.java2s.com/Tutorials/Java/Java_Design_Patterns/0170__Java_Observer_Pattern.html
---
```java title=Example.java
```

Observer pattern is used to notify its depenedent objects if one object is modified,.

Observer pattern is a behavioral pattern category.

## Example

```java title=Example.java
import java.util.ArrayList;
import java.util.List;
/*www.java2s.com*/class MyValue {
   private List<Observer> observers
      = new ArrayList<Observer>();
   privateint state;
   publicint getState() {
      return state;
   }
   publicvoid setState(int state) {
      this.state = state;
      notifyAllObservers();
   }
   publicvoid attach(Observer observer){
      observers.add(observer);
   }
   publicvoid notifyAllObservers(){
      for (Observer observer : observers) {
         observer.update();
      }
   }
}
abstractclass Observer {
   protected MyValue subject;
   publicabstractvoid update();
}
class PrinterObserver extends Observer{
   public PrinterObserver(MyValue subject){
      this.subject = subject;
      this.subject.attach(this);
   }
   @Override
   publicvoid update() {
      System.out.println("Printer: " + subject.getState() );
   }
}
class EmailObserver extends Observer{
   public EmailObserver(MyValue subject){
      this.subject = subject;
      this.subject.attach(this);
   }
   @Override
   publicvoid update() {
     System.out.println("Email: "+ subject.getState() );
   }
}
class FileObserver extends Observer{
   public FileObserver(MyValue subject){
      this.subject = subject;
      this.subject.attach(this);
   }
   @Override
   publicvoid update() {
      System.out.println("File: " + subject.getState());
   }
}
publicclass Main {
   publicstaticvoid main(String[] args) {
      MyValue subject = new MyValue();
      new FileObserver(subject);
      new EmailObserver(subject);
      new PrinterObserver(subject);
      subject.setState(15);
      subject.setState(10);
   }
}
```

The code above generates the following result.

- « Previous
