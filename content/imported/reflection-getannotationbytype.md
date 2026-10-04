---
title: Get annotation by type
nav: Get annotation by type
description: Imported from the java2s.com archive: Get annotation by type
section: Imported - java2s Archive
order: 2157
source: https://web.archive.org/web/20140829082528/http://www.java2s.com/Tutorial/Java/0125__Reflection/Getannotationbytype.htm
---
```java title=Example.java
import java.lang.annotation.Annotation;
import javax.ejb.Entity;
public class GetAnnotation {
    public static void main(String[] args) {
        Annotation[] as = Person.class.getAnnotations();
        for(int i=0;i<as.length;i++){
            System.out.println(as[i].annotationType());
        }
        Annotation a =Person.class.getAnnotation(Entity.class);
        System.out.println(a);
        Annotation[] das = Person.class.getDeclaredAnnotations();
        for(int i=0;i<das.length;i++){
            System.out.println(das[i].annotationType());
        }
    }
}
///
import javax.ejb.Entity;
import javax.ejb.AccessType;
import javax.ejb.Id;
import javax.ejb.GeneratorType;
import java.io.Serializable;
@Entity(access = AccessType.FIELD)
public class Person implements Serializable {
  @Id(generate = GeneratorType.AUTO)
  Integer id;
  String name;
}
```

| 7.8.1. | Use reflection to display the annotation associated with a method. |
|---|---|
| 7.8.2. | Show all annotations for a class and a method. |
| 7.8.3. | Get annotation by Annotation class |
| 7.8.4. | Get annotation by type |
