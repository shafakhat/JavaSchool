---
title: Check if a string is a valid number
nav: Check if a string is a val...
description: Imported from the java2s.com archive: Check if a string is a valid number
section: Imported - java2s Archive
order: 1013
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Checkifastringisavalidnumber.htm
---
```java title=Example.java
publicclass Main {
  publicstaticvoid main(String[] argv) throws Exception {
    String age = "1";
    String height = "1.5";
    String weight = "5.9";

    int theAge = Integer.parseInt(age);
    float theHeight = Float.parseFloat(height);
    double theWeight = Double.parseDouble(weight);

    System.out.println("Age: " + theAge);
    System.out.println("Height: " + theHeight);
    System.out.println("Weight: " + theWeight);
  }
}
```
