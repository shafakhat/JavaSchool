---
title: enum type with its own method
nav: enum type with its own met...
description: Imported from the java2s.com archive: enum type with its own method
section: Imported - java2s Archive
order: 1064
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/enumtypewithitsownmethod.htm
---
```java title=Example.java
publicclass SizeIterator {
  publicstaticvoid main(String[] args) {
    Size[] sizes = Size.values();
    for (Size s : sizes) {
      System.out.println(s);
    }
  }
}
enum Size implements Countable {
  S, M, L, XL, XXL, XXXL;
  @Deprecated
  public Size increase() {
    Size sizes[] = this.values();
    int pos = this.ordinal();
    if (pos < sizes.length - 1)
      pos++;
    return sizes[pos];
  }
}
interface Countable {
  public Size increase();
}
```
