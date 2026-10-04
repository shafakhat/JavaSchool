---
title: Interface Generic (Has compile error)
nav: Interface Generic (Has com...
description: class ChildClass extends ParentClass implements BaseInterface<String> { }
section: Imported - java2s Archive
order: 1034
source: https://web.archive.org/web/20090501061725/http://www.java2s.com:80/Code/Java/Generics/InterfaceGenericHascompileerror.htm
---
```java title=Example.java
import java.util.*;
interface BaseInterface<A> {
    A getInfo();
}
class ParentClass implements BaseInterface<Integer> {
    public Integer getInfo()
    {
        return(null);
    }
}
class ChildClass extends ParentClass implements BaseInterface<String> { }
public class BadParents {
    public static void main(String args[])
    {
        Vector<Integer> v1 = new Vector<Integer>();
        Vector v2;
        v1 = v2;
        v2 = v1;
    }
}
```

1.  A generic interface example.
