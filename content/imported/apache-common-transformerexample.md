---
title: Transformer Example
nav: Transformer Example
description: Transformer transformer = TransformerUtils.invokerTransformer(
section: Imported - java2s Archive
order: 1094
source: https://web.archive.org/web/20140829211556/http://www.java2s.com/Code/Java/Apache-Common/TransformerExample.htm
---
```java title=Example.java
import org.apache.commons.collections.Transformer;
import org.apache.commons.collections.TransformerUtils;
public class TransformerExampleV1 {
  public static void main(String args[]) {
    Transformer transformer = TransformerUtils.invokerTransformer(
                               "append",
                               new Class[] {String.class},
                               new Object[] {" a Transformer?"});
    Object newObject =  transformer.transform(new StringBuffer("Are you"));
    System.err.println(newObject);
  }
}
```

ApacheCommonTransformerExampleV1.zip( 876 k)
1.  Collection Bag
2.  Collection BidiMap
3.  Collection Buffer
4.  Collection Closure
5.  Comparator Example For BuildIn Data Type
6.  Comparator Example For User Defined Class
7.  Cookie Bag 2
8.  Factory Example 1
9.  HashMap Example 1
10.  List Example 1
11.  MapHeaven 1
12.  Multi Key Example 1
13.  MultiKey Example 2
14.  Set Example 1
15.  Set Example 2
16.  Bean Comparator ( Sorting based on Properties of class )
