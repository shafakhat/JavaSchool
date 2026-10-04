---
title: Serializable Clone
nav: Serializable Clone
description: public static Object clone(final Object obj) throws Exception {
section: Imported - java2s Archive
order: 1067
source: https://web.archive.org/web/20100212194924/http://java2s.com/Code/Java/Class/SerializableClone.htm
---
```java title=Example.java
import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
public abstract class SerializableClone {
  public static Object clone(final Object obj) throws Exception {
    ByteArrayOutputStream out = new ByteArrayOutputStream();
    ObjectOutputStream oout = new ObjectOutputStream(out);
    oout.writeObject(obj);
    ObjectInputStream in = new ObjectInputStream(new ByteArrayInputStream(out.toByteArray()));
    return in.readObject();
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
8.  Uses serialization to perform deep copy cloning.
9.  Tests cloning to see if destination of references are also cloned
10.  Creating local copies with clone
11.  You can insert Cloneability at any level of inheritance
12.  Cloning a composed object
13.  Serializable and clone
14.  Go through a few gyrations to add cloning to your own class
15.  Checking to see if a reference can be cloned
16.  The clone operation works for only a few items in the standard Java library
17.  Demonstration of cloning
18.  Simple demo of avoiding side-effects by using Object.clone
19.  Clone an object with clone method from parent
20.  Manipulate properties after clone operation
21.  Deep clone Object
22.  Utility for object cloning
23.  Clone Via Serialization
24.  Clone demo
25.  Deep clone serializing/de-serializng Clone
26.  Implements a pool of internalized objects
27.  A collection of utilities to workaround limitations of Java clone framework
