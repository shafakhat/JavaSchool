---
title: EJB Tutorial from JBoss
nav: EJB Tutorial from JBoss
description: EJB Tutorial from JBoss: stateful session bean deployment descriptor
section: Imported - java2s Archive
order: 1040
source: https://web.archive.org/web/20090129104613/http://www.java2s.com:80/Code/Java/EJB3/EJBTutorialfromJBossstatefulsessionbeandeploymentdescriptor.htm
---
EJB Tutorial from JBoss: stateful session bean deployment descriptor

```java title=Example.java
File: jboss.xml
<?xml version="1.0"?>
<jboss
        xmlns="http://java.sun.com/xml/ns/javaee"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:schemaLocation="http://java.sun.com/xml/ns/javaee
                            http://www.jboss.org/j2ee/schema/jboss_5_0.xsd"
        version="3.0">
   <enterprise-beans>
      <session>
         <ejb-name>ShoppingCart</ejb-name>
         <jndi-name>org.jboss.tutorial.stateful_deployment_descriptor.bean.ShoppingCart</jndi-name>
      </session>
   </enterprise-beans>
</jboss>
File: ejb-jar.xml
<?xml version="1.0" encoding="UTF-8"?>
<ejb-jar
        xmlns="http://java.sun.com/xml/ns/javaee"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:schemaLocation="http://java.sun.com/xml/ns/javaee
                            http://java.sun.com/xml/ns/javaee/ejb-jar_3_0.xsd"
        version="3.0">
   <description>JBoss Stateful Session Bean Tutorial</description>
   <display-name>JBoss Stateful Session Bean Tutorial</display-name>
   <enterprise-beans>
      <session>
         <ejb-name>ShoppingCart</ejb-name>
         <remote>org.jboss.tutorial.stateful_deployment_descriptor.bean.ShoppingCart</remote>
         <ejb-class>org.jboss.tutorial.stateful_deployment_descriptor.bean.ShoppingCartBean</ejb-class>
         <session-type>Stateful</session-type>
         <remove-method>
            <bean-method>
               <method-name>checkout</method-name>
            </bean-method>
            <retain-if-exception>false</retain-if-exception>
         </remove-method>
         <transaction-type>Container</transaction-type>
      </session>
   </enterprise-beans>
</ejb-jar>
```

jboss-EJB-3.0_RC9_Patch_1.zip( 10,289 k)
1.  Stateful Session Bean Lifecycle: PrePassivate
2.  Stateful Session Bean Lifecycle: PreDestroy
3.  Stateful Session Bean Lifecycle: PostConstruct
4.  Stateful Session Bean Lifecycle: PostActivate
5.  Stateful Session Bean And Shopping Cart
6.  Stateful Session Bean And Entity Manager
7.  Use Lifecycle Method To Manage Collection In Stateful Session Bean
8.  EJB Tutorial from JBoss: stateful session bean
9.  Remove a Stateful Session Bean
10.  Remove Annotation
11.  Ejb With Generic Method
