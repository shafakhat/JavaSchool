---
title: EJB Tutorial from JBoss
nav: EJB Tutorial from JBoss
description: EJB Tutorial from JBoss: message driven bean deployment descriptor
section: Imported - java2s Archive
order: 1031
source: https://web.archive.org/web/20081202015812/http://www.java2s.com:80/Code/Java/EJB3/EJBTutorialfromJBossmessagedrivenbeandeploymentdescriptor.htm
---
EJB Tutorial from JBoss: message driven bean deployment descriptor

```java title=Example.java
File: ejb-jar.xml
<?xml version="1.0" encoding="UTF-8"?>
<ejb-jar
        xmlns="http://java.sun.com/xml/ns/javaee"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:schemaLocation="http://java.sun.com/xml/ns/javaee
                            http://java.sun.com/xml/ns/javaee/ejb-jar_3_0.xsd"
        version="3.0">
   <description>JBoss Message Driven Bean Tutorial</description>
   <display-name>JBoss Message Driven Bean Tutorial</display-name>
   <enterprise-beans>
      <message-driven>
     <ejb-name>ExampleMDB</ejb-name>
     <ejb-class>org.jboss.tutorial.mdb_deployment_descriptor.bean.ExampleMDB</ejb-class>
         <transaction-type>Bean</transaction-type>
         <message-destination-type>javax.jms.Queue</message-destination-type>
       <activation-config>
          <activation-config-property>
            <activation-config-property-name>acknowledgeMode</activation-config-property-name>
            <activation-config-property-value>AUTO_ACKNOWLEDGE</activation-config-property-value>
          </activation-config-property>
        </activation-config>
      </message-driven>
   </enterprise-beans>
</ejb-jar>
File: jboss.xml
<?xml version="1.0" encoding="utf-8"?>
<jboss
        xmlns="http://java.sun.com/xml/ns/javaee"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:schemaLocation="http://java.sun.com/xml/ns/javaee
                            http://www.jboss.org/j2ee/schema/jboss_5_0.xsd"
        version="3.0">
   <enterprise-beans>
      <message-driven>
         <ejb-name>ExampleMDB</ejb-name>
         <destination-jndi-name>queue/tutorial/example</destination-jndi-name>
      </message-driven>
   </enterprise-beans>
</jboss>
```

jboss-EJB-3.0_RC9_Patch_1.zip( 10,289 k)
1.  EJB Tutorial from JBoss: Consumer producer
2.  EJB Tutorial from JBoss: Message driven bean
3.  EJB Tutorial from JBoss: demo for message driven bean
