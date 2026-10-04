---
title: Using the Diamond Operator and Suppressing Unchecked Warnings(SuppressWarnings)
nav: Using the Diamond Operator...
description: Using the Diamond Operator and Suppressing Unchecked Warnings(SuppressWarnings)
section: Imported - java2s Archive
order: 1149
source: https://web.archive.org/web/20130821052157/http://java2s.com/Code/Java/JDK-7/UsingtheDiamondOperatorandSuppressingUncheckedWarningsSuppressWarnings.htm
---
```java title=Example.java
import java.util.ArrayList;
import java.util.List;
public class Test {
  public static void main(String[] args) {
  @SuppressWarnings("unchecked")
    List<String> arrayList = new ArrayList();
  }
}
```

1.  Using the Diamond Operator for Constructor Type Inference
---  ---
2.  Using the Diamond Operator when type is not obvious
3.  Using the @SafeVarargs Annotation
