---
title: hex String To Byte Array
nav: hex String To Byte Array
description: Imported from the java2s.com archive: hex String To Byte Array
section: Imported - java2s Archive
order: 1186
source: https://web.archive.org/web/20140829084813/http://www.java2s.com/Tutorial/Java/0040__Data-Type/hexStringToByteArray.htm
---
```java title=Example.java
public class Main {
  public static byte[] hexStringToByteArray(String s) {
    byte[] b = new byte[s.length() / 2];
    for (int i = 0; i < b.length; i++) {
      int index = i * 2;
      int v = Integer.parseInt(s.substring(index, index + 2), 16);
      b[i] = (byte) v;
    }
    return b;
  }
}
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
