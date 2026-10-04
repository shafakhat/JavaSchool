---
title: Override toString() for Box class.
nav: Override toString() for Bo...
description: return "Dimensions are " + width + " by " + depth + " by " + height + ".";
section: Imported - java2s Archive
order: 1150
source: https://web.archive.org/web/20140829080836/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/OverridetoStringforBoxclass.htm
---
```java title=Example.java
class Box {
  double width;
  double height;
  double depth;
  Box(double w, double h, double d) {
    width = w;
    height = h;
    depth = d;
  }
  public String toString() {
    return "Dimensions are " + width + " by " + depth + " by " + height + ".";
  }
}
class toStringDemo {
  public static void main(String args[]) {
    Box b = new Box(10, 12, 14);
    String s = "Box b: " + b; // concatenate Box object
    System.out.println(b); // convert Box to string
    System.out.println(s);
  }
}
```

| 5.32.1. | Override toString() for Box class. |
|---|---|
| 5.32.2. | override the toString method in your classes |
| 5.32.3. | Use Reflection To build toString method |
| 5.32.4. | Reflection based toString() utilities |
| 5.32.5. | Use a generic toString() |
| 5.32.6. | Jakarta Commons toString Builder |
