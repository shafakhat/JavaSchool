---
title: EJB Tutorial from JBoss
nav: EJB Tutorial from JBoss
description: * Copyright 2006, Red Hat Middleware LLC, and individual contributors
section: Imported - java2s Archive
order: 1029
source: https://web.archive.org/web/20090801104303/http://www.java2s.com:80/Code/Java/EJB3/EJBTutorialfromJBossmergeentityback.htm
---
EJB Tutorial from JBoss: merge entity back

```java title=Example.java
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
package org.jboss.tutorial.merge.bean;
import java.util.List;
public interface CustomerDAO
{
   int create(String first, String last, String street, String city, String state, String zip);
   Customer find(int id);
   List findByLastName(String name);
   void merge(Customer c);
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
package org.jboss.tutorial.merge.bean;
import java.util.List;
import javax.ejb.Remote;
import javax.ejb.Stateless;
import javax.persistence.EntityManager;
import javax.persistence.PersistenceContext;
@Stateless
@Remote(CustomerDAO.class)
public class CustomerDAOBean implements CustomerDAO
{
   @PersistenceContext
   private EntityManager manager;
   public int create(String first, String last, String street, String city, String state, String zip)
   {
      Customer customer = new Customer(first, last, street, city, state, zip);
      manager.persist(customer);
      return customer.getId();
   }
   public Customer find(int id)
   {
      return manager.find(Customer.class, id);
   }
   public List findByLastName(String name)
   {
      return manager.createQuery("select c from Customer c where c.last = :name").setParameter("name", name).getResultList();
   }
   public void merge(Customer c)
   {
      manager.merge(c);
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
package org.jboss.tutorial.merge.bean;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue; import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.Table;
import javax.persistence.Table;
import javax.persistence.Column;
import javax.persistence.Id;
@Entity
@Table(name = "CUSTOMER")
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
package org.jboss.tutorial.merge.client;
import org.jboss.tutorial.merge.bean.Customer;
import org.jboss.tutorial.merge.bean.CustomerDAO;
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
   }
}
```

jboss-EJB-3.0_RC9_Patch_1.zip( 10,289 k)
1.  Entity With Transient Fields
