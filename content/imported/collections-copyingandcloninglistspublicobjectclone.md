---
title: Copying and Cloning Lists
nav: Copying and Cloning Lists
description: Imported from the java2s.com archive: Copying and Cloning Lists
section: Imported - java2s Archive
order: 2418
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0140__Collections/CopyingandCloningListspublicObjectclone.htm
---
- When you call the clone() method of an ArrayList, a shallow copy of the list is created.
- The new list refers to the same set of elements as the original.
- It does not duplicate those elements.
- Since clone() is a method of the ArrayList class and not the List (or Collection) interface, you must call clone() on a reference to the class, not the interface.

```java title=Example.java
import java.util.ArrayList;
import java.util.List;
public class MainClass {
  public static void main(String[] a) {
    List list = new ArrayList();
    list.add("A");
    List list2 = ((List) ((ArrayList) list).clone());
    System.out.println(list);
    System.out.println(list2);
    list.clear();
    System.out.println(list);
    System.out.println(list2);
  }
}
java title=Example.java
[A]
[A]
[]
[A]
```

| 9.11.1. | ArrayList Class |
|---|---|
| 9.11.2. | Creating an ArrayList |
| 9.11.3. | A boolean is being stored and then retrieved from an ArrayList |
| 9.11.4. | The final constructor is the copy constructor: creating a new ArrayList from another collection |
| 9.11.5. | Adding Single Elements |
| 9.11.6. | Adding elements in the middle of a List |
| 9.11.7. | Add an element to specified index of ArrayList |
| 9.11.8. | Append all elements of other Collection to ArrayList |
| 9.11.9. | Insert all elements of other Collection to Specified Index of ArrayList |
| 9.11.10. | To create a read-only list, use the unmodifiableList() method of the Collections class |
| 9.11.11. | Adding Another Collection |
| 9.11.12. | Getting an Element |
| 9.11.13. | Get Sub List of ArrayList |
| 9.11.14. | Removing a Single Element |
| 9.11.15. | Removing Another Collection(Removing elements): public boolean removeAll(Collection c) |
| 9.11.16. | Retaining Another Collection: public boolean retainAll(Collection c) |
| 9.11.17. | Removing Ranges |
| 9.11.18. | Fetching Elements with iterator |
| 9.11.19. | Checking for Existence: public boolean contains(Object element) |
| 9.11.20. | Checking for Position |
| 9.11.21. | Checking for List Containment: public boolean containsAll(Collection c) |
| 9.11.22. | Replacing Elements with the set() method: public Object set(int index, Object element) |
| 9.11.23. | Checking Size: public int size(), public boolean isEmpty() |
| 9.11.24. | Checking Capacity |
| 9.11.25. | After adding all of the elements, call the trimToSize() method |
| 9.11.26. | Copying and Cloning Lists: public Object clone() |
| 9.11.27. | ArrayList implements the empty Serializable interface |
| 9.11.28. | Checking for Equality |
| 9.11.29. | Copying elements out of a list into an array |
| 9.11.30. | Convert a List (ArrayList) to an Array with zero length array |
| 9.11.31. | Convert a List (ArrayList) to an Array with full length array |
| 9.11.32. | Copy all elements of ArrayList to an Object Array |
| 9.11.33. | Remove duplicate items from an ArrayList |
| 9.11.34. | Removing All Elements |
| 9.11.35. | Looping through a Collection object: while loop, iterator, and for each |
| 9.11.36. | If an ArrayList contains a given item |
| 9.11.37. | Search an element of ArrayList with indexOf and lastIndexOf |
| 9.11.38. | Get container with Iterator from ArrayList |
