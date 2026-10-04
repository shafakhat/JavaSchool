---
title: Switch statement with enum
nav: Switch statement with enum
description: Imported from the java2s.com archive: Switch statement with enum
section: Imported - java2s Archive
order: 1054
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Switchstatementwithenum.htm
---
```java title=Example.java
publicclass MainClass {
  enum Choice { Choice1, Choice2, Choice3 }
  publicstaticvoid main(String[] args) {
    Choice ch = Choice.Choice1;
    switch(ch) {
      case Choice1:
        System.out.println("Choice1 selected");
        break;
     case Choice2:
       System.out.println("Choice2 selected");
       break;
     case Choice3:
       System.out.println("Choice3 selected");
       break;
    }
  }
}
```

```java title=Example.java
Choice1 selected
```
