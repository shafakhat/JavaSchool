---
title: Console output with format
nav: Console output with format
description: public static void main(String[] args) throws ClassNotFoundException, SQLException {
section: Imported - java2s Archive
order: 1939
source: https://web.archive.org/web/20140829074836/http://www.java2s.com/Tutorial/Java/0120__Development/Consoleoutputwithformat.htm
---
```java title=Example.java
import java.io.Console;
import java.sql.SQLException;
public class MainClass {
  public static void main(String[] args) throws ClassNotFoundException, SQLException {
    Console console = System.console();
    if (console == null) {
      System.err.println("sales: unable to obtain console");
      return;
    }
    console.printf("%s ", "string");
  }
}
```

| 6.40.1. | Java Console readLine |
|---|---|
| 6.40.2. | Console read Password |
| 6.40.3. | Console output with format |
| 6.40.4. | Password Prompting with java.io.Console |
