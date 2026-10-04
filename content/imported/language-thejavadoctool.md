---
title: The javadoc Tool
nav: The javadoc Tool
description: The javadoc tool generates HTML documentation from Java source files.
section: Imported - java2s Archive
order: 1006
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0020__Language/ThejavadocTool.htm
---
The javadoc tool generates HTML documentation from Java source files.

The javadoc tool locates and parses the documentation comments present in a Java source file and produces a set of HTML pages describing the class, methods, and variables present in the source file.

The syntax to use the javadoc tool is:

```java title=Example.java
javadoc [options] [packagenames] [sourcefilenames] [-subpackages pkg1:pkg2:...] [@argfiles]
```

- options refers to the command line options that you can pass to the javadoc tool.
- packagenames refers to multiple packages, separated by spaces, that javadoc should use to generate documentation. For example:
- packagesnames java.lang java.lang.reflect java.awt
- sourcefilenames refers to the source files for which javadoc needs to generate documentation.
- -subpackages: Generates documentation from the source files in specified packages and recursively in their subpackages.
- @argfiles: Refers to a file that contains Javadoc options.
