---
title: enum with switch
nav: enum with switch
description: Imported from the java2s.com archive: enum with switch
section: Imported - java2s Archive
order: 1052
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/enumwithswitch.htm
---
```java title=Example.java
publicclass SizeSwitch {
    publicstaticvoid main(String[] args) {
        Size size = Size.XL;
        switch(size){
            case S:
                System.out.println("S");
                break;
            case M:
                System.out.println("M");
                break;
            case L:
                System.out.println("L");
                break;
            case XL:
                System.out.println("XL");
                break;
            case XXL:
                System.out.println("XXL");
                break;
            case XXXL:
                System.out.println("XXXL");
                break;
        }
    }
}
enum Size {
  S, M, L, XL, XXL, XXXL;
}
```
