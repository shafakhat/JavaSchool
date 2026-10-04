---
title: Java Design Patterns Tutorial - Java Design Pattern - Iterator Pattern
nav: Java Design Patterns Tutor...
description: Iterator pattern accesses the elements of a collection object in sequential manner without knowing its underlying representation.
section: Imported - java2s Archive
order: 50126
source: https://www.java2s.com/Tutorials/Java/Java_Design_Patterns/0160__Java_Iterator_Pattern.html
---
```java title=Example.java
```

Iterator pattern accesses the elements of a collection object in sequential manner without knowing its underlying representation.

Iterator pattern is one of the behavioral patterns.

## Example

```java title=Example.java
interface Iterator {
   publicboolean hasNext();
   public Object next();
}class LetterBag {
   public String names[] = {"R" , "J" ,"A" , "L"};
   public Iterator getIterator() {
      returnnew NameIterator();
   }
   class NameIterator implements Iterator {
      int index;
      @Override
      publicboolean hasNext() {
         if(index < names.length){
            return true;
         }
         return false;
      }
      @Override
      public Object next() {
         if(this.hasNext()){
            return names[index++];
         }
         return null;
      }
   }
}
publicclass Main {
   publicstaticvoid main(String[] args) {
      LetterBag bag = new LetterBag();
      for(Iterator iter = bag.getIterator(); iter.hasNext();){
         String name = (String)iter.next();
         System.out.println("Name : " + name);
      }
   }
}
```

The code above generates the following result.

- « Previous
