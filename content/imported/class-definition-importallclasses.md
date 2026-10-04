---
title: import all classes
nav: import all classes
description: You can import all classes in the same package by using the wild character *. For example, the following code imports all members of the java.io package.
section: Imported - java2s Archive
order: 1153
source: https://web.archive.org/web/2018/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/importallclasses.htm
---
You can import all classes in the same package by using the wild character *. For example, the following code imports all members of the java.io package.

```java title=Example.java
import java.io.*;
public class Demo {
    //...
}
```

However, to make your code more readable, it is recommended that you import a package member one at a time.

```java title=Example.java
import java.io.File;
import java.io.FileReader;
```

| 5.30.1. | Importing Other Classes |
|---|---|
| 5.30.2. | import statements |
| 5.30.3. | import all classes |
| 5.30.4. | fully qualified name |
