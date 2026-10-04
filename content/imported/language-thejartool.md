---
title: The jar Tool
nav: The jar Tool
description: The jar tool creates a JAR archive file by combining multiple files of a Java application.
section: Imported - java2s Archive
order: 1003
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0020__Language/ThejarTool.htm
---
The jar tool creates a JAR archive file by combining multiple files of a Java application.

The jar tool compresses content based on the ZIP and ZLIB compression formats.

You can also use the jar tool to extract the content of a JAR file.

The syntax to use the jar tool is:

```java title=Example.java
Usage: jar {ctxui}[vfm0Me] [jar-file] [manifest-file] [entry-point] [-C dir] files
```

Option  Description
---  ---
c  Creates a new archive.
t  Lists the contents of an archive.
x  Extracts contents from an archive.
u  Updates an existing archive.
v  Displays output at the command prompt while the jar tool performs an operation.
f  Specifies the name of the archive file.
m  Includes a specified manifest file in the archive.
o  Instructs the jar tool not to compress content.
M  Instructs the jar tool not to create a manifest file for an archive. The jar tool, by default, creates an empty manifest file in an archive.
C  Specifies the directories to include in the archive.
