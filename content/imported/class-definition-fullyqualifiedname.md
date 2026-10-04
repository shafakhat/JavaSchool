---
title: fully qualified name
nav: fully qualified name
description: Members of the java.lang package are imported automatically. Thus, to use the java.lang.String, for example, you do not need to explicitly import the class.
section: Imported - java2s Archive
order: 1149
source: https://web.archive.org/web/20140829075246/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/fullyqualifiedname.htm
---
Members of the java.lang package are imported automatically. Thus, to use the java.lang.String, for example, you do not need to explicitly import the class.
The only way to use classes that belong to other packages without importing them is to use the fully qualified names of the classes in your code. For example, the following code declares the java.io.File class using its fully qualified name.

```java title=Example.java
java.io.File file = new java.io.File(filename);
```

If you class import identically-named classes from different packages, you must use the fully qualified names when declaring the classes. For example, the Java core libraries contain the classes java.sql.Date and java.util.Date. In this case, you must write the fully qualified names of java.sql.Date and java.util.Date to use them.
