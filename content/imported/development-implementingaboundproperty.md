---
title: Implementing a Bound Property
nav: Implementing a Bound Prope...
description: PropertyChangeSupport pceListeners = new PropertyChangeSupport(this);
section: Imported - java2s Archive
order: 2012
source: https://web.archive.org/web/20140829082947/http://www.java2s.com/Tutorial/Java/0120__Development/ImplementingaBoundProperty.htm
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

| 6.56.1. | Listening for Changes to the Selected File in a JFileChooser Dialog |
|---|---|
| 6.56.2. | Get a list of selected files |
| 6.56.3. | Listening for Changes to the Current Directory in a JFileChooser Dialog |
| 6.56.4. | Displaying the Current Directory in the Title of a JFileChooser Dialog |
| 6.56.5. | Setting an Accessory Component in a JFileChooser Dialog |
| 6.56.6. | Convert a bean to XML persistence |
| 6.56.7. | Listen for bean's property change event |
| 6.56.8. | List property names of a Bean |
| 6.56.9. | Prevent bean's property being serialized to XML |
| 6.56.10. | Create an instance a Bean |
| 6.56.11. | Convert an XML persistence to bean |
| 6.56.12. | Determine bean's property type |
| 6.56.13. | Listen for a constrained property change |
| 6.56.14. | Bean has a single property called property. |
| 6.56.15. | Implementing a Bound Property |
| 6.56.16. | Implementing a Constrained Property: fires a PropertyChangeEvent whenever its value is about to be changed. |
| 6.56.17. | Instantiating a Bean |
| 6.56.18. | Listing the Property Names of a Bean |
| 6.56.19. | Getting and Setting a Property of a Bean |
| 6.56.20. | Get and set the value of a property in a bean using Expression and Statement |
| 6.56.21. | Get and set an Object type property |
| 6.56.22. | gets and sets a primitive type property |
| 6.56.23. | gets and sets an array type property |
| 6.56.24. | Serializing a Bean to XML: XMLEncoder only persists the value of public properties. |
| 6.56.25. | Deserializing a Bean from XML |
| 6.56.26. | Preventing a Bean Property from Being Serialized to XML |
| 6.56.27. | Serializing an Immutable Bean Property to XML |
| 6.56.28. | Listening for a Property Change Event: A property change event is fired when a bound property is changed. |
| 6.56.29. | Listening for a Vetoable Property Change Event |
| 6.56.30. | Read bean's property value |
| 6.56.31. | extends SimpleBeanInfo |
| 6.56.32. | Get and set properties on a bean |
| 6.56.33. | Process bean properties getter by applying the JavaBean naming conventions. |
| 6.56.34. | Is JavaBean Compliant Setter |
| 6.56.35. | Constructs a method name from element's bean name for a given prefix |
| 6.56.36. | Returns attribute's setter method. If the method not found then NoSuchMethodException will be thrown. |
