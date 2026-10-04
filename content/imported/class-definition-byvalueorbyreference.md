---
title: By Value or By Reference
nav: By Value or By Reference
description: Primitive variables are passed by value. reference variables are passed by reference. When you pass a primitive variable, the JVM will copy the value of the passed-in var
section: Imported - java2s Archive
order: 1199
source: https://web.archive.org/web/20140829080527/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/ByValueorByReference.htm
---
Primitive variables are passed by value. reference variables are passed by reference. When you pass a primitive variable, the JVM will copy the value of the passed-in variable to a new local variable. If you change the value of the local variable, the change will not affect the passed in primitive variable. If you pass a reference variable, the local variable will refer to the same object as the passed in reference variable. If you change the object referenced within your method, the change will also be reflected in the calling code.
5.7.4.  Use an array to pass a variable number of arguments to a method. This is the old-style approach to variable-length arguments.
