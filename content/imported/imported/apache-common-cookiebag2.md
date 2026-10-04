---
title: Cookie Bag 2
nav: Cookie Bag 2
description: System.err.println("Sorted Cookie Bag Contents: " + sortedCookieBag);
section: Imported - java2s Archive
order: 1025
source: https://web.archive.org/web/20061018180948/http://www.java2s.com/Code/Java/Apache-Common/CookieBag2.htm
---
```java title=Example.java
import org.apache.commons.collections.Bag;
import org.apache.commons.collections.bag.HashBag;
import org.apache.commons.collections.bag.TreeBag;
import org.apache.commons.collections.TransformerUtils;
import org.apache.commons.collections.bag.TransformedBag;
import java.util.Arrays;
public class CookieBagV2 {
  private Bag cookieBag;
  private Bag sortedCookieBag;
  public static void main(String args[]) {
    CookieBagV2 app = new CookieBagV2();
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
    cookieBag =
      TransformedBag.decorate(
        new HashBag(Arrays.asList(cookieJar)),
        TransformerUtils.constantTransformer(cookieJar[2]));
    // cookieBag.addAll(Arrays.asList(cookieJar));
  }
  private void prepareSortedCookieBag() {
    sortedCookieBag = new TreeBag(Arrays.asList(cookieJar));
  }
  private String[] cookieJar =
    {"Bar", "Drop", "Brownies", "Cut Out", "Molded", "Sliced", "No Bake"};
}
```

Download: ApacheCollectionCookieBagV2.zip ( 514 K )
Related examples in the same category
