---
title: EJB Tutorial from JBoss
nav: EJB Tutorial from JBoss
description: * Copyright 2006, Red Hat Middleware LLC, and individual contributors
section: Imported - java2s Archive
order: 1023
source: https://web.archive.org/web/20090201063114/http://www.java2s.com:80/Code/Java/EJB3/EJBTutorialfromJBossInjection.htm
---
EJB Tutorial from JBoss: Injection

```java title=Example.java
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
package org.jboss.tutorial.injection.bean;
import javax.ejb.Stateless;
@Stateless
public class CalculatorBean implements Calculator
{
   public int add(int x, int y)
   {
      return x + y;
   }
   public int subtract(int x, int y)
   {
      return x - y;
   }
}
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
package org.jboss.tutorial.injection.bean;
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
package org.jboss.tutorial.injection.bean;
import java.util.HashMap;
import javax.ejb.EJB;
import javax.ejb.Remote;
import javax.ejb.Remove;
import javax.ejb.Stateful;
@Stateful
@Remote(ShoppingCart.class)
public class ShoppingCartBean implements ShoppingCart, java.io.Serializable
{
   private HashMap<String, Integer> cart = new HashMap<String, Integer>();
   @EJB
   private Calculator calculator;
   private Calculator set;
   @EJB(beanName="CalculatorBean")
   public void setCalculator(Calculator c)
   {
      set = c;
   }
   public void buy(String product, int quantity)
   {
      if (cart.containsKey(product))
      {
         int currq = cart.get(product);
         currq = calculator.add(currq, quantity);
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
package org.jboss.tutorial.injection.bean;
public interface Calculator
{
   int add(int x, int y);
   int subtract(int x, int y);
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
package org.jboss.tutorial.injection.client;
import org.jboss.tutorial.injection.bean.ShoppingCart;
import javax.naming.InitialContext;
import java.util.HashMap;
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
   }
}
```

jboss-EJB-3.0_RC9_Patch_1.zip( 10,289 k)
1.  Field Injection
2.  Setter Injection
3.  Use Injected Context To Loopup An other EJB
4.  Inject Transaction As Resource
5.  Use EJB To Reference Another EJB In One EJB
