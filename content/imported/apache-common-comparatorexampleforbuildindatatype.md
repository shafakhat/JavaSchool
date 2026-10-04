---
title: Comparator Example For BuildIn Data Type
nav: Comparator Example For Bui...
description: import org.apache.commons.collections.comparators.BooleanComparator;
section: Imported - java2s Archive
order: 1020
source: https://web.archive.org/web/20061018181009/http://www.java2s.com/Code/Java/Apache-Common/ComparatorExampleForBuildInDataType.htm
---
Comparator Example For BuildIn Data Type

```java title=Example.java
import org.apache.commons.collections.ComparatorUtils;
import org.apache.commons.collections.comparators.BooleanComparator;
import org.apache.commons.collections.comparators.FixedOrderComparator;
import java.util.Arrays;
import java.util.Comparator;
public class ComparatorExampleForBuildInDataType {
  private static Comparator boolComp;
  private static Comparator fixedComp;
  private static Boolean boolParams[] = {new Boolean(true), new Boolean(true),
                                         new Boolean(false), new Boolean(false)};
  private static String  stringParams[] = {"Russia", "Canada", "USA", "Australia", "India"};
  public static void main(String args[]) {
    ComparatorExampleForBuildInDataType example = new ComparatorExampleForBuildInDataType();
    example.createComparators();
    Arrays.sort(boolParams, boolComp);
    example.printArray(boolParams);
    Arrays.sort(stringParams);
    example.printArray(stringParams);
    Arrays.sort(stringParams, fixedComp);
    example.printArray(stringParams);
  }
  private void createComparators() {
    boolComp = ComparatorUtils.booleanComparator(true);
    fixedComp = new FixedOrderComparator(stringParams);
  }
  private void printArray(Object[] array) {
    for(int i = 0; i < array.length; i++)
      System.err.println(array[i]);
  }
}
```

Download: ApacheCollectionComparatorExampleForBuildInDataType.zip ( 514 K )
Related examples in the same category
