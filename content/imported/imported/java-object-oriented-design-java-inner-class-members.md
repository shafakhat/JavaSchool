---
title: Java Object Oriented Design - Java Inner Class Members
nav: Java Object Oriented Desig...
description: An inner class has access to all instance members, instance fields, and instance methods of its enclosing class.
section: Imported - java2s Archive
order: 50164
source: https://www.java2s.com/Tutorials/Java/Java_Object_Oriented_Design/0280__Java_Inner_Class_Members.html
---
```java title=Example.java
« Previous
```

- Next »

An inner class has access to all instance members, instance fields, and instance methods of its enclosing class.

```java title=Example.java
class Outer {/*fromwww.java2s.com*/privateint value = 2014;
  publicclass Inner {
    publicvoid printValue() {
      System.out.println("Inner: Value  = " + value);
    }
  } // Inner class ends here
publicvoid printValue() {
    System.out.println("Outer: Value  = " + value);
  }
  publicvoid setValue(int newValue) {
    this.value = newValue;
  }
}
publicclass Main {
  publicstaticvoid main(String[] args) {
    Outer out = new Outer();
    Outer.Inner in = out.new Inner();
    out.printValue();
    in.printValue();
    out.setValue(2015);
    out.printValue();
    in.printValue();
  }
}
```

The code above generates the following result.

## Example

The following code shows how to access inner variable for inner class.

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String[] args) {
    Outer out = new Outer();
    Outer.Inner in = out.new Inner();/*www.java2s.com*/
    out.printValue();
    in.printValue();
    out.setValue(3);
    out.printValue();
    in.printValue();
  }
}
class Outer {
  privateint value = 1;
  publicclass Inner {
    privateint value = 2;
    publicvoid printValue() {
      System.out.println("Inner: Value  = " + value);
    }
  } // Inner class ends here
publicvoid printValue() {
    System.out.println("Outer: Value  = " + value);
  }
  publicvoid setValue(int newValue) {
    this.value = newValue;
  }
}
```

The code above generates the following result.

## this keyword for Inner class

The following code shows how to use the keyword this in the inner class.

```java title=Example.java
class Outer {/*www.java2s.com*/privateint value = 1;
  class QualifiedThis {
    privateint value = 2;
    publicvoid printValue() {
      System.out.println("value=" + value);
      System.out.println("this.value=" + this.value);
      System.out.println("QualifiedThis.this.value=" + QualifiedThis.this.value);
    }
    publicvoid printHiddenValue() {
      int value = 2;
      System.out.println("value=" + value);
      System.out.println("this.value=" + this.value);
      System.out.println("QualifiedThis.this.value=" + QualifiedThis.this.value);
    }
  }
  publicvoid printValue() {
    System.out.println("value=" + value);
    System.out.println("this.value=" + this.value);
  }
}
publicclass Main {
  publicstaticvoid main(String[] args) {
    Outer outer = new Outer();
    Outer.QualifiedThis qt = outer.new QualifiedThis();
    System.out.println("printValue():");
    qt.printValue();
    System.out.println("printHiddenValue():");
    qt.printHiddenValue();
    outer.printValue();
  }
}
```

The code above generates the following result.

## Hidden variable

If the instance variable name is hidden, you must qualify its name with the keyword this or the class name as well as the keyword this.

```java title=Example.java
class TopLevelOuter {
  privateint v1 = 100;
/*www.java2s.com*/// Here, only v1 is in scope
publicclass InnerLevelOne {
    privateint v2 = 200;
    // Here, only v1 and v2 are in scope
publicclass InnerLevelTwo {
      privateint v3 = 300;
      // Here, only v1, v2, and v3 are in scope
publicclass InnerLevelThree {
        privateint v4 = 400;
        // Here, all v1, v2, v3, and v4 are in scope

      }
    }
  }
}
```

## From outer class

The following code shows how to reference the variable from the outer class.

```java title=Example.java
publicclass Test{
  privateint value = 1;
  publicclass Inner {
    privateint value = 2;
//www.java2s.compublicvoid printValue() {
      System.out.println("Inner: Value  = " + value);
      System.out.println("Outer: Value  = " + Test.this.value);
    }
  } // Inner class ends here
publicvoid printValue() {
    System.out.println("\nOuter - printValue()...");
    System.out.println("Outer: Value  = " + value);
  }
  publicvoid setValue(int newValue) {
    System.out.println("\nSetting  Outer's value to " + newValue);
    this.value = newValue;
  }
}
```

- Next »
- « Previous
