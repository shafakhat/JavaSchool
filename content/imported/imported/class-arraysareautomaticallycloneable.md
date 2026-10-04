---
title: Arrays are automatically cloneable
nav: Arrays are automatically c...
description: 8. Tests cloning to see if destination of references are also cloned
section: Imported - java2s Archive
order: 1133
source: https://web.archive.org/web/20090531214947/http://www.java2s.com:80/Code/Java/Class/Arraysareautomaticallycloneable.htm
---
```java title=Example.java
public class Main {
  public static void main(String[] argv) throws Exception {
    int[] ints = new int[] { 123, 234 };
    int[] intsClone = (int[]) ints.clone();
  }
}
```

1.  A Cloning Example
---  ---
2.  Class is declared to be cloneable.
3.  Clone objects
4.  Creating a Deep Copy
5.  Shallow Copy Test
6.  Deep Copy Test
7.  Uses serialization to perform deep copy cloning.
8.  Tests cloning to see if destination of references are also cloned
9.  Creating local copies with clone
10.  You can insert Cloneability at any level of inheritance
11.  Cloning a composed object
12.  Serializable and clone
13.  Go through a few gyrations to add cloning to your own class
14.  Checking to see if a reference can be cloned
15.  The clone operation works for only a few items in the standard Java library
16.  Demonstration of cloning
17.  Simple demo of avoiding side-effects by using Object.clone
18.  Clone an object with clone method from parent
19.  Manipulate properties after clone operation
20.  Clone demo
