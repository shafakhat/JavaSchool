---
title: EJB Tutorial from JBoss
nav: EJB Tutorial from JBoss
description: * Copyright 2006, Red Hat Middleware LLC, and individual contributors
section: Imported - java2s Archive
order: 1019
source: https://web.archive.org/web/20090126210752/http://www.java2s.com:80/Code/Java/EJB3/EJBTutorialfromJBossejbsecurity.htm
---
EJB Tutorial from JBoss: ejb security

```java title=Example.java
File: Calculator.java
/*
 * JBoss, Home of Professional Open Source.
 * Copyright 2006, Red Hat Middleware LLC, and individual contributors
 * as indicated by the @author tags. See the copyright.txt file in the
 * distribution for a full listing of individual contributors.
 *
 * This is free software; you can redistribute it and/or modify it
 * under the terms of the GNU Lesser General Public License as
 * published by the Free Software Foundation; either version 2.1 of
 * the License, or (at your option) any later version.
 *
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
 * Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public
 * License along with this software; if not, write to the Free
 * Software Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA
 * 02110-1301 USA, or see the FSF site: http://www.fsf.org.
 */
package org.jboss.tutorial.security.bean;
public interface Calculator
{
   int add(int x, int y);
   int subtract(int x, int y);
   int divide(int x, int y);
}
File: CalculatorBean.java
/*
 * JBoss, Home of Professional Open Source.
 * Copyright 2006, Red Hat Middleware LLC, and individual contributors
 * as indicated by the @author tags. See the copyright.txt file in the
 * distribution for a full listing of individual contributors.
 *
 * This is free software; you can redistribute it and/or modify it
 * under the terms of the GNU Lesser General Public License as
 * published by the Free Software Foundation; either version 2.1 of
 * the License, or (at your option) any later version.
 *
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
 * Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public
 * License along with this software; if not, write to the Free
 * Software Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA
 * 02110-1301 USA, or see the FSF site: http://www.fsf.org.
 */
package org.jboss.tutorial.security.bean;
import javax.annotation.security.RolesAllowed;
import javax.ejb.Stateless;
import javax.ejb.TransactionAttribute;
import javax.ejb.TransactionAttributeType;
import javax.annotation.security.PermitAll;
import javax.annotation.security.RolesAllowed;
import javax.ejb.Remote;
import org.jboss.annotation.security.SecurityDomain;
import org.jboss.annotation.security.SecurityDomain;
@Stateless
@SecurityDomain("other")
@Remote(Calculator.class)
public class CalculatorBean implements Calculator
{
   @PermitAll
   @TransactionAttribute(TransactionAttributeType.REQUIRES_NEW)
   public int add(int x, int y)
   {
      return x + y;
   }
   @RolesAllowed({"student"})
   public int subtract(int x, int y)
   {
      return x - y;
   }
   @RolesAllowed({"teacher"})
   public int divide(int x, int y)
   {
      return x / y;
   }
}
File: Client.java
/*
 * JBoss, Home of Professional Open Source.
 * Copyright 2006, Red Hat Middleware LLC, and individual contributors
 * as indicated by the @author tags. See the copyright.txt file in the
 * distribution for a full listing of individual contributors.
 *
 * This is free software; you can redistribute it and/or modify it
 * under the terms of the GNU Lesser General Public License as
 * published by the Free Software Foundation; either version 2.1 of
 * the License, or (at your option) any later version.
 *
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
 * Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public
 * License along with this software; if not, write to the Free
 * Software Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA
 * 02110-1301 USA, or see the FSF site: http://www.fsf.org.
 */
package org.jboss.tutorial.security.client;
import java.util.Properties;
import javax.ejb.EJBAccessException;
import javax.naming.Context;
import javax.naming.InitialContext;
import org.jboss.tutorial.security.bean.Calculator;
/**
 * @version $Revision: 57207 $
 */
public class Client
{
   public static void main(String[] args) throws Exception
   {
      // Establish the proxy with an incorrect security identity
      Properties env = new Properties();
      env.setProperty(Context.SECURITY_PRINCIPAL, "kabir");
      env.setProperty(Context.SECURITY_CREDENTIALS, "invalidpassword");
      env.setProperty(Context.INITIAL_CONTEXT_FACTORY, "org.jboss.security.jndi.JndiLoginInitialContextFactory");
      InitialContext ctx = new InitialContext(env);
      Calculator calculator = (Calculator) ctx.lookup("CalculatorBean/remote");
      System.out.println("Kabir is a student.");
      System.out.println("Kabir types in the wrong password");
      try
      {
         System.out.println("1 + 1 = " + calculator.add(1, 1));
      }
      catch (EJBAccessException ex)
      {
         System.out.println("Saw expected SecurityException: " + ex.getMessage());
      }
      System.out.println("Kabir types in correct password.");
      System.out.println("Kabir does unchecked addition.");
      // Re-establish the proxy with the correct security identity
      env.setProperty(Context.SECURITY_CREDENTIALS, "validpassword");
      ctx = new InitialContext(env);
      calculator = (Calculator) ctx.lookup("CalculatorBean/remote");
      System.out.println("1 + 1 = " + calculator.add(1, 1));
      System.out.println("Kabir is not a teacher so he cannot do division");
      try
      {
         calculator.divide(16, 4);
      }
      catch (javax.ejb.EJBAccessException  ex)
      {
         System.out.println(ex.getMessage());
      }
      System.out.println("Students are allowed to do subtraction");
      System.out.println("1 - 1 = " + calculator.subtract(1, 1));
   }
}
File: users.properties
kabir=validpassword
```

jboss-EJB-3.0_RC9_Patch_1.zip( 10,289 k)
1.  Setup security-domain For JBoss
2.  EJB Tutorial from JBoss: entity security
3.  EJB Tutorial from JBoss: ssl service
4.  User Properties And Role Properties
5.  security stateless ear
6.  ssl jaxws
