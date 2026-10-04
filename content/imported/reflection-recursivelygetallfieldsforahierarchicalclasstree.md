---
title: Recursively get all fields for a hierarchical class tree
nav: Recursively get all fields...
description: * @author Aniruddha Dutta Chowdhury [a.d.chowdhury@gmail.com]<br>
section: Imported - java2s Archive
order: 2080
source: https://web.archive.org/web/20140829082634/http://www.java2s.com/Tutorial/Java/0125__Reflection/Recursivelygetallfieldsforahierarchicalclasstree.htm
---
```java title=Example.java
import java.lang.reflect.Field;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
/**
 *
 * @author Aniruddha Dutta Chowdhury [a.d.chowdhury@gmail.com]<br>
 *         http://www.google.com/profiles/a.d.chowdhury<br>
 *         http://in.linkedin.com/in/adchowdhury
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    @@@@@@@@@@@@@@@@    @@@@@    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@       @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    @@@@@@@@@@@@@@@@    @@@@@    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@       @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    @@@@@@@@@@@@@@@@    @@@@@    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@       @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    @@@@@@@@@@@@@@@@    @@@@@    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@    @    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    @@@@@@@@@@@@@@@@    @@@@@    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@    @    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    @@@@@@@@@@@@@@@@    @@@@@    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@     @     @@@@@@@@@@    @@     @@@@@@@@    @@@@@    @     @@@@@    @@@@@@    @@@@@@@@@     @@    @@@@@@@@@     @@    @@@@@    @@     @@@@@@@@@@@@       @@@@@@@
@@@@@@@    @@@    @@@@@@@@@@    @        @@@@@@    @@@@@         @@@@@@    @@@@@@    @@@@@@@        @    @@@@@@@        @    @@@@@    @        @@@@@@@@           @@@@@
@@@@@@@    @@@    @@@@@@@@@@             @@@@@@    @@@@@         @@@@@@    @@@@@@    @@@@@@              @@@@@@              @@@@@             @@@@@@@@            @@@@
@@@@@@     @@@     @@@@@@@@@      @@@     @@@@@    @@@@@     @@@@@@@@@@    @@@@@@    @@@@@@     @@@      @@@@@@     @@@      @@@@@      @@@     @@@@@@    @@@@     @@@@
@@@@@@    @@@@@    @@@@@@@@@     @@@@@    @@@@@    @@@@@     @@@@@@@@@@    @@@@@@    @@@@@     @@@@@     @@@@@     @@@@@     @@@@@     @@@@@    @@@@@@@  @@@@@@    @@@@
@@@@@@    @@@@@    @@@@@@@@@    @@@@@@    @@@@@    @@@@@    @@@@@@@@@@@    @@@@@@    @@@@@    @@@@@@@    @@@@@    @@@@@@@    @@@@@    @@@@@@    @@@@@@@@@@@@@@@    @@@@
@@@@@     @@@@@@    @@@@@@@@    @@@@@@    @@@@@    @@@@@    @@@@@@@@@@@    @@@@@@    @@@@@    @@@@@@@    @@@@@    @@@@@@@    @@@@@    @@@@@@    @@@@@@@@@@@@@      @@@@
@@@@@               @@@@@@@@    @@@@@@    @@@@@    @@@@@    @@@@@@@@@@@    @@@@@@    @@@@@    @@@@@@@    @@@@@    @@@@@@@    @@@@@    @@@@@@    @@@@@@@@@          @@@@
@@@@@               @@@@@@@@    @@@@@@    @@@@@    @@@@@    @@@@@@@@@@@    @@@@@@    @@@@@    @@@@@@@    @@@@@    @@@@@@@    @@@@@    @@@@@@    @@@@@@             @@@@
@@@@                 @@@@@@@    @@@@@@    @@@@@    @@@@@    @@@@@@@@@@@    @@@@@@    @@@@@    @@@@@@@    @@@@@    @@@@@@@    @@@@@    @@@@@@    @@@@@@      @@@    @@@@
@@@@                 @@@@@@@    @@@@@@    @@@@@    @@@@@    @@@@@@@@@@@    @@@@@@    @@@@@    @@@@@@@    @@@@@    @@@@@@@    @@@@@    @@@@@@    @@@@@    @@@@@@    @@@@
@@@@    @@@@@@@@@    @@@@@@@    @@@@@@    @@@@@    @@@@@    @@@@@@@@@@@    @@@@@     @@@@@@    @@@@@     @@@@@@    @@@@@     @@@@@    @@@@@@    @@@@@    @@@@@@    @@@@
@@@    @@@@@@@@@@@    @@@@@@    @@@@@@    @@@@@    @@@@@    @@@@@@@@@@@     @@@      @@@@@@     @@@      @@@@@@     @@@      @@@@@    @@@@@@    @@@@@     @@@@     @@@@
@@@    @@@@@@@@@@@    @@@@@@    @@@@@@    @@@@@    @@@@@    @@@@@@@@@@@@             @@@@@@@             @@@@@@@             @@@@@    @@@@@@    @@@@@              @@@@
@@@    @@@@@@@@@@@    @@@@@@    @@@@@@    @@@@@    @@@@@    @@@@@@@@@@@@        @    @@@@@@@        @    @@@@@@@        @    @@@@@    @@@@@@    @@@@@@         @   @@@@
@@    @@@@@@@@@@@@@    @@@@@    @@@@@@    @@@@@    @@@@@    @@@@@@@@@@@@@@     @@    @@@@@@@@@     @@    @@@@@@@@@     @@    @@@@@    @@@@@@    @@@@@@@@     @@@    @@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
 *
 */
public class testReflection {
    public static void main(String[] args) {
        try {
            C c = new C();
            Class klass = c.getClass();
            Field[] fields = getAllFields(klass);
            for (Field field : fields) {
                System.out.println(field.getName());
            }
        } catch (Throwable a_th) {
            a_th.printStackTrace();
        }
    }
    public static Field[] getAllFields(Class klass) {
        List<Field> fields = new ArrayList<Field>();
        fields.addAll(Arrays.asList(klass.getDeclaredFields()));
        if (klass.getSuperclass() != null) {
            fields.addAll(Arrays.asList(getAllFields(klass.getSuperclass())));
        }
        return fields.toArray(new Field[] {});
    }
}
class A {
    public String    nameA    = "";
}
class B extends A {
    public String    nameB    = "";
    public String    nameB1    = "";
    public String    nameB2    = "";
}
class C extends B {
    public String    nameC    = "";
}
```

| 7.4.1. | Recursively get all fields for a hierarchical class tree |
|---|---|
| 7.4.2. | Reflect All |
| 7.4.3. | System class reflection |
| 7.4.4. | Get all declared fields from a class |
| 7.4.5. | Getting the Field Objects of a Class Object: By obtaining a list of all declared fields. |
| 7.4.6. | Getting the Field Objects of a Class Object: By obtaining a list of all public fields, both declared and inherited. |
| 7.4.7. | Getting the Field Objects of a Class Object: By obtaining a particular Field object. |
| 7.4.8. | Reflection, Introspection, and Naming |
| 7.4.9. | Get the name of a primitive type |
| 7.4.10. | Getting and Setting the Value of a Field (assumes that the field has the type int) |
| 7.4.11. | Retrieving a Predefined Color by Name |
| 7.4.12. | Get a variable value from the variable name |
| 7.4.13. | Return a list of all fields (whatever access status, and on whatever superclass they were defined) that can be found on this class. |
| 7.4.14. | Checks whether the specified class contains a field matching the specified name. |
| 7.4.15. | Return Retrurns the Type of the given Field or Method |
