---
title: Perform Binary Search on ArrayList
nav: Perform Binary Search on A...
description: System.out.println("Sorted ArrayList contains : " + arrayList);
section: Imported - java2s Archive
order: 2277
source: https://web.archive.org/web/20140725211937/http://www.java2s.com/Tutorial/Java/0140__Collections/PerformBinarySearchonArrayList.htm
---
```java title=Example.java
import java.util.ArrayList;
import java.util.Collections;
public class Main {
  public static void main(String[] args) {
    ArrayList<String> arrayList = new ArrayList<String>();
    arrayList.add("1");
    arrayList.add("4");
    arrayList.add("2");
    arrayList.add("5");
    arrayList.add("3");
    Collections.sort(arrayList);
    System.out.println("Sorted ArrayList contains : " + arrayList);
    int index = Collections.binarySearch(arrayList, "4");
    System.out.println("Element found at : " + index);
  }
}
```

| 9.2.1. | Using the Collections.synchronized methods |
|---|---|
| 9.2.2. | Get Synchronized List from ArrayList |
| 9.2.3. | Sort elements of ArrayList |
| 9.2.4. | Copy Elements of ArrayList to Java Vector |
| 9.2.5. | Copy Elements of One ArrayList to Another ArrayList |
| 9.2.6. | Find maximum element of ArrayList |
| 9.2.7. | Find Minimum element of ArrayList |
| 9.2.8. | Get Enumeration over ArrayList |
| 9.2.9. | Perform Binary Search on ArrayList |
| 9.2.10. | Replace All Elements Of ArrayList |
| 9.2.11. | Replace all occurrences of specified element of ArrayList |
| 9.2.12. | Reverse order of all elements of ArrayList |
| 9.2.13. | Shuffle elements of ArrayList |
| 9.2.14. | Swap elements of ArrayList |
| 9.2.15. | Sort ArrayList in descending order using comparator |
| 9.2.16. | Search collection element |
| 9.2.17. | Rotate elements of a collection |
| 9.2.18. | Sort items of an ArrayList with Collections.reverseOrder() |
| 9.2.19. | Create an empty collection object |
| 9.2.20. | The Collections.fill() method |
| 9.2.21. | Create and demonstrate an immutable collection. |
| 9.2.22. | A combination of two collections into a collection |
