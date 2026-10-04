---
title: EJB Tutorial from JBoss
nav: EJB Tutorial from JBoss
description: * Copyright 2006, Red Hat Middleware LLC, and individual contributors
section: Imported - java2s Archive
order: 1032
source: https://web.archive.org/web/20100401121636/http://www.java2s.com:80/Code/Java/EJB3/EJBTutorialfromJBossPrimaryKeyComposition.htm
---
EJB Tutorial from JBoss: Primary Key Composition

```java title=Example.java
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
package org.jboss.tutorial.composite.bean;
import java.util.Set;
import javax.persistence.CascadeType;
import javax.persistence.EmbeddedId;
import javax.persistence.Entity;
import javax.persistence.FetchType;
import javax.persistence.ManyToMany;
import javax.persistence.Transient;
import javax.persistence.JoinTable;
import javax.persistence.JoinColumn;
/**
 *
 */
@Entity
public class Customer implements java.io.Serializable
{
   CustomerPK pk;
   Set<Flight> flights;
   public Customer()
   {
   }
   @EmbeddedId
   public CustomerPK getPk()
   {
      return pk;
   }
   public void setPk(CustomerPK pk)
   {
      this.pk = pk;
   }
   @Transient
   public String getName()
   {
      return pk.getName();
   }
   @ManyToMany(cascade = {CascadeType.PERSIST, CascadeType.MERGE}, fetch = FetchType.EAGER, mappedBy="customers")
   @JoinTable(name="flight_customer_table",
              joinColumns = {@JoinColumn(name = "FLIGHT_ID")},
              inverseJoinColumns = {@JoinColumn(name = "CUSTOMER_ID"), @JoinColumn(name = "CUSTOMER_NAME")})
   public Set<Flight> getFlights()
   {
      return flights;
   }
   public void setFlights(Set<Flight> flights)
   {
      this.flights = flights;
   }
}
File: CustomerPK.java
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
package org.jboss.tutorial.composite.bean;
import javax.persistence.Embeddable;
import javax.persistence.Embeddable;
/**
 * Comment
 *
 * @author <a href="mailto:bill@jboss.org">Bill Burke</a>
 * @version $Revision: 57207 $
 */
@Embeddable
public class CustomerPK implements java.io.Serializable
{
   private long id;
   private String name;
   public CustomerPK()
   {
   }
   public CustomerPK(long id, String name)
   {
      this.id = id;
      this.name = name;
   }
   public long getId()
   {
      return id;
   }
   public void setId(long id)
   {
      this.id = id;
   }
   public String getName()
   {
      return name;
   }
   public void setName(String name)
   {
      this.name = name;
   }
   public int hashCode()
   {
      return (int) id + name.hashCode();
   }
   public boolean equals(Object obj)
   {
      if (obj == this) return true;
      if (!(obj instanceof CustomerPK)) return false;
      if (obj == null) return false;
      CustomerPK pk = (CustomerPK) obj;
      return pk.id == id && pk.name.equals(name);
   }
}
File: EntityTest.java
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
package org.jboss.tutorial.composite.bean;
/**
 * Comment
 *
 * @author <a href="mailto:bill@jboss.org">Bill Burke</a>
 * @version $Revision: 57207 $
 */
public interface EntityTest
{
   Flight findFlightById(Long id) throws Exception;
   void manyToManyCreate() throws Exception;
}
File: EntityTestBean.java
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
package org.jboss.tutorial.composite.bean;
import java.util.HashSet;
import java.util.Set;
import javax.ejb.Remote;
import javax.ejb.Stateless;
import javax.persistence.EntityManager;
import javax.persistence.PersistenceContext;
import javax.persistence.PersistenceContext;
/**
 * Comment
 *
 * @author <a href="mailto:bill@jboss.org">Bill Burke</a>
 * @version $Revision: 57207 $
 */
@Stateless
@Remote(EntityTest.class)
public class EntityTestBean implements EntityTest
{
   private @PersistenceContext EntityManager manager;
   private static long genid = 0;
   public void manyToManyCreate() throws Exception
   {
      Flight firstOne = new Flight();
      firstOne.setId(new Long(1));
      firstOne.setName("AF0101");
      manager.persist(firstOne);
      Flight second = new Flight();
      second.setId(new Long(2));
      second.setName("US1");
      Set<Customer> customers1 = new HashSet<Customer>();
      Set<Customer> customers2 = new HashSet<Customer>();
      Customer bill = new Customer();
      CustomerPK pk = new CustomerPK(genid++, "Bill");
      bill.setPk(pk);
      customers1.add(bill);
      Customer monica = new Customer();
      CustomerPK moPK = new CustomerPK(genid++, "Monica");
      monica.setPk(moPK);
      customers1.add(monica);
      Customer molly = new Customer();
      CustomerPK mollyPK = new CustomerPK(genid++, "Molly");
      molly.setPk(mollyPK);
      customers2.add(molly);
      firstOne.setCustomers(customers1);
      second.setCustomers(customers2);
      manager.persist(second);
   }
   public Flight findFlightById(Long id) throws Exception
   {
      return manager.find(Flight.class, id);
   }
}
File: Flight.java
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
package org.jboss.tutorial.composite.bean;
import java.util.Set;
import javax.persistence.Basic;
import javax.persistence.CascadeType;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.FetchType;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.JoinTable;
import javax.persistence.ManyToMany;
import javax.persistence.Transient;
import javax.persistence.Version;
@Entity()
public class Flight implements java.io.Serializable
{
   Long id;
   String name;
   long duration;
   long durationInSec;
   Integer version;
   Set<Customer> customers;
   @Id
   public Long getId()
   {
      return id;
   }
   public void setId(Long long1)
   {
      id = long1;
   }
   @Column(updatable = false, name = "flight_name", nullable = false, length = 50)
   public String getName()
   {
      return name;
   }
   public void setName(String string)
   {
      name = string;
   }
   @Basic(fetch = FetchType.LAZY)
   public long getDuration()
   {
      return duration;
   }
   public void setDuration(long l)
   {
      duration = l;
      //durationInSec = duration / 1000;
   }
   @Transient
   public long getDurationInSec()
   {
      return durationInSec;
   }
   public void setDurationInSec(long l)
   {
      durationInSec = l;
   }
   @Version
   @Column(name = "OPTLOCK")
   public Integer getVersion()
   {
      return version;
   }
   public void setVersion(Integer i)
   {
      version = i;
   }
   @ManyToMany(cascade = {CascadeType.PERSIST, CascadeType.MERGE}, fetch = FetchType.EAGER)
   @JoinTable(name = "flight_customer_table",
                     joinColumns = {@JoinColumn(name = "FLIGHT_ID")},
                     inverseJoinColumns = {@JoinColumn(name = "CUSTOMER_ID"), @JoinColumn(name = "CUSTOMER_NAME")})
   public Set<Customer> getCustomers()
   {
      return customers;
   }
   public void setCustomers(Set<Customer> customers)
   {
      this.customers = customers;
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
package org.jboss.tutorial.composite.client;
import org.jboss.tutorial.composite.bean.Customer;
import org.jboss.tutorial.composite.bean.EntityTest;
import org.jboss.tutorial.composite.bean.Flight;
import javax.naming.InitialContext;
/**
 * Comment
 *
 * @author <a href="mailto:bill@jboss.org">Bill Burke</a>
 * @version $Revision: 57207 $
 */
public class Client
{
   public static void main(String[] args) throws Exception
   {
      InitialContext ctx = new InitialContext();
      EntityTest test = (EntityTest) ctx.lookup("EntityTestBean/remote");
      test.manyToManyCreate();
      Flight one = test.findFlightById(new Long(1));
      Flight two = test.findFlightById(new Long(2));
      System.out.println("Air France customers");
      for (Customer c : one.getCustomers())
      {
         System.out.println(c.getName());
      }
      System.out.println("USAir customers");
      for (Customer c : two.getCustomers())
      {
         System.out.println(c.getName());
      }
   }
}
```

jboss-EJB-3.0_RC9_Patch_1.zip( 10,289 k)
1.  Use Combined Fields As Primary Key
