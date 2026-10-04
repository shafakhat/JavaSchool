---
title: Adding Elements
nav: Adding Elements
description: Adding the element to the end of the list unless an index is specified.
section: Imported - java2s Archive
order: 2434
source: https://web.archive.org/web/20140829084248/http://www.java2s.com/Tutorial/Java/0140__Collections/AddingElementsaddasingleelement.htm
---
Adding the element to the end of the list unless an index is specified.

```java title=Example.java
public boolean add(Object element)
public boolean add(int index, Object element)
```

To Treat the linked list as a stack or queue:

```java title=Example.java
public boolean addFirst(Object element)
public boolean addLast(Object element)
```

The addLast() method is equivalent to call add(), with no index.

```java title=Example.java
import java.util.LinkedList;
public class MainClass {
  public static void main(String[] a) {
    LinkedList list = new LinkedList();
    list.add("A");
    list.add("B");
    list.add("C");
    list.add("D");
    list.addFirst("X");
    list.addLast("Z");
    System.out.println(list);
  }
}
java title=Example.java
[X, A, B, C, D, Z]
```

| 9.12.1. | LinkedList Class |
|---|---|
| 9.12.2. | Get first and last elements from LinkedList |
| 9.12.3. | Get elements from LinkedList |
| 9.12.4. | Get SubList from LinkedList |
| 9.12.5. | Adding Elements: add a single element |
| 9.12.6. | Add elements at beginning and end of LinkedList |
| 9.12.7. | LinkedList: add, addFirst, addLast, remove |
| 9.12.8. | Retrieving the Ends from a LinkedList |
| 9.12.9. | Removing Elements |
| 9.12.10. | Making a stack from a LinkedList |
| 9.12.11. | Making a queue from a LinkedList |
| 9.12.12. | Convert Collection to ArrayList |
| 9.12.13. | Remove all elements or clear LinkedList |
| 9.12.14. | Remove first and last elements of LinkedList |
| 9.12.15. | Remove range of elements from LinkedList |
| 9.12.16. | Remove specified element from LinkedList |
| 9.12.17. | Convert LinkedList to Array with zero length array |
| 9.12.18. | Convert LinkedList to Array with full length array |
| 9.12.19. | Convert a LinkedList to ArrayList |
| 9.12.20. | Implementing a Stack |
| 9.12.21. | Implementing a Queue with LinkedList |
| 9.12.22. | Wrap queue to synchronize the methods |
| 9.12.23. | Search elements of LinkedList |
| 9.12.24. | Replace an Element of LinkedList |
| 9.12.25. | Add object to LinkedList |
| 9.12.26. | Check if a particular element exists in LinkedList |
| 9.12.27. | Create an object array from elements of LinkedList |
| 9.12.28. | Using a LinkedList in multi-thread |
| 9.12.29. | A basic priority linked list: maintaining an individual LinkedList for each priority level. |
| 9.12.30. | Helper method for creating list |
