---
title: Collections and Data structure
nav: Collections and Data struc...
description: You can use the examples and the source code any way you want, but
section: Imported - java2s Archive
order: 1014
source: https://web.archive.org/web/20090520052412/http://www.java2s.com:80/Code/Java/Generics/CollectionsandDatastructurethegenericway.htm
---
Collections and Data structure: the generic way

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
import java.util.ArrayList;
import java.io.IOException;
import java.io.PrintStream;
import java.util.HashMap;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
public class GenericsTester {
  public GenericsTester() {
  }
  public void testTypeSafeMaps(PrintStream out) throws IOException {
    Map<Integer, Integer> squares = new HashMap<Integer, Integer>();
    for (int i=0; i<100; i++) {
      squares.put(i, i*i);
    }
    for (int i=0; i<10; i++) {
      int n = i*3;
      out.println("The square of " + n + " is " + squares.get(n));
    }
  }
  public void testTypeSafeLists(PrintStream out) throws IOException {
    List listOfStrings = getListOfStrings();
    for (Iterator i = listOfStrings.iterator(); i.hasNext(); ) {
      String item = (String)i.next();
      // Work with that string
    }
    List<String> onlyStrings = new LinkedList<String>();
    onlyStrings.add("Legal addition");
    /**
     * Uncomment these two lines for an error
    onlyStrings.add(new StringBuilder("Illegal Addition"));
    onlyStrings.add(25);
     */
  }
  public void testTypeSafeIterators(PrintStream out) throws IOException {
    List<String> listOfStrings = new LinkedList<String>();
    listOfStrings.add("Happy");
    listOfStrings.add("Birthday");
    listOfStrings.add("To");
    listOfStrings.add("You");
    for (Iterator<String> i = listOfStrings.iterator(); i.hasNext(); ) {
      String s = i.next();
      out.println(s);
    }
    printListOfStrings(getListOfStrings(), out);
  }
  private List getList() {
    List list = new LinkedList();
    list.add(3);
    list.add("Blind");
    list.add("Mice");
    return list;
  }
  private List<String> getListOfStrings() {
    List<String> list = new LinkedList<String>();
    list.add("Hello");
    list.add("World");
    list.add("How");
    list.add("Are");
    list.add("You?");
    return list;
  }
  public void testTypeSafeReturnValues(PrintStream out) throws IOException {
    List<String> strings = getListOfStrings();
    for (String s : strings) {
      out.println(s);
    }
  }
  private void printListOfStrings(List<String> list, PrintStream out)
    throws IOException {
    for (Iterator<String> i = list.iterator(); i.hasNext(); ) {
      out.println(i.next());
    }
  }
  public void printList(List<?> list, PrintStream out) throws IOException {
    for (Iterator<?> i = list.iterator(); i.hasNext(); ) {
      out.println(i.next().toString());
    }
  }
  public static void main(String[] args) {
    GenericsTester tester = new GenericsTester();
    try {
      tester.testTypeSafeLists(System.out);
      tester.testTypeSafeMaps(System.out);
      tester.testTypeSafeIterators(System.out);
      tester.testTypeSafeReturnValues(System.out);
      List<Integer> ints = new LinkedList<Integer>();
      ints.add(1);
      ints.add(2);
      ints.add(3);
      tester.printList(ints, System.out);
      /** Uncomment for an error
      NumberBox<String> illegal = new NumberBox<String>();
       */
    } catch (Exception e) {
      e.printStackTrace();
    }
  }
}
class NumberBox<N extends Number> extends Box<N> {
  public NumberBox() {
    super();
  }
  // Sum everything in the box
  public double sum() {
    double total = 0;
    for (Iterator<N> i = contents.iterator(); i.hasNext(); ) {
      total = total + i.next().doubleValue();
    }
    return total;
  }
  public static <A extends Number> double sum(Box<A> box1,
                                              Box<A> box2) {
    double total = 0;
    for (Iterator<A> i = box1.contents.iterator(); i.hasNext(); ) {
      total = total + i.next().doubleValue();
    }
    for (Iterator<A> i = box2.contents.iterator(); i.hasNext(); ) {
      total = total + i.next().doubleValue();
    }
    return total;
  }
}
class Box<T> {
  protected List<T> contents;
  public Box() {
    contents = new ArrayList<T>();
  }
  public int getSize() {
    return contents.size();
  }
  public boolean isEmpty() {
    return (contents.size() == 0);
  }
  public void add(T o) {
    contents.add(o);
  }
  public T grab() {
    if (!isEmpty()) {
      return contents.remove(0);
    } else
      return null;
  }
}
```

1.  Creating a Type-Specific List
---  ---
2.  A list declared to hold objects of a type T can also hold objects that extend from T.
3.  A value retrieved from a type-specific list does not need to be casted
4.  Generic ArrayList
5.  Generic Data Structure
6.  Unchecked Example
7.  Generic Stack
8.  Enum and Generic
9.  Generic HashMap
10.  Foreach and generic data structure
11.  Pre generics example that uses a collection.
12.  Data structure and collections: Modern, generics version.
13.  Java generic: Generics and arrays.
14.  The GenStack Class
