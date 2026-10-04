---
title: Prevent bean's property being serialized to XML
nav: Prevent bean's property be...
description: BeanInfo bi = Introspector.getBeanInfo(BeanToXmlTransient.class);
section: Imported - java2s Archive
order: 2019
source: https://web.archive.org/web/20140829084632/http://www.java2s.com/Tutorial/Java/0120__Development/PreventbeanspropertybeingserializedtoXML.htm
---
```java title=Example.java
import java.beans.BeanInfo;
import java.beans.Introspector;
import java.beans.PropertyDescriptor;
import java.beans.XMLEncoder;
import java.io.BufferedOutputStream;
import java.io.FileOutputStream;
public class Main {
  public static void main(String[] argv) throws Exception {
    BeanInfo bi = Introspector.getBeanInfo(BeanToXmlTransient.class);
    PropertyDescriptor[] pds = bi.getPropertyDescriptors();
    for (int i = 0; i < pds.length; i++) {
      PropertyDescriptor propertyDescriptor = pds[i];
      if (propertyDescriptor.getName().equals("itemQuantities")) {
        propertyDescriptor.setValue("transient", Boolean.TRUE);
      }
    }
    BeanToXmlTransient bean = new BeanToXmlTransient();
    bean.setId(new Long(1));
    bean.setItemName("Item");
    bean.setItemColour("Red");
    bean.setItemQuantities(new Integer(100));
    XMLEncoder encoder = new XMLEncoder(new BufferedOutputStream(new FileOutputStream(
        "BeanTransient.xml")));
    encoder.writeObject(bean);
    encoder.close();
  }
}
class BeanToXmlTransient {
  private Long id;
  private String itemName;
  private String itemColour;
  private Integer itemQuantities;
  public Long getId() {
    return id;
  }
  public void setId(Long id) {
    this.id = id;
  }
  public String getItemName() {
    return itemName;
  }
  public void setItemName(String itemName) {
    this.itemName = itemName;
  }
  public String getItemColour() {
    return itemColour;
  }
  public void setItemColour(String itemColour) {
    this.itemColour = itemColour;
  }
  public Integer getItemQuantities() {
    return itemQuantities;
  }
  public void setItemQuantities(Integer itemQuantities) {
    this.itemQuantities = itemQuantities;
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
