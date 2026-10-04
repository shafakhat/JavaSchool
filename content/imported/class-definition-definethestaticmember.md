---
title: Define the static member
nav: Define the static member
description: You can use the keyword static in front of a field or method declaration. The static keyword may come before or after the access modifier.
section: Imported - java2s Archive
order: 1204
source: https://web.archive.org/web/20140829082534/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/Definethestaticmember.htm
---
You can use the keyword static in front of a field or method declaration. The static keyword may come before or after the access modifier.
These two are correct:

```java title=Example.java
public static int a;
static public int b;
```

To define a static method in the MathUtil class:

```java title=Example.java
public class MathUtil {
    public static int add(int a, int b) {
        return a + b;
    }
}
```

From inside a static method, you cannot call instance methods or instance fields because they only exist after you create an object. You can access other static methods or fields from a static method. You can only declare a static variable in a class level. You cannot declare local static variables even if the method is static.
