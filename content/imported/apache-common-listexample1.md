---
title: List Example 1
nav: List Example 1
description: import org.apache.commons.collections.list.CursorableLinkedList;
section: Imported - java2s Archive
order: 1046
source: https://web.archive.org/web/20061018181044/http://www.java2s.com/Code/Java/Apache-Common/ListExample1.htm
---
List Example 1

```java title=Example.java
import org.apache.commons.collections.list.TreeList;
import org.apache.commons.collections.list.SetUniqueList;
import org.apache.commons.collections.list.CursorableLinkedList;
import java.util.List;
import java.util.ListIterator;
public class ListExampleV1 {
  public static void main(String args[]) {
    ListExampleV1 listExample = new ListExampleV1();
    listExample.createLists();
    uniqueList.add("Value1");
    uniqueList.add("Value1");
    System.err.println(uniqueList); // should contain only one element
    cursorList.add("Element1");
    cursorList.add("Element2");
    cursorList.add("Element3");
    ListIterator iterator = cursorList.listIterator();
    iterator.next(); // cursor now between 0th and 1st element
    iterator.add("Element2.5"); // adds this between 0th and 1st element
    System.err.println(cursorList); // modification done to the iterator are visible in the list
  }
  private void createLists() {
    uniqueList = SetUniqueList.decorate(new TreeList());
    cursorList = new CursorableLinkedList();
  }
  private static List uniqueList;
  private static List cursorList;
}
```

Download: ApacheCommonListExampleV1.zip ( 514 K )
Related examples in the same category
