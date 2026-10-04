---
title: Creating Objects of a Class
nav: Creating Objects of a Class
description: Imported from the java2s.com archive: Creating Objects of a Class
section: Imported - java2s Archive
order: 1204
source: https://web.archive.org/web/2016/http://www.java2s.com:80/Tutorial/Java/0100__Class-Definition/CreatingObjectsofaClass.htm
---
```java title=Example.java
class Sphere {
  double radius; // Radius of a sphere
  Sphere() {
  }
  // Class constructor
  Sphere(double theRadius) {
    radius = theRadius; // Set the radius
  }
}
public class MainClass {
  public static void main(String[] arg){
    Sphere sp = new Sphere();
  }
}
```

| 5.1.1. | What Is a Java Class? |
|---|---|
| 5.1.2. | Fields |
| 5.1.3. | Defining Classes: A class has fields and methods |
| 5.1.4. | Creating Objects of a Class |
| 5.1.5. | Checking whether the object referenced was of type String |
| 5.1.6. | Class declaration with one method |
| 5.1.7. | Class declaration with a method that has a parameter |
| 5.1.8. | Class that contains a String instance variable and methods to set and get its value |
| 5.1.9. | Class with a constructor to initialize instance variables |
| 5.1.10. | Specifying initial values in a class definition |
