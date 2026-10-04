---
title: Access inner class from outside
nav: Access inner class from ou...
description: Imported from the java2s.com archive: Access inner class from outside
section: Imported - java2s Archive
order: 1123
source: https://web.archive.org/web/20090531214942/http://www.java2s.com:80/Code/Java/Class/Accessinnerclassfromoutside.htm
---
Access inner class from outside

```java title=Example.java
public class Main {
    public static void main(String[] args) {
        Outer outer = new Outer();
        outer.new Inner().hello();
    }
}
class Outer {
    public class Inner {
        public void hello(){
          System.out.println("Hello from Inner()");
        }
    }
}
```

1.  an example of a simple anonymous class
---  ---
2.  Tick Tock with an Anonymous Class
3.  Anonymous inner class
