---
title: Handling an Assertion Error
nav: Handling an Assertion Error
description: Imported from the java2s.com archive: Handling an Assertion Error
section: Imported - java2s Archive
order: 1804
source: https://web.archive.org/web/20140829082550/http://www.java2s.com/Tutorial/Java/0120__Development/HandlinganAssertionError.htm
---
```java title=Example.java
public class Main {
  public static void main(String[] argv) throws Exception {
    try {
      assert argv.length > 0;
    } catch (AssertionError e) {
      String message = e.getMessage();
      System.out.println(message);
    }
  }
}
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
