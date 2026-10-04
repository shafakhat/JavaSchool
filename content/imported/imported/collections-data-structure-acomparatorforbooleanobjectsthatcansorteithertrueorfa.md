---
title: A Comparator for Boolean objects that can sort either true or false first
nav: A Comparator for Boolean o...
description: A Comparator for Boolean objects that can sort either true or false first : Comparator « Collections Data Structure « Java
section: Imported - java2s Archive
order: 1009
source: https://web.archive.org/web/20091124193831/http://www.java2s.com:80/Code/Java/Collections-Data-Structure/AComparatorforBooleanobjectsthatcansorteithertrueorfalsefirst.htm
---
A Comparator for Boolean objects that can sort either true or false first : Comparator « Collections Data Structure « Java
A Comparator for Boolean objects that can sort either true or false first

```java title=Example.java
/*
 * Copyright 2002-2005 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
import java.io.Serializable;
import java.util.Comparator;
/**
 * A Comparator for Boolean objects that can sort either true or false first.
 *
 * @author Keith Donald
 * @since 1.2.2
 */
public final class BooleanComparator implements Comparator, Serializable {
  /**
   * A shared default instance of this comparator, treating true lower
   * than false.
   */
  public static final BooleanComparator TRUE_LOW = new BooleanComparator(true);
  /**
   * A shared default instance of this comparator, treating true higher
   * than false.
   */
  public static final BooleanComparator TRUE_HIGH = new BooleanComparator(false);
  private final boolean trueLow;
  /**
   * Create a BooleanComparator that sorts boolean values based on
   * the provided flag.
   * <p>Alternatively, you can use the default shared instances:
   * <code>BooleanComparator.TRUE_LOW</code> and
   * <code>BooleanComparator.TRUE_HIGH</code>.
   * @param trueLow whether to treat true as lower or higher than false
   * @see #TRUE_LOW
   * @see #TRUE_HIGH
   */
  public BooleanComparator(boolean trueLow) {
    this.trueLow = trueLow;
  }
  public int compare(Object o1, Object o2) {
    boolean v1 = ((Boolean) o1).booleanValue();
    boolean v2 = ((Boolean) o2).booleanValue();
    return (v1 ^ v2) ? ((v1 ^ this.trueLow) ? 1 : -1) : 0;
  }
  public boolean equals(Object obj) {
    if (this == obj) {
      return true;
    }
    if (!(obj instanceof BooleanComparator)) {
      return false;
    }
    return (this.trueLow == ((BooleanComparator) obj).trueLow);
  }
  public int hashCode() {
    return (this.trueLow ? -1 : 1) * getClass().hashCode();
  }
  public String toString() {
    return "BooleanComparator: " + (this.trueLow ? "true low" : "true high");
  }
}
```

1.  Creating a Comparable object
---  ---
2.  Writing Your own Comparator
3.  A Class Implementing Comparable
4.  Comparator for comparing strings ignoring first character
5.  Customized Sort Test
6.  List and Comparators
7.  Sort backwards
8.  Company and Employee
9.  Search with a Comparator
10.  Keep upper and lowercase letters together
11.  Uses anonymous inner classes
12.  Building the anonymous inner class in-place
13.  Sort an array of strings in reverse order.
14.  Sort an array of strings, ignore case difference.
15.  Comparator uses a Collator to determine the proper, case-insensitive lexicographical ordering of two strings.
16.  Using the Comparable interface to compare and sort objects
17.  Sort on many(more than one) fields
18.  File Name Comparator
19.  Comparator similar to String.CASE_INSENSITIVE_ORDER, but handles only ASCII characters
20.  Natural Order Comparator
21.  Reverse Order Comparator
22.  Invertible Comparator
