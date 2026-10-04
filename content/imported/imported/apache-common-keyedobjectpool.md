---
title: Keyed Object Pool
nav: Keyed Object Pool
description: System.err.println("Employee " + toString() + " made redundant");
section: Imported - java2s Archive
order: 1045
source: https://web.archive.org/web/20061016093642/http://www.java2s.com/Code/Java/Apache-Common/KeyedObjectPool.htm
---
```java title=Example.java
import org.apache.commons.pool.impl.GenericKeyedObjectPool;
public class TestKeyedObjectPool {
  public static void main(String args[]) throws Exception {
    GenericKeyedObjectPool pool = new GenericKeyedObjectPool();
    pool.setFactory(new SkilledEmployeeFactory());
    pool.addObject("Java");
    pool.addObject("Java");
    pool.addObject("VB");
    pool.addObject("C++");
    System.err.println("Number of Java employees in pool: " +
      pool.getNumIdle("Java") + " out of total employees: " +
      pool.getNumIdle());
    Employee employee = (Employee)pool.borrowObject("Java");
    employee.doWork();
    System.err.println("Employee: "  + employee);
    pool.returnObject("Java", employee);
    System.err.println("Number of Java employees in pool: " +
      pool.getNumIdle("Java") + " out of total employees: " +
      pool.getNumIdle());
  }
}
---------------------
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
--------------------
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
-------------------------
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

Related examples in the same category
3. Soft Reference Object Pool Demo
