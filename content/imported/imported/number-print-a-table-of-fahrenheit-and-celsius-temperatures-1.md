---
title: Java Algorithms How to - Print a table of fahrenheit and celsius temperatures 1
nav: Java Algorithms How to - P...
description: We would like to know how to print a table of fahrenheit and celsius temperatures 1.
section: Imported - java2s Archive
order: 1021
source: https://web.archive.org/web/20150331235514/http://www.java2s.com:80/Tutorials/Java/Algorithms_How_to/Number/Print_a_table_of_fahrenheit_and_celsius_temperatures_1.htm
---
```java title=Example.java
Back to Number  ↑
```

## Question

We would like to know how to print a table of fahrenheit and celsius temperatures 1.

## Answer

```java title=Example.java
//fromwww.java2s.com/* Print a table of Fahrenheit and Celsius temperatures
 * @author Ian F. Darwin, http://www.darwinsys.com/
 * @version $Id: TempConverter.java,v 1.10 2004/03/16 01:43:31 ian Exp $
 */publicclass TempConverter {

  publicstaticvoid main(String[] args) {
    TempConverter t = new TempConverter();
    t.start();
    t.data();
    t.end();
  }

  protectedvoid start() {
  }

  protectedvoid data() {
    for (int i=-40; i<=120; i+=10) {
      float c = (i-32)*(5f/9);
      print(i, c);
    }
  }

  protectedvoid print(float f, float c) {
    System.out.println(f + " " + c);
  }

  protectedvoid end() {
  }
}
```

```java title=Example.java
Back to Number  ↑
```
