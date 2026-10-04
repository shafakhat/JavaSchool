---
title: How to convert Array to List in Java
nav: How to convert Array to Li...
description: static<T> List<T> asList(T... a) Returns a fixed-size list backed by the specified array.
section: Imported - java2s Archive
order: 1124
source: https://web.archive.org/web/2014/http://java2s.com/Tutorials/Java/Array/How_to_convert_Array_to_List_in_Java.htm
---
In this chapter you will learn:

- Convert array to list

### Convert array to list

static<T> List<T> asList(T... a) Returns a fixed-size list backed by the specified array.

The following code creates List from Object Array.

```java title=Example.java
import java.util.Arrays;
import java.util.List;
public class Main {
  public static void main(String[] args) {
    String[] strArray = new String[] { "JavaSchool", "A", "B", "C", "D" };
    List list = Arrays.asList(strArray);
    System.out.println(list);
  }
}
```

The output:

#### Next chapter...

What you will learn in the next chapter:

- Convert array to set
