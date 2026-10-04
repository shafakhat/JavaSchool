---
title: The java Tool
nav: The java Tool
description: To execute a Java class, the java tool loads the bytecode of the specified class and invokes the main() method of the class.
section: Imported - java2s Archive
order: 1028
source: https://web.archive.org/web/2014/http://www.java2s.com/Tutorial/Java/0020__Language/ThejavaTool.htm
---
The java tool executes a Java class.
---
To execute a Java class, the java tool loads the bytecode of the specified class and invokes the main() method of the class.
You can also use the java tool to run executable JAR files.
The syntax to use the java tool to execute a Java class is:

```java title=Example.java
java [options]
```

options refers to the command line options that you can pass to the java tool.
---
The class-name specifies the name of the class file to execute.
Option Description -client Selects the Java HotSpot Client Virtual Machine (VM) to use for executing a class. -server Selects the Java HotSpot Server VM to use for executing a class. -cp classpath Specifies a list of directories, JAR archives, and ZIP archives to search class files. -jar Executes a JAR file. -version Displays the JVM version.
