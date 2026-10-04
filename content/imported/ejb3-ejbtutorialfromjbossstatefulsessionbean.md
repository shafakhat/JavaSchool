---
title: EJB Tutorial from JBoss
nav: EJB Tutorial from JBoss
description: * Copyright 2006, Red Hat Middleware LLC, and individual contributors
section: Imported - java2s Archive
order: 1039
source: https://web.archive.org/web/20090125020940/http://java2s.com:80/Code/Java/EJB3/EJBTutorialfromJBossstatefulsessionbean.htm
---
EJB Tutorial from JBoss: stateful session bean

```java title=Example.java
File: ShoppingCart.java
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
package org.jboss.tutorial.stateful.bean;
import java.util.HashMap;
import javax.ejb.Remove;
public interface ShoppingCart
{
   void buy(String product, int quantity);
   HashMap<String, Integer> getCartContents();
   @Remove void checkout();
}
File: ShoppingCartBean.java
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
package org.jboss.tutorial.stateful.bean;
import java.io.Serializable;
import java.util.HashMap;
import javax.ejb.Remove;
import javax.ejb.Stateful;
import javax.ejb.Remote;
@Stateful
@Remote(ShoppingCart.class)
public class ShoppingCartBean implements ShoppingCart, Serializable
{
   private HashMap<String, Integer> cart = new HashMap<String, Integer>();
   public void buy(String product, int quantity)
   {
      if (cart.containsKey(product))
      {
         int currq = cart.get(product);
         currq += quantity;
         cart.put(product, currq);
      }
      else
      {
         cart.put(product, quantity);
      }
   }
   public HashMap<String, Integer> getCartContents()
   {
      return cart;
   }
   @Remove
   public void checkout()
   {
      System.out.println("To be implemented");
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
package org.jboss.tutorial.stateful.client;
import java.util.HashMap;
import javax.naming.InitialContext;
import org.jboss.tutorial.stateful.bean.ShoppingCart;
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
      ShoppingCart cart = (ShoppingCart) ctx.lookup("ShoppingCartBean/remote");
      System.out.println("Buying 1 memory stick");
      cart.buy("Memory stick", 1);
      System.out.println("Buying another memory stick");
      cart.buy("Memory stick", 1);
      System.out.println("Buying a laptop");
      cart.buy("Laptop", 1);
      System.out.println("Print cart:");
      HashMap<String, Integer> fullCart = cart.getCartContents();
      for (String product : fullCart.keySet())
      {
         System.out.println(fullCart.get(product) + "     " + product);
      }
      System.out.println("Checkout");
      cart.checkout();
      System.out.println("Should throw an object not found exception by invoking on cart after @Remove method");
      try
      {
         cart.getCartContents();
      }
      catch (javax.ejb.EJBNoSuchObjectException e)
      {
         System.out.println("Successfully caught no such object exception.");
      }
   }
}
```

jboss-EJB-3.0_RC9_Patch_1.zip( 10,289 k)
1.  Stateful Session Bean Lifecycle: PrePassivate
2.  Stateful Session Bean Lifecycle: PreDestroy
3.  Stateful Session Bean Lifecycle: PostConstruct
4.  Stateful Session Bean Lifecycle: PostActivate
5.  Stateful Session Bean And Shopping Cart
6.  Stateful Session Bean And Entity Manager
7.  Use Lifecycle Method To Manage Collection In Stateful Session Bean
8.  EJB Tutorial from JBoss: stateful session bean deployment descriptor
9.  Remove a Stateful Session Bean
10.  Remove Annotation
11.  Ejb With Generic Method
