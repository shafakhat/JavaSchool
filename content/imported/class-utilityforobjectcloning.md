---
title: Utility for object cloning
nav: Utility for object cloning
description: * Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 1101
source: https://web.archive.org/web/20100212194911/http://java2s.com/Code/Java/Class/Utilityforobjectcloning.htm
---
```java title=Example.java
/*
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
/**
 *
 * @author <a href="mailto:weaver@apache.org">Scott T. Weaver</a>
 */
public class CloneUtil
{
    /**
     * Provides a deep clone serializing/de-serializng <code>objToClone</code>
     *
     * @param objToClone The object to be cloned
     * @return The cloned object
     */
    public static final Object deepClone(Object objToClone)
    {
        try
        {
            ByteArrayOutputStream bytearrayoutputstream = new ByteArrayOutputStream(100);
            ObjectOutputStream objectoutputstream = new ObjectOutputStream(bytearrayoutputstream);
            objectoutputstream.writeObject(objToClone);
            byte abyte0[] = bytearrayoutputstream.toByteArray();
            objectoutputstream.close();
            ByteArrayInputStream bytearrayinputstream = new ByteArrayInputStream(abyte0);
            ObjectInputStream objectinputstream = new ObjectInputStream(bytearrayinputstream);
            Object clone = objectinputstream.readObject();
            objectinputstream.close();
            return clone;
        }
        catch (Exception exception)
        {
            // nothing
        }
        return null;
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
23.  Clone Via Serialization
24.  Clone demo
25.  Deep clone serializing/de-serializng Clone
26.  Implements a pool of internalized objects
27.  A collection of utilities to workaround limitations of Java clone framework
