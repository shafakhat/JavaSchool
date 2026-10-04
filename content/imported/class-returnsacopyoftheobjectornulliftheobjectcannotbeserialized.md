---
title: Returns a copy of the object, or null if the object cannot be serialized.
nav: Returns a copy of the obje...
description: Returns a copy of the object, or null if the object cannot be serialized.
section: Imported - java2s Archive
order: 1065
source: https://web.archive.org/web/20111013063840/http://www.java2s.com:80/Code/Java/Class/Returnsacopyoftheobjectornulliftheobjectcannotbeserialized.htm
---
```java title=Example.java
/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
//package wekinator.util;
import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
/**
 *
 * http://javatechniques.com/blog/faster-deep-copies-of-java-objects/
 */
public class DeepCopy {
    /**
     * Returns a copy of the object, or null if the object cannot
     * be serialized.
     */
     // http://javatechniques.com/blog/faster-deep-copies-of-java-objects/
    public static Object copy(Object orig) throws IOException, ClassNotFoundException {
        Object obj = null;
            // Write the object out to a byte array
            ByteArrayOutputStream bos = new ByteArrayOutputStream();
            ObjectOutputStream out = new ObjectOutputStream(bos);
            out.writeObject(orig);
            out.flush();
            out.close();
            // Make an input stream from the byte array and read
            // a copy of the object back in.
            ObjectInputStream in = new ObjectInputStream(
                new ByteArrayInputStream(bos.toByteArray()));
            obj = in.readObject();
        return obj;
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
22.  Serializable Clone
23.  Utility for object cloning
24.  Clone Via Serialization
25.  Clone demo
26.  Deep clone serializing/de-serializng Clone
27.  Implements a pool of internalized objects
28.  A collection of utilities to workaround limitations of Java clone framework
29.  This program demonstrates cloning
30.  Deep-copies the values from one object to the other
31.  Object Deep copy
