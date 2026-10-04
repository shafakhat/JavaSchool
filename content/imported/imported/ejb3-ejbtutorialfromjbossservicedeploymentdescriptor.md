---
title: EJB Tutorial from JBoss
nav: EJB Tutorial from JBoss
description: <ejb-class>org.jboss.tutorial.service_deployment_descriptor.bean.ServiceOne</ejb-class>
section: Imported - java2s Archive
order: 1035
source: https://web.archive.org/web/20090203095517/http://www.java2s.com:80/Code/Java/EJB3/EJBTutorialfromJBossservicedeploymentdescriptor.htm
---
EJB Tutorial from JBoss: service deployment descriptor

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
      <service>
       <ejb-name>ServiceOne</ejb-name>
         <ejb-class>org.jboss.tutorial.service_deployment_descriptor.bean.ServiceOne</ejb-class>
         <local>org.jboss.tutorial.service_deployment_descriptor.bean.ServiceOneLocal</local>
         <remote>org.jboss.tutorial.service_deployment_descriptor.bean.ServiceOneRemote</remote>
         <management>org.jboss.tutorial.service_deployment_descriptor.bean.ServiceOneManagement</management>
         <jndi-name>serviceOne/remote</jndi-name>
         <local-jndi-name>serviceOne/local</local-jndi-name>
      </service>
      <service>
     <ejb-name>ServiceTwo</ejb-name>
         <ejb-class>org.jboss.tutorial.service_deployment_descriptor.bean.ServiceTwo</ejb-class>
       <object-name>tutorial:service=serviceTwo</object-name>
         <management>org.jboss.tutorial.service_deployment_descriptor.bean.ServiceTwoManagement</management>
      </service>
      <service>
     <ejb-name>ServiceThree</ejb-name>
         <ejb-class>org.jboss.tutorial.service_deployment_descriptor.bean.ServiceThree</ejb-class>
         <management>org.jboss.tutorial.service_deployment_descriptor.bean.ServiceThreeManagement</management>
      </service>
   </enterprise-beans>
</jboss>
File: jboss-service.xml
<?xml version="1.0" encoding="UTF-8"?>
<server>
   <mbean code="org.jboss.ejb3.test.service.Tester" name="jboss.ejb3:service=Tester,test=service"/>
</server>
```

jboss-EJB-3.0_RC9_Patch_1.zip( 10,289 k)
1.  Use JBoss Remote Binding
2.  Use JBoss Enterprise Beans Session Config
3.  EJB Tutorial from JBoss: Deployment descriptor
4.  EJB Tutorial from JBoss: JBoss deployment descriptor
5.  Entry Point In ejb-jar.xml
