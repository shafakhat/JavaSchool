---
title: The this Keyword
nav: The this Keyword
description: You use the this keyword from any method or constructor to refer to the current object.
section: Imported - java2s Archive
order: 1220
source: https://web.archive.org/web/20140829090036/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/ThethisKeyword.htm
---
You use the this keyword from any method or constructor to refer to the current object.

```java title=Example.java
public class Box {
    int length;
    int width;
    int height;
    public Box(int length, int width, int height) {
        this.length = length;
        this.width = width;
        this.height = height;
    }
}
```

5.13.1.  The this Keyword
