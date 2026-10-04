---
title: Class declaration with a method that has a parameter
nav: Class declaration with a m...
description: Imported from the java2s.com archive: Class declaration with a method that has a parameter
section: Imported - java2s Archive
order: 1006
source: https://web.archive.org/web/20070612203809/http://www.java2s.com:80/Tutorial/Java/0100__Class-Definition/Classdeclarationwithamethodthathasaparameter.htm
---
```java title=Example.java
public class MainClass
{
   public static void main( String args[] )
   {
      GradeBook myGradeBook = new GradeBook();
      String courseName = "Java ";
      myGradeBook.displayMessage( courseName );
   }
}
class GradeBook
{
   public void displayMessage( String courseName )
   {
      System.out.printf( "Welcome to the grade book for\n%s!\n",
         courseName );
   }
}
java title=Example.java
Welcome to the grade book for
Java !
```
