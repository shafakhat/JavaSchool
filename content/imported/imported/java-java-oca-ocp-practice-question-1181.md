---
title: Java OCA OCP Practice Question 1181
nav: Java OCA OCP Practice Ques...
description: Without generics, the compiler has no way of knowing what type is appropriate for this TreeSet, so it allows everything to compile.
section: Imported - java2s Archive
order: 1144
source: https://web.archive.org/web/20210101014729/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1181.html
---
## Question

Given:

```java title=Example.java
import java.util.Iterator;
import java.util.Set;
import java.util.TreeSet;

publicclass Main {
   publicstaticvoid before() {
      Set set = newTreeSet();
      set.add("2");
      set.add(3);//fromwww.java2s.com
      set.add("1");
      Iterator it = set.iterator();
      while (it.hasNext())
         System.out.print(it.next() + " ");
   }

   publicstaticvoid main(String args[]) {
      before();

   }
}
```

Which statements are true?

- A. The before() method will print 1 2
- B. The before() method will print 1 2 3
- C. The before() method will print three numbers, but the order cannot be determined
- D. The before() method will not compile
- E. The before() method will throw an exception at runtime

```java title=Example.java
E is correct.
```

## Note

You can't put both Strings and ints into the same TreeSet.

Without generics, the compiler has no way of knowing what type is appropriate for this TreeSet, so it allows everything to compile.

At runtime, the TreeSet will try to sort the elements as they're added, and when it tries to compare an Integer with a String, it will throw a ClassCastException.

Note that although the before() method does not use generics, it does use autoboxing.

Watch out for code that uses some new features and some old features mixed together.

PreviousNext

## Related

- Java OCA OCP Practice Question 1178
- Java OCA OCP Practice Question 1179
- Java OCA OCP Practice Question 1180
- Java OCA OCP Practice Question 1182
- Java OCA OCP Practice Question 1183
