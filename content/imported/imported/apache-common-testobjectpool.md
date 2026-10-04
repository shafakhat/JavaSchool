---
title: Test Object Pool
nav: Test Object Pool
description: System.err.println("Number of employees in pool: " + pool.getNumIdle());
section: Imported - java2s Archive
order: 1068
source: https://web.archive.org/web/20061016093854/http://www.java2s.com/Code/Java/Apache-Common/TestObjectPool.htm
---
```java title=Example.java
import org.apache.commons.pool.impl.GenericObjectPool;
public class TestObjectPool {
  public static void main(String args[]) throws Exception {
    GenericObjectPool pool = new GenericObjectPool();
    pool.setFactory(new EmployeeFactory());
    /*First way of initializing pool
    pool.setMinIdle(5);
    pool.setTimeBetweenEvictionRunsMillis(500);
    Thread.currentThread().sleep(600);*/
    /* second, and preferred way */
    for(int i = 0; i < 5; ++i) {
      pool.addObject();
    }
    // pool.setTestOnReturn(true);
    pool.setMinEvictableIdleTimeMillis(1000);
    pool.setTimeBetweenEvictionRunsMillis(600);
    System.err.println("Number of employees in pool: " + pool.getNumIdle());
        Thread.currentThread().sleep(1500);
    Employee employee = (Employee)pool.borrowObject();
    employee.setName("Fred Flintstone");
    employee.doWork();
    System.err.println("Employee: "  + employee);
    pool.returnObject(employee);
        System.err.println("Number of employees in pool: " + pool.getNumIdle());
  }
}
--------------------------------------------
public class Employee {
  private static int base = 0;
  private int id;
  private String name;
  public Employee() {
    this.id = base++;
  }
  public int getId() {
    return this.id;
  }
  public String getName() {
    return this.name;
  }
  public void setName(String name) {
    this.name = name;
  }
  public void doWork() {
    // does nothing
  }
  public String toString() {
    return ("Id: " + this.id + ", Name: " + this.name);
  }
  public void finalize() {
    System.err.println("Employee " + toString() + " made redundant");
  }
}
-----------------------------
import org.apache.commons.pool.BasePoolableObjectFactory;
public class EmployeeFactory extends BasePoolableObjectFactory {
  public Object makeObject() {
    return new Employee();
  }
  public boolean validateObject(Object obj) {
    if(obj instanceof Employee) {
      if(((Employee)obj).getName() == null)
        return true;
    }
    return false;
  }
  public void passivateObject(Object obj) throws Exception {
    if(obj instanceof Employee) {
      ((Employee)obj).setName(null);
    } else throw new Exception("Unknown object");
  }
}
---------------------------------------------
import org.apache.commons.pool.BaseKeyedPoolableObjectFactory;
public class SkilledEmployeeFactory extends BaseKeyedPoolableObjectFactory {
  public Object makeObject(Object key) {
    if(key == null || !(key instanceof String) || ((String)key).length() == 0)
      throw new IllegalArgumentException("Invalid key specified");
    return new SkilledEmployee(key.toString());
  }
  /*public boolean validateObject(Object key, Object obj) {
    if(obj instanceof Employee) {
      if(((Employee)obj).getName() == null)
        return true;
    }
    return false;
  }
  public void passivateObject(Object obj) throws Exception {
    if(obj instanceof Employee) {
      ((Employee)obj).setName(null);
    } else throw new Exception("Unknown object");
  }*/
}
-------------------------------------
public class SkilledEmployee extends Employee {
  private String skill;
  public SkilledEmployee(String skill) {
    this.skill = skill;
  }
  public String getSkill() {
    return this.skill;
  }
  public String toString() {
    return getSkill() + " -- " + getName();
  }
}
```

Download: TestObjectPool.zip ( 1,218 K )
---
Related examples in the same category
1. Keyed Object Pool
3. Soft Reference Object Pool Demo
