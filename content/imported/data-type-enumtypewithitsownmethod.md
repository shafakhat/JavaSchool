---
title: enum type with its own method
nav: enum type with its own met...
description: Imported from the java2s.com archive: enum type with its own method
section: Imported - java2s Archive
order: 1143
source: https://web.archive.org/web/20140829075605/http://www.java2s.com/Tutorial/Java/0040__Data-Type/enumtypewithitsownmethod.htm
---
```java title=Example.java
public class SizeIterator {
  public static void main(String[] args) {
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

| 2.43.1. | Enumeration Fundamentals |
|---|---|
| 2.43.2. | How to define an enumeration |
| 2.43.3. | Enums in a Class |
| 2.43.4. | equals and = operator for enum data type |
| 2.43.5. | Comparing Enumeration Values |
| 2.43.6. | Two enumeration constants can be compared for equality by using the == relational operator |
| 2.43.7. | uses an enum, rather than interface variables, to represent the answers. |
| 2.43.8. | enum type with its own method |
| 2.43.9. | Enum type field |
| 2.43.10. | enum with switch |
