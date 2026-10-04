---
title: Shows default initial values
nav: Shows default initial values
description: Imported from the java2s.com archive: Shows default initial values
section: Imported - java2s Archive
order: 1112
source: https://web.archive.org/web/20070716070603/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/Showsdefaultinitialvalues.htm
---
```java title=Example.java
public class MainClass {
  boolean t;
  char c;
  byte b;
  short s;
  int i;
  long l;
  float f;
  double d;
  void print(String s) {
    System.out.println(s);
  }
  void printInitialValues() {
    print("Data type      Initial value");
    print("boolean        " + t);
    print("char           [" + c + "]");
    print("byte           " + b);
    print("short          " + s);
    print("int            " + i);
    print("long           " + l);
    print("float          " + f);
    print("double         " + d);
  }
  public static void main(String[] args) {
    MainClass iv = new MainClass();
    iv.printInitialValues();
  }
}
java title=Example.java
Data type      Initial value
boolean        false
char           []
byte           0
short          0
int            0
long           0
float          0.0
double         0.0
```
