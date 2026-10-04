---
title: Java Compiler Options
nav: Java Compiler Options
description: Imported from the java2s.com archive: Java Compiler Options
section: Imported - java2s Archive
order: 1002
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0020__Language/JavaCompilerOptions.htm
---
```java title=Example.java
Folder                         Description
-g                             Generate all debugging info
-g:none                        Generate no debugging info
-g:{lines, vars, source}       Generate only some debugging info
-nowarn                        Generate no warnings
-verbose                       Output messages about what the compiler is doing
-deprecation                   Output source locations where deprecated APIs are used
-classpath <path>              Specify where to find user class files
-cp <path>                     Specify where to find user class files
-sourcepath <path>             Specify where to find input source files
-bootclasspath <path>          Override location of bootstrap class files
-extdirs <dirs>                Override location of installed extensions
-endorseddirs <dirs>           Override location of endorsed standards path
-d <directory>                 Specify where to place generated class files
-encoding <encoding>           Specify character encoding used by source files
-source <release>              Provide source compatibility with specified release
-target <release>              Generate class files for specific VM version
-version                       Version information
-help                          Print a synopsis of standard options
-X                             Print a synopsis of nonstandard options
-J<flag>                       Pass <flag> directly to the runtime system
```
