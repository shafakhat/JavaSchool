---
title: EJB Tutorial from JBoss
nav: EJB Tutorial from JBoss
description: EJB Tutorial from JBoss: stateless session bean deployment descriptor : Stateless Session Bean « EJB3 « Java
section: Imported - java2s Archive
order: 1042
source: https://web.archive.org/web/20090503180143/http://www.java2s.com:80/Code/Java/EJB3/EJBTutorialfromJBossstatelesssessionbeandeploymentdescriptor.htm
---
EJB Tutorial from JBoss: stateless session bean deployment descriptor : Stateless Session Bean « EJB3 « Java
EJB Tutorial from JBoss: stateless session bean deployment descriptor

```java title=Example.java
File: ejb-jar.xml
<?xml version="1.0" encoding="UTF-8"?>
<ejb-jar
        xmlns="http://java.sun.com/xml/ns/javaee"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:schemaLocation="http://java.sun.com/xml/ns/javaee
                            http://java.sun.com/xml/ns/javaee/ejb-jar_3_0.xsd"
        version="3.0">
   <description>JBoss Stateless Session Bean Tutorial</description>
   <display-name>JBoss Stateless Session Bean Tutorial</display-name>
   <enterprise-beans>
      <session>
         <ejb-name>Calculator</ejb-name>
         <remote>org.jboss.tutorial.stateless_deployment_descriptor.bean.CalculatorRemote</remote>
         <local>org.jboss.tutorial.stateless_deployment_descriptor.bean.CalculatorLocal</local>
         <ejb-class>org.jboss.tutorial.stateless_deployment_descriptor.bean.CalculatorBean</ejb-class>
         <session-type>Stateless</session-type>
         <transaction-type>Container</transaction-type>
      </session>
   </enterprise-beans>
</ejb-jar>
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
         <ejb-name>Calculator</ejb-name>
         <jndi-name>org.jboss.tutorial.stateless_deployment_descriptor.bean.CalculatorRemote</jndi-name>
         <local-jndi-name>org.jboss.tutorial.stateless_deployment_descriptor.bean.CalculatorLocal</local-jndi-name>
      </session>
   </enterprise-beans>
</jboss>
```

jboss-EJB-3.0_RC9_Patch_1.zip( 10,289 k)
1.  Throw Exception Out of Ejb Method
2.  Stateless Session Bean With Three Methods
3.  Use EJB To Mark EJB
4.  Use Stateless Session Bean To PersistEntity
5.  Use Stateless Annotation To Change Ejb Name
6.  EJB Tutorial from JBoss: stateless session bean
7.  One Stateless Session Bean Call Another Stateless Bean
8.  Mark One Method With Two Lifecycle Annotations
9.  EJB Method With Interceptors
