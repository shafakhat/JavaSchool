---
title: Java Design Patterns Tutorial - Java Design Pattern - Filter/Criteria Pattern
nav: Java Design Patterns Tutor...
description: The criteria can be chained together through logical operations.
section: Imported - java2s Archive
order: 50119
source: https://www.java2s.com/Tutorials/Java/Java_Design_Patterns/0080__Java_Filter_Pattern.html
---
```java title=Example.java
« Previous
```

- Next »

Filter pattern filters objects using different criteria.

The criteria can be chained together through logical operations.

Filter pattern is a structural pattern.

## Example

```java title=Example.java
import java.util.List;
import java.util.ArrayList;
//fromwww.java2s.comclass Employee {
  private String name;
  private String gender;
  private String retireStatus;
  public Employee(String name, String gender, String r) {
    this.name = name;
    this.gender = gender;
    this.retireStatus = r;
  }
  public String getName() {
    return name;
  }
  public String getGender() {
    return gender;
  }
  public String getRetireStatus() {
    return retireStatus;
  }
  @Override
  public String toString() {
    return"Employee [name=" + name + ", gender=" + gender
        + ", retireStatus=" + retireStatus + "]";
  }
}
interface Criteria {
  public List<Employee> meetCriteria(List<Employee> persons);
}
class CriteriaMale implements Criteria {
  @Override
  public List<Employee> meetCriteria(List<Employee> persons) {
    List<Employee> malePersons = new ArrayList<Employee>();
    for (Employee person : persons) {
      if (person.getGender().equalsIgnoreCase("MALE")) {
        malePersons.add(person);
      }
    }
    return malePersons;
  }
}
class CriteriaFemale implements Criteria {
  @Override
  public List<Employee> meetCriteria(List<Employee> persons) {
    List<Employee> femalePersons = new ArrayList<Employee>();
    for (Employee person : persons) {
      if (person.getGender().equalsIgnoreCase("FEMALE")) {
        femalePersons.add(person);
      }
    }
    return femalePersons;
  }
}
class CriteriaRetire implements Criteria {
  @Override
  public List<Employee> meetCriteria(List<Employee> persons) {
    List<Employee> singlePersons = new ArrayList<Employee>();
    for (Employee person : persons) {
      if (person.getRetireStatus().equalsIgnoreCase("YES")) {
        singlePersons.add(person);
      }
    }
    return singlePersons;
  }
}
class AndCriteria implements Criteria {
  private Criteria criteria;
  private Criteria otherCriteria;
  public AndCriteria(Criteria criteria, Criteria otherCriteria) {
    this.criteria = criteria;
    this.otherCriteria = otherCriteria;
  }
  @Override
  public List<Employee> meetCriteria(List<Employee> persons) {
    List<Employee> firstCriteriaPersons = criteria.meetCriteria(persons);
    return otherCriteria.meetCriteria(firstCriteriaPersons);
  }
}
class OrCriteria implements Criteria {
  private Criteria criteria;
  private Criteria otherCriteria;
  public OrCriteria(Criteria criteria, Criteria otherCriteria) {
    this.criteria = criteria;
    this.otherCriteria = otherCriteria;
  }
  @Override
  public List<Employee> meetCriteria(List<Employee> persons) {
    List<Employee> firstCriteriaItems = criteria.meetCriteria(persons);
    List<Employee> otherCriteriaItems = otherCriteria.meetCriteria(persons);
    for (Employee person : otherCriteriaItems) {
      if (!firstCriteriaItems.contains(person)) {
        firstCriteriaItems.add(person);
      }
    }
    return firstCriteriaItems;
  }
}
publicclass Main {
  publicstaticvoid main(String[] args) {
    List<Employee> persons = new ArrayList<Employee>();
    persons.add(new Employee("Tom", "Male", "YES"));
    persons.add(new Employee("Jack", "Male", "NO"));
    persons.add(new Employee("Jane", "Female", "NO"));
    persons.add(new Employee("Diana", "Female", "YES"));
    persons.add(new Employee("Mike", "Male", "NO"));
    persons.add(new Employee("Bob", "Male", "YES"));
    Criteria male = new CriteriaMale();
    Criteria female = new CriteriaFemale();
    Criteria retire = new CriteriaRetire();
    Criteria retireMale = new AndCriteria(retire, male);
    Criteria retireOrFemale = new OrCriteria(retire, female);
    System.out.println("Males: ");
    printPersons(male.meetCriteria(persons));
    System.out.println("Females: ");
    printPersons(female.meetCriteria(persons));
    System.out.println("Retire Males: ");
    printPersons(retireMale.meetCriteria(persons));
    System.out.println("Retire Or Females: ");
    printPersons(retireOrFemale.meetCriteria(persons));
  }
  publicstaticvoid printPersons(List<Employee> persons) {
    for (Employee person : persons) {
      System.out.println(person);
    }
  }
}
```

The code above generates the following result.

- Next »
- « Previous
