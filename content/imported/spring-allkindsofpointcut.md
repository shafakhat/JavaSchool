---
title: All Kinds Of Pointcut
nav: All Kinds Of Pointcut
description: <bean id="transactionManager" class="NoopTransactionManager"/>
section: Imported - java2s Archive
order: 1007
source: https://web.archive.org/web/20090608151341/http://www.java2s.com:80/Code/Java/Spring/AllKindsOfPointcut.htm
---
All Kinds Of Pointcut

```java title=Example.java
File: context.xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:tx="http://www.springframework.org/schema/tx"
       xmlns:aop="http://www.springframework.org/schema/aop"
       xsi:schemaLocation="
            http://www.springframework.org/schema/beans
            http://www.springframework.org/schema/beans/spring-beans.xsd
            http://www.springframework.org/schema/aop
            http://www.springframework.org/schema/aop/spring-aop.xsd
            http://www.springframework.org/schema/tx
            http://www.springframework.org/schema/tx/spring-tx.xsd">
    <bean id="test" class="bean.TestBean2">
        <property name="simpleBean" ref="simple"/>
    </bean>
    <bean id="simple" class="bean.SimpleBean"/>
    <aop:config>
        <aop:advisor advice-ref="tx-advice"
                     pointcut="SystemPointcuts.testBeanExecution()"/>
    </aop:config>
    <bean id="transactionManager" class="NoopTransactionManager"/>
    <tx:advice id="tx-advice" transaction-manager="transactionManager">
        <tx:attributes>
            <tx:method name="*" propagation="REQUIRED"/>
        </tx:attributes>
    </tx:advice>
</beans>
File: Main.java
import org.aspectj.lang.annotation.Pointcut;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;
import org.springframework.transaction.TransactionDefinition;
import org.springframework.transaction.TransactionException;
import org.springframework.transaction.support.AbstractPlatformTransactionManager;
import org.springframework.transaction.support.DefaultTransactionStatus;
import bean.SimpleBean;
import bean.TestBean2;
public class Main {
  public static void main(String[] args) {
    ApplicationContext ac = new ClassPathXmlApplicationContext("context.xml");
    TestBean2 testBean = (TestBean2) ac.getBean("test");
    SimpleBean simpleBean = (SimpleBean) ac.getBean("simple");
    testBean.work();
    testBean.stop();
    simpleBean.sayHello();
    simpleBean.x("a", "b");
  }
}
final class SystemPointcuts {
  private SystemPointcuts() {
  }
  @Pointcut("execution(* bean..*.*(..)) &&" +
          "!execution(* bean..*.set*(..)) &&" +
          "!execution(* bean..*.get*())")
  public void serviceExecution() { }
  @Pointcut("within(bean.TestBean2)")
  public void within1() { }
  @Pointcut("execution(* bean.TestBean2.*(..))")
  public void testBeanExecution() { }
  @Pointcut("execution(* bean.TestBean2.*(..))")
  private void testBeanExec() { }
  @Pointcut("execution(* bean..*.*(..))")
  public void inProsringPackage() { }
  @Pointcut("within(bean..*)")
  private void withinProSpringPackage() { }
  @Pointcut("execution(* bean.TestBean2.*(..)) &&" +
          "within(bean..*)")
  public void same1() { }
  @Pointcut("execution(* bean.TestBean2.*(..)) &&" +
          "withinProSpringPackage()")
  public void same2() { }
  @Pointcut("testBeanExec() && withinProSpringPackage()")
  public void same3() { }
  @Pointcut("within(bean.TestBean2)")
  public void fromTestBeanExecution() { }
  @Pointcut("this(bean.SimpleBean)")
  public void onlyFromSimpleBean() { }
  @Pointcut("target(bean.SimpleBean)")
  public void onlyToSimpleBean() { }
  @Pointcut("args(String, String)")
  public void onlyTwoStringArguments() { }
//  @Pointcut("bean(test)")
  public void beanName() { }
}
class NoopTransactionManager extends AbstractPlatformTransactionManager {
  protected Object doGetTransaction() throws TransactionException {
      return new Object();
  }
  protected void doBegin(Object object, TransactionDefinition transactionDefinition) throws TransactionException {
      System.out.println("Begin");
  }
  protected void doCommit(DefaultTransactionStatus defaultTransactionStatus) throws TransactionException {
      System.out.println("Commit");
  }
  protected void doRollback(DefaultTransactionStatus defaultTransactionStatus) throws TransactionException {
      System.out.println("Rollback");
  }
}
```

Spring-AllKindsOfPointcut.zip( 4,652 k)
1.  Use NameMatchMethodPointcutAdvisor
2.  Use NameMatchMethodPointcut
