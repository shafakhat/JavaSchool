---
title: Class with a constructor to initialize instance variables
nav: Class with a constructor t...
description: Account account1 = new Account( 50.00 ); // create Account object
section: Imported - java2s Archive
order: 1195
source: https://web.archive.org/web/20140829084917/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/Classwithaconstructortoinitializeinstancevariables.htm
---
```java title=Example.java
public class MainClass
{
   public static void main( String args[] )
   {
      Account account1 = new Account( 50.00 ); // create Account object
      Account account2 = new Account( -7.53 ); // create Account object
      System.out.printf( "account1 balance: $%.2f\n", account1.getBalance() );
      System.out.printf( "account2 balance: $%.2f\n\n", account2.getBalance() );
      double depositAmount; // deposit amount read from user
      depositAmount = 10.10;
      account1.credit( depositAmount ); // add to account1 balance
      System.out.printf( "account1 balance: $%.2f\n", account1.getBalance() );
      System.out.printf( "account2 balance: $%.2f\n\n", account2.getBalance() );
      depositAmount = 12.12;
      account2.credit( depositAmount ); // add to account2 balance
      System.out.printf( "account1 balance: $%.2f\n", account1.getBalance() );
      System.out.printf( "account2 balance: $%.2f\n", account2.getBalance() );
   }
}
class Account
{
   private double balance; // instance variable that stores the balance
   // constructor
   public Account( double initialBalance )
   {
      if ( initialBalance > 0.0 )
         balance = initialBalance;
   }
   public void credit( double amount )
   {
      balance = balance + amount;
   }
   public double getBalance()
   {
      return balance;
   }
}
java title=Example.java
account1 balance: $50.00
account2 balance: $0.00
account1 balance: $60.10
account2 balance: $0.00
account1 balance: $60.10
account2 balance: $12.12
```
