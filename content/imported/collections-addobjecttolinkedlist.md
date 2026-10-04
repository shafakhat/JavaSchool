---
title: Add object to LinkedList
nav: Add object to LinkedList
description: Address(String n, String s, String c, String st, String cd) {
section: Imported - java2s Archive
order: 2456
source: https://web.archive.org/web/20140829083846/http://www.java2s.com/Tutorial/Java/0140__Collections/AddobjecttoLinkedList.htm
---
```java title=Example.java
import java.util.LinkedList;
class Address {
  private String name;
  private String street;
  private String city;
  private String state;
  private String code;
  Address(String n, String s, String c, String st, String cd) {
    name = n;
    street = s;
    city = c;
    state = st;
    code = cd;
  }
  public String toString() {
    return name + " " + street + " " + city + " " + state + " " + code;
  }
}
class MailList {
  public static void main(String args[]) {
    LinkedList<Address> ml = new LinkedList<Address>();
    ml.add(new Address("A", "11 Ave", "U", "IL", "11111"));
    ml.add(new Address("R", "11 Lane", "M", "IL", "22222"));
    ml.add(new Address("T", "8 St", "C", "IL", "33333"));
    for (Address element : ml)
      System.out.println(element + "\n");
  }
}
```

| 9.12.1. | LinkedList Class |
|---|---|
| 9.12.2. | Get first and last elements from LinkedList |
| 9.12.3. | Get elements from LinkedList |
| 9.12.4. | Get SubList from LinkedList |
| 9.12.5. | Adding Elements: add a single element |
| 9.12.6. | Add elements at beginning and end of LinkedList |
| 9.12.7. | LinkedList: add, addFirst, addLast, remove |
| 9.12.8. | Retrieving the Ends from a LinkedList |
| 9.12.9. | Removing Elements |
| 9.12.10. | Making a stack from a LinkedList |
| 9.12.11. | Making a queue from a LinkedList |
| 9.12.12. | Convert Collection to ArrayList |
| 9.12.13. | Remove all elements or clear LinkedList |
| 9.12.14. | Remove first and last elements of LinkedList |
| 9.12.15. | Remove range of elements from LinkedList |
| 9.12.16. | Remove specified element from LinkedList |
| 9.12.17. | Convert LinkedList to Array with zero length array |
| 9.12.18. | Convert LinkedList to Array with full length array |
| 9.12.19. | Convert a LinkedList to ArrayList |
| 9.12.20. | Implementing a Stack |
| 9.12.21. | Implementing a Queue with LinkedList |
| 9.12.22. | Wrap queue to synchronize the methods |
| 9.12.23. | Search elements of LinkedList |
| 9.12.24. | Replace an Element of LinkedList |
| 9.12.25. | Add object to LinkedList |
| 9.12.26. | Check if a particular element exists in LinkedList |
| 9.12.27. | Create an object array from elements of LinkedList |
| 9.12.28. | Using a LinkedList in multi-thread |
| 9.12.29. | A basic priority linked list: maintaining an individual LinkedList for each priority level. |
| 9.12.30. | Helper method for creating list |
