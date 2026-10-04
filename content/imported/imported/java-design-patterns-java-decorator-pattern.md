---
title: Java Design Patterns Tutorial - Java Design Pattern - Decorator Pattern
nav: Java Design Patterns Tutor...
description: Decorator pattern adds new functionality an existing object without chaining its structure.
section: Imported - java2s Archive
order: 50121
source: https://www.java2s.com/Tutorials/Java/Java_Design_Patterns/0100__Java_Decorator_Pattern.html
---
```java title=Example.java
```

Decorator pattern adds new functionality an existing object without chaining its structure.

It is a structural pattern as it acts as a wrapper to existing class.

Decorator pattern creates a decorator class to wrap the original class and provides additional functionality.

## Example

```java title=Example.java
interface Printer {
   void print();/*fromwww.java2s.com*/
}
class PaperPrinter implements Printer {
   @Override
   publicvoid print() {
      System.out.println("Paper Printer");
   }
}
class PlasticPrinter implements Printer {
   @Override
   publicvoid print() {
      System.out.println("Plastic Printer");
   }
}
abstractclass PrinterDecorator implements Printer {
   protected Printer decoratedPrinter;
   public PrinterDecorator(Printer d){
      this.decoratedPrinter = d;
   }
   publicvoid print(){
      decoratedPrinter.print();
   }
}
class Printer3D extends PrinterDecorator {
   public Printer3D(Printer decoratedShape) {
      super(decoratedShape);
   }
   @Override
   publicvoid print() {
     System.out.println("3D.");
     decoratedPrinter.print();
   }
}
publicclass Main {
   publicstaticvoid main(String[] args) {
      Printer plasticPrinter = new PlasticPrinter();
      Printer plastic3DPrinter = new Printer3D(new PlasticPrinter());
      Printer paper3DPrinter = new Printer3D(new PaperPrinter());
      plasticPrinter.print();
      plastic3DPrinter.print();
      paper3DPrinter.print();
   }
}
```

The code above generates the following result.

- « Previous
