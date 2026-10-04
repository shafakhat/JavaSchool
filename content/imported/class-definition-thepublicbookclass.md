---
title: The public Book class
nav: The public Book class
description: The Book class is a member of the yourpackagename package and has five fields. Since Book is public, it can be instantiated from any other classes.
section: Imported - java2s Archive
order: 1122
source: https://web.archive.org/web/20140829075835/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/ThepublicBookclass.htm
---
```java title=Example.java
package yourpackagename;
public class Book {
    String isbn;
    String title;
    int width;
    int height;
    int numberOfPages;
}
```

The Book class is a member of the yourpackagename package and has five fields. Since Book is public, it can be instantiated from any other classes.
A public class must be saved in a file that has the same name as the class, and the extension must be java. A Java source file can only contain one public class. A Java source file can contain other classes that are not public.
