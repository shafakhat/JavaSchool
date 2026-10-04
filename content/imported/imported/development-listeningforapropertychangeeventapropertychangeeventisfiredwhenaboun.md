---
title: Listening for a Property Change Event
nav: Listening for a Property C...
description: bean.addPropertyChangeListener(new MyPropertyChangeListener());
section: Imported
order: 20055
source: http://www.java2s.com:80/Tutorial/Java/0120__Development/ListeningforaPropertyChangeEventApropertychangeeventisfiredwhenaboundpropertyischanged.htm
---
```java title=Example.java
import java.beans.PropertyChangeEvent;
import java.beans.PropertyChangeListener;
import java.beans.PropertyChangeSupport;
public class Main {
  public static void main(String[] argv) throws Exception {
    MyBean bean = new MyBean();
    bean.addPropertyChangeListener(new MyPropertyChangeListener());
  }
}
class MyPropertyChangeListener implements PropertyChangeListener {
  public void propertyChange(PropertyChangeEvent evt) {
    Object oldValue = evt.getOldValue();
    Object newValue = evt.getNewValue();
  }
}
class MyBean {
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
