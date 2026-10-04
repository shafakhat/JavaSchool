---
title: Determine the JDK Version Number
nav: Determine the JDK Version ...
description: * There is a human readible JDK version number available as a Java property. The property name is called "java.version".
section: Imported - java2s Archive
order: 1041
source: https://web.archive.org/web/20111105140554/http://java2s.com/Tutorial/Java/0120__Development/DeterminetheJDKVersionNumber.htm
---
```java title=Example.java
/** Determine the JDK Version Number
 *
 * There is a human readible JDK version number available as a Java property. The property name is called "java.version".
 * Unfortunately it is complicated to parse it mechanically. A somewhat better choice is the Java property called
 * "java.class.version". The property value can be converted to a floating pointer value. JDK 1.1 implies 45.3. JDK 1.2
 * implies 46.0. JDK 1.3 implies 47.0. JDK 1.4 implies 48.0.
 *
 * java.class.version property value
 * <ul>
 * <li> JDK 1.1 = 45.3
 * <li> JDK 1.2 = 46.0
 * <li> JDK 1.3 = 47.0
 * <li> JDK 1.4 = 48.0
 * </ul>
 *
 * @author Thomas Rischbeck <thomas.rischbeck@arjuna.com>
 * @version $Id: VersionCheck.java 2342 2006-03-30 13:06:17Z  $
 */
public class VersionCheck {
   private static final String CLASS_VERSION = System.getProperty("java.class.version","44.0");
   private static final boolean IS_JDK_11 = ("46.0".compareTo(CLASS_VERSION) > 0) && ("45.3".compareTo(CLASS_VERSION) <= 0);
   private static final boolean IS_JDK_12 = ("47.0".compareTo(CLASS_VERSION) > 0) && ("46.0".compareTo(CLASS_VERSION) <= 0);
   private static final boolean IS_JDK_13 = ("48.0".compareTo(CLASS_VERSION) > 0) && ("47.0".compareTo(CLASS_VERSION) <= 0);
   private static final boolean IS_JDK_14 = ("49.0".compareTo(CLASS_VERSION) > 0) && ("48.0".compareTo(CLASS_VERSION) <= 0);
   private static final boolean IS_JDK_13_OR_BELOW = IS_JDK_11 || IS_JDK_12 || IS_JDK_13;
   private static final boolean IS_JDK_14_OR_ABOVE = ("48.0".compareTo(CLASS_VERSION) <= 0);
   public static final boolean isJDK11only()
   {
     return IS_JDK_11;
   }
   public static final boolean isJDK12only()
   {
     return IS_JDK_12;
   }
   public static final boolean isJDK13only()
   {
     return IS_JDK_13;
   }
   public static final boolean isJDK14only()
   {
     return IS_JDK_14;
   }
   public static final boolean isJDK13orBelow()
   {
      return IS_JDK_13_OR_BELOW;
   }
   public static final boolean isJDK14orAbove()
   {
      return IS_JDK_14_OR_ABOVE;
   }
}
```
