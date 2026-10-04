---
title: Bean Lifecycle Initializing
nav: Bean Lifecycle Initializing
description: http://www.springframework.org/schema/beans/spring-beans.xsd">
section: Imported - java2s Archive
order: 1031
source: https://web.archive.org/web/20090420180109/http://www.java2s.com:80/Code/Java/Spring/BeanLifecycleInitializing.htm
---
Bean Lifecycle Initializing

```java title=Example.java
File: context.xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="
                http://www.springframework.org/schema/beans
                http://www.springframework.org/schema/beans/spring-beans.xsd">
    <bean id="simple1" class="SoutSimpleBean">
        <property name="person" value="A"/>
        <property name="value" value="my value"/>
    </bean>
</beans>
File: Main.java
import org.springframework.beans.factory.InitializingBean;
import org.springframework.beans.factory.xml.XmlBeanFactory;
import org.springframework.core.io.ClassPathResource;
public class Main {
  public static void main(String[] args) throws Exception {
    XmlBeanFactory factory = new XmlBeanFactory(new ClassPathResource("context.xml"));
    System.out.println(factory.getBean("simple1"));
  }
}
class SoutSimpleBean extends SimpleBeanSupport {
  private String person;
  public void setPerson(String person) {
    this.person = person;
  }
  @Override
  public String toString() {
    return String.format("%s : \"%s\"", this.person, getValue());
  }
}
abstract class SimpleBeanSupport implements InitializingBean {
  private String value;
  public final void afterPropertiesSet() throws Exception {
  }
  public final void setValue(String value) {
    this.value = value;
  }
  protected final String getValue() {
    return this.value;
  }
}
```

Spring-BeanLiftCycleInitializing.zip( 2,599 k)
1.  XML Bean Injection
2.  Reference another bean and set property
3.  Static Factory
4.  Serach By Base Package
5.  throw RequiredPropertyNotSetException
6.  Properties File Based Spring Bean
7.  Non Static Factory
8.  Local Reference
9.  Link With DataSource
10.  Inheritance Demo
11.  HierarchicalBeanFactory Demo
12.  Filtered By Annotatoin
13.  destroy method
14.  dependency check Demo
15.  Custom InitializationMethod
16.  component scan
17.  Component Scan and scope
18.  Component Filter Assignable
19.  implements BeanNameAware
20.  Bean Lifecycle DisposableBean
21.  Autowiring
22.  Alias Bean Demo
