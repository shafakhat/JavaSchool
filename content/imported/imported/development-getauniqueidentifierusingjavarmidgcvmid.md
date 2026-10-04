---
title: Get a unique identifier Using java.rmi.dgc.VMID
nav: Get a unique identifier Us...
description: Imported from java2s.com: Get a unique identifier Using java.rmi.dgc.VMID
section: Imported
order: 20026
source: http://java2s.com/Tutorial/Java/0120__Development/GetauniqueidentifierUsingjavarmidgcVMID.htm
---
```java title=Example.java
public class Main {
  public static void main(String arg[]) {
    System.out.println(new java.rmi.dgc.VMID().toString());
  }
}
//4129eb1d7419293f:-148094f1:11fc9788387:-8000
```
