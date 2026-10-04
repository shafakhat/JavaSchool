---
title: Assertions
nav: Assertions
description: Imported from the java2s.com archive: Assertions
section: Imported - java2s Archive
order: 1799
source: https://web.archive.org/web/20140829082440/http://www.java2s.com/Tutorial/Java/0120__Development/Assertions.htm
---
```java title=Example.java
public class MainClass {
  public static void main(String[] arg) {
    int a = 0;
    assert a == 0;
  }
}
java title=Example.java
java -enableassertions MyProg
You can also use its abbreviated form -ea:
   java -ea MyProg
```

| 6.24.1. | Assertions |
|---|---|
| 6.24.2. | More Complex Assertions |
| 6.24.3. | Assert with an informative message |
| 6.24.4. | Compile 'assert' |
| 6.24.5. | A Program with Assertions |
| 6.24.6. | Enabling Assertions from the Command Line: -ea and -da enable and disable assertion in a package subtree or in a class. |
| 6.24.7. | Handling an Assertion Error |
| 6.24.8. | Catch assert exception with message |
| 6.24.9. | Using the class loader to enable assertions |
