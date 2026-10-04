---
title: Sort items of an ArrayList with Collections.reverseOrder()
nav: Sort items of an ArrayList...
description: Imported from the java2s.com archive: Sort items of an ArrayList with Collections.reverseOrder()
section: Imported - java2s Archive
order: 2286
source: https://web.archive.org/web/20140726063747/http://www.java2s.com/Tutorial/Java/0140__Collections/SortitemsofanArrayListwithCollectionsreverseOrder.htm
---
```java title=Example.java
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
public class Main {
  public static void main(String[] args) {
    List<String> colours = new ArrayList<String>();
    colours.add("red");
    colours.add("green");
    colours.add("blue");
    colours.add("yellow");
    colours.add("cyan");
    colours.add("white");
    colours.add("black");
    Collections.sort(colours);
    System.out.println(Arrays.toString(colours.toArray()));
    Collections.sort(colours, Collections.reverseOrder());
    System.out.println(Arrays.toString(colours.toArray()));
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
