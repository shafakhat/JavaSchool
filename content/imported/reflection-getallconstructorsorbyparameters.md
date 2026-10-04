---
title: Get all constructors or by parameters
nav: Get all constructors or by...
description: Constructor c = String.class.getConstructor(new Class[]{String.class});
section: Imported - java2s Archive
order: 2078
source: https://web.archive.org/web/2020/http://www.java2s.com/Tutorial/Java/0125__Reflection/Getallconstructorsorbyparameters.htm
---
```java title=Example.java
import java.lang.reflect.Constructor;
public class GetConstructor {
    public static void main(String[] args) {
        Constructor[] cs = String.class.getConstructors();
        for(int i=0;i<cs.length;i++){
            System.out.println(cs[i]);
        }
        try {
            Constructor c = String.class.getConstructor(new Class[]{String.class});
            System.out.println(c);
        } catch (SecurityException e) {
            e.printStackTrace();
        } catch (NoSuchMethodException e) {
            e.printStackTrace();
        }
    }
}
```
