---
title: Collection Bag
nav: Collection Bag
description: System.err.println("Sorted Cookie Bag Contents: " + sortedCookieBag);
section: Imported - java2s Archive
order: 1016
source: https://web.archive.org/web/20061018181015/http://www.java2s.com/Code/Java/Apache-Common/CollectionBag.htm
---
```java title=Example.java
import org.apache.commons.collections.Bag;
import org.apache.commons.collections.bag.HashBag;
import org.apache.commons.collections.bag.TreeBag;
import java.util.Arrays;
public class CookieBagV1 {
  private Bag cookieBag;
  private Bag sortedCookieBag;
  public static void main(String args[]) {
    CookieBagV1 app = new CookieBagV1();
    app.prepareBags();
    app.printBagContents();
    app.addRandomCookies();
    app.printBagContents();
  }
  private void printBagContents() {
    System.err.println("Cookie Bag Contents: " + cookieBag);
    System.err.println("Sorted Cookie Bag Contents: " + sortedCookieBag);
  }
  private void addRandomCookies() {
    int count = (int)(Math.random() * 10);
    int pick  = (int)(Math.random() * 10);
    pick = pick > 6 ? 6 : pick;
    if (count > 5) cookieBag.add(cookieJar[pick], count);
    else sortedCookieBag.add(cookieJar[pick], count);
  }
  private void prepareBags() {
    prepareCookieBag();
    prepareSortedCookieBag();
  }
  private void prepareCookieBag() {
    cookieBag = new HashBag(Arrays.asList(cookieJar));
  }
  private void prepareSortedCookieBag() {
    sortedCookieBag = new TreeBag(Arrays.asList(cookieJar));
  }
  private String[] cookieJar =
    {"Bar", "Drop", "Brownies", "Cut Out", "Molded", "Sliced", "No Bake"};
}
```

Download: CookieBagV1.zip ( 514 K )
Related examples in the same category
