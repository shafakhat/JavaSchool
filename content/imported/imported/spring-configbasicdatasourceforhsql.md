---
title: Config BasicDataSource for HSQL
nav: Config BasicDataSource for...
description: <bean id="dataSource" class="org.apache.commons.dbcp.BasicDataSource">
section: Imported - java2s Archive
order: 1051
source: https://web.archive.org/web/20090327131055/http://www.java2s.com:80/Code/Java/Spring/ConfigBasicDataSourceforHSQL.htm
---
```java title=Example.java
File: context.xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE beans PUBLIC "-//SPRING//DTD BEAN//EN"
    "http://www.springframework.org/dtd/spring-beans.dtd">
<beans>
  <bean id="matchDao"
        class="JdbcMatchDao">
    <property name="dataSource" ref="dataSource"/>
  </bean>
  <bean id="dataSource" class="org.apache.commons.dbcp.BasicDataSource">
    <property name="driverClassName" value="org.hsqldb.jdbcDriver"/>
    <property name="url" value="jdbc:hsqldb:hsql:/localhost/test"/>
    <property name="username" value="sa"/>
    <property name="password" value=""/>
    <property name="initialSize" value="10"/>
    <property name="testOnBorrow" value="true"/>
  </bean>
</beans>
File: Main.java
import org.springframework.beans.factory.config.ConfigurableListableBeanFactory;
import org.springframework.beans.factory.xml.XmlBeanFactory;
import org.springframework.core.io.ClassPathResource;
public class Main {
  public static void main(String[] args) throws Exception {
    ConfigurableListableBeanFactory beanFactory = new XmlBeanFactory(new ClassPathResource(
        "context.xml"));
  }
}
```

Spring-ConfigBasicDataSource.zip( 2,598 k)
1.  Load Two DataSources
2.  Set up DataSource for Oracle
3.  Set up DataSource for MySQL
4.  Set up DataSource for HSQL
5.  JdbcOdbc driver DataSource
