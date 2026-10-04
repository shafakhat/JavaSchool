---
title: CallableStatement Callback And Procedure
nav: CallableStatement Callback...
description: xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans-2.0.xsd
section: Imported - java2s Archive
order: 1034
source: https://web.archive.org/web/20090208172717/http://java2s.com:80/Code/Java/Spring/CallableStatementCallbackAndProcedure.htm
---
CallableStatement Callback And Procedure

```java title=Example.java
File: context.xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:util="http://www.springframework.org/schema/util"
       xmlns:tx="http://www.springframework.org/schema/tx"
       xmlns:aop="http://www.springframework.org/schema/aop"
       xmlns:lang="http://www.springframework.org/schema/lang"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans-2.0.xsd
                           http://www.springframework.org/schema/util http://www.springframework.org/schema/util/spring-util-2.0.xsd
                           http://www.springframework.org/schema/tx http://www.springframework.org/schema/tx/spring-tx-2.0.xsd
                           http://www.springframework.org/schema/aop http://www.springframework.org/schema/aop/spring-aop-2.0.xsd
                           http://www.springframework.org/schema/lang http://www.springframework.org/schema/lang/spring-lang-2.0.xsd">
<!--
    <bean id="dataSource" class="org.apache.commons.dbcp.BasicDataSource" destroy-method="close">
        <property name="driverClassName" value="oracle.jdbc.driver.OracleDriver"/>
        <property name="url" value="jdbc:oracle:thin:@oracle.devcake.co.uk:1521:INTL"/>
        <property name="username" value="sa"/>
        <property name="password" value=""/>
    </bean>
-->
    <bean id="dataSource" class="org.apache.commons.dbcp.BasicDataSource" destroy-method="close">
    <property name="driverClassName" value="org.hsqldb.jdbcDriver"/>
    <property name="url" value="jdbc:hsqldb:mem:."/>
    <property name="username" value="sa"/>
    <property name="password" value=""/>
    </bean>
<!--
    <bean id="mysqlDataSource" class="org.apache.commons.dbcp.BasicDataSource" destroy-method="close">
        <property name="driverClassName" value="com.mysql.jdbc.Driver"/>
        <property name="url" value="jdbc:mysql://dbhost-prospring-psql/prospring"/>
        <property name="username" value="sa"/>
        <property name="password" value=""/>
    </bean>
-->
    <bean id="lobHandler" class="org.springframework.jdbc.support.lob.OracleLobHandler">
        <property name="nativeJdbcExtractor" ref="nativeJdbcExtractor"/>
    </bean>
    <bean id="nativeJdbcExtractor" class="org.springframework.jdbc.support.nativejdbc.CommonsDbcpNativeJdbcExtractor"/>
    <bean id="jdbcTemplate" class="org.springframework.jdbc.core.JdbcTemplate">
        <property name="dataSource" ref="dataSource"/>
    </bean>
</beans>
File: Main.java
import java.sql.CallableStatement;
import java.sql.SQLException;
import javax.sql.DataSource;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;
import org.springframework.dao.DataAccessException;
import org.springframework.jdbc.core.CallableStatementCallback;
import org.springframework.jdbc.core.JdbcTemplate;
class Main {
  public static void main(String args[]) throws Exception {
    ApplicationContext ac = new ClassPathXmlApplicationContext("context.xml", Main.class);
    DataSource dataSource = (DataSource) ac.getBean("dataSource");
    // DataSource mysqlDataSource = (DataSource) ac.getBean("mysqlDataSource");
    JdbcTemplate jdbcTemplate = new JdbcTemplate(dataSource);
    jdbcTemplate.execute("{call p_proc(42)}", new CallableStatementCallback() {
      public Object doInCallableStatement(CallableStatement callableStatement) throws SQLException,
          DataAccessException {
        callableStatement.execute();
        return null;
      }
    });
  }
}
```

Spring-CallableStatementCallbackAndProcedure.zip( 3,655 k)
