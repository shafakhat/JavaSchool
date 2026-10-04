---
title: Soft Reference Object Pool Demo
nav: Soft Reference Object Pool...
description: this.pool = new SoftReferenceObjectPool(new PoolableObjectFactory() {
section: Imported - java2s Archive
order: 1055
source: https://web.archive.org/web/20061016093607/http://www.java2s.com/Code/Java/Apache-Common/SoftReferenceObjectPoolDemo.htm
---
```java title=Example.java
import junit.framework.TestCase;
import junit.framework.TestSuite;
import org.apache.commons.pool.PoolableObjectFactory;
import org.apache.commons.pool.impl.SoftReferenceObjectPool;
import java.util.HashMap;
import java.lang.ref.SoftReference;
public class TestSoftRef extends TestCase {
  private SoftReferenceObjectPool pool;
  public static TestSuite suite() {
    return new TestSuite(TestSoftRef.class);
  }
  public static void main(String[] args) {
  String[] testClassName = { TestSoftRef.class.getName() };
    junit.textui.TestRunner.main(testClassName);
  }
  public TestSoftRef(String s) {
    super(s);
  }
public void testOutOfMemory() throws Exception {
  Object obj = pool.borrowObject();
  pool.returnObject(obj);
  obj = null;
  assertEquals(5, pool.getNumIdle());
  try {
    HashMap map = new HashMap();
    for(int i = 0; i < 1000000; i++) {
      map.put(new Integer(i), new String("Fred Flintstone" + i));
    }
  }catch(OutOfMemoryError ex) {
      pool.borrowObject();
      pool.borrowObject();
      pool.borrowObject();
      pool.borrowObject();
      pool.borrowObject();
     // assertEquals(0, pool.getNumIdle());
  }
}
  public void setUp() throws Exception {
    this.pool = new SoftReferenceObjectPool(new PoolableObjectFactory() {
       int counter;
       public Object makeObject()                   { return String.valueOf(counter++); }
       public void destroyObject( Object obj )      {}
       public boolean validateObject( Object obj )  { return true; }
       public void activateObject( Object obj )     {}
       public void passivateObject( Object obj )    {}
    }, 5);
  }
}
-------------------------------------------
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
---------------------------------------
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
----------------------------------
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
-------------------------------------
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

Related examples in the same category
1. Keyed Object Pool
