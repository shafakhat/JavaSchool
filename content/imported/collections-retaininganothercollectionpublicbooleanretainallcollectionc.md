---
title: Retaining Another Collection
nav: Retaining Another Collection
description: Only those elements within the collection argument are kept within the vector. Everything else is removed instead.
section: Imported - java2s Archive
order: 2410
source: https://web.archive.org/web/20140829075336/http://www.java2s.com/Tutorial/Java/0140__Collections/RetainingAnotherCollectionpublicbooleanretainAllCollectionc.htm
---
Only those elements within the collection argument are kept within the vector. Everything else is removed instead.

```java title=Example.java
import java.util.Vector;
public class MainClass {
  public static void main(String args[]) {
    Vector v = new Vector(5);
    for (int i = 0; i < 10; i++) {
      v.add(0,i);
    }
    System.out.println(v);
    Vector v2 = new Vector(5);
    for (int i = 0; i < 5; i++) {
      v2.add(0,i);
    }
    System.out.println(v2);
    System.out.println(v2.equals(v));
    v.retainAll(v2);
    System.out.println(v);
  }
}
java title=Example.java
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
[4, 3, 2, 1, 0]
false
[4, 3, 2, 1, 0]
```

| 9.47.1. | Java vectors: dynamically sized arrays with synchronized access. |
|---|---|
| 9.47.2. | The asList() method of the Arrays class will create an object |
| 9.47.3. | Adding Elements: Adding at the End |
| 9.47.4. | Adding in the Middle |
| 9.47.5. | Adding Another Collection |
| 9.47.6. | Printing Vectors: a comma-delimited list, in index order and surrounded by square brackets ([]) |
| 9.47.7. | Removing All Elements: clear out all of a vector's elements: clear() and removeAllElements() |
| 9.47.8. | When removing all the elements from a vector, the capacity does not change. |
| 9.47.9. | Removing Single Elements |
| 9.47.10. | Passing the object to remove to either of the remove() or removeElement() methods |
| 9.47.11. | Removing Another Collection: public boolean removeAll(Collection c) |
| 9.47.12. | Retaining Another Collection: public boolean retainAll(Collection c) |
| 9.47.13. | Replacing Elements |
| 9.47.14. | Replace an element at specified index of Java Vector |
| 9.47.15. | Search an element of Java Vector |
| 9.47.16. | Search an element of Vector from specific index |
| 9.47.17. | Replace All Elements Of Vector with Collections.fill |
| 9.47.18. | Sizing Vectors |
| 9.47.19. | Setting vector's size to trim elements |
| 9.47.20. | Storage Capacity |
| 9.47.21. | ensureCapacity(): make sure a vector is large enough before adding elements: public void ensureCapacity(int minCapacity) |
| 9.47.22. | Vector Immutability |
| 9.47.23. | Getting elements by Index without generics |
| 9.47.24. | Getting elements by Index with Generics |
| 9.47.25. | Getting by Position |
| 9.47.26. | Enumerating through the Elements |
| 9.47.27. | Using Iterator to loop through Vector elements |
| 9.47.28. | Using list Iterator to loop through the vector |
| 9.47.29. | Multidimensional Vectors (Vectors of Vectors) |
| 9.47.30. | The contains() method: reports if a specific element is within the vector |
| 9.47.31. | Checking for Position: where it is in the vector |
| 9.47.32. | Checking for Position from End |
| 9.47.33. | Finding all the positions for a single element |
| 9.47.34. | Checking for Collection Containment: containsAll() |
| 9.47.35. | Copying and Cloning Vectors |
| 9.47.36. | Converting the vector to an array: public Object[] toArray() |
| 9.47.37. | Converting the vector to an array: public Object[] toArray(Object[] a) |
| 9.47.38. | Converting the vector to an array: public void copyInto(Object[] anArray) |
| 9.47.39. | subList(): taking a subset of the vector's elements and referencing them from another List |
| 9.47.40. | The Vector's subList() method does not make a clone of the element references |
| 9.47.41. | The equals() method is used to check for element equality |
| 9.47.42. | Checking Vectors for Equality: Containing equivalent elements in identical order |
| 9.47.43. | Count distinct elements in a Vector |
| 9.47.44. | The Vector class overrides the hashCode() method: public int hashCode() |
| 9.47.45. | Serializing Vector |
| 9.47.46. | Replace all occurrences of specified element of Java Vector |
| 9.47.47. | Reverse order of all elements of Java Vector |
| 9.47.48. | Shuffle elements of Vector |
| 9.47.49. | Swap elements of Vector |
| 9.47.50. | Sort Vector in descending order using comparator |
| 9.47.51. | Enumerate through a Vector using Java Enumeration |
| 9.47.52. | Append all elements of other Collection to Vector |
| 9.47.53. | Perform Binary Search on Java Vector |
| 9.47.54. | Get Enumeration over Java Vector |
| 9.47.55. | Find maximum element of Java Vector |
| 9.47.56. | Find Minimum element of Java Vector |
| 9.47.57. | Create Java ArrayList From Enumeration which is from Vector |
| 9.47.58. | Copy Elements of Vector to ArrayList with Collection.copy |
| 9.47.59. | Copy Elements of One Vector to Another Vector with Collection.copy |
| 9.47.60. | Unmodifiable Vector Adapter |
