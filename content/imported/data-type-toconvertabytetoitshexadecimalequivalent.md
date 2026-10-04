---
title: To convert a byte to it's hexadecimal equivalent
nav: To convert a byte to it's ...
description: Imported from the java2s.com archive: To convert a byte to it's hexadecimal equivalent
section: Imported - java2s Archive
order: 1349
source: https://web.archive.org/web/20140829084709/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Toconvertabytetoitshexadecimalequivalent.htm
---
```java title=Example.java
public class Main {
  public static void main(String[] argv) {
    System.out.println(byteToHex((byte) 123));
  }
  public static String byteToHex(byte b) {
    int i = b & 0xFF;
    return Integer.toHexString(i);
  }
}
//7b
```

| 2.4.1. | Java byte: byte is smallest Java integer type.byte is 8 bit signed type ranges from –128 to 127. |
|---|---|
| 2.4.2. | Using byte data type |
| 2.4.3. | Convert byte to String: Using the static toString method of the Byte class |
| 2.4.4. | Convert byte to String: Using simple concatenation with an empty String |
| 2.4.5. | Convert byte to String: Creating a byte array and passing it to the String constructor |
| 2.4.6. | Convert String to byte |
| 2.4.7. | Use toString method of Byte class to convert Byte into String |
| 2.4.8. | Use Byte constructor to convert byte primitive type to Byte object |
| 2.4.9. | Compare Two Java byte Arrays Example |
| 2.4.10. | Convert an UNSIGNED byte to a JAVA type |
| 2.4.11. | To convert a byte to it's hexadecimal equivalent |
| 2.4.12. | byte Array To Hex String |
| 2.4.13. | hex String To Byte Array |
| 2.4.14. | Convert byte[ ] array to String |
| 2.4.15. | Convert String to byte array |
| 2.4.16. | Convert Byte to numeric primitive data types example |
| 2.4.17. | Min and Max values of datatype byte |
| 2.4.18. | Byte Range |
