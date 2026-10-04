---
title: A value retrieved from a type-specific list does not need to be casted
nav: A value retrieved from a t...
description: A value retrieved from a type-specific list does not need to be casted
section: Imported - java2s Archive
order: 1010
source: https://web.archive.org/web/20090603182340/http://www.java2s.com:80/Code/Java/Generics/Avalueretrievedfromatypespecificlistdoesnotneedtobecasted.htm
---
A value retrieved from a type-specific list does not need to be casted

```java title=Example.java
import java.net.MalformedURLException;
import java.net.URL;
import java.util.ArrayList;
import java.util.List;
public class Main {
  public static void main(String[] argv) {
    List<URL> urlList = new ArrayList<URL>();
    try {
      urlList.add(new URL("http://www.java2s.com"));
    } catch (MalformedURLException e) {
    }
    String s = urlList.get(0).getHost();
  }
}
```

1.  Creating a Type-Specific List
---  ---
2.  A list declared to hold objects of a type T can also hold objects that extend from T.
3.  Generic ArrayList
4.  Generic Data Structure
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
