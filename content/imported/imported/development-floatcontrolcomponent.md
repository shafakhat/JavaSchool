---
title: Float Control Component
nav: Float Control Component
description: Imported from java2s.com: Float Control Component
section: Imported
order: 20013
source: http://www.java2s.com:80/Tutorial/Java/0120__Development/FloatControlComponent.htm
---
```java title=Example.java
import javax.sound.sampled.FloatControl;
public class Main {
  FloatControl control;
  public Main(FloatControl c) {
    control = c;
    control.setValue(3);
  }
}
```
