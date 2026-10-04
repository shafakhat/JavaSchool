---
title: EJB Tutorial from JBoss
nav: EJB Tutorial from JBoss
description: * Copyright 2006, Red Hat Middleware LLC, and individual contributors
section: Imported - java2s Archive
order: 1044
source: https://web.archive.org/web/20090309180437/http://www.java2s.com:80/Code/Java/EJB3/EJBTutorialfromJBossturnEJBtowebservice.htm
---
EJB Tutorial from JBoss: turn EJB to web service

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
package org.jboss.tutorial.webservice.bean;
import javax.jws.WebService;
import javax.jws.WebMethod;
import java.rmi.Remote;
import java.rmi.RemoteException;
import javax.jws.soap.SOAPBinding;
import javax.jws.soap.SOAPBinding.Style;
@WebService
@SOAPBinding(style=Style.RPC)
public interface Calculator extends Remote
{
   @WebMethod int add(int x, int y);
   @WebMethod int subtract(int x, int y);
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
package org.jboss.tutorial.webservice.bean;
import javax.ejb.Stateless;
import javax.jws.WebService;
import javax.jws.soap.SOAPBinding;
import javax.jws.soap.SOAPBinding.Style;
@Stateless
@WebService(endpointInterface="org.jboss.tutorial.webservice.bean.Calculator")
public class CalculatorBean
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
package org.jboss.tutorial.webservice.client;
import org.jboss.tutorial.webservice.bean.Calculator;
import javax.xml.namespace.QName;
import javax.xml.rpc.Service;
import javax.xml.rpc.ServiceFactory;
import java.net.URL;
import java.io.File;
public class Client
{
   public static void main(String[] args) throws Exception
   {
      URL url = new URL("http://localhost:8080/tutorial/CalculatorBean?wsdl");
      QName qname = new QName("http://bean.webservice.tutorial.jboss.org/jaws",
              "CalculatorService");
      ServiceFactory factory = ServiceFactory.newInstance();
      Service service = factory.createService(url, qname);
      Calculator calculator = (Calculator) service.getPort(Calculator.class);
      System.out.println("1 + 1 = " + calculator.add(1, 1));
      System.out.println("1 - 1 = " + calculator.subtract(1, 1));
   }
}
```

jboss-EJB-3.0_RC9_Patch_1.zip( 10,289 k)
1.  EJB With Web Method
2.  Turn Ejb To Web Service
3.  Web Method With Return Type And Parameters
4.  EJB Based Web Services
