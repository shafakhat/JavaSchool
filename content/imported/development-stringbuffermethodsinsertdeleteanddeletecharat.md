---
title: StringBuffer methods insert, delete and deleteCharAt
nav: StringBuffer methods inser...
description: System.out.printf("buffer after inserts:\n%s\n\n", buffer.toString());
section: Imported - java2s Archive
order: 1643
source: https://web.archive.org/web/20140829085944/http://www.java2s.com/Tutorial/Java/0120__Development/StringBuffermethodsinsertdeleteanddeleteCharAt.htm
---
```java title=Example.java
public class MainClass {
  public static void main(String args[]) {
    Object objectRef = "hello";
    String string = "goodbye";
    char charArray[] = { 'a', 'b', 'c', 'd', 'e', 'f' };
    boolean booleanValue = true;
    char characterValue = 'K';
    int integerValue = 7;
    long longValue = 10000000;
    float floatValue = 2.5f;
    double doubleValue = 33.3;
    StringBuffer buffer = new StringBuffer();
    buffer.insert(0, objectRef);
    buffer.insert(0, "  ");
    buffer.insert(0, string);
    buffer.insert(0, "  ");
    buffer.insert(0, charArray);
    buffer.insert(0, "  ");
    buffer.insert(0, charArray, 3, 3);
    buffer.insert(0, "  ");
    buffer.insert(0, booleanValue);
    buffer.insert(0, "  ");
    buffer.insert(0, characterValue);
    buffer.insert(0, "  ");
    buffer.insert(0, integerValue);
    buffer.insert(0, "  ");
    buffer.insert(0, longValue);
    buffer.insert(0, "  ");
    buffer.insert(0, floatValue);
    buffer.insert(0, "  ");
    buffer.insert(0, doubleValue);
    System.out.printf("buffer after inserts:\n%s\n\n", buffer.toString());
    buffer.deleteCharAt(10);
    buffer.delete(2, 6);
    System.out.printf("buffer after deletes:\n%s\n", buffer.toString());
  }
}
java title=Example.java
buffer after inserts:
33.3  2.5  10000000  7  K  true  def  abcdef  goodbye  hello
buffer after deletes:
332.5 10000000  7  K  true  def  abcdef  goodbye  hello
```

| 6.15.1. | StringBuffer and StringBuilder |
|---|---|
| 6.15.2. | You can also create a StringBuffer object using a reference stored in a variable of type String: |
| 6.15.3. | Creating a String Object From a StringBuffer Object |
| 6.15.4. | Creating a StringBuffer object with a specific value for the capacity |
| 6.15.5. | Check the capacity of StringBuilder object |
| 6.15.6. | Adding String to a StringBuffer Object |
| 6.15.7. | The append() method returns a reference to the extended StringBuffer object |
| 6.15.8. | Calling append() method to construct a StringBuffer object |
| 6.15.9. | Appending a Substring: append part of the aString object to the buf object |
| 6.15.10. | Appending Basic Types: long, double |
| 6.15.11. | Appending a subset of the elements from a char array |
| 6.15.12. | StringBuffer methods charAt, setCharAt, getChars and reverse |
| 6.15.13. | StringBuffer methods insert, delete and deleteCharAt |
| 6.15.14. | Convert digit to character with Character.forDigit |
| 6.15.15. | Inserting Strings |
| 6.15.16. | The Length of a StringBuffer Object |
| 6.15.17. | Changing the StringBufer Length for a StringBuffer Object |
| 6.15.18. | To find out a StringBuffer object's capacity |
| 6.15.19. | The ensureCapacity() method changes the default capacity of a StringBuffer object |
| 6.15.20. | Finding the Position of a Substring |
| 6.15.21. | Specifying the index position in the buffer where the search is to start |
| 6.15.22. | Replacing a Substring in the Buffer |
| 6.15.23. | Extracting Characters From a Mutable String: charAt() and getChars() methods |
| 6.15.24. | Changing a single character in a StringBuffer object |
| 6.15.25. | Using the deleteCharAt() method to remove a character from a StringBuffer object at the index position |
| 6.15.26. | Removing several characters from a StringBuffer object |
| 6.15.27. | Remove substring from StringBuilder |
| 6.15.28. | Deletes text from the StringBuilder object |
| 6.15.29. | Reversing the sequence of characters in a StringBuffer object with the reverse() method |
