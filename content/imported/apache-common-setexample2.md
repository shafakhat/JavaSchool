---
title: Set Example 2
nav: Set Example 2
description: Imported from the java2s.com archive: Set Example 2
section: Imported - java2s Archive
order: 1054
source: https://web.archive.org/web/20061018181000/http://www.java2s.com/Code/Java/Apache-Common/SetExample2.htm
---
```java title=Example.java
import org.apache.commons.collections.collection.*;
import org.apache.commons.collections.set.*;
import java.util.Set;
import java.util.HashSet;
import java.util.Iterator;
import java.util.Collection;
public class SetExampleV2 {
  public static void main(String args[]) {
    // create two sets
    Set set1 = new HashSet();
    set1.add("Red");
    set1.add("Green");
    Set set2 = new HashSet();
    set2.add("Yellow");
    set2.add("Red");
    // create a composite set out of these two
    CompositeSet composite = new CompositeSet();
    // set the class that handles additions, conflicts etc
    // composite.setMutator(new CompositeMutator());
    // initialize the composite with the sets
    // Cannot be used if set1 and set2 intersect is not null and
    // a strategy to deal with it has not been set
    composite.addComposited(new Set[] {set1, set2});
    // do some addition/deletions
    // composite.add("Pink");
    // composite.remove("Green");
    // whats left in the composite?
    Iterator itr = composite.iterator();
    while(itr.hasNext()) {
      System.err.println(itr.next());
    }
  }
}
class CompositeMutator implements CompositeSet.SetMutator {
  public void resolveCollision(
    CompositeSet comp,
    Set existing,
    Set added,
    Collection intersection) {
    added.removeAll(intersection);
  }
  public boolean add(
    CompositeCollection collection,
    Collection[] collections,
    Object obj) {
    return collections[0].add(obj);
  }
  public boolean remove(
    CompositeCollection collection,
    Collection[] collections,
    Object obj) {
    return collections[0].remove(obj);
  }
  public boolean addAll(
    CompositeCollection collection,
    Collection[] collections,
    Collection coll) {
    return collections[0].addAll(coll);
  }
}
```

Download: ApacheCommonSetExampleV2.zip ( 514 K )
Related examples in the same category
