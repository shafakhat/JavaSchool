---
title: Variable Scope in a block
nav: Variable Scope in a block
description: Imported from the java2s.com archive: Variable Scope in a block
section: Imported - java2s Archive
order: 1005
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0020__Language/VariableScopeinablock.htm
---
```java title=Example.java
publicclass MainClass {
  publicstaticvoid main(String[] args) {
    int outer = 1;

    {
      int inner = 2;
      System.out.println("inner = " + inner);
      System.out.println("outer = " + outer);
    }

    int inner = 3;
    System.out.println("inner = " + inner);
    System.out.println("outer = " + outer);
  }
}
```

```java title=Example.java
inner = 2
outer = 1
inner = 3
outer = 1
```
