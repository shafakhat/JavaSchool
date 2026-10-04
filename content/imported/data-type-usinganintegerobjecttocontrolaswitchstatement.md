---
title: Using an integer object to control a switch statement
nav: Using an integer object to...
description: Imported from the java2s.com archive: Using an integer object to control a switch statement
section: Imported - java2s Archive
order: 1049
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Usinganintegerobjecttocontrolaswitchstatement.htm
---
```java title=Example.java
publicclass MainClass {
  publicstaticvoid main(String args[]) {
    Integer intObject = 2;
    switch(intObject) {
      case 1: System.out.println("one");
        break;
      case 2: System.out.println("two");
        break;
      default: System.out.println("error");
    }
  }
}
java title=Example.java
two
```
