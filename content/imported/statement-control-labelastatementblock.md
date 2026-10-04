---
title: Label a statement block
nav: Label a statement block
description: Label statement can be referenced by the break and continue statements.
section: Imported - java2s Archive
order: 1051
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0080__Statement-Control/Labelastatementblock.htm
---
- A statement and a statement block can be labeled.
- Label names follow the same rule as Java identifiers and are terminated with a colon.

```java title=Example.java
publicclass MainClass {
  publicstaticvoid main(String[] args) {
    int x = 0, y = 0;
    sectionA: x = y + 1;
  }
}
```

And, here is an example of labeling a block:

```java title=Example.java
publicclass MainClass {
  publicstaticvoid main(String[] args) {
    start: {
      // statements
    }
  }
}
```

Label statement can be referenced by the break and continue statements.
