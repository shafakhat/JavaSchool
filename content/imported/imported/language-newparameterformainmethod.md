---
title: New parameter for main method
nav: New parameter for main met...
description: Imported from the java2s.com archive: New parameter for main method
section: Imported - java2s Archive
order: 1001
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0020__Language/Newparameterformainmethod.htm
---
```java title=Example.java
publicclass Main {
  publicstaticvoid main(String... args) {
    for (String arg : args) {
      System.out.println(arg);
    }
  }
}
```
