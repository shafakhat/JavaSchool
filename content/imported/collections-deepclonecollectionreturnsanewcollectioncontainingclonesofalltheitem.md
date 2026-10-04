---
title: Deep clone collection
nav: Deep clone collection
description: 9.1.7.Deep clone collection: Returns a new collection containing clones of all the items in the specified collection. Previous / Next
section: Imported - java2s Archive
order: 2324
source: https://web.archive.org/web/20140223094859/http://www.java2s.com/Tutorial/Java/0140__Collections/DeepclonecollectionReturnsanewcollectioncontainingclonesofalltheitemsinthespecifiedcollection.htm
---
9.1.7.Deep clone collection: Returns a new collection containing clones of all the items in the specified collection. Previous / Next

```java title=Example.java
/*
 * JCommon : a free general purpose class library for the Java(tm) platform
 *
 *
 * (C) Copyright 2000-2008, by Object Refinery Limited and Contributors.
 *
 * Project Info:  http://www.jfree.org/jcommon/index.html
 *
 * This library is free software; you can redistribute it and/or modify it
 * under the terms of the GNU Lesser General Public License as published by
 * the Free Software Foundation; either version 2.1 of the License, or
 * (at your option) any later version.
 *
 * This library is distributed in the hope that it will be useful, but
 * WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
 * or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public
 * License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public
 * License along with this library; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301,
 * USA.
 *
 * [Java is a trademark or registered trademark of Sun Microsystems, Inc.
 * in the United States and other countries.]
 *
 * -------------------
 * ShapeUtilities.java
 * -------------------
 * (C)opyright 2003-2008, by Object Refinery Limited and Contributors.
 *
 * Original Author:  David Gilbert (for Object Refinery Limited);
 * Contributor(s):   -;
 *
 * $Id: ShapeUtilities.java,v 1.18 2008/06/02 06:58:28 mungady Exp $
 *
 * Changes
 * -------
 * 13-Aug-2003 : Version 1 (DG);
 * 16-Mar-2004 : Moved rotateShape() from RefineryUtilities.java to here (DG);
 * 13-May-2004 : Added new shape creation methods (DG);
 * 30-Sep-2004 : Added createLineRegion() method (DG);
 *               Moved drawRotatedShape() method from RefineryUtilities class
 *               to this class (DG);
 * 04-Oct-2004 : Renamed ShapeUtils --> ShapeUtilities (DG);
 * 26-Oct-2004 : Added a method to test the equality of two Line2D
 *               instances (DG);
 * 10-Nov-2004 : Added new translateShape() and equal(Ellipse2D, Ellipse2D)
 *               methods (DG);
 * 11-Nov-2004 : Renamed translateShape() --> createTranslatedShape() (DG);
 * 07-Jan-2005 : Minor Javadoc fix (DG);
 * 11-Jan-2005 : Removed deprecated code in preparation for 1.0.0 release (DG);
 * 21-Jan-2005 : Modified return type of RectangleAnchor.coordinates()
 *               method (DG);
 * 22-Feb-2005 : Added equality tests for Arc2D and GeneralPath (DG);
 * 16-Mar-2005 : Fixed bug where equal(Shape, Shape) fails for two Polygon
 *               instances (DG);
 * 01-Jun-2008 : Fixed bug in equal(GeneralPath, GeneralPath) method (DG);
 *
 */
import java.awt.Shape;
import java.awt.geom.AffineTransform;
import java.awt.geom.Point2D;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.lang.reflect.Modifier;
import java.util.Collection;
import java.util.Iterator;
/**
 * Utility methods for {@link Shape} objects.
 *
 * @author David Gilbert
 */
public class Main {
  /**
   * Returns a new collection containing clones of all the items in the
   * specified collection.
   *
   * @param collection
   *          the collection (<code>null</code> not permitted).
   * @return A new collection containing clones of all the items in the
   *         specified collection.
   * @throws CloneNotSupportedException
   *           if any of the items in the collection cannot be cloned.
   */
  public static Collection deepClone(final Collection collection) throws CloneNotSupportedException {
    if (collection == null) {
      throw new IllegalArgumentException("Null 'collection' argument.");
    }
    // all JDK-Collections are cloneable ...
    // and if the collection is not clonable, then we should throw
    // a CloneNotSupportedException anyway ...
    final Collection result = (Collection) clone(collection);
    result.clear();
    final Iterator iterator = collection.iterator();
    while (iterator.hasNext()) {
      final Object item = iterator.next();
      if (item != null) {
        result.add(clone(item));
      } else {
        result.add(null);
      }
    }
    return result;
  }
  /**
   * Returns a clone of the specified object, if it can be cloned, otherwise
   * throws a CloneNotSupportedException.
   *
   * @param object
   *          the object to clone (<code>null</code> not permitted).
   * @return A clone of the specified object.
   * @throws CloneNotSupportedException
   *           if the object cannot be cloned.
   */
  public static Object clone(final Object object) throws CloneNotSupportedException {
    if (object == null) {
      throw new IllegalArgumentException("Null 'object' argument.");
    }
    try {
      final Method method = object.getClass().getMethod("clone", (Class[]) null);
      if (Modifier.isPublic(method.getModifiers())) {
        return method.invoke(object, (Object[]) null);
      }
    } catch (NoSuchMethodException e) {
      System.out.println("Object without clone() method is impossible.");
    } catch (IllegalAccessException e) {
      System.out.println("Object.clone(): unable to call method.");
    } catch (InvocationTargetException e) {
      System.out.println("Object without clone() method is impossible.");
    }
    throw new CloneNotSupportedException("Failed to clone.");
  }
}
```

| 9.1.1. | The Collections Framework consists of three parts |
|---|---|
| 9.1.2. | Framework Interfaces |
| 9.1.3. | Interface type and its implementation |
| 9.1.4. | Conversion of different Collection data types |
| 9.1.5. | Making Your Objects Comparable and Sortable |
| 9.1.6. | Using Comparable and Comparator |
| 9.1.7. | Deep clone collection: Returns a new collection containing clones of all the items in the specified collection. |
