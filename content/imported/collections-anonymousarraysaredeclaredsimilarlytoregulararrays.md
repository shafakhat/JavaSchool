---
title: Anonymous arrays are declared similarly to regular arrays
nav: Anonymous arrays are decla...
description: Imported from the java2s.com archive: Anonymous arrays are declared similarly to regular arrays
section: Imported - java2s Archive
order: 1042
source: https://web.archive.org/web/20070520061533/http://www.java2s.com:80/Tutorial/Java/0140__Collections/Anonymousarraysaredeclaredsimilarlytoregulararrays.htm
---
```java title=Example.java
new type[] {comma-delimited-list}
java title=Example.java
public class MainClass {
  public static void main (String args[]) {
    int array1[] = {1, 2, 3, 4, 5};
    for(int i: array1){
      System.out.println(i);
    }
  }
}
java title=Example.java
1
2
3
4
5
```
