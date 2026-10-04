---
title: The full process of initialization
nav: The full process of initia...
description: // www.BruceEckel.com. See copyright notice in CopyRight.txt.
section: Imported - java2s Archive
order: 1080
source: https://web.archive.org/web/20090531085254/http://www.java2s.com:80/Code/Java/Class/Thefullprocessofinitialization.htm
---
```java title=Example.java
// : c06:Beetle.java
// From 'Thinking in Java, 3rd ed.' (c) Bruce Eckel 2002
// www.BruceEckel.com. See copyright notice in CopyRight.txt.
class Insect {
  private int i = 9;
  protected int j;
  Insect() {
    System.out.println("i = " + i + ", j = " + j);
    j = 39;
  }
  private static int x1 = print("static Insect.x1 initialized");
  static int print(String s) {
    System.out.println(s);
    return 47;
  }
}
public class Beetle extends Insect {
  private int k = print("Beetle.k initialized");
  public Beetle() {
    System.out.println("k = " + k);
    System.out.println("j = " + j);
  }
  private static int x2 = print("static Beetle.x2 initialized");
  public static void main(String[] args) {
    System.out.println("Beetle constructor");
    Beetle b = new Beetle();
  }
} ///:~
```

1.  Declaring Variables
---  ---
2.  Accessing Outer Class Variables
3.  Specifying initial values in a class definition
