---
title: A Superclass Variable Can Reference a Subclass Object
nav: A Superclass Variable Can ...
description: System.out.println("Weight of weightbox is " + weightbox.weight);
section: Imported - java2s Archive
order: 1130
source: https://web.archive.org/web/20140829080002/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/ASuperclassVariableCanReferenceaSubclassObject.htm
---
```java title=Example.java
class RefDemo {
  public static void main(String args[]) {
    BoxWeight weightbox = new BoxWeight(3, 5, 7, 8.37);
    Box plainbox = new Box();
    double vol;
    vol = weightbox.volume();
    System.out.println("Volume of weightbox is " + vol);
    System.out.println("Weight of weightbox is " + weightbox.weight);
    System.out.println();
    plainbox = weightbox;
    vol = plainbox.volume();
    System.out.println("Volume of plainbox is " + vol);
  }
}
class Box {
  private double width;
  private double height;
  private double depth;
  Box(Box ob) {
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
    width = -1;
    height = -1;
    depth = -1;
  }
  Box(double len) {
    width = height = depth = len;
  }
  double volume() {
    return width * height * depth;
  }
}
class BoxWeight extends Box {
  double weight;
  BoxWeight(BoxWeight ob) {
    super(ob);
    weight = ob.weight;
  }
  BoxWeight(double w, double h, double d, double m) {
    super(w, h, d);
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
```

| 5.25.1. | Access Control: four access control modifiers |
|---|---|
| 5.25.2. | Class Access Control Modifiers |
| 5.25.3. | Using Access Attributes |
| 5.25.4. | Class Member Access Matrix |
| 5.25.5. | Specifying Access Attributes |
| 5.25.6. | The public Book class |
| 5.25.7. | Default access level |
| 5.25.8. | Class Member Access Control Modifiers |
| 5.25.9. | Composition with public objects |
| 5.25.10. | The protected keyword |
| 5.25.11. | Private Override |
| 5.25.12. | Understand the effects of public and private access |
| 5.25.13. | In a class hierarchy, private members remain private to their class. |
| 5.25.14. | A Superclass Variable Can Reference a Subclass Object |
| 5.25.15. | Create a Singleton Object |
