---
title: EJB Tutorial from JBoss
nav: EJB Tutorial from JBoss
description: * Copyright 2006, Red Hat Middleware LLC, and individual contributors
section: Imported - java2s Archive
order: 1020
source: https://web.archive.org/web/20090420041727/http://www.java2s.com:80/Code/Java/EJB3/EJBTutorialfromJBossEntityrelationship.htm
---
EJB Tutorial from JBoss: Entity relationship

```java title=Example.java
File: Address.java
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
package org.jboss.tutorial.relationships.bean;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue; import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.GeneratedValue; import javax.persistence.GenerationType;
/**
 * Comment
 *
 * @author <a href="mailto:bill@jboss.org">Bill Burke</a>
 * @version $Revision: 57207 $
 */
@Entity
public class Address implements java.io.Serializable
{
   private Long id;
   private String street;
   private String city;
   private String state;
   private String zip;
   @Id @GeneratedValue(strategy=GenerationType.IDENTITY)
   public Long getId()
   {
      return id;
   }
   public void setId(Long id)
   {
      this.id = id;
   }
   public String getStreet()
   {
      return street;
   }
   public void setStreet(String street)
   {
      this.street = street;
   }
   public String getCity()
   {
      return city;
   }
   public void setCity(String city)
   {
      this.city = city;
   }
   public String getState()
   {
      return state;
   }
   public void setState(String state)
   {
      this.state = state;
   }
   public String getZip()
   {
      return zip;
   }
   public void setZip(String zip)
   {
      this.zip = zip;
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
//$Id: Customer.java 57207 2006-09-26 12:06:13Z dimitris@jboss.org $
package org.jboss.tutorial.relationships.bean;
import javax.persistence.CascadeType;
import javax.persistence.Entity;
import javax.persistence.FetchType;
import javax.persistence.GeneratedValue; import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.ManyToMany;
import javax.persistence.OneToOne;
import javax.persistence.JoinColumn;
import javax.persistence.Id;
import javax.persistence.ManyToMany;
import javax.persistence.CascadeType;
import javax.persistence.GeneratedValue; import javax.persistence.GenerationType;
import javax.persistence.Entity;
import java.util.Set;
/**
 * Company customer
 *
 * @author Emmanuel Bernard
 */
@Entity
public class Customer implements java.io.Serializable
{
   Long id;
   String name;
   Set<Flight> flights;
   Address address;
   public Customer()
   {
   }
   @Id @GeneratedValue(strategy=GenerationType.IDENTITY)
   public Long getId()
   {
      return id;
   }
   public String getName()
   {
      return name;
   }
   public void setId(Long long1)
   {
      id = long1;
   }
   public void setName(String string)
   {
      name = string;
   }
   @OneToOne(cascade = {CascadeType.ALL})
   @JoinColumn(name = "ADDRESS_ID")
   public Address getAddress()
   {
      return address;
   }
   public void setAddress(Address address)
   {
      this.address = address;
   }
   @ManyToMany(cascade = {CascadeType.PERSIST, CascadeType.MERGE}, fetch = FetchType.EAGER, mappedBy="customers")
   public Set<Flight> getFlights()
   {
      return flights;
   }
   public void setFlights(Set<Flight> flights)
   {
      this.flights = flights;
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
package org.jboss.tutorial.relationships.bean;
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
package org.jboss.tutorial.relationships.bean;
import java.util.HashSet;
import java.util.Set;
import javax.ejb.Remote;
import javax.ejb.Stateless;
import javax.persistence.EntityManager;
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
      bill.setName("Bill");
      Address address = new Address();
      address.setStreet("Clarendon Street");
      address.setCity("Boston");
      address.setState("MA");
      address.setZip("02116");
      bill.setAddress(address);
      customers1.add(bill);
      Customer monica = new Customer();
      monica.setName("Monica");
      address = new Address();
      address.setStreet("Beach Street");
      address.setCity("Somerville");
      address.setState("MA");
      address.setZip("02116");
      monica.setAddress(address);
      customers1.add(monica);
      Customer molly = new Customer();
      molly.setName("Molly");
      address = new Address();
      address.setStreet("Main Street");
      address.setCity("Billerica");
      address.setState("MA");
      address.setZip("02116");
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
//$Id: Flight.java 57207 2006-09-26 12:06:13Z dimitris@jboss.org $
package org.jboss.tutorial.relationships.bean;
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
/**
 * Flight
 *
 * @author Emmanuel Bernard
 */
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
                     inverseJoinColumns = {@JoinColumn(name = "CUSTOMER_ID")})
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
package org.jboss.tutorial.relationships.client;
import org.jboss.tutorial.relationships.bean.Customer;
import org.jboss.tutorial.relationships.bean.EntityTest;
import org.jboss.tutorial.relationships.bean.Flight;
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
