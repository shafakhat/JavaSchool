---
title: Some Restrictions
nav: Some Restrictions
description: Imported from the java2s.com archive: Some Restrictions
section: Imported - java2s Archive
order: 1004
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0020__Language/SomeRestrictions.htm
---
- No annotation can inherit another.
- All methods declared by an annotation must be without parameters.
- Annotations cannot be generic.
- They cannot specify a throws clause.

They must return one of the following:

```java title=Example.java
A simple type, such as int or double,
          An object of type String or Class
          An enum type
          Another annotation type
          An array of one of the preceding types
```
