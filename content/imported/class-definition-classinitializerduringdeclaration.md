---
title: Class Initializer
nav: Class Initializer
description: Imported from the java2s.com archive: Class Initializer
section: Imported - java2s Archive
order: 1088
source: https://web.archive.org/web/20140829082331/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/ClassInitializerduringdeclaration.htm
---
```java title=Example.java
// ClassInitializer2.java
class ClassInitializer2 {
  static boolean bool = true;
  static byte by = 20;
  static char ch = 'X';
  static double d = 8.95;
  static float f = 2.1f;
  static int i = 63;
  static long l = 2L;
  static short sh = 200;
  static String str = "test";
  public static void main(String[] args) {
    System.out.println("bool = " + bool);
    System.out.println("by = " + by);
    System.out.println("ch = " + ch);
    System.out.println("d = " + d);
    System.out.println("f = " + f);
    System.out.println("i = " + i);
    System.out.println("l = " + l);
    System.out.println("sh = " + sh);
    System.out.println("str = " + str);
  }
}
```

| 5.2.1. | Using Constructors |
|---|---|
| 5.2.2. | The Default Constructor |
| 5.2.3. | Multiple Constructors |
| 5.2.4. | Calling a Constructor From a Constructor |
| 5.2.5. | Duplicating Objects using a Constructor |
| 5.2.6. | Class Initializer: during declaration |
| 5.2.7. | Order of constructor calls |
