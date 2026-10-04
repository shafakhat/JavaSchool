---
title: Declaring Variables
nav: Declaring Variables
description: In this example, a String object is declared and initialized with a reference to the
section: Imported - java2s Archive
order: 1001
source: https://web.archive.org/web/20090530095922/http://www.java2s.com:80/Code/Java/Class/DeclaringVariables.htm
---
```java title=Example.java
/*
In this example, a String object is declared and initialized with a reference to the
String "blah" at the top of the main() method. An int named k is declared after the
String object but is not given a value until later in the program. Another int named
j is declared and intialized in the for loop. This variable will not be accessible
outside of the for loop.
*/
public class TestDeclare {
  public static void main(String args[]) {
    String str = "blah";
    int k;
    System.out.println(str);
    k = 2;
    for (int j = 0; j < 2; ++j) {
      System.out.println("j is " + j);
    }
  }
}
```

1.  Accessing Outer Class Variables
---  ---
2.  Specifying initial values in a class definition
3.  The full process of initialization
