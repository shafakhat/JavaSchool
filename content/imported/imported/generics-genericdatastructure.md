---
title: Generic Data Structure
nav: Generic Data Structure
description: 2. A list declared to hold objects of a type T can also hold objects that extend from T.
section: Imported - java2s Archive
order: 1027
source: https://web.archive.org/web/20090603133127/http://www.java2s.com:80/Code/Java/Generics/GenericDataStructure.htm
---
```java title=Example.java
import java.io.*;
interface Executor<E extends Exception> {
    void execute() throws E;
}
public class GenericExceptionTest {
    public static void main(String args[]) {
        try {
            Executor<IOException> e =
                new Executor<IOException>() {
                public void execute() throws IOException
                {
                    // code here that may throw an
                    // IOException or a subtype of
                    // IOException
                }
            };
            e.execute();
        } catch(IOException ioe) {
            System.out.println("IOException: " + ioe);
            ioe.printStackTrace();
        }
    }
}
```

1.  Creating a Type-Specific List
---  ---
2.  A list declared to hold objects of a type T can also hold objects that extend from T.
3.  A value retrieved from a type-specific list does not need to be casted
4.  Generic ArrayList
5.  Unchecked Example
6.  Generic Stack
7.  Enum and Generic
8.  Generic HashMap
9.  Foreach and generic data structure
10.  Pre generics example that uses a collection.
11.  Data structure and collections: Modern, generics version.
12.  Java generic: Generics and arrays.
13.  Collections and Data structure: the generic way
14.  The GenStack Class
