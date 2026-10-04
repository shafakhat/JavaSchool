---
title: Scope class demonstrates field and local variable scopes
nav: Scope class demonstrates f...
description: int x = 25; // initialized each time useLocalVariable is called
section: Imported - java2s Archive
order: 1200
source: https://web.archive.org/web/20140829081346/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/Scopeclassdemonstratesfieldandlocalvariablescopes.htm
---
```java title=Example.java
public class MainClass
{
   public static void main( String args[] )
   {
      Scope testScope = new Scope();
      testScope.begin();
   }
}
class Scope
{
   private int x = 1;
   public void begin()
   {
      int x = 5; // method's local variable x shadows field x
      System.out.printf( "local x in method begin is %d\n", x );
      useLocalVariable();
      useField();
      useLocalVariable();
      useField();
      System.out.printf( "\nlocal x in method begin is %d\n", x );
   }
   public void useLocalVariable()
   {
      int x = 25; // initialized each time useLocalVariable is called
      System.out.printf("\nlocal x on entering method useLocalVariable is %d\n", x );
      ++x; // modifies this method's local variable x
      System.out.printf(
         "local x before exiting method useLocalVariable is %d\n", x );
   }
   // modify class Scope's field x during each call
   public void useField()
   {
      System.out.printf("\nfield x on entering method useField is %d\n", x );
      x *= 10; // modifies class Scope's field x
      System.out.printf("field x before exiting method useField is %d\n", x );
   }
}
java title=Example.java
local x in method begin is 5
local x on entering method useLocalVariable is 25
local x before exiting method useLocalVariable is 26
field x on entering method useField is 1
field x before exiting method useField is 10
local x on entering method useLocalVariable is 25
local x before exiting method useLocalVariable is 26
field x on entering method useField is 10
field x before exiting method useField is 100
local x in method begin is 5
```
