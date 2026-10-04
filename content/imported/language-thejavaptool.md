---
title: The javap Tool
nav: The javap Tool
description: The javap command displays information about the methods, variables, and parameters present in a class file.
section: Imported - java2s Archive
order: 1005
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0020__Language/ThejavapTool.htm
---
The javap command displays information about the methods, variables, and parameters present in a class file.

The output of the javap tool depends on the options used. If you do not specify any options while using the jap tool, the javap tool prints the package, protected, and public fields and methods of the classes passed to the tool.

The syntax to use the javap tool is:

```java title=Example.java
javap [options] class. . .
```

Option  Description
---  ---
-help  Displays a help message for the javap tool.
public  Shows only the public classes and members.
protected  Shows only the public and protected classes and members.
private  Shows all classes and members.
package  Shows the package, protected, and public classes and members. This is the default option of the javap tool.
-classpath path  Specifies the class path that javap should use to locate the class file to disassemble.
