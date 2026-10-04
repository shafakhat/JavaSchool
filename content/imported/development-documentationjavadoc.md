---
title: Documentation(JavaDoc)
nav: Documentation(JavaDoc)
description: Imported from the java2s.com archive: Documentation(JavaDoc)
section: Imported - java2s Archive
order: 1755
source: https://web.archive.org/web/20140829075629/http://www.java2s.com/Tutorial/Java/0120__Development/DocumentationJavaDoc.htm
---
A documentation comment begins with /** and ends with */.

```java title=Example.java
/**
    This is a documentation comment.
    */
```

| A documentation comment can also include HTML tags, and special tags beginning with @. |
|---|
| The @ character is followed by a keyword that defines the purpose of the tag. |
| Command Meaning @author Defines the author of the code. @deprecated Indicates deprecated methods. @exception Documents exceptions {@link} Generates a link. @param Describes the parameters for a method. @return Document the value returned from a method. @see Used to specify cross-references to some other part of the code. @throws A synonym for @exception. @version Used to describe the current version of the code. |

```java title=Example.java
/**
  @author your name
*/
public class MainClass{
  /**
    @exception IOException  When an I/O error occurs.
  */
  public static void main(String[] ){
  }
}
```

6.22.1.  Documentation(JavaDoc)
