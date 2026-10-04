---
title: Class that contains a String instance variable and methods to set and get its value
nav: Class that contains a Stri...
description: System.out.printf( "Initial course name is: %s\n\n",myGradeBook.getCourseName() );
section: Imported - java2s Archive
order: 1008
source: https://web.archive.org/web/20070613001439/http://www.java2s.com:80/Tutorial/Java/0100__Class-Definition/ClassthatcontainsaStringinstancevariableandmethodstosetandgetitsvalue.htm
---
```java title=Example.java
public class MainClass
{
   public static void main( String args[] )
   {
      GradeBook myGradeBook = new GradeBook();
      System.out.printf( "Initial course name is: %s\n\n",myGradeBook.getCourseName() );
      String theName = "Java";
      myGradeBook.setCourseName( theName ); // set the course name
      myGradeBook.displayMessage();
   }
}
class GradeBook
{
   private String courseName; // course name for this GradeBook
   // method to set the course name
   public void setCourseName( String name )
   {
      courseName = name; // store the course name
   }
   // method to retrieve the course name
   public String getCourseName()
   {
      return courseName;
   }
   // display a welcome message to the GradeBook user
   public void displayMessage()
   {
      System.out.printf( "Welcome to the grade book for\n%s!\n",
         getCourseName() );
   }
}
```

```java title=Example.java

Initial course name is: null

Welcome to the grade book for
Java!
```
