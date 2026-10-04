---
title: Extract Substring with indexOf
nav: Extract Substring with ind...
description: Imported from the java2s.com archive: Extract Substring with indexOf
section: Imported - java2s Archive
order: 1104
source: https://web.archive.org/web/20140829091042/http://www.java2s.com/Tutorial/Java/0040__Data-Type/ExtractSubstringwithindexOf.htm
---
```java title=Example.java
public class ExtractSubstring {
  public static void main(String[] args) {
    String text = "To be or not to be";
    int count = 0;
    char separator = ' ';
    int index = 0;
    do {
      ++count;
      ++index;
      index = text.indexOf(separator, index);
    } while (index != -1);
    String[] subStr = new String[count];
    index = 0;
    int endIndex = 0;
    for (int i = 0; i < count; i++) {
      endIndex = text.indexOf(separator, index);
      if (endIndex == -1)
        subStr[i] = text.substring(index);
      else
        subStr[i] = text.substring(index, endIndex);
      index = endIndex + 1;
    }
    for (int i = 0; i < subStr.length; i++)
      System.out.println(subStr[i]);
  }
}
```
