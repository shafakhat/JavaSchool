---
title: Instantiate unknown class at runtime and call the object's methods
nav: Instantiate unknown class ...
description: Imported from the java2s.com archive: Instantiate unknown class at runtime and call the object's methods
section: Imported - java2s Archive
order: 2152
source: https://web.archive.org/web/20140829075529/http://www.java2s.com/Tutorial/Java/0125__Reflection/Instantiateunknownclassatruntimeandcalltheobjectsmethods.htm
---
```java title=Example.java
import java.lang.reflect.Method;
public class Main {
  public static void main(String[] args) throws Exception {
    Class myclass = Class.forName("java.lang.String");
    Method[] methods = myclass.getMethods();
    //Object object = myclass.newInstance();
    for (int i = 0; i < methods.length; i++) {
      System.out.println(methods[i].getName());
      //System.out.println(methods[i].invoke(object));
    }
  }
}
/*
hashCode
compareTo
compareTo
indexOf
indexOf
indexOf
indexOf
equals
toString
charAt
codePointAt
codePointBefore
codePointCount
compareToIgnoreCase
concat
contains
contentEquals
contentEquals
copyValueOf
copyValueOf
endsWith
equalsIgnoreCase
format
format
getBytes
getBytes
getBytes
getBytes
getChars
intern
isEmpty
lastIndexOf
lastIndexOf
lastIndexOf
lastIndexOf
length
matches
offsetByCodePoints
regionMatches
regionMatches
replace
replace
replaceAll
replaceFirst
split
split
startsWith
startsWith
subSequence
substring
substring
toCharArray
toLowerCase
toLowerCase
toUpperCase
toUpperCase
trim
valueOf
valueOf
valueOf
valueOf
valueOf
valueOf
valueOf
valueOf
valueOf
getClass
wait
wait
wait
notify
notifyAll
*/
```

| 7.7.1. | URL class loader |
|---|---|
| 7.7.2. | extends URLClassLoader |
| 7.7.3. | Load classes |
| 7.7.4. | how to use reflection to print the names and values of all nonstatic fields of an object |
| 7.7.5. | Runs a jar application from any url |
| 7.7.6. | BufferedReader reflection |
| 7.7.7. | Get the class By way of an object |
| 7.7.8. | Get the class By way of a string |
| 7.7.9. | Get the class By way of .class |
| 7.7.10. | Catch InvocationTargetException |
| 7.7.11. | Determining from Where a Class Was Loaded |
| 7.7.12. | Dynamically Reloading a Modified Class |
| 7.7.13. | Creating an Object Using a Constructor Object |
| 7.7.14. | Create an object from a string |
| 7.7.15. | Using the forName() method |
| 7.7.16. | Context ClassLoader |
| 7.7.17. | A tree structure that maps inheritance hierarchies of classes |
| 7.7.18. | Analyze ClassLoader hierarchy for any given object or class loader |
| 7.7.19. | Instantiate unknown class at runtime and call the object's methods |
| 7.7.20. | Load Class |
