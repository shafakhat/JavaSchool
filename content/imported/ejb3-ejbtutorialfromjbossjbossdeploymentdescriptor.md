---
title: EJB Tutorial from JBoss
nav: EJB Tutorial from JBoss
description: <description>JBoss Stateful Session Bean Tutorial</description>
section: Imported - java2s Archive
order: 1025
source: https://web.archive.org/web/20090203095512/http://www.java2s.com:80/Code/Java/EJB3/EJBTutorialfromJBossJBossdeploymentdescriptor.htm
---
EJB Tutorial from JBoss: JBoss deployment descriptor

```java title=Example.java
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
         <remote>org.jboss.tutorial.jboss_deployment_descriptor.bean.ShoppingCart</remote>
         <ejb-class>org.jboss.tutorial.jboss_deployment_descriptor.bean.ShoppingCartBean</ejb-class>
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
   <assembly-descriptor>
        <method-permission>
            <role-name>shopper</role-name>
            <method>
                <ejb-name>ShoppingCart</ejb-name>
                <method-name>buy</method-name>
            </method>
        </method-permission>
        <method-permission>
            <role-name>clerk</role-name>
            <method>
                <ejb-name>ShoppingCart</ejb-name>
                <method-name>priceCheck</method-name>
            </method>
        </method-permission>
   </assembly-descriptor>
</ejb-jar>
File: jaas-test-config.xml
<?xml version='1.0'?>
<!DOCTYPE policy PUBLIC
      "-//JBoss//DTD JBOSS Security Config 3.0//EN"
      "http://www.jboss.org/j2ee/dtd/security_config.dtd">
<policy>
    <application-policy name = "tutorial-test">
       <authentication>
          <login-module code = "org.jboss.security.auth.spi.UsersRolesLoginModule"
             flag = "required">
             <module-option name="usersProperties">security/users1.properties</module-option>
             <module-option name="rolesProperties">security/roles1.properties</module-option>
          </login-module>
       </authentication>
    </application-policy>
   <application-policy name = "tutorial-default">
      <authentication>
         <login-module code = "org.jboss.security.auth.spi.UsersRolesLoginModule"
            flag = "required">
            <module-option name="usersProperties">security/users2.properties</module-option>
            <module-option name="rolesProperties">security/roles2.properties</module-option>
         </login-module>
      </authentication>
   </application-policy>
</policy>
File: jboss.xml
<?xml version="1.0"?>
<jboss
        xmlns="http://java.sun.com/xml/ns/javaee"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:schemaLocation="http://java.sun.com/xml/ns/javaee
                            http://www.jboss.org/j2ee/schema/jboss_5_0.xsd"
        version="3.0">
    <security-domain>tutorial-default</security-domain>
  <enterprise-beans>
      <session>
           <ejb-name>ShoppingCart</ejb-name>
           <jndi-name>ShoppingCart</jndi-name>
           <clustered>true</clustered>
          <cluster-config>
              <partition-name>DefaultPartition</partition-name>
              <load-balance-policy>org.jboss.ha.framework.interfaces.RandomRobin</load-balance-policy>
           </cluster-config>
           <security-domain>tutorial-test</security-domain>
        </session>
        <session>
           <ejb-name>StatelessTest</ejb-name>
           <jndi-name>StatelessTest</jndi-name>
        </session>
     </enterprise-beans>
</jboss>
File: jboss-service.xml
<?xml version="1.0" encoding="UTF-8"?>
<server>
   <!-- The custom JAAS login configuration service that installs
       a Configuration capable of dynamically updating the
       config settings
   -->
   <mbean code="org.jboss.security.auth.login.DynamicLoginConfig"
         name="jboss.tutorial:service=DynamicLoginConfig">
      <attribute name="AuthConfig">META-INF/jaas-test-config.xml</attribute>
      <depends optional-attribute-name="LoginConfigService">
         jboss.security:service=XMLLoginConfig
      </depends>
      <depends optional-attribute-name="SecurityManagerService">
         jboss.security:service=JaasSecurityManager
      </depends>
   </mbean>
</server>
File: application.xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE application PUBLIC
   "-//Sun Microsystems, Inc.//DTD J2EE Application 1.3//EN"
   "http://java.sun.com/dtd/application_1_3.dtd">
<application>
   <display-name>Tutorial</display-name>
   <module>
      <ejb>tutorial.jar</ejb>
   </module>
</application>
```

jboss-EJB-3.0_RC9_Patch_1.zip( 10,289 k)
1.  Use JBoss Remote Binding
2.  Use JBoss Enterprise Beans Session Config
3.  EJB Tutorial from JBoss: Deployment descriptor
4.  EJB Tutorial from JBoss: service deployment descriptor
5.  Entry Point In ejb-jar.xml
