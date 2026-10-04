---
title: Examination of the way the class loader works
nav: Examination of the way the...
description: // www.BruceEckel.com. See copyright notice in CopyRight.txt.
section: Imported - java2s Archive
order: 1017
source: https://web.archive.org/web/20090504072510/http://www.java2s.com:80/Code/Java/Class/Examinationofthewaytheclassloaderworks.htm
---
```java title=Example.java
// : c10:SweetShop.java
// From 'Thinking in Java, 3rd ed.' (c) Bruce Eckel 2002
// www.BruceEckel.com. See copyright notice in CopyRight.txt.
class Candy {
  static {
    System.out.println("Loading Candy");
  }
}
class Gum {
  static {
    System.out.println("Loading Gum");
  }
}
class Cookie {
  static {
    System.out.println("Loading Cookie");
  }
}
public class SweetShop {
  public static void main(String[] args) {
    System.out.println("inside main");
    new Candy();
    System.out.println("After creating Candy");
    try {
      Class.forName("Gum");
    } catch (ClassNotFoundException e) {
      System.out.println("Couldn't find Gum");
    }
    System.out.println("After Class.forName(\"Gum\")");
    new Cookie();
    System.out.println("After creating Cookie");
  }
} ///:~
```

1.  Create Object Demo
---  ---
2.  Passing objects to methods may not be what you're used to.
3.  Demonstrates Reference objects
4.  A companion class to modify immutable objects
5.  Objects that cannot be modified are immune to aliasing
6.  A changeable wrapper class
