---
title: Float Control Component
nav: Float Control Component
description: Imported from the java2s.com archive: Float Control Component
section: Imported - java2s Archive
order: 1009
source: https://web.archive.org/web/20100206191315/http://www.java2s.com:80/Tutorial/Java/0120__Development/FloatControlComponent.htm
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
