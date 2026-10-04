---
title: EJB Tutorial from JBoss
nav: EJB Tutorial from JBoss
description: * Copyright 2006, Red Hat Middleware LLC, and individual contributors
section: Imported - java2s Archive
order: 1021
source: https://web.archive.org/web/20090126210758/http://www.java2s.com:80/Code/Java/EJB3/EJBTutorialfromJBossentitysecurity.htm
---
EJB Tutorial from JBoss: entity security

```java title=Example.java
File: AllEntity.java
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
package org.jboss.tutorial.entity.security.bean;
import java.io.Serializable;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
@Entity
public class AllEntity implements Serializable
{
   @Id @GeneratedValue(strategy=GenerationType.AUTO)
   public int id;
   public String val;
}
File: SomeEntity.java
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
package org.jboss.tutorial.entity.security.bean;
import java.io.Serializable;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
@Entity
public class SomeEntity implements Serializable
{
   @Id @GeneratedValue(strategy=GenerationType.AUTO)
   public int id;
   public String val;
}
File: StarEntity.java
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
package org.jboss.tutorial.entity.security.bean;
import java.io.Serializable;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
@Entity
public class StarEntity  implements Serializable
{
   @Id @GeneratedValue(strategy=GenerationType.AUTO)
   public int id;
   public String val;
}
File: Stateless.java
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
package org.jboss.tutorial.entity.security.bean;
import org.jboss.tutorial.entity.security.bean.AllEntity;
import org.jboss.tutorial.entity.security.bean.SomeEntity;
import org.jboss.tutorial.entity.security.bean.StarEntity;
/**
 *
 * @author <a href="mailto:kabir.khan@jboss.org">Kabir Khan</a>
 * @version $Revision: 57207 $
 */
public interface Stateless
{
   int unchecked(int i);
   int checked(int i);
   AllEntity insertAllEntity();
   AllEntity readAllEntity(int key);
   void updateAllEntity(AllEntity e);
   void deleteAllEntity(AllEntity e);
   StarEntity insertStarEntity();
   StarEntity readStarEntity(int key);
   void updateStarEntity(StarEntity e);
   void deleteStarEntity(StarEntity e);
   SomeEntity insertSomeEntity();
   SomeEntity readSomeEntity(int key);
   void updateSomeEntity(SomeEntity e);
   void deleteSomeEntity(SomeEntity e);
}
File: StatelessBean.java
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
package org.jboss.tutorial.entity.security.bean;
import javax.annotation.security.RolesAllowed;
import javax.annotation.security.PermitAll;
import javax.ejb.Remote;
import javax.persistence.EntityManager;
import javax.persistence.PersistenceContext;
import org.jboss.annotation.security.SecurityDomain;
import org.jboss.annotation.ejb.AspectDomain;
import org.jboss.tutorial.entity.security.bean.AllEntity;
import org.jboss.tutorial.entity.security.bean.SomeEntity;
import org.jboss.tutorial.entity.security.bean.StarEntity;
import org.jboss.tutorial.entity.security.bean.Stateless;
/**
 *
 * @author <a href="mailto:kabir.khan@jboss.org">Kabir Khan</a>
 * @version $Revision: 57207 $
 */
@javax.ejb.Stateless
@Remote (Stateless.class)
@SecurityDomain ("other")
@AspectDomain("JACC Stateless Bean")
public class StatelessBean implements Stateless
{
   @PersistenceContext
   EntityManager em;
   @PermitAll
   public int unchecked(int i)
   {
      System.out.println("stateless unchecked");
      return i;
   }
   @RolesAllowed ("allowed")
   public int checked(int i)
   {
      System.out.println("stateless checked");
      return i;
   }
   @PermitAll
   public AllEntity insertAllEntity()
   {
      AllEntity e = new AllEntity();
      e.val = "x";
      em.persist(e);
      return e;
   }
   @PermitAll
   public AllEntity readAllEntity(int key)
   {
      AllEntity e = em.find(AllEntity.class, key);
      return e;
   }
   @PermitAll
   public void updateAllEntity(AllEntity e)
   {
      em.merge(e);
   }
   @PermitAll
   public void deleteAllEntity(AllEntity e)
   {
      em.remove(em.find(AllEntity.class, e.id));
   }
   @PermitAll
   public StarEntity insertStarEntity()
   {
      StarEntity e = new StarEntity();
      e.val = "x";
      em.persist(e);
      return e;
   }
   @PermitAll
   public StarEntity readStarEntity(int key)
   {
      StarEntity e = em.find(StarEntity.class, key);
      return e;
   }
   @PermitAll
   public void updateStarEntity(StarEntity e)
   {
      em.merge(e);
   }
   @PermitAll
   public void deleteStarEntity(StarEntity e)
   {
      em.remove(em.find(StarEntity.class, e.id));
   }
   @PermitAll
   public SomeEntity insertSomeEntity()
   {
      SomeEntity e = new SomeEntity();
      e.val = "x";
      em.persist(e);
      return e;
   }
   @PermitAll
   public SomeEntity readSomeEntity(int key)
   {
      SomeEntity e = em.find(SomeEntity.class, key);
      return e;
   }
   @PermitAll
   public void updateSomeEntity(SomeEntity e)
   {
      em.merge(e);
   }
   @PermitAll
   public void deleteSomeEntity(SomeEntity e)
   {
      em.remove(em.find(SomeEntity.class, e.id));
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
package org.jboss.tutorial.entity.security.client;
import org.jboss.tutorial.entity.security.bean.AllEntity;
import org.jboss.tutorial.entity.security.bean.SomeEntity;
import org.jboss.tutorial.entity.security.bean.StarEntity;
import org.jboss.tutorial.entity.security.bean.Stateless;
import org.jboss.security.SecurityAssociation;
import org.jboss.security.SimplePrincipal;
import javax.naming.Context;
import javax.naming.InitialContext;
import java.util.Properties;
/**
 *
 * @author <a href="mailto:kabir.khan@jboss.org">Kabir Khan</a>
 * @version $Revision: 57207 $
 */
public class Client
{
   public static void main(String[] args) throws Exception
   {
      testAllEntity();
      testSomeEntity();
      testStarEntity();
   }
   public static InitialContext getInitialContext(String username, String password) throws Exception
   {
      Properties env = new Properties();
      env.setProperty(Context.SECURITY_PRINCIPAL, username);
      env.setProperty(Context.SECURITY_CREDENTIALS, password);
      env.setProperty(Context.INITIAL_CONTEXT_FACTORY, "org.jboss.security.jndi.JndiLoginInitialContextFactory");
      return new InitialContext(env);
   }
   public static void testAllEntity()throws Exception
   {
      InitialContext ctx = getInitialContext("somebody", "password");
      Stateless stateless = (Stateless)ctx.lookup("StatelessBean/remote");
      System.out.println("Good role");
      System.out.println("Inserting...");
      AllEntity e = stateless.insertAllEntity();
      System.out.println("Reading...");
      e = stateless.readAllEntity(e.id);
      e.val += "y";
      System.out.println("Updating...");
      stateless.updateAllEntity(e);
      System.out.println("Deleting...");
      stateless.deleteAllEntity(e);
      System.out.println("Inserting...");
      e = stateless.insertAllEntity();
      System.out.println("Bad role");
      getInitialContext("rolefail", "password");
      AllEntity ae2 = null;
      try
      {
         System.out.println("Inserting...");
         ae2 = stateless.insertAllEntity();
         throw new RuntimeException("security exception should have been thrown!");
      }
      catch(Exception ex)
      {
         System.out.println("Expected failure: " + ex.getMessage());
      }
      try
      {
         System.out.println("Reading...");
         ae2 = stateless.readAllEntity(e.id);
         throw new RuntimeException("security exception should have been thrown!");
      }
      catch(Exception ex)
      {
         System.out.println("Expected failure: " + ex.getMessage());
      }
      try
      {
         e.val += "y";
         stateless.updateAllEntity(e);
         throw new RuntimeException("security exception should have been thrown!");
      }
      catch(Exception ex)
      {
         System.out.println("Expected failure: " + ex.getMessage());
      }
      try
      {
         stateless.deleteAllEntity(e);
         throw new RuntimeException("security exception should have been thrown!");
      }
      catch(Exception ex)
      {
         System.out.println("Expected failure: " + ex.getMessage());
      }
      try
      {
         e = stateless.insertAllEntity();
         throw new RuntimeException("security exception should have been thrown!");
      }
      catch(Exception ex)
      {
         System.out.println("Expected failure: " + ex.getMessage());
      }
   }
   public static void testStarEntity()throws Exception
   {
      InitialContext ctx = getInitialContext("somebody", "password");
      Stateless stateless = (Stateless)ctx.lookup("StatelessBean/remote");
      System.out.println("Good role");
      System.out.println("Inserting...");
      StarEntity e = stateless.insertStarEntity();
      System.out.println("Reading...");
      e = stateless.readStarEntity(e.id);
      e.val += "y";
      System.out.println("Updating...");
      stateless.updateStarEntity(e);
      System.out.println("Deleting...");
      stateless.deleteStarEntity(e);
      System.out.println("Inserting...");
      e = stateless.insertStarEntity();
      System.out.println("Bad role");
      getInitialContext("rolefail", "password");
      StarEntity ae2 = null;
      try
      {
         System.out.println("Inserting...");
         ae2 = stateless.insertStarEntity();
         throw new RuntimeException("security exception should have been thrown!");
      }
      catch(Exception ex)
      {
         System.out.println("Expected failure: " + ex.getMessage());
      }
      try
      {
         System.out.println("Reading...");
         ae2 = stateless.readStarEntity(e.id);
         throw new RuntimeException("security exception should have been thrown!");
      }
      catch(Exception ex)
      {
         System.out.println("Expected failure: " + ex.getMessage());
      }
      try
      {
         e.val += "y";
         stateless.updateStarEntity(e);
         throw new RuntimeException("security exception should have been thrown!");
      }
      catch(Exception ex)
      {
         System.out.println("Expected failure: " + ex.getMessage());
      }
      try
      {
         stateless.deleteStarEntity(e);
         throw new RuntimeException("security exception should have been thrown!");
      }
      catch(Exception ex)
      {
         System.out.println("Expected failure: " + ex.getMessage());
      }
      try
      {
         e = stateless.insertStarEntity();
         throw new RuntimeException("security exception should have been thrown!");
      }
      catch(Exception ex)
      {
         System.out.println("Expected failure: " + ex.getMessage());
      }
   }
   public static void testSomeEntity()throws Exception
   {
      InitialContext ctx = getInitialContext("somebody", "password");
      Stateless stateless = (Stateless)ctx.lookup("StatelessBean/remote");
      System.out.println("Good role");
      System.out.println("Inserting...");
      SomeEntity e = stateless.insertSomeEntity();
      try
      {
         System.out.println("Reading...");
         e = stateless.readSomeEntity(e.id);
         throw new RuntimeException("security exception should have been thrown!");
      }
      catch(Exception ex)
      {
         System.out.println("Expected failure: " + ex.getMessage());
      }
      try
      {
         e.val += "y";
         System.out.println("Updating...");
         stateless.updateSomeEntity(e);
         throw new RuntimeException("security exception should have been thrown!");
      }
      catch(Exception ex)
      {
         System.out.println("Expected failure: " + ex.getMessage());
      }
      System.out.println("Inserting...");
      e = stateless.insertSomeEntity();
      System.out.println("Bad role");
      getInitialContext("rolefail", "password");
      SomeEntity ae2 = null;
      try
      {
         System.out.println("Inserting...");
         ae2 = stateless.insertSomeEntity();
         throw new RuntimeException("security exception should have been thrown!");
      }
      catch(Exception ex)
      {
         System.out.println("Expected failure: " + ex.getMessage());
      }
      try
      {
         stateless.deleteSomeEntity(e);
         throw new RuntimeException("security exception should have been thrown!");
      }
      catch(Exception ex)
      {
         System.out.println("Expected failure: " + ex.getMessage());
      }
      try
      {
         e = stateless.insertSomeEntity();
         throw new RuntimeException("security exception should have been thrown!");
      }
      catch(Exception ex)
      {
         System.out.println("Expected failure: " + ex.getMessage());
      }
   }
}
File: roles.properties
rolefail=willfail
somebody=allowed
File: users.properties
somebody=password
rolefail=password
```

jboss-EJB-3.0_RC9_Patch_1.zip( 10,289 k)
1.  Setup security-domain For JBoss
2.  EJB Tutorial from JBoss: ejb security
3.  EJB Tutorial from JBoss: ssl service
4.  User Properties And Role Properties
5.  security stateless ear
6.  ssl jaxws
