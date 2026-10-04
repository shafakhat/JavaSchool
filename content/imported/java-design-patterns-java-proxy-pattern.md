---
title: Java Design Patterns Tutorial - Java Design Pattern - Proxy Pattern
nav: Java Design Patterns Tutor...
description: In Proxy pattern, a class represents functionality of another class.
section: Imported - java2s Archive
order: 50123
source: https://www.java2s.com/Tutorials/Java/Java_Design_Patterns/0130__Java_Proxy_Pattern.html
---
In Proxy pattern, a class represents functionality of another class.

Proxy pattern is a structural pattern.

In Proxy pattern, we create object with original interface to expose its functionality to outer world.

## Example

```java title=Example.java
interface Printer {
   void print();
}
class ConsolePrinter implements Printer {
   private String fileName;
   public ConsolePrinter(String fileName){
      this.fileName = fileName;
   }
   @Override
   publicvoid print() {
      System.out.println("Displaying " + fileName);
   }
}
class ProxyPrinter implements Printer{
   private ConsolePrinter consolePrinter;
   private String fileName;
   public ProxyPrinter(String fileName){
      this.fileName = fileName;
   }
   @Override
   publicvoid print() {
      if(consolePrinter == null){
         consolePrinter = new ConsolePrinter(fileName);
      }
      consolePrinter.print();
   }
}
publicclass Main {
   publicstaticvoid main(String[] args) {
      Printer image = new ProxyPrinter("test");
      image.print();
   }
}
```

The code above generates the following result.

- « Previous
