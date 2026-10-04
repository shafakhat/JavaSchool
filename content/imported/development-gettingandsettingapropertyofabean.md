---
title: Getting and Setting a Property of a Bean
nav: Getting and Setting a Prop...
description: Expression expr = new Expression(o, "getProp1", new Object[0]);
section: Imported - java2s Archive
order: 2016
source: https://web.archive.org/web/20140829083344/http://www.java2s.com/Tutorial/Java/0120__Development/GettingandSettingaPropertyofaBean.htm
---
```java title=Example.java
import java.beans.Expression;
import java.beans.Statement;
public class Main {
  public static void main(String[] argv) throws Exception {
    Object o = new MyBean();
    // Get the value of prop1
    Expression expr = new Expression(o, "getProp1", new Object[0]);
    expr.execute();
    String s = (String) expr.getValue();
    // Set the value of prop1
    Statement stmt = new Statement(o, "setProp1", new Object[] { "new string" });
    stmt.execute();
  }
}
class MyBean {
  String prop1;
  public String getProp1() {
    return prop1;
  }
  public void setProp1(String s) {
    prop1 = s;
  }
  int prop2;
  public int getProp2() {
    return prop2;
  }
  public void setProp2(int i) {
    prop2 = i;
  }
  byte[] prop3;
  public byte[] getProp3() {
    return prop3;
  }
  public void setProp3(byte[] bytes) {
    prop3 = bytes;
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
