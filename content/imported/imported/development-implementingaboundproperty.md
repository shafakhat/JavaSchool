---
title: Implementing a Bound Property
nav: Implementing a Bound Prope...
description: PropertyChangeSupport pceListeners = new PropertyChangeSupport(this);
section: Imported
order: 20048
source: http://www.java2s.com:80/Tutorial/Java/0120__Development/ImplementingaBoundProperty.htm
---
```java title=Example.java
import java.beans.PropertyChangeListener;
import java.beans.PropertyChangeSupport;
public class MyBean {
  PropertyChangeSupport pceListeners = new PropertyChangeSupport(this);
  int myProperty;
  public int getMyProperty() {
    return myProperty;
  }
  public void setMyProperty(int newValue) {
    int oldValue = myProperty;
    myProperty = newValue;
    pceListeners.firePropertyChange("myProperty", new Integer(oldValue),
        new Integer(newValue));
  }
  public synchronized void addPropertyChangeListener(
      PropertyChangeListener listener) {
    pceListeners.addPropertyChangeListener(listener);
  }
  public synchronized void removePropertyChangeListener(
      PropertyChangeListener listener) {
    pceListeners.removePropertyChangeListener(listener);
  }
}
```
