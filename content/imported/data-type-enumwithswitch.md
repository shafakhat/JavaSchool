---
title: enum with switch
nav: enum with switch
description: Imported from the java2s.com archive: enum with switch
section: Imported - java2s Archive
order: 1146
source: https://web.archive.org/web/20140829075206/http://www.java2s.com/Tutorial/Java/0040__Data-Type/enumwithswitch.htm
---
```java title=Example.java
public class SizeSwitch {
    public static void main(String[] args) {
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
