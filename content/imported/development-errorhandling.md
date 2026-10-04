---
title: Error Handling
nav: Error Handling
description: You can isolate code that may cause a runtime error using the try statement. try statement normally is accompanied by the catch and the finally statements. In case of an
section: Imported - java2s Archive
order: 1771
source: https://web.archive.org/web/20140829080035/http://www.java2s.com/Tutorial/Java/0120__Development/ErrorHandling.htm
---
You can isolate code that may cause a runtime error using the try statement. try statement normally is accompanied by the catch and the finally statements. In case of an error, Java stops the processing of the try block and jump to the catch block. In the catch block, you can handle the error or notify the user by 'throwing' a java.lang.Exception object. Or you can re-throw the exception or a new Exception object back to the code that called the method. If a thrown exception is not caught, the application will stop abruptly. In the finally block, you write code that will be run whether or not an error has occurred. The finally block is optional. You can have more than one catch block. This is because the code can throw different types of exceptions. If the type of exception thrown does not match the exception type in the first catch block, the JVM goes to the next catch block and does the same thing until it finds a match. If no match is found, the exception object will be thrown to the method caller. If the caller does not put the offending code that calls the method in a try block, the program crashes.
This is the syntax of the try statement.

```java title=Example.java
try {
         [code that may throw an exception]
     } catch (ExceptionType-1 e) {
         [code that is executed when ExceptionType-1 is thrown]
     } [catch (ExceptionType-2 e) {
         [code that is executed when ExceptionType-2 is thrown]
     }]
       ...
     } [catch (ExceptionType-n e) {
         [code that is executed when ExceptionType-n is thrown]
     }]
     [finally {
         [code that runs regardless of whether an exception was thrown]]
     }]
```

| 6.23.1. | Error Handling |
|---|---|
| 6.23.2. | Types of Exceptions |
| 6.23.3. | Java's Unchecked RuntimeException Subclasses |
| 6.23.4. | Java's Checked Exceptions Defined in java.lang |
| 6.23.5. | Throwing an Exception from a Method |
| 6.23.6. | Write a catch block that handles java.lang.Exception |
| 6.23.7. | Handling Exceptions |
| 6.23.8. | Multiple catch Blocks |
| 6.23.9. | The finally Block |
| 6.23.10. | Exception Objects: stack trace |
| 6.23.11. | Defining Your Own Exceptions, Throwing Your Own Exception |
| 6.23.12. | Demonstrate exception chaining. |
| 6.23.13. | Getting the Stack Trace of an Exception |
| 6.23.14. | Put printStackTrace() into a String: redirect the StackTrace to a String with a StringWriter/PrintWriter |
| 6.23.15. | Check whether given exception is compatible with the exceptions declared in a throws clause |
| 6.23.16. | Convert an exception to a String with full stack trace |
| 6.23.17. | Get Deepest Throwable |
| 6.23.18. | Get the stack trace of the supplied exception. |
| 6.23.19. | Is Checked Exception |
| 6.23.20. | Locates a particular type of exception |
| 6.23.21. | Make a string representation of the exception |
| 6.23.22. | Print all of the thread's information and stack traces |
| 6.23.23. | Return stack trace from the passed exception as a string |
| 6.23.24. | Returns the root cause of an exception |
| 6.23.25. | Create a new Exception, setting the cause if possible. |
| 6.23.26. | Returns the output of printStackTrace as a String. |
| 6.23.27. | This program creates a custom exception type. |
| 6.23.28. | Utility methods for dealing with stack traces |
