---
title: Simple utility class for CSS style formatting
nav: Simple utility class for C...
description: * Licensed under the Common Development and Distribution License,
section: Imported - java2s Archive
order: 1038
source: https://web.archive.org/web/20100212185235/http://java2s.com/Code/Java/J2EE/SimpleutilityclassforCSSstyleformatting.htm
---
Simple utility class for CSS style formatting

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
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
/**
 * Simple utility class for CSS style formatting
 * Current version isn't thread-safe and doesn't provide any validation
 *
 * Usage is simle
 * <code>
 *  CSSFormat format = new CSSFormat();
 *  format.add("background-position", "top left");
 *  format.addURL("background-image", "/images/corner.gif");
 *  responseWriter.writeAttribute("style", format, null);
 * </code>
 *
 * @author Maksim Kaszynski
 *
 */
public class CSSFormat {
  /**
   * Surrounds given URL with <code>url()</code>
   * @param url
   * @return
   */
  public static String url(String url){
    StringBuffer buf = new StringBuffer(url.length() + 7);
    buf.append("url(").append(url).append(")");
    return buf.toString();
  }
  /**
   * Formats property-value pair in CSS fashion
   * @param property
   * @param value
   * @return
   */
  public static String propertyValue(String property, String value){
    return formatPropertyValue(property, value);
  }
  private static String formatPropertyValue(Object property, Object value){
    StringBuffer buf = new StringBuffer();
    buf.append(property).append(": ").append(value).append(";");
    return buf.toString();
  }
  private Map properties;
  /**
   * Constructs an empty CSSFormat object
   */
  public CSSFormat() {
    properties = new HashMap();
  }
  /**
   * Constructs CSSFormat object
   * and fills it with given parameters
   * @param property
   * @param value
   */
  public CSSFormat(String property, String value){
    properties = new HashMap(3);
    add(property, value);
  }
  /**
   * Adds property. If such property already exists,
   * its value is replaced with new one
   * @param property
   * @param value
   * @return itself
   */
  public CSSFormat add(String property, String value){
    properties.put(property, value);
    return this;
  }
  /**
   * adds a property with URL value
   * given value is wrapped in <code>url()</code> clause
   * @param property
   * @param url
   * @return itself
   */
  public CSSFormat addURL(String property, String url){
    properties.put(property, url(url));
    return this;
  }
  /**
   * Concatenates all properties with their values to produce single-line CSS output
   */
  public String toString() {
    return concatenate(null);
  }
  /**
   * Concatenates all properties with their values to produce CSS output
   * @param separator - custom string to be inserted between properties
   * @return
   */
  public String concatenate(String separator){
    StringBuffer output = new StringBuffer();
    for(Iterator iter = properties.entrySet().iterator(); iter.hasNext();){
      Map.Entry entry = (Map.Entry) iter.next();
      output.append(formatPropertyValue(entry.getKey(), entry.getValue()));
      if(separator != null && iter.hasNext()){
        output.append(separator);
      }
    }
    return output.toString();
  }
}
```

1.  Change Bean Property
---  ---
2.  Hello World JSF
3.  JavaServer Faces
4.  jsf jpa war
5.  Gathers all select items from specified component's children
6.  Converts UISelectMany submitted value to converted value
7.  Common static utility methods that help in implementing JSF tags
8.  Jsf Utility
