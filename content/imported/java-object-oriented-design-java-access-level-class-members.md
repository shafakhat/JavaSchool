---
title: Java Object Oriented Design - Java Access Level Class Members
nav: Java Object Oriented Desig...
description: The access level for a class member determines what area of the program can access it. One of the following four access level modifiers can be used for a class member:
section: Imported - java2s Archive
order: 1013
source: https://web.archive.org/web/2016/https://www.java2s.com/Tutorials/Java/Java_Object_Oriented_Design/0090__Java_Access_Level_Class_Members.html
---
A class can be public or default (or package level).

The access level for a class member determines what area of the program can access it. One of the following four access level modifiers can be used for a class member:

- public
- private
- protected
- Default or package-level access

The first three types of access levels are specified using one of the three keywords: public, private, or protected.

The fourth type is called the default access level (or package-level), and it is specified by using no access modifiers.

If a class member is declared as public using the public keyword, it can be accessed from anywhere in Java code, if the class itself is accessible.

If a class member is declared as private using the private keyword, it can be accessed only within the body of the declaring class, and nowhere else.

If a class member is declared as protected using the protected keyword, it can be accessed from the same package or from descendants of the class, even if the descendants are in a different package.

If we do not use any access level modifier for a class member, it has package-level access. A class member with a package-level access can be accessed from the same package.

Access levels for a class member can be listed from the most restrictive to the least restrictive as private, package-level, protected, and public.

## Example

The following code shows how to use different access levels:

```java title=Example.java
public class Main {
  private int num1; // private access level
 int num2; // package-level access
 protected int num3; // protected access level
 public int num4; // public access level
public static int count = 1; // public access level
 // private access level
 private void m1() {
  }
  // package-level access
 void m2() {
  }
  // protected access level
 protected void m3() {
  }
  // public access level
 public void m4() {
  }
  // private access level
 private static void doSometing() {
  }
}
```

## Note

Access levels can be specified for both instance and static members of a class.

It is a convention to specify the access level modifier as the first modifier in the declaration.

To declare a static public field, use the public modifier first, and then the static modifier, as a convention.

We must consider the access level of both the class and its member to determine whether a class member is accessible.

The following code shows how to use access level modifiers when creating a Java bean.

```java title=Example.java
class Account { private double balance;
  public double getBalance() {
    return this.balance;
  }
  public int save(double amount) {
    if (amount < 0.0 || Double.isNaN(amount) || Double.isInfinite(amount)) {
      System.out.println("Invalid credit amount:  " + amount);
      return -1;
    }
    this.balance = this.balance + amount;
    return 1;
  }
  public int spend(double amount) {
    if (amount < 0.0 || Double.isNaN(amount) || Double.isInfinite(amount)) {
      System.out.println("Invalid debit amount:  " + amount);
      return -1;
    }
    if (this.balance < amount) {
      System.out.println("Insufficient  fund. Debit   attempted: " + amount);
      return -1;
    }
    this.balance = this.balance - amount;
    return 1;
  }
}
public class Main {
  public static void main(String[] args) {
    Account ac = new Account();
    double balance = ac.getBalance();
    System.out.println("Balance = " + balance);
    ac.save(2);
    ac.spend(1);
    balance = ac.getBalance();
    System.out.println("Balance = " + balance);
    // Attempt to credit and debit invalid amounts
    ac.save(-2);
    ac.spend(Double.POSITIVE_INFINITY);
    balance = ac.getBalance();
    System.out.println("Balance = " + balance);
    // Attempt to debit more than the balance
    ac.spend(200.00);
    balance = ac.getBalance();
    System.out.println("Balance = " + balance);
  }
}
```

The code above generates the following result.

- « Previous
