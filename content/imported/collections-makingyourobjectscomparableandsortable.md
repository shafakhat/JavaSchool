---
title: Making Your Objects Comparable and Sortable
nav: Making Your Objects Compar...
description: You can make objects comparable by implementing the java.lang.Comparable and java.util.Comparator interfaces.
section: Imported - java2s Archive
order: 2318
source: https://web.archive.org/web/20140829075931/http://www.java2s.com/Tutorial/Java/0140__Collections/MakingYourObjectsComparableandSortable.htm
---
You can make objects comparable by implementing the java.lang.Comparable and java.util.Comparator interfaces.
Classes such as java.lang.String, java.util.Date, and primitive wrapper classes all implement java.lang.Comparable.

```java title=Example.java
import java.util.Arrays;
public class MainClass {
  public static void main(String[] args) {
    int[] intArray = new int[] { 5, 4, 3, 2, 1 };
    Arrays.sort(intArray);
    for (int i : intArray) {
      System.out.println(i);
    }
  }
}
```

```java title=Example.java
1
2
3
4
5
```

| 9.1.1. | The Collections Framework consists of three parts |
|---|---|
| 9.1.2. | Framework Interfaces |
| 9.1.3. | Interface type and its implementation |
| 9.1.4. | Conversion of different Collection data types |
| 9.1.5. | Making Your Objects Comparable and Sortable |
| 9.1.6. | Using Comparable and Comparator |
| 9.1.7. | Deep clone collection: Returns a new collection containing clones of all the items in the specified collection. |
