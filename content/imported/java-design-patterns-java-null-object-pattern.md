---
title: Java Design Patterns Tutorial - Java Design Pattern - Null Object Pattern
nav: Java Design Patterns Tutor...
description: In Null Object pattern, a business-meaningless object is created incase of null object.
section: Imported - java2s Archive
order: 50131
source: https://www.java2s.com/Tutorials/Java/Java_Design_Patterns/0220__Java_Null_Object_Pattern.html
---
```java title=Example.java
```

In Null Object pattern, a business-meaningless object is created incase of null object.

We use the business-meaningless object to replace the null pointer check.

We call the a business-meaningless object Null Object.

Null object provides default behaviour when data is not available.

In Null Object pattern, we usually create an abstract class to specify the various operations.

Both Null Object and concreate classes will extends this abstract class.

The Null Object class just provide empty logic.

## Example

```java title=Example.java
abstractclass AbstractEmployee {
   protected String name;
   publicabstractboolean isNull();
   publicabstract String getName();
}class Programmer extends AbstractEmployee {
   public Programmer(String name) {
      this.name = name;
   }
   @Override
   public String getName() {
      return name;
   }
   @Override
   publicboolean isNull() {
      return false;
   }
}
class NullCustomer extends AbstractEmployee {
   @Override
   public String getName() {
      return"Not Available";
   }
   @Override
   publicboolean isNull() {
      return true;
   }
}
class EmployeeFactory {
   publicstaticfinal String[] names = {"Rob", "Joe", "Jack"};
   publicstatic AbstractEmployee getCustomer(String name){
      for (int i = 0; i < names.length; i++) {
         if (names[i].equalsIgnoreCase(name)){
            returnnew Programmer(name);
         }
      }
      returnnew NullCustomer();
   }
}
publicclass Main {
   publicstaticvoid main(String[] args) {
      AbstractEmployee emp = EmployeeFactory.getCustomer("Rob");
      AbstractEmployee emp2 = EmployeeFactory.getCustomer("Bob");
      AbstractEmployee emp3 = EmployeeFactory.getCustomer("Jack");
      AbstractEmployee emp4 = EmployeeFactory.getCustomer("Tom");
      System.out.println(emp.getName());
      System.out.println(emp2.getName());
      System.out.println(emp3.getName());
      System.out.println(emp4.getName());
   }
}
```

The code above generates the following result.

- « Previous
