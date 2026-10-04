---
title: Constructor Argument And Local Reference
nav: Constructor Argument And L...
description: import org.springframework.context.support.ClassPathXmlApplicationContext;
section: Imported - java2s Archive
order: 1052
source: https://web.archive.org/web/20100211001952/http://java2s.com/Code/Java/Spring/ConstructorArgumentAndLocalReference.htm
---
Constructor Argument And Local Reference

```java title=Example.java
File: context.xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE beans PUBLIC "-//SPRING//DTD BEAN//EN"
    "http://www.springframework.org/dtd/spring-beans.dtd">
<beans>
  <bean id="RangeService" class="RangeServiceImpl">
    <constructor-arg>
      <ref local="RangeDao"/>
    </constructor-arg>
  </bean>
  <bean id="RangeDao" class="StaticDataRangeDaoImpl">
  </bean>
</beans>
File: Main.java
import java.util.Date;
import java.util.GregorianCalendar;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;
class Main {
  public static void main(String args[]) throws Exception {
    ApplicationContext ctx = new ClassPathXmlApplicationContext("context.xml");
    RangeService ws = (RangeService) ctx.getBean("RangeService");
    Double high = ws.getHistoricalHigh(new GregorianCalendar(2004, 0, 1).getTime());
    System.out.println("High was: " + high);
  }
}
interface RangeService {
  Double getHistoricalHigh(Date date);
}
class RangeServiceImpl implements RangeService {
  RangeDao RangeDao;
  public RangeServiceImpl(RangeDao RangeDao) {
    this.RangeDao = RangeDao;
  }
  public Double getHistoricalHigh(Date date) {
    RangeData wd = RangeDao.find(date);
    if (wd != null)
      return new Double(wd.getHigh());
    return null;
  }
}
class RangeData {
  Date date;
  double low;
  double high;
  public Date getDate() {
    return date;
  }
  public void setDate(Date date) {
    this.date = date;
  }
  public double getLow() {
    return low;
  }
  public void setLow(double low) {
    this.low = low;
  }
  public double getHigh() {
    return high;
  }
  public void setHigh(double high) {
    this.high = high;
  }
}
interface RangeDao {
  RangeData find(Date date);
  RangeData save(Date date);
  RangeData update(Date date);
}
class StaticDataRangeDaoImpl implements RangeDao {
  public RangeData find(Date date) {
    RangeData wd = new RangeData();
    wd.setDate((Date) date.clone());
    wd.setLow(5);
    wd.setHigh(15);
    return wd;
  }
  public RangeData save(Date date) {
   return null;
  }
  public RangeData update(Date date) {
    return null;
  }
}
```

Spring-ConstructorArgumentAndLocalReference.zip( 2,896 k)
1.  Call Constructor
2.  Constructor Confusion Demo
3.  ConstructorCaller In ContextConfig
4.  SingletonScope And PrototypeScope
