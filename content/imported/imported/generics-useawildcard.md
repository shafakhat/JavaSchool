---
title: Use a wildcard.
nav: Use a wildcard.
description: Imported from the java2s.com archive: Use a wildcard.
section: Imported - java2s Archive
order: 1000
source: https://web.archive.org/web/20081212073650/http://www.java2s.com:80/Code/Java/Generics/Useawildcard.htm
---
```java title=Example.java
class Stats<T extends Number> {
  T[] nums;
  Stats(T[] o) {
    nums = o;
  }
  double average() {
    double sum = 0.0;
    for (int i = 0; i < nums.length; i++)
      sum += nums[i].doubleValue();
    return sum / nums.length;
  }
  boolean sameAvg(Stats<?> ob) {
    if (average() == ob.average())
      return true;
    return false;
  }
}
class WildcardDemo {
  public static void main(String args[]) {
    Integer inums[] = { 1, 2, 3, 4, 5 };
    Stats<Integer> iob = new Stats<Integer>(inums);
    double v = iob.average();
    System.out.println("iob average is " + v);
    Double dnums[] = { 1.1, 2.2, 3.3, 4.4, 5.5 };
    Stats<Double> dob = new Stats<Double>(dnums);
    double w = dob.average();
    System.out.println("dob average is " + w);
    Float fnums[] = { 1.0F, 2.0F, 3.0F, 4.0F, 5.0F };
    Stats<Float> fob = new Stats<Float>(fnums);
    double x = fob.average();
    System.out.println("fob average is " + x);
    // See which arrays have same average.
    System.out.print("Averages of iob and dob ");
    if (iob.sameAvg(dob))
      System.out.println("are the same.");
    else
      System.out.println("differ.");
    System.out.print("Averages of iob and fob ");
    if (iob.sameAvg(fob))
      System.out.println("are the same.");
    else
      System.out.println("differ.");
  }
}
```

1.  Java generic: Use a wildcard.
---  ---
2.  Java generic: Bounded Wildcard arguments
3.  Bounded Wildcard arguments.
