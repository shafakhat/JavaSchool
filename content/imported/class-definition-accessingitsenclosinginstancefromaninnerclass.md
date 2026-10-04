---
title: Accessing its enclosing instance from an inner class
nav: Accessing its enclosing in...
description: Imported from the java2s.com archive: Accessing its enclosing instance from an inner class
section: Imported - java2s Archive
order: 1063
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/Accessingitsenclosinginstancefromaninnerclass.htm
---
```java title=Example.java
publicclass Main {
  privateint number = 12;
  public Main() {
    InnerClass inner = new InnerClass();
    inner.printNumber();
  }
  class InnerClass {
    publicvoid printNumber() {
      System.out.println(Main.this.number);
    }
  }
  publicstaticvoid main(String[] args) {
    new Main();
  }
}
```
