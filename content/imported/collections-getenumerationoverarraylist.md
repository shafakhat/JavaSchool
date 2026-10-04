---
title: Get Enumeration over ArrayList
nav: Get Enumeration over Array...
description: Imported from the java2s.com archive: Get Enumeration over ArrayList
section: Imported - java2s Archive
order: 2276
source: https://web.archive.org/web/20140829081728/http://www.java2s.com/Tutorial/Java/0140__Collections/GetEnumerationoverArrayList.htm
---
```java title=Example.java
import java.util.ArrayList;
import java.util.Collections;
import java.util.Enumeration;
public class Main {
  public static void main(String[] args) {
    ArrayList<String> arrayList = new ArrayList<String>();
    arrayList.add("A");
    arrayList.add("B");
    arrayList.add("D");
    arrayList.add("E");
    arrayList.add("F");
    Enumeration e = Collections.enumeration(arrayList);
    while (e.hasMoreElements())
      System.out.println(e.nextElement());
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
