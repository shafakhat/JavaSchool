---
title: Alias Bean Demo
nav: Alias Bean Demo
description: http://www.springframework.org/schema/beans/spring-beans.xsd">
section: Imported - java2s Archive
order: 1006
source: https://web.archive.org/web/20090307144311/http://www.java2s.com:80/Code/Java/Spring/AliasBeanDemo.htm
---
```java title=Example.java
File: context.xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="
                http://www.springframework.org/schema/beans
                http://www.springframework.org/schema/beans/spring-beans.xsd">
    <bean id="name1" name="name2,name3,name4" class="java.lang.String"/>
    <alias name="name1" alias="namex1"/>
    <alias name="name1" alias="namex2"/>
</beans>
File: Main.java
import org.springframework.beans.factory.BeanFactory;
import org.springframework.beans.factory.xml.XmlBeanFactory;
import org.springframework.core.io.ClassPathResource;
public class Main {
  public static void main(String[] a) {
    BeanFactory factory = new XmlBeanFactory(new ClassPathResource("context.xml"));
    String s1 = (String) factory.getBean("name1");
    String s2 = (String) factory.getBean("name2");
    String s3 = (String) factory.getBean("name3");
    String s4 = (String) factory.getBean("name4");
    String s5 = (String) factory.getBean("namex1");
    String s6 = (String) factory.getBean("namex2");
    System.out.println((s1 == s2));
    System.out.println((s2 == s3));
    System.out.println((s3 == s4));
    System.out.println((s4 == s5));
    System.out.println((s5 == s6));
  }
}
```

Spring-AliasBeanDemo.zip( 2,598 k)
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
20.  Bean Lifecycle Initializing
21.  Bean Lifecycle DisposableBean
22.  Autowiring
