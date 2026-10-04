---
title: A combination of two collections into a collection
nav: A combination of two colle...
description: This program is distributed under GPL Version 3.0 in the hope that
section: Imported - java2s Archive
order: 2292
source: https://web.archive.org/web/20140725213057/http://www.java2s.com/Tutorial/Java/0140__Collections/Acombinationoftwocollectionsintoacollection.htm
---
```java title=Example.java
/* DualCollection.java
{{IS_NOTE
  Purpose:
  Description:
  History:
    Sun Sep  2 21:29:38     2007, Created by tomyeh
}}IS_NOTE
Copyright (C) 2007 Potix Corporation. All Rights Reserved.
{{IS_RIGHT
  This program is distributed under GPL Version 3.0 in the hope that
  it will be useful, but WITHOUT ANY WARRANTY.
}}IS_RIGHT
*/
import java.util.Collection;
import java.util.Collections;
import java.util.Iterator;
import java.util.AbstractCollection;
/**
 *
 * @author tomyeh
 * @since 3.0.0
 */
public class DualCollection extends AbstractCollection
implements java.io.Serializable {
  private final Collection _first, _second;
  /** Returns a collection by combining two collections.
   * It checks whether any of them is null, or equals. And, returns
   * the non-null one if another is null.
   * If both null, it returns null.
   */
  public static final
  Collection combine(Collection first, Collection second) {
    if (first == second) //we don't use equals to have better performance
      return first;
    if (first != null)
      if (second != null)
        return new DualCollection(first, second);
      else
        return first;
    else
      return second;
  }
  /** Constructor.
   * It is better to use {@link #combine} instead of this method
   * since it checks whether any of them is null or equals.
   */
  public DualCollection(Collection first, Collection second) {
    _first = first != null ? first: Collections.EMPTY_LIST;
    _second = second != null ? second: Collections.EMPTY_LIST;
  }
  //Collection//
  public int size() {
    return _first.size() + _second.size();
  }
  public Iterator iterator() {
    return new Iter();
  }
  private class Iter implements Iterator {
    private Iterator _it;
    private boolean _bSecond;
    private Iter() {
      _it = _first.iterator();
    }
    public boolean hasNext() {
      return _it.hasNext() || (!_bSecond && !_second.isEmpty());
    }
    public Object next() {
      if (!_bSecond && !_it.hasNext()) {
        _it = _second.iterator();
        _bSecond = true;
      }
      return _it.next();
    }
    public void remove() {
      _it.remove();
    }
  }
}
```

| 9.2.1. | Using the Collections.synchronized methods |
|---|---|
| 9.2.2. | Get Synchronized List from ArrayList |
| 9.2.3. | Sort elements of ArrayList |
| 9.2.4. | Copy Elements of ArrayList to Java Vector |
| 9.2.5. | Copy Elements of One ArrayList to Another ArrayList |
| 9.2.6. | Find maximum element of ArrayList |
| 9.2.7. | Find Minimum element of ArrayList |
| 9.2.8. | Get Enumeration over ArrayList |
| 9.2.9. | Perform Binary Search on ArrayList |
| 9.2.10. | Replace All Elements Of ArrayList |
| 9.2.11. | Replace all occurrences of specified element of ArrayList |
| 9.2.12. | Reverse order of all elements of ArrayList |
| 9.2.13. | Shuffle elements of ArrayList |
| 9.2.14. | Swap elements of ArrayList |
| 9.2.15. | Sort ArrayList in descending order using comparator |
| 9.2.16. | Search collection element |
| 9.2.17. | Rotate elements of a collection |
| 9.2.18. | Sort items of an ArrayList with Collections.reverseOrder() |
| 9.2.19. | Create an empty collection object |
| 9.2.20. | The Collections.fill() method |
| 9.2.21. | Create and demonstrate an immutable collection. |
| 9.2.22. | A combination of two collections into a collection |
