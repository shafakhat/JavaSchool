---
title: The keyword super represents an instance of the direct superclass of the current object.
nav: The keyword super represen...
description: You can explicitly call the parent's constructor from a subclass's constructor by using the super keyword. 'super' must be the first statement in the constructor.
section: Imported - java2s Archive
order: 1283
source: https://web.archive.org/web/20140829075431/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/Thekeywordsuperrepresentsaninstanceofthedirectsuperclassofthecurrentobject.htm
---
You can explicitly call the parent's constructor from a subclass's constructor by using the super keyword. 'super' must be the first statement in the constructor.

```java title=Example.java
class Parent {
       public Parent(){
       }
     }
     public class Child extends Parent {
         public Child () {
           super();
         }
     }
```
