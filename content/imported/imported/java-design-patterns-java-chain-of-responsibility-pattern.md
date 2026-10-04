---
title: Java Design Patterns Tutorial - Java Design Pattern - Chain of Responsibility Pattern
nav: Java Design Patterns Tutor...
description: The chain of responsibility pattern creates a list of receiver objects for a request.
section: Imported - java2s Archive
order: 50124
source: https://www.java2s.com/Tutorials/Java/Java_Design_Patterns/0140__Java_Chain_of_Responsibility_Pattern.html
---
```java title=Example.java
« Previous
```

- Next »

The chain of responsibility pattern creates a list of receiver objects for a request.

This pattern is behavioral patterns.

When using chain of responsibility pattern, normally each receiver contains reference to another receiver.

If one object cannot handle the request then it passes the same to the next receiver and so on.

## Example

```java title=Example.java
abstractclass Logger {
   protected Logger nextLogger;
//fromwww.java2s.compublicvoid setNextLogger(Logger nextLogger){
      this.nextLogger = nextLogger;
   }
   publicvoid logMessage(String message){
      log(message);
      if(nextLogger !=null){
         nextLogger.logMessage(message);
      }
   }
   abstractprotectedvoid log(String message);
}
class ConsoleLogger extends Logger {
   public ConsoleLogger(){
   }
   @Override
   protectedvoid log(String message) {
      System.out.println("Console::Logger: " + message);
   }
}
class EMailLogger extends Logger {
   public EMailLogger(){
   }
   @Override
   protectedvoid log(String message) {
      System.out.println("EMail::Logger: " + message);
   }
}
class FileLogger extends Logger {
   public FileLogger(){
   }
   @Override
   protectedvoid log(String message) {
      System.out.println("File::Logger: " + message);
   }
}
publicclass Main {
   privatestatic Logger getChainOfLoggers(){
      Logger emailLogger = new EMailLogger();
      Logger fileLogger = new FileLogger();
      Logger consoleLogger = new ConsoleLogger();
      emailLogger.setNextLogger(fileLogger);
      fileLogger.setNextLogger(consoleLogger);
      return emailLogger;
   }
   publicstaticvoid main(String[] args) {
      Logger loggerChain = getChainOfLoggers();
      loggerChain.logMessage("Null pointer");
      loggerChain.logMessage("Array Index Out of Bound");
      loggerChain.logMessage("Illegal Parameters");
   }
}
```

The code above generates the following result.

- Next »
- « Previous
