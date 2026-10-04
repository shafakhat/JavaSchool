---
title: OCA Java SE 8 Method - Java Method Declaration
nav: OCA Java SE 8 Method - Jav...
description: publicfinal void myMethod(int minutes) throws InterruptedException {
section: Imported - java2s Archive
order: 50002
source: https://www.java2s.com/Tutorials/Java/OCA_Java_SE_8_Method_Class/index.html
---
- Next »

For example, we can write a basic method.

```java title=Example.java
publicfinal void myMethod(int minutes) throws InterruptedException {
    // method body
}
```

This is called a method declaration, which specifies all the information needed to call the method.

To call this method, just type its name, followed by a single int value in parentheses:

```java title=Example.java

myMethod(10);
```

## Access Modifiers

Java offers four choices of access modifier:

Modifier  Meaning
---  ---
public  The method can be called from any class.
private  The method can only be called from within the same class.
protected  The method can only be called from classes in the same package or subclasses.
Default (Package Private) Access  The method can only be called from classes in the same package. There is no keyword for default access. Just omit the access modifier.

myMethod1() is a valid method declaration with public access.

```java title=Example.java
public void myMethod1() {}
```

myMethod2() doesn't compile because default is not a valid access modifier.

```java title=Example.java
default void myMethod2() {} // DOES NOT COMPILE
```

myMethod3() doesn't compile because the access modifier is specified after the return type.

```java title=Example.java

void public myMethod3() {} // DOES NOT COMPILE
```

myMethod4() is a valid method declaration with default access.

```java title=Example.java

void myMethod4() {}
```

## Optional Specifiers

There are a number of optional specifiers in the following list.

Unlike with access modifiers, you can have multiple specifiers in the same method although not all combinations are legal.

When this happens, you can specify them in any order.

You can have zero or more specifiers in a method declaration.

Specifiers  Meaning
---  ---
static  Used for class methods.
abstract  Used when not providing a method body.
final  Used when a method is not allowed to be overridden by a subclass.
synchronized  On the OCP but not the OCA exam.
native  Not on the OCA or OCP exam. Used with code written in another language such as C++.
strictfp  Not on the OCA or OCP exam. Used for making floating-point calculations portable.

myMethod1() is a valid method declaration with no optional specifier.

```java title=Example.java
public void myMethod1() {}
```

myMethod2() is a valid method declaration, with final as the optional specifier.

```java title=Example.java
publicfinal void myMethod2() {}
```

myMethod3() and myMethod4() are valid method declarations with both final and static as optional specifiers. The order of these two keywords doesn't matter.

```java title=Example.java
publicstaticfinal void myMethod3() {}
publicfinalstatic void myMethod4() {}
```

myMethod5() doesn't compile because modifier is not a valid optional specifier.

```java title=Example.java
public modifier void myMethod5() {} // DOES NOT COMPILE
```

myMethod6() doesn't compile because the optional specifier is after the return type.

```java title=Example.java
public void final myMethod6() {} // DOES NOT COMPILE
```

myMethod7() does compile. Java allows the optional specifiers to appear before the access modifier.

```java title=Example.java
finalpublic void myMethod7() {}
```

## Return Type

The return type might be an actual Java type such as String or int.

If there is no return type, the void keyword is used.

void means without contents.

Remember that a method must have a return type. If no value is returned, the return type is void. You cannot omit the return type.

Methods with a return type other than void MUST have a return statement inside the method body.

This return statement must include the primitive or object to be returned.

Methods that have a return type of void can have a return statement with no value returned or omit the return statement entirely.

Since the return type of myMethod1 () is void, the return statement is optional.

```java title=Example.java
public void myMethod1() { }
```

myMethod2 () shows the optional return statement that correctly doesn't return anything.

```java title=Example.java
public void myMethod2() { return; }
```

myMethod3() is a valid method with a String return type and a return statement that returns a String.

```java title=Example.java
public String myMethod3() { return ""; }
```

myMethod4() doesn't compile because the return statement is missing.

```java title=Example.java
public String myMethod4() { }  // DOES NOT COMPILE
```

myMethod5() doesn't compile because the return type is missing.

```java title=Example.java
public myMethod5() { }  // DOES NOT COMPILE
```

myMethod6() has a return statement, but it doesn't always get run. If a is 5, the return statement doesn't get executed. myMethod6() requires a String to be returned.

```java title=Example.java

String myMethod6(int a) { if (a == 4) return ""; }  // DOES NOT COMPILE
```

When returning a value, it must be assignable to the return type.

long1 method returns a long type which cannot be assigned to int type.

```java title=Example.java

int integer1() {
  return 9;
}
int long1() {
  return 9L; // DOES NOT COMPILE
}
```

- Next »
