---
title: The native2ascii Tool
nav: The native2ascii Tool
description: You can use the native2ascii tool to convert files with native encoded characters to a file with Unicode encoded characters.
section: Imported - java2s Archive
order: 1004
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0020__Language/Thenative2asciiTool.htm
---
You can use the native2ascii tool to convert files with native encoded characters to a file with Unicode encoded characters.

The syntax to use the native2ascii tool is:

```java title=Example.java
native2ascii [options] [inputfile [outputfile]]
```

- options: Refers to various options that you can use to pass information or configure the native2ascii tool.
- inputfile: Refers to the file that contains native encoded characters.
- outputfile: Represents the file that will contain the converted text.

Options of the native2ascii Tool

Option  Description
---  ---
-reverse  Allows you to perform the reverse operation, which reverse the sense of the conversion.
-encoding encoding_name  Specifies the encoding name that is used by the conversion procedure.
-Joption  Allows you to pass configuration options to JVM.
