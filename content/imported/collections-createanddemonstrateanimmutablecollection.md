---
title: Create and demonstrate an immutable collection.
nav: Create and demonstrate an ...
description: Collection<Character> immutableCol = Collections.unmodifiableCollection(list);
section: Imported - java2s Archive
order: 2290
source: https://web.archive.org/web/20140829081533/http://www.java2s.com/Tutorial/Java/0140__Collections/Createanddemonstrateanimmutablecollection.htm
---
```java title=Example.java
import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.List;
public class Main {
  public static void main(String args[]) {
    List<Character> list = new ArrayList<Character>();
    list.add('X');
    System.out.println("Element added to list: " + list.get(0));
    Collection<Character> immutableCol = Collections.unmodifiableCollection(list);
    immutableCol.add('Y');
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
