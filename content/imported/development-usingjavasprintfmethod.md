---
title: Using Java's printf( ) Method
nav: Using Java's printf( ) Met...
description: The printf( ) method automatically uses Formatter to create a formatted string.
section: Imported - java2s Archive
order: 1566
source: https://web.archive.org/web/20140217201049/http://www.java2s.com/Tutorial/Java/0120__Development/UsingJavasprintfMethod.htm
---
The printf( ) method automatically uses Formatter to create a formatted string.
The printf( ) method is defined by both PrintStream and PrintWriter.
For PrintStream, printf( ) has these forms:
PrintStream printf(String fmtString, Object ... args) PrintStream printf(Local loc, String fmtString, Object ... args)
The first version writes args to standard output in the format specified by fmtString, using the default locale.
The second lets you specify a locale.
