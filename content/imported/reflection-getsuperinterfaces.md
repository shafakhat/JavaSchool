---
title: Get Super Interfaces
nav: Get Super Interfaces
description: * The contents of this file are subject to the Sapient Public License
section: Imported - java2s Archive
order: 2064
source: https://web.archive.org/web/20140102193729/http://www.java2s.com/Tutorial/Java/0125__Reflection/GetSuperInterfaces.htm
---
```java title=Example.java
/*
 * The contents of this file are subject to the Sapient Public License
 * Version 1.0 (the "License"); you may not use this file except in compliance
 * with the License. You may obtain a copy of the License at
 * http://carbon.sf.net/License.html.
 *
 * Software distributed under the License is distributed on an "AS IS" basis,
 * WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License for
 * the specific language governing rights and limitations under the License.
 *
 * The Original Code is The Carbon Component Framework.
 *
 * The Initial Developer of the Original Code is Sapient Corporation
 *
 * Copyright (C) 2003 Sapient Corporation. All Rights Reserved.
 */
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
/**
 *
 *
 * Copyright 2003 Sapient
 * @since carbon 2.0
 * @author Greg Hinkle, March 2003
 * @version $Revision: 1.5 $($Author: dvoet $ / $Date: 2003/05/05 21:21:23 $)
 */
public class ClassUtil {
    /**
     * Retrieves all interfaces implemented by a specified interface
     * including all recursively extended interfaces and the classes supplied
     * int the parameter.
     * @param childInterfaces a set of interfaces
     * @return Class[] an array of interfaces that includes those specifed
     * in childInterfaces plus all of those interfaces' super interfaces
     */
    public static Class[] getSuperInterfaces(Class[] childInterfaces) {
        List allInterfaces = new ArrayList();
        for (int i = 0; i < childInterfaces.length; i++) {
            allInterfaces.add(childInterfaces[i]);
            allInterfaces.addAll(
                Arrays.asList(
                    getSuperInterfaces(childInterfaces[i].getInterfaces())));
        }
        return (Class[]) allInterfaces.toArray(new Class[allInterfaces.size()]);
    }
    /**
     * Builds an <b>unordered</b> set of all interface and object classes that
     * are generalizations of the provided class.
     * @param classObject the class to find generalization of.
     * @return a Set of class objects.
     */
    public static Set getGeneralizations(Class classObject) {
        Set generalizations = new HashSet();
        generalizations.add(classObject);
        Class superClass = classObject.getSuperclass();
        if (superClass != null) {
            generalizations.addAll(getGeneralizations(superClass));
        }
        Class[] superInterfaces = classObject.getInterfaces();
        for (int i = 0; i < superInterfaces.length; i++) {
            Class superInterface = superInterfaces[i];
            generalizations.addAll(getGeneralizations(superInterface));
        }
        return generalizations;
    }
}
```

| 7.2.1. | The superclass of interfaces is always null |
|---|---|
| 7.2.2. | Listing the Interfaces That an Interface Extends |
| 7.2.3. | Checking whether String is an interface or class |
| 7.2.4. | If a class object is an interface or a class |
| 7.2.5. | Listing the Interfaces That a Class Implements |
| 7.2.6. | Although the type of o2 is an interface, getSuperclass() returns the object's superclass |
| 7.2.7. | The interfaces for a primitive type is an empty array |
| 7.2.8. | Return Returns true if type is implementing Map |
| 7.2.9. | Returns true if a class implements Serializable and false otherwise. |
| 7.2.10. | Get Super Interfaces |
| 7.2.11. | Get all interface and object classes that are generalizations of the provided class |
