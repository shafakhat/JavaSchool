---
title: Converts UISelectMany submitted value to converted value
nav: Converts UISelectMany subm...
description: Converts UISelectMany submitted value to converted value : JavaServer Faces « J2EE « Java
section: Imported - java2s Archive
order: 1004
source: https://web.archive.org/web/20091101181649/http://www.java2s.com:80/Code/Java/J2EE/ConvertsUISelectManysubmittedvaluetoconvertedvalue.htm
---
Converts UISelectMany submitted value to converted value : JavaServer Faces « J2EE « Java
Converts UISelectMany submitted value to converted value

```java title=Example.java
/**
 * Licensed under the Common Development and Distribution License,
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *   http://www.sun.com/cddl/
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
 * implied. See the License for the specific language governing
 * permissions and limitations under the License.
 */
import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Collection;
import java.util.Iterator;
import java.util.List;
import java.util.Map;
import javax.faces.FacesException;
import javax.faces.component.UIComponent;
import javax.faces.component.UIInput;
import javax.faces.component.UIOutput;
import javax.faces.component.UISelectItem;
import javax.faces.component.UISelectItems;
import javax.faces.component.UISelectMany;
import javax.faces.context.FacesContext;
import javax.faces.convert.Converter;
import javax.faces.convert.ConverterException;
import javax.faces.el.ValueBinding;
import javax.faces.model.SelectItem;
/**
 * @author Maksim Kaszynski
 *
 */
public class SelectUtils {
  /**
   * Gathers all select items from specified component's children
   * @param context
   * @param component
   * @return list of {@link SelectItems} taken from f:selectItem and f:selectItems
   */
  public static List getSelectItems(FacesContext context, UIComponent component) {
        ArrayList list = new ArrayList();
    Iterator kids = component.getChildren().iterator();
    while (kids.hasNext()) {
      UIComponent kid = (UIComponent) kids.next();
      if (kid instanceof UISelectItem) {
        Object value = ((UISelectItem) kid).getValue();
        if (value == null) {
          UISelectItem item = (UISelectItem) kid;
          list.add(new SelectItem(item.getItemValue(), item.getItemLabel(), item.getItemDescription(), item.isItemDisabled()));
        } else if (value instanceof SelectItem) {
          list.add(value);
        } else {
          String valueClass = (value != null ? "'" + value.getClass().getName() + "'" : "");
          throw new IllegalArgumentException(Messages.getMessage(Messages.INVALID_ATTRIBUTE_VALUE, valueClass, "<selectItem>"));
        }
      } else if (kid instanceof UISelectItems && null != context) {
        Object value = ((UISelectItems) kid).getValue();
        if (value instanceof SelectItem) {
          list.add(value);
        } else if (value instanceof SelectItem[]) {
          SelectItem items[] = (SelectItem[]) value;
          for (int i = 0; i < items.length; i++) {
            list.add(items[i]);
          }
        } else if (value instanceof Collection) {
          Iterator elements = ((Collection) value).iterator();
          while (elements.hasNext()) {
            list.add(elements.next());
          }
        } else if (value instanceof Map) {
          Iterator keys = ((Map) value).keySet().iterator();
          while (keys.hasNext()) {
            Object key = keys.next();
            if (key == null) {
              continue;
            }
            Object val = ((Map) value).get(key);
            if (val == null) {
              continue;
            }
            list.add(new SelectItem(val.toString(), key.toString(),
                null));
          }
        } else {
          String valueClass = (value != null ? "'" + value.getClass().getName() + "'" : "");
          throw new IllegalArgumentException("INVALID_ATTRIBUTE_VALUE, valueClass");
        }
      }
    }
        return list;
  }
  /**
   * Converts UISelectMany submitted value to converted value
   *
   * @author Manfred Geiler
   * @param facesContext
   * @param component
   * @param submittedValue
   * @return
   * @throws ConverterException
   */
  public static Object getConvertedUISelectManyValue(
      FacesContext facesContext, UISelectMany component,
      String[] submittedValue) throws ConverterException {
    // Attention!
    // This code is duplicated in jsfapi component package.
    // If you change something here please do the same in the other class!
    if (submittedValue == null)
      throw new NullPointerException("submittedValue");
    ValueBinding vb = component.getValueBinding("value");
    Class valueType = null;
    Class arrayComponentType = null;
    if (vb != null) {
      valueType = vb.getType(facesContext);
      if (valueType != null && valueType.isArray()) {
        arrayComponentType = valueType.getComponentType();
      }
    }
    Converter converter = component.getConverter();
    if (converter == null) {
      if (valueType == null) {
        // No converter, and no idea of expected type
        // --> return the submitted String array
        return submittedValue;
      }
      if (List.class.isAssignableFrom(valueType)) {
        // expected type is a List
        // --> according to javadoc of UISelectMany we assume that the
        // element type
        // is java.lang.String, and copy the String array to a new List
        int len = submittedValue.length;
        List lst = new ArrayList(len);
        for (int i = 0; i < len; i++) {
          lst.add(submittedValue[i]);
        }
        return lst;
      }
      if (arrayComponentType == null) {
        throw new IllegalArgumentException(Messages.getMessage(Messages.VALUE_BINDING_TYPE_ERROR));
      }
      if (String.class.equals(arrayComponentType))
        return submittedValue; // No conversion needed for String type
      if (Object.class.equals(arrayComponentType))
        return submittedValue; // No conversion for Object class
      try {
        converter = facesContext.getApplication().createConverter(
            arrayComponentType);
      } catch (FacesException e) {
        System.out.println("NO_CONVERTER_FOUND_ERROR");
        return submittedValue;
      }
    }
    // Now, we have a converter...
    if (valueType == null) {
      // ...but have no idea of expected type
      // --> so let's convert it to an Object array
      int len = submittedValue.length;
      Object[] convertedValues = (Object[]) Array.newInstance(
          arrayComponentType == null ? Object.class
              : arrayComponentType, len);
      for (int i = 0; i < len; i++) {
        convertedValues[i] = converter.getAsObject(facesContext,
            component, submittedValue[i]);
      }
      return convertedValues;
    }
    if (List.class.isAssignableFrom(valueType)) {
      // Curious case: According to specs we should assume, that the
      // element type
      // of this List is java.lang.String. But there is a Converter set
      // for this
      // component. Because the user must know what he is doing, we will
      // convert the values.
      int len = submittedValue.length;
      List lst = new ArrayList(len);
      for (int i = 0; i < len; i++) {
        lst.add(converter.getAsObject(facesContext, component,
            submittedValue[i]));
      }
      return lst;
    }
    if (arrayComponentType == null) {
      throw new IllegalArgumentException("VALUE_BINDING_TYPE_ERROR");
    }
    if (arrayComponentType.isPrimitive()) {
      // primitive array
      int len = submittedValue.length;
      Object convertedValues = Array.newInstance(arrayComponentType, len);
      for (int i = 0; i < len; i++) {
        Array.set(convertedValues, i, converter.getAsObject(
            facesContext, component, submittedValue[i]));
      }
      return convertedValues;
    } else {
      // Object array
      int len = submittedValue.length;
      ArrayList convertedValues = new ArrayList(len);
      for (int i = 0; i < len; i++) {
        convertedValues.add(i, converter.getAsObject(facesContext,
            component, submittedValue[i]));
      }
      return convertedValues.toArray((Object[]) Array.newInstance(
          arrayComponentType, len));
    }
  }
  public static Object getConvertedUIInputValue(
      FacesContext facesContext, UIInput component,
      String submittedValue) throws ConverterException{
    Object convertedValue = null;
    /*
    if (submittedValue == null)
      throw new NullPointerException("submittedValue");
    */
    if(InputUtils.EMPTY_STRING.equals(submittedValue)){
      return null;
    }
    Converter converter = getConverterForProperty(facesContext, component, "value");
    if(converter != null){
      convertedValue = converter.getAsObject(facesContext, component, submittedValue);
    } else {
      convertedValue = submittedValue;
    }
    return convertedValue;
  }
  /**
   *
   * @param facesContext
   * @param component
   * @param property
   * @return converter for specified component attribute
   */
  public static Converter getConverterForProperty(FacesContext facesContext, UIOutput component, String property){
    Converter converter = component.getConverter();
    if(converter == null){
      ValueBinding valueBinding = component.getValueBinding(property);
      if(valueBinding != null){
        Class valueType = valueBinding.getType(facesContext);
        if(valueType == null || String.class.equals(valueType) || Object.class.equals(valueType)){
          //No converter needed
        } else {
          converter = facesContext.getApplication().createConverter(valueType);
          if(converter == null){
            throw new ConverterException("NO_CONVERTER_FOUND_ERROR");
          }
        }
      }
    }
    return converter;
  }
}
```

1.  Change Bean Property
---  ---
2.  Hello World JSF
3.  JavaServer Faces
4.  jsf jpa war
5.  Gathers all select items from specified component's children
6.  Simple utility class for CSS style formatting
7.  Common static utility methods that help in implementing JSF tags
8.  Jsf Utility
