---
title: Using the For-Each Loop with Collections
nav: Using the For-Each Loop wi...
description: For-Each Loop can be used to any object that implements the Iterable interface. This includes all collections defined by the Collections Framework,
section: Imported - java2s Archive
order: 1328
source: https://web.archive.org/web/20140829083538/http://www.java2s.com/Tutorial/Java/0080__Statement-Control/UsingtheForEachLoopwithCollectionsArrayList.htm
---
For-Each Loop can be used to any object that implements the Iterable interface. This includes all collections defined by the Collections Framework,

```java title=Example.java
import java.util.ArrayList;
public class MainClass {
  public static void main(String args[]) {
    ArrayList<Double> list = new ArrayList<Double>();
    list.add(10.14);
    list.add(20.22);
    list.add(30.78);
    list.add(40.46);
    double sum = 0.0;
    for(double itr : list)
      sum = sum + itr;
    System.out.println(sum);
  }
}
```
