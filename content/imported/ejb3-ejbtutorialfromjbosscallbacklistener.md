---
title: EJB Tutorial from JBoss
nav: EJB Tutorial from JBoss
description: * Copyright 2006, Red Hat Middleware LLC, and individual contributors
section: Imported - java2s Archive
order: 1012
source: https://web.archive.org/web/20090202195314/http://www.java2s.com:80/Code/Java/EJB3/EJBTutorialfromJBossCallbackListener.htm
---
EJB Tutorial from JBoss: Callback Listener

```java title=Example.java
File: CustomerCallbackListener.java
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
package org.jboss.tutorial.callback.bean;
import javax.persistence.PreRemove;
import javax.persistence.PostRemove;
import javax.persistence.PreUpdate;
import javax.persistence.PostUpdate;
import javax.persistence.PostLoad;
import javax.persistence.PrePersist;
import javax.persistence.PostPersist;
/**
 * @author <a href="mailto:kabir.khan@jboss.org">Kabir Khan</a>
 * @version $Revision: 57207 $
 */
public class CustomerCallbackListener
{
   @PrePersist
   public void doPrePersist(Customer customer)
   {
      System.out.println("doPrePersist: About to create Customer: " + customer.getFirst() + " " + customer.getLast());
   }
   @PostPersist
   public void doPostPersist(Object customer)
   {
      System.out.println("doPostPersist: Created Customer: " + ((Customer)customer).getFirst() + " " + ((Customer)customer).getLast());
   }
   @PreRemove
   public void doPreRemove(Customer customer)
   {
      System.out.println("doPreRemove: About to delete Customer: " + customer.getFirst() + " " + customer.getLast());
   }
   @PostRemove
   public void doPostRemove(Customer customer)
   {
      System.out.println("doPostRemove: Deleted Customer: " + customer.getFirst() + " " + customer.getLast());
   }
   @PreUpdate
   public void doPreUpdate(Customer customer)
   {
      System.out.println("doPreUpdate: About to update Customer: " + customer.getFirst() + " " + customer.getLast());
   }
   @PostUpdate
   public void doPostUpdate(Customer customer)
   {
      System.out.println("doPostUpdate: Updated Customer: " + customer.getFirst() + " " + customer.getLast());
   }
   @PostLoad
   public void doPostLoad(Customer customer)
   {
      System.out.println("doPostLoad: Loaded Customer: " + customer.getFirst() + " " + customer.getLast());
   }
}
File: CustomerDAO.java
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
package org.jboss.tutorial.callback.bean;
import java.util.List;
public interface CustomerDAO
{
   int create(String first, String last, String street, String city, String state, String zip);
   Customer find(int id);
   List findByLastName(String name);
   void merge(Customer c);
   void delete(List l);
}
File: CustomerDAOBean.java
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
package org.jboss.tutorial.callback.bean;
import java.util.Iterator;
import java.util.List;
import javax.interceptor.Interceptors;
import javax.annotation.PostConstruct;
import javax.annotation.PreDestroy;
import javax.ejb.Remote;
import javax.ejb.Stateless;
import javax.persistence.EntityManager;
import javax.persistence.PersistenceContext;
@Stateless
@Remote(CustomerDAO.class)
@Interceptors({LifecycleInterceptor.class})
public class CustomerDAOBean implements CustomerDAO
{
   @PersistenceContext
   private EntityManager manager;
   public int create(String first, String last, String street, String city, String state, String zip)
   {
      System.out.println("-- CustomerDAOBean.create()");
      Customer customer = new Customer(first, last, street, city, state, zip);
      manager.persist(customer);
      return customer.getId();
   }
   public Customer find(int id)
   {
      System.out.println("-- CustomerDAOBean.find()");
      return manager.find(Customer.class, id);
   }
   public List findByLastName(String last)
   {
      System.out.println("-- CustomerDAOBean.findByLastName(id)");
      return manager.createQuery("select c from Customer c where c.last = :last").setParameter("last", last).getResultList();
   }
   public void merge(Customer c)
   {
      System.out.println("-- CustomerDAOBean.merge()");
      manager.merge(c);
   }
   public void delete(List l)
   {
      System.out.println("-- CustomerDAOBean.delete()");
      for (Iterator it = l.iterator() ; it.hasNext() ; )
      {
         Customer c = (Customer)it.next();
         manager.remove(manager.find(Customer.class, c.getId()));
      }
   }
   // Callbacks ----------------------------------------------------------------
   @PostConstruct
   public void postConstructCallback()
   {
      System.out.println("PostConstruct - Have EntityManager: " + (manager != null));
   }
   @PreDestroy
   public void preDestroyCallback()
   {
      System.out.println("PreDestory - Have EntityManager: " + (manager != null));
   }
}
File: LifecycleInterceptor.java
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
package org.jboss.tutorial.callback.bean;
import javax.interceptor.InvocationContext;
import javax.annotation.PostConstruct;
/**
 *
 * @author <a href="kabir.khan@jboss.com">Kabir Khan</a>
 * @version $Revision: 57207 $
 */
public class LifecycleInterceptor
{
   @PostConstruct
   public void postConstruct(InvocationContext ctx)
   {
      try
      {
         System.out.println("LifecycleInterceptor postConstruct");
         ctx.proceed();
      }
      catch(Exception e)
      {
         throw new RuntimeException(e);
      }
   }
}
File: Customer.java
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
package org.jboss.tutorial.callback.bean;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.EntityListeners;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.Table;
@Entity
@Table(name = "CUSTOMER")
@EntityListeners(CustomerCallbackListener.class)
public class Customer implements java.io.Serializable
{
   private int id;
   private String first;
   private String last;
   private String street;
   private String city;
   private String state;
   private String zip;
   public Customer()
   {
   }
   public Customer(String first, String last, String street, String city, String state, String zip)
   {
      this.first = first;
      this.last = last;
      this.street = street;
      this.city = city;
      this.state = state;
      this.zip = zip;
   }
   @Id @GeneratedValue(strategy=GenerationType.AUTO)
   public int getId()
   {
      return id;
   }
   public void setId(int id)
   {
      this.id = id;
   }
   @Column(name = "FIRST")
   public String getFirst()
   {
      return first;
   }
   public void setFirst(String first)
   {
      this.first = first;
   }
   @Column(name = "LAST")
   public String getLast()
   {
      return last;
   }
   public void setLast(String last)
   {
      this.last = last;
   }
   @Column(name = "STREET")
   public String getStreet()
   {
      return street;
   }
   public void setStreet(String street)
   {
      this.street = street;
   }
   @Column(name = "CITY")
   public String getCity()
   {
      return city;
   }
   public void setCity(String city)
   {
      this.city = city;
   }
   @Column(name = "STATE")
   public String getState()
   {
      return state;
   }
   public void setState(String state)
   {
      this.state = state;
   }
   @Column(name = "ZIP")
   public String getZip()
   {
      return zip;
   }
   public void setZip(String zip)
   {
      this.zip = zip;
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
package org.jboss.tutorial.callback.client;
import org.jboss.tutorial.callback.bean.Customer;
import org.jboss.tutorial.callback.bean.CustomerDAO;
import javax.naming.InitialContext;
import java.util.List;
public class Client
{
   public static void main(String[] args) throws Exception
   {
      InitialContext ctx = new InitialContext();
      CustomerDAO dao = (CustomerDAO) ctx.lookup("CustomerDAOBean/remote");
      System.out.println("Create Bill Burke and Monica Smith");
      dao.create("Bill", "Burke", "1 Boston Road", "Boston", "MA", "02115");
      int moId = dao.create("Monica", "Smith", "1 Boston Road", "Boston", "MA", "02115");
      System.out.println("Bill and Monica get married");
      Customer monica = dao.find(moId);
      monica.setLast("Burke");
      dao.merge(monica);
      System.out.println("Get all the Burkes");
      List burkes = dao.findByLastName("Burke");
      System.out.println("There are now " + burkes.size() + " Burkes");
      System.out.println("Bill and Monica are moving abroad");
      dao.delete(burkes);
   }
}
```

jboss-EJB-3.0_RC9_Patch_1.zip( 10,289 k)
1.  Around InvokeMethod
2.  Get Ejb Info From InvocationContext
3.  Get Set Parameters In InvocationContext
4.  Use Interceptors To Check Permission
5.  EJB Tutorial from JBoss: Interceptor
6.  Mark Interceptors For A Remote Method
7.  annotation override interceptor
8.  interceptor stateless
