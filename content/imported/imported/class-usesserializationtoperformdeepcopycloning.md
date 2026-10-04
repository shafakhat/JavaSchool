---
title: Uses serialization to perform deep copy cloning.
nav: Uses serialization to perf...
description: ByteArrayInputStream bais = new ByteArrayInputStream(baos.toByteArray());
section: Imported - java2s Archive
order: 1097
source: https://web.archive.org/web/20090531211856/http://www.java2s.com:80/Code/Java/Class/Usesserializationtoperformdeepcopycloning.htm
---
```java title=Example.java
import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.io.Serializable;
public class Main implements Cloneable, Serializable {
  public Object clone() {
    Object clonedObj = null;
    try {
      ByteArrayOutputStream baos = new ByteArrayOutputStream();
      ObjectOutputStream oos = new ObjectOutputStream(baos);
      oos.writeObject(this);
      oos.close();
      ByteArrayInputStream bais = new ByteArrayInputStream(baos.toByteArray());
      ObjectInputStream ois = new ObjectInputStream(bais);
      clonedObj = ois.readObject();
      ois.close();
    } catch (Exception cnfe) {
      System.out.println("Class not found " + cnfe);
    }
    return clonedObj;
  }
}
```

1.  A Cloning Example
---  ---
2.  Class is declared to be cloneable.
3.  Arrays are automatically cloneable
4.  Clone objects
5.  Creating a Deep Copy
6.  Shallow Copy Test
7.  Deep Copy Test
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
