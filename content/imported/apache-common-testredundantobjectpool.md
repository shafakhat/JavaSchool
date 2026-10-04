---
title: Test Redundant Object Pool
nav: Test Redundant Object Pool
description: System.err.println("Number of employees in pool: " + pool.getNumIdle());
section: Imported - java2s Archive
order: 1092
source: https://web.archive.org/web/20140829221211/http://www.java2s.com/Code/Java/Apache-Common/TestRedundantObjectPool.htm
---
```java title=Example.java
import java.util.HashMap;
import org.apache.commons.pool.impl.SoftReferenceObjectPool;
public class TestRedundantObjectPool {
  public static void main(String args[]) throws Exception {
    SoftReferenceObjectPool pool =
      new SoftReferenceObjectPool(new EmployeeFactory(), 5);
    try{
      System.err.println("Number of employees in pool: " + pool.getNumIdle());
      Employee employee = (Employee)pool.borrowObject();
      System.err.println("Borrowed Employee: " + employee);
      employee.doWork();
      pool.returnObject(employee);
      // employee = null;
      HashMap map = new HashMap();
      System.err.println("Running memory intensive operation");
      for(int i = 0; i < 1000000; i++) {
        map.put(new Integer(i), new String("Fred Flintstone" + i));
      }
    }catch(OutOfMemoryError e) {
      System.err.println("Borrowed employee after OutOfMemory: " +
        pool.borrowObject());
      System.err.println("Error: "  + e);
    }
  }
}
----------------------------
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
---------------------------------
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
---------------------------------------
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
--------------------------------
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
```

TestRedundantObjectPool.zip( 1,219 k)
1.  Keyed Object Pool
2.  Test Object Pool
3.  Soft Reference Object Pool Demo
