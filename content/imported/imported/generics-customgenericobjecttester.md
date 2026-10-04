---
title: Custom Generic Object Tester
nav: Custom Generic Object Tester
description: You can use the examples and the source code any way you want, but
section: Imported - java2s Archive
order: 1018
source: https://web.archive.org/web/20090408024048/http://www.java2s.com:80/Code/Java/Generics/CustomGenericObjectTester.htm
---
Custom Generic Object Tester

```java title=Example.java
/*
License for Java 1.5 'Tiger': A Developer's Notebook
     (O'Reilly) example package
Java 1.5 'Tiger': A Developer's Notebook (O'Reilly)
by Brett McLaughlin and David Flanagan.
ISBN: 0-596-00738-8
You can use the examples and the source code any way you want, but
please include a reference to where it comes from if you use it in
your own products or services. Also note that this software is
provided by the author "as is", with no expressed or implied warranties.
In no event shall the author be liable for any direct or indirect
damages arising in any way out of the use of this software.
*/
import java.io.IOException;
import java.io.PrintStream;
import java.util.LinkedList;
import java.util.List;
class GuitarManufacturerList extends LinkedList<String> {
  public GuitarManufacturerList() {
    super();
  }
  public boolean add(String manufacturer) {
    if (manufacturer.indexOf("Guitars") == -1) {
      return false;
    } else {
      super.add(manufacturer);
      return true;
    }
  }
}
public class CustomObjectTester {
  /** A custom object that extends List */
  private GuitarManufacturerList manufacturers;
  public CustomObjectTester() {
    this.manufacturers = new GuitarManufacturerList();
  }
  /**
   * <p>Test iterating over an object that extends List</p>
   */
  public void testListExtension(PrintStream out) throws IOException {
    // Add some items for good measure
    manufacturers.add("Epiphone Guitars");
    manufacturers.add("Gibson Guitars");
    // Iterate with for/in
    for (String manufacturer : manufacturers) {
      out.println(manufacturer);
    }
  }
  public static void main(String[] args) {
    try {
      CustomObjectTester tester = new CustomObjectTester();
      tester.testListExtension(System.out);
    } catch (Exception e) {
      e.printStackTrace();
    }
  }
}
```

1.  A simple generic class.
---  ---
2.  Demonstrate the non generic class
3.  Stats attempts (unsuccessfully) to create a generic class
4.  A simple generic class heirarchy.
5.  A nongeneric class can be the superclass of a generic subclass.
6.  Use the instanceof operator with a generic class hierarchy.
7.  Java hierarchy generic class
