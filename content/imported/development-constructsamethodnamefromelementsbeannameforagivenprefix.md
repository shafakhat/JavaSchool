---
title: Constructs a method name from element's bean name for a given prefix
nav: Constructs a method name f...
description: * Copyright 1997-2007 Sun Microsystems, Inc. All rights reserved.
section: Imported - java2s Archive
order: 2031
source: https://web.archive.org/web/20140829083432/http://www.java2s.com/Tutorial/Java/0120__Development/Constructsamethodnamefromelementsbeannameforagivenprefix.htm
---
```java title=Example.java
/*
 * DO NOT ALTER OR REMOVE COPYRIGHT NOTICES OR THIS HEADER.
 *
 * Copyright 1997-2007 Sun Microsystems, Inc. All rights reserved.
 *
 * The contents of this file are subject to the terms of either the GNU
 * General Public License Version 2 only ("GPL") or the Common Development
 * and Distribution License("CDDL") (collectively, the "License").  You
 * may not use this file except in compliance with the License. You can obtain
 * a copy of the License at https://glassfish.dev.java.net/public/CDDL+GPL.html
 * or glassfish/bootstrap/legal/LICENSE.txt.  See the License for the specific
 * language governing permissions and limitations under the License.
 *
 * When distributing the software, include this License Header Notice in each
 * file and include the License file at glassfish/bootstrap/legal/LICENSE.txt.
 * Sun designates this particular file as subject to the "Classpath" exception
 * as provided by Sun in the GPL Version 2 section of the License file that
 * accompanied this code.  If applicable, add the following below the License
 * Header, with the fields enclosed by brackets [] replaced by your own
 * identifying information: "Portions Copyrighted [year]
 * [name of copyright owner]"
 *
 * Contributor(s):
 *
 * If you wish your version of this file to be governed by only the CDDL or
 * only the GPL Version 2, indicate your decision by adding "[Contributor]
 * elects to include this software in this distribution under the [CDDL or GPL
 * Version 2] license."  If you don't indicate a single choice of license, a
 * recipient has the option to distribute your version of this file under
 * either the CDDL, the GPL Version 2 or to extend the choice of license to
 * its licensees as provided above.  However, if you add GPL Version 2 code
 * and therefore, elected the GPL Version 2 license, then the option applies
 * only if the new code is made subject to such option by the copyright
 * holder.
 */
/**
 *
 * @author  Rajeshwar Patil
 * @version %I%, %G%
 */
public class Utils {
  /**
   * Constructs a method name from  element's bean
   * name for a given prefix.(schema2beans convention)
   *
   * @param elementName the given element name
   * @param prefix the given prefix
   * @return a method name formed from the given name and the prefix
   */
  public String methodNameFromBeanName(String elementName,
          String prefix){
      if((null == elementName) || (null == prefix) ||
              (prefix.length() <= 0 )){
          return elementName;
      }
      String methodName = upperCaseFirstLetter(elementName);
      return methodName = prefix + methodName;
  }
  /**
   * Converts the first letter of the given string to Uppercase.
   *
   * @param string the input string
   * @return the string with the Uppercase first letter
   */
   public String upperCaseFirstLetter(String string)
   {
       if(string == null || string.length() <= 0){
           return string;
       }
       return string.substring(0, 1).toUpperCase() + string.substring(1);
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
