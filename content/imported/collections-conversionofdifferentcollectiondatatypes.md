---
title: Conversion of different Collection data types
nav: Conversion of different Co...
description: Implementations of the Collection interface normally have a constructor that accepts a Collection object. This enables you to convert a Collection to a different type of
section: Imported - java2s Archive
order: 2317
source: https://web.archive.org/web/20140829080032/http://www.java2s.com/Tutorial/Java/0140__Collections/ConversionofdifferentCollectiondatatypes.htm
---
Implementations of the Collection interface normally have a constructor that accepts a Collection object. This enables you to convert a Collection to a different type of Collection, such as a Queue to a List, or a List to a Set, etc. Here are the constructors of some implementations:

```java title=Example.java
public ArrayList (Collection c)
     public HashSet (Collection c)
     public LinkedList (Collection c)
```

As an example, the following code converts a Queue to a List.

```java title=Example.java
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
public class MainClass {
  public static void main(String[] args) {
    Queue queue = new LinkedList();
    queue.add("Hello");
    queue.add("World");
    List list = new ArrayList(queue);
    System.out.println(list);
  }
}
```

```java title=Example.java
[Hello, World]
```

And this converts a List to a Set.

```java title=Example.java
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
public class MainClass {
  public static void main(String[] args) {
    List myList = new ArrayList();
    myList.add("Hello");
    myList.add("World");
    myList.add("World");
    Set set = new HashSet(myList);
    System.out.println(set);
  }
}
```

```java title=Example.java
[World, Hello]
```

| 9.1.1. | The Collections Framework consists of three parts |
|---|---|
| 9.1.2. | Framework Interfaces |
| 9.1.3. | Interface type and its implementation |
| 9.1.4. | Conversion of different Collection data types |
| 9.1.5. | Making Your Objects Comparable and Sortable |
| 9.1.6. | Using Comparable and Comparator |
| 9.1.7. | Deep clone collection: Returns a new collection containing clones of all the items in the specified collection. |
