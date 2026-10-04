---
title: Java Format - Java printf format flags
nav: Java Format - Java printf ...
description: The following table lists all flags that can be used in a format specifier.
section: Imported - java2s Archive
order: 50393
source: https://www.java2s.com/Tutorials/Java/Java_Format/0080__Java_Format_Flags.html
---
Java printf flags changes the formatted output.

The following table lists all flags that can be used in a format specifier.

Flag  Description  //
'-'  left justify. If there is no '-' flag, right justify.
'#'  format in alternate form for the format specifier
'+'  Add + sign to positive values. Applies only to numeric values.
' '  Add a leading space for positive values. Applies only to numeric values.
'0'  Add zero padded. Applies only to numeric values.
' , '  Add a locale-specific grouping separator. It applied only to numeric values.
'('  Add parentheses for a negative number. It applies only to numeric values.
'<'  Reuse the argument for the previous format specifier. It is mostly used in formatting dates and times.

Example:

Format String  Argument  Result
---  ---  ---
"'%6s'"  "abc"  ' abc'
"'%-6s'"  "abc"  'abc '
"%x"  1234  4d2
"%#x"  1234  0x4d2
"%d"  123  123
"%+d"  123  +123
"'%d'"  123  '123'
"'% d'"  123  ' 123'
"'%6d'"  123  ' 123'
"'%06d'"  123  '000123'
"%,d"  12345  12,345(US Locale)
"%,d"  12345  12 345 (France locale)
"%d"  -2014  -2014
"%(d"  -2014  (2014)
"%s and %<s"  "abc"  abc and abc

- « Previous
