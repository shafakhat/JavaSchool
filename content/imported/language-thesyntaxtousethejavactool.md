---
title: The syntax to use the javac tool
nav: The syntax to use the java...
description: Imported from the java2s.com archive: The syntax to use the javac tool
section: Imported - java2s Archive
order: 1004
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0020__Language/Thesyntaxtousethejavactool.htm
---
```java title=Example.java
javac [options] [sourcefiles] [classes]
```

- options: Refers to command line options.
- sourcefiles: Refers to the source files that need to be compiled.
- classes: Refers to one or more classes to be processed for annotations.

Option  Description
---  ---
-cp path or -classpath path  Specifies the Java classpath.
-d directory  Sets the destination directory to store class files.
-g  Generates debugging information.
-g:none  Instructs the javac tool not to generate any debugging information.
-help  Prints information about the options of the javac tool.
-Xlint  Displays warnings against the use of deprecated classes and methods.
-Xlint:-name  Disables deprecation warnings for a specified class, interface, or method.
-Xlint:path  Displays a warning when you specify a directory to compile but the directory does not exist.
