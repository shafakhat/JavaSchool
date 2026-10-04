---
title: Creating a Multilevel Hierarchy
nav: Creating a Multilevel Hier...
description: System.out.println("Weight of shipment1 is " + shipment1.weight);
section: Imported - java2s Archive
order: 1293
source: https://web.archive.org/web/20140829075520/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/CreatingaMultilevelHierarchy.htm
---
```java title=Example.java
class Box {
  private double width;
  private double height;
  private double depth;
  Box(Box ob) { // pass object to constructor
    width = ob.width;
    height = ob.height;
    depth = ob.depth;
  }
  Box(double w, double h, double d) {
    width = w;
    height = h;
    depth = d;
  }
  Box() {
    width = -1; // use -1 to indicate
    height = -1; // an uninitialized
    depth = -1; // box
  }
  Box(double len) {
    width = height = depth = len;
  }
  double volume() {
    return width * height * depth;
  }
}
class BoxWeight extends Box {
  double weight; // weight of box
  BoxWeight(BoxWeight ob) { // pass object to constructor
    super(ob);
    weight = ob.weight;
  }
  BoxWeight(double w, double h, double d, double m) {
    super(w, h, d); // call superclass constructor
    weight = m;
  }
  BoxWeight() {
    super();
    weight = -1;
  }
  BoxWeight(double len, double m) {
    super(len);
    weight = m;
  }
}
class Shipment extends BoxWeight {
  double cost;
  Shipment(Shipment ob) { // pass object to constructor
    super(ob);
    cost = ob.cost;
  }
  Shipment(double w, double h, double d, double m, double c) {
    super(w, h, d, m); // call superclass constructor
    cost = c;
  }
  Shipment() {
    super();
    cost = -1;
  }
  Shipment(double len, double m, double c) {
    super(len, m);
    cost = c;
  }
}
class DemoShipment {
  public static void main(String args[]) {
    Shipment shipment1 = new Shipment(10, 20, 15, 10, 3.41);
    Shipment shipment2 = new Shipment(2, 3, 4, 0.76, 1.28);
    double vol;
    vol = shipment1.volume();
    System.out.println("Volume of shipment1 is " + vol);
    System.out.println("Weight of shipment1 is " + shipment1.weight);
    System.out.println("Shipping cost: $" + shipment1.cost);
    System.out.println();
    vol = shipment2.volume();
    System.out.println("Volume of shipment2 is " + vol);
    System.out.println("Weight of shipment2 is " + shipment2.weight);
    System.out.println("Shipping cost: $" + shipment2.cost);
  }
}
```
