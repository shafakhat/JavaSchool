---
title: Add or insert an element to ArrayList using Java ListIterator
nav: Add or insert an element t...
description: Imported from the java2s.com archive: Add or insert an element to ArrayList using Java ListIterator
section: Imported - java2s Archive
order: 1028
source: https://web.archive.org/web/20101014165412/http://www.java2s.com:80/Tutorial/Java/0140__Collections/AddorinsertanelementtoArrayListusingJavaListIterator.htm
---
```java title=Example.java
import java.util.ArrayList;
import java.util.ListIterator;
public class Main {
  public static void main(String[] args) {
    ArrayList<String> aList = new ArrayList<String>();
    aList.add("1");
    aList.add("2");
    aList.add("3");
    aList.add("4");
    aList.add("5");
    ListIterator<String> listIterator = aList.listIterator();
    listIterator.next();
    listIterator.add("Added Element");
    for (String str: aList){
      System.out.println(str);
    }
  }
}
```
