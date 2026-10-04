---
title: Compute distance light travels using long variables
nav: Compute distance light tra...
description: Imported from the java2s.com archive: Compute distance light travels using long variables
section: Imported - java2s Archive
order: 1017
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Computedistancelighttravelsusinglongvariables.htm
---
```java title=Example.java
public class MainClass {
  public static void main(String args[]) {
    int lightspeed;
    long days;
    long seconds;
    long distance;
    // approximate speed of light in miles per second
    lightspeed = 186000;
    days = 1000; // specify number of days here
    seconds = days * 24 * 60 * 60; // convert to seconds
    distance = lightspeed * seconds; // compute distance
    System.out.print("In " + days);
    System.out.print(" days light will travel about ");
    System.out.println(distance + " miles.");
  }
}
java title=Example.java
In 1000 days light will travel about 16070400000000 miles
```
