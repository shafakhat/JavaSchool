---
title: Define constant
nav: Define constant
description: The naming convention for static final variables is to have them in upper case and separate two words with an underscore. For example:
section: Imported - java2s Archive
order: 1005
source: https://web.archive.org/web/20070513042840/http://www.java2s.com:80/Tutorial/Java/0020__Language/Defineconstant.htm
---
'public static final' variables are constant.

The naming convention for static final variables is to have them in upper case and separate two words with an underscore. For example:

```java title=Example.java
static final int NUMBER_OF_MONTHS = 12;
static final float PI = (float) 22 / 7;
```

If you want to make a static final variable accessible from outside the class, you can make it public too:

```java title=Example.java
public static final int NUMBER_OF_MONTHS = 12;
public static final float PI = (float) 22 / 7;
```
