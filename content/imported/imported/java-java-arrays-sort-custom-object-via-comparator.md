---
title: Java Arrays sort custom object via Comparator
nav: Java Arrays sort custom ob...
description: //fromwww.java2s.comArrays.sort(myArray, Language.NAME_COMPARATOR);
section: Imported
order: 20029
source: http://www.java2s.com/ref/java/java-arrays-sort-custom-object-via-comparator.html
---
- java.util
- java.util AbstractList ArrayDeque ArrayList Arrays Base64 BitSet Calendar Collection Collections Comparator Currency Date Deque DoubleSummaryStatistics EnumMap EnumSet EventListener EventObject Formatter GregorianCalendar HashMap HashSet Hashtable IntSummaryStatistics Iterator LinkedHashMap LinkedHashSet LinkedList List ListIterator ResourceBundle Locale LongSummaryStatistics Map NavigableMap Objects Observer Optional OptionalInt PriorityQueue Properties Queue Random Scanner Set SortedMap SortedSet Spliterator Stack StringTokenizer TimerTask TimeZone TreeMap TreeSet UUID Vector

## Description

Java Arrays sort custom object via Comparator

```java title=Example.java
import java.util.Arrays;
import java.util.Comparator;

publicclass Main {
  publicstaticvoid main(String[] args) {
    Language[] myArray = new Language[5];
    myArray[0] = new Language("CSS", 15);
    myArray[1] = new Language("HTML", 12);
    myArray[2] = new Language("Java", 15);
    myArray[3] = new Language("Javascript", 18);
    myArray[4] = new Language("SQL", 37);
    //fromwww.java2s.comArrays.sort(myArray, Language.NAME_COMPARATOR);
    System.out.println(Arrays.toString(myArray));
    Arrays.sort(myArray, Language.AGE_COMPARATOR);
    System.out.println(Arrays.toString(myArray));
  }
}

class Language {
  publicstaticComparator<Language> AGE_COMPARATOR = newComparator<Language>() {
    @Overridepublicint compare(final Language o1, final Language o2) {
      returnInteger.valueOf(o1.age).compareTo(o2.age);
    }
  };
  //Lambda expressionpublicstaticComparator<Language> NAME_COMPARATOR = (Language o1, Language o2) ->{
    return o1.name.compareTo(o2.name);
  };

  String name;
  int age;

  public Language(String name, int age) {
    this.name = name;
    this.age = age;
  }

  publicString toString() {
    return"[name: " + name + ", age: " + age + "]";
  }
}
```

PreviousNext

## Related

- Java Arrays sort sub array
- Java Arrays sort using lambda expression as Comparator
- Java Arrays sort via Stream
- Java Base64 decode to byte array
- Java Base64 encode byte array to String
