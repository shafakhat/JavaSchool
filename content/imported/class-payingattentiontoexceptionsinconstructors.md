---
title: Paying attention to exceptions in constructors
nav: Paying attention to except...
description: // www.BruceEckel.com. See copyright notice in CopyRight.txt.
section: Imported - java2s Archive
order: 1058
source: https://web.archive.org/web/20081006032356/http://www.java2s.com:80/Code/Java/Class/Payingattentiontoexceptionsinconstructors.htm
---
Paying attention to exceptions in constructors

```java title=Example.java
// : c09:Cleanup.java
// Paying attention to exceptions in constructors.
// From 'Thinking in Java, 3rd ed.' (c) Bruce Eckel 2002
// www.BruceEckel.com. See copyright notice in CopyRight.txt.
import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
class InputFile {
  private BufferedReader in;
  public InputFile(String fname) throws Exception {
    try {
      in = new BufferedReader(new FileReader(fname));
      // Other code that might throw exceptions
    } catch (FileNotFoundException e) {
      System.err.println("Could not open " + fname);
      // Wasn't open, so don't close it
      throw e;
    } catch (Exception e) {
      // All other exceptions must close it
      try {
        in.close();
      } catch (IOException e2) {
        System.err.println("in.close() unsuccessful");
      }
      throw e; // Rethrow
    } finally {
      // Don't close it here!!!
    }
  }
  public String getLine() {
    String s;
    try {
      s = in.readLine();
    } catch (IOException e) {
      throw new RuntimeException("readLine() failed");
    }
    return s;
  }
  public void dispose() {
    try {
      in.close();
      System.out.println("dispose() successful");
    } catch (IOException e2) {
      throw new RuntimeException("in.close() failed");
    }
  }
}
public class Cleanup {
  public static void main(String[] args) {
    try {
      InputFile in = new InputFile("Cleanup.java");
      String s;
      int i = 1;
      while ((s = in.getLine()) != null)
        ; // Perform line-by-line processing here...
      in.dispose();
    } catch (Exception e) {
      System.err.println("Caught Exception in main");
      e.printStackTrace();
    }
  }
} ///:~
```

1.  Order of constructor calls
---  ---
2.  Constructors and polymorphism don't produce what you might expect
3.  Constructor initialization with composition
4.  Demonstration of a simple constructor
5.  Constructors can have arguments
6.  Show Constructors conflicting
7.  Show that if your class has no constructors, your superclass constructors still get called
8.  Constructor calls during inheritance
9.  A constructor for copying an object of the same
