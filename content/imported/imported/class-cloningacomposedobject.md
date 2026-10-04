---
title: Cloning a composed object
nav: Cloning a composed object
description: // www.BruceEckel.com. See copyright notice in CopyRight.txt.
section: Imported - java2s Archive
order: 1144
source: https://web.archive.org/web/20081009143441/http://www.java2s.com:80/Code/Java/Class/Cloningacomposedobject.htm
---
Cloning a composed object

```java title=Example.java
// : appendixa:DeepCopy.java
// Cloning a composed object.
// {Depends: junit.jar}
// From 'Thinking in Java, 3rd ed.' (c) Bruce Eckel 2002
// www.BruceEckel.com. See copyright notice in CopyRight.txt.
import junit.framework.*;
class DepthReading implements Cloneable {
  private double depth;
  public DepthReading(double depth) {
    this.depth = depth;
  }
  public Object clone() {
    Object o = null;
    try {
      o = super.clone();
    } catch (CloneNotSupportedException e) {
      e.printStackTrace();
    }
    return o;
  }
  public double getDepth() {
    return depth;
  }
  public void setDepth(double depth) {
    this.depth = depth;
  }
  public String toString() {
    return String.valueOf(depth);
  }
}
class TemperatureReading implements Cloneable {
  private long time;
  private double temperature;
  public TemperatureReading(double temperature) {
    time = System.currentTimeMillis();
    this.temperature = temperature;
  }
  public Object clone() {
    Object o = null;
    try {
      o = super.clone();
    } catch (CloneNotSupportedException e) {
      e.printStackTrace();
    }
    return o;
  }
  public double getTemperature() {
    return temperature;
  }
  public void setTemperature(double temperature) {
    this.temperature = temperature;
  }
  public String toString() {
    return String.valueOf(temperature);
  }
}
class OceanReading implements Cloneable {
  private DepthReading depth;
  private TemperatureReading temperature;
  public OceanReading(double tdata, double ddata) {
    temperature = new TemperatureReading(tdata);
    depth = new DepthReading(ddata);
  }
  public Object clone() {
    OceanReading o = null;
    try {
      o = (OceanReading) super.clone();
    } catch (CloneNotSupportedException e) {
      e.printStackTrace();
    }
    // Must clone references:
    o.depth = (DepthReading) o.depth.clone();
    o.temperature = (TemperatureReading) o.temperature.clone();
    return o; // Upcasts back to Object
  }
  public TemperatureReading getTemperatureReading() {
    return temperature;
  }
  public void setTemperatureReading(TemperatureReading tr) {
    temperature = tr;
  }
  public DepthReading getDepthReading() {
    return depth;
  }
  public void setDepthReading(DepthReading dr) {
    this.depth = dr;
  }
  public String toString() {
    return "temperature: " + temperature + ", depth: " + depth;
  }
}
public class DeepCopy extends TestCase {
  public DeepCopy(String name) {
    super(name);
  }
  public void testClone() {
    OceanReading reading = new OceanReading(33.9, 100.5);
    // Now clone it:
    OceanReading clone = (OceanReading) reading.clone();
    TemperatureReading tr = clone.getTemperatureReading();
    tr.setTemperature(tr.getTemperature() + 1);
    clone.setTemperatureReading(tr);
    DepthReading dr = clone.getDepthReading();
    dr.setDepth(dr.getDepth() + 1);
    clone.setDepthReading(dr);
    assertEquals(reading.toString(), "temperature: 33.9, depth: 100.5");
    assertEquals(clone.toString(), "temperature: 34.9, depth: 101.5");
  }
  public static void main(String[] args) {
    junit.textui.TestRunner.run(DeepCopy.class);
  }
} ///:~
```

1.  A Cloning Example
---  ---
2.  Creating a Deep Copy
3.  Shallow Copy Test
4.  Deep Copy Test
5.  Tests cloning to see if destination of references are also cloned
6.  Creating local copies with clone
7.  You can insert Cloneability at any level of inheritance
8.  Serializable and clone
9.  Go through a few gyrations to add cloning to your own class
10.  Checking to see if a reference can be cloned
11.  The clone operation works for only a few items in the standard Java library
12.  Demonstration of cloning
13.  Simple demo of avoiding side-effects by using Object.clone
14.  Clone demo
