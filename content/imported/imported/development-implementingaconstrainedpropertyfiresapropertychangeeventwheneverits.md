---
title: Implementing a Constrained Property
nav: Implementing a Constrained...
description: VetoableChangeSupport vceListeners = new VetoableChangeSupport(this);
section: Imported
order: 20049
source: http://www.java2s.com:80/Tutorial/Java/0120__Development/ImplementingaConstrainedPropertyfiresaPropertyChangeEventwheneveritsvalueisabouttobechanged.htm
---
```java title=Example.java
import java.beans.PropertyVetoException;
import java.beans.VetoableChangeListener;
import java.beans.VetoableChangeSupport;
public class MyBean {
  VetoableChangeSupport vceListeners = new VetoableChangeSupport(this);
  int myProperty;
  public int getMyProperty() {
    return myProperty;
  }
  public void setMyProperty(int newValue) throws PropertyVetoException {
    try {
      vceListeners.fireVetoableChange("myProperty", new Integer(myProperty),
          new Integer(newValue));
      myProperty = newValue;
    } catch (PropertyVetoException e) {
      throw e;
    }
  }
  public synchronized void addVetoableChangeListener(
      VetoableChangeListener listener) {
    vceListeners.addVetoableChangeListener(listener);
  }
  public synchronized void removeVetoableChangeListener(
      VetoableChangeListener listener) {
    vceListeners.removeVetoableChangeListener(listener);
  }
}
```
