---
title: Java Object Oriented Design - Java Method Overload
nav: Java Object Oriented Desig...
description: Having more than one method with the same name in the same class is called method overloading.
section: Imported - java2s Archive
order: 50142
source: https://www.java2s.com/Tutorials/Java/Java_Object_Oriented_Design/0055__Java_Method_Overload.html
---
```java title=Example.java
« Previous
```

- Next »

Having more than one method with the same name in the same class is called method overloading.

Methods with the same name in a class could be declared methods, inherited methods, or a combination of both.

Overloaded methods must have different number of parameters, different types of parameters, or both.

The return type, access level and throws clause of a method play no effect in making it an overloaded method.

```java title=Example.java
import java.io.IOException;
/*www.java2s.com*/class MyClass {
  publicvoid m1(int a) {
    // Code goes here
  }
  publicvoid m1(int a, int b) {
    // Code goes here
  }
  publicint m1(String a) {
    // Code goes here
return 0;
  }
  publicint m1(String a, int b) throws IOException {
    // Code goes here
return 0;
  }
}
```

## Example

The following code shows how to use overload.

```java title=Example.java
publicclass Main {
  publicdouble add(int a, int b) {
    System.out.println("Inside add(int a, int b)");
    double s = a + b;
    return s;//fromwww.java2s.com
  }
  publicdouble add(double a, double b) {
    System.out.println("Inside add(double a,  double   b)");
    double s = a + b;
    return s;
  }
  publicstaticvoid main(String[] args) {
    Main ot = new Main();
    int i = 1;
    int j = 1;
    double d1 = 10.42;
    float f1 = 22.3F;
    float f2 = 24.5F;
    short s1 = 22;
    short s2 = 26;
    ot.add(i, j);
    ot.add(d1, j);
    ot.add(i, s1);
    ot.add(s1, s2);
    ot.add(f1, f2);
    ot.add(f1, s2);
  }
}
```

The code above generates the following result.

## Example 2

Sometimes, overloaded methods and automatic type widening may confuse the compiler resulting in a compiler error.

```java title=Example.java
class Adder {/*fromwww.java2s.com*/publicdouble add(int a, double b) {
    return a + b;
  }
  publicdouble add(double a, int b) {
    return a + b;
  }
}
publicclass Main {
  publicstaticvoid main(String[] args) {
    Adder a = new Adder();
    // double d = a.add(2, 3); // A compile-time error
double d1 = a.add((double) 2, 3); // OK. Will use add(double, int)
double d2 = a.add(2, (double) 3); // OK. Will use add(int, double)

  }
}
```

- Next »
- « Previous
