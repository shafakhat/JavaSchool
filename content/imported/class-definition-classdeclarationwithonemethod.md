---
title: Class declaration with one method
nav: Class declaration with one...
description: Imported from the java2s.com archive: Class declaration with one method
section: Imported - java2s Archive
order: 1007
source: https://web.archive.org/web/20070716084112/http://www.java2s.com:80/Tutorial/Java/0100__Class-Definition/Classdeclarationwithonemethod.htm
---
```java title=Example.java
public class MainClass
{
   public static void main( String args[] )
   {
      GradeBook myGradeBook = new GradeBook();
      myGradeBook.displayMessage();
   }
}
class GradeBook
{
   public void displayMessage()
   {
      System.out.println( "Welcome to the Grade Book!" );
   }
}
```

```java title=Example.java

Welcome to the Grade Book!
```
