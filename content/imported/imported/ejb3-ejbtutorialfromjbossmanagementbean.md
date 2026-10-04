---
title: EJB Tutorial from JBoss
nav: EJB Tutorial from JBoss
description: * Copyright 2006, Red Hat Middleware LLC, and individual contributors
section: Imported - java2s Archive
order: 1028
source: https://web.archive.org/web/20090201184126/http://www.java2s.com:80/Code/Java/EJB3/EJBTutorialfromJBossmanagementbean.htm
---
EJB Tutorial from JBoss: management bean

```java title=Example.java
File: ServiceOneLocal.java
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
package org.jboss.tutorial.service.bean;
/**
 * @author <a href="mailto:kabir.khan@jboss.org">Kabir Khan</a>
 * @version $Revision: 57207 $
 */
public interface ServiceOneLocal
{
   public void setAttribute(int attribute);
   public int getAttribute();
}
File: ServiceOneManagement.java
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
package org.jboss.tutorial.service.bean;
import org.jboss.annotation.ejb.Management;
/**
 * @author <a href="mailto:kabir.khan@jboss.org">Kabir Khan</a>
 * @version $Revision: 57207 $
 */
public interface ServiceOneManagement
{
   void setAttribute(int attribute);
   int getAttribute();
   String sayHello();
   void create() throws Exception;
   void start() throws Exception;
   void stop();
   void destroy();
}
File: ServiceOneRemote.java
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
package org.jboss.tutorial.service.bean;
/**
 * @author <a href="mailto:kabir.khan@jboss.org">Kabir Khan</a>
 * @version $Revision: 57207 $
 */
public interface ServiceOneRemote
{
   public void setAttribute(int attribute);
   public int getAttribute();
}
File: ServiceThree.java
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
package org.jboss.tutorial.service.bean;
import org.jboss.annotation.ejb.Service;
import org.jboss.annotation.ejb.Depends;
import org.jboss.annotation.ejb.Management;
import javax.interceptor.AroundInvoke;
import javax.interceptor.InvocationContext;
import javax.management.ObjectName;
import javax.management.MBeanServerFactory;
import javax.management.MBeanServer;
/**
 * @author <a href="mailto:kabir.khan@jboss.org">Kabir Khan</a>
 * @version $Revision: 57207 $
 */
@Service
@Management(ServiceThreeManagement.class)
public class ServiceThree implements ServiceThreeManagement
{
   @Depends ("jboss.j2ee:jar=tutorial.jar,name=ServiceOne,service=EJB3,type=ManagementInterface")
   public ObjectName serviceOneName;
   private ServiceTwoManagement service2;
   @Depends ("tutorial:service=serviceTwo")
   public void setServiceTwo(ServiceTwoManagement service2)
   {
      this.service2 = service2;
   }
   public String serviceOneHello()throws Exception
   {
      Object[] args = new Object[0];
      String[] signature = new String[0];
      System.out.println("ServiceThree - Calling ServiceOne.sayHello() via JMX server");
      MBeanServer server = (MBeanServer)MBeanServerFactory.findMBeanServer(null).get(0);
      return (String)server.invoke(serviceOneName, "sayHello", args, signature);
   }
   public String serviceTwoHello()
   {
      System.out.println("ServiceThree - Calling ServiceTwo.sayHello() via MBean proxy");
      return service2.sayHello();
   }
   // Interceptors
   @AroundInvoke
   public Object intercept(InvocationContext ctx) throws Exception
   {
      System.out.println("ServiceThree - Interceptor");
      return ctx.proceed();
   }
   // Lifecycle methods
   public void start() throws Exception
   {
      System.out.println("ServiceThree - Starting");
   }
   public void stop()
   {
      System.out.println("ServiceThree - Stopping");
   }
}
File: ServiceThreeManagement.java
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
package org.jboss.tutorial.service.bean;
import javax.management.MBeanServer;
import javax.management.MBeanServerFactory;
/**
 * @author <a href="mailto:kabir.khan@jboss.org">Kabir Khan</a>
 * @version $Revision: 57207 $
 */
public interface ServiceThreeManagement
{
   String serviceOneHello()throws Exception;
   String serviceTwoHello();
   void start() throws Exception;
   void stop();
}
File: ServiceTwo.java
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
package org.jboss.tutorial.service.bean;
import org.jboss.annotation.ejb.Service;
import org.jboss.annotation.ejb.Depends;
import org.jboss.annotation.ejb.Management;
/**
 * @author <a href="mailto:kabir.khan@jboss.org">Kabir Khan</a>
 * @version $Revision: 57207 $
 */
@Service (objectName = "tutorial:service=serviceTwo")
@Management(ServiceTwoManagement.class)
@Depends ("jboss.j2ee:jar=tutorial.jar,name=ServiceOne,service=EJB3")
public class ServiceTwo implements ServiceTwoManagement
{
   public String sayHello()
   {
      return "Hello from service Two";
   }
   // Lifecycle methods
   public void start() throws Exception
   {
      System.out.println("ServiceTwo - Starting");
   }
   public void stop()
   {
      System.out.println("ServiceTwo - Stopping");
   }
}
File: ServiceTwoManagement.java
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
package org.jboss.tutorial.service.bean;
/**
 * @author <a href="mailto:kabir.khan@jboss.org">Kabir Khan</a>
 * @version $Revision: 57207 $
 */
public interface ServiceTwoManagement
{
   String sayHello();
   void start() throws Exception;
   void stop() throws Exception;
}
File: ServiceOne.java
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
package org.jboss.tutorial.service.bean;
import javax.ejb.Local;
import javax.ejb.Remote;
import org.jboss.annotation.ejb.Service;
import org.jboss.annotation.ejb.Management;
/**
 * @author <a href="mailto:kabir.khan@jboss.org">Kabir Khan</a>
 * @version $Revision: 57207 $
 */
@Service
@Local(ServiceOneLocal.class)
@Remote(ServiceOneRemote.class)
@Management(ServiceOneManagement.class)
public class ServiceOne implements ServiceOneLocal, ServiceOneRemote, ServiceOneManagement
{
   int attribute;
   public void setAttribute(int attribute)
   {
      this.attribute = attribute;
   }
   public int getAttribute()
   {
      return this.attribute;
   }
   public String sayHello()
   {
      return "Hello from service One";
   }
   // Lifecycle methods
   public void create() throws Exception
   {
      System.out.println("ServiceOne - Creating");
   }
   public void start() throws Exception
   {
      System.out.println("ServiceOne - Starting");
   }
   public void stop()
   {
      System.out.println("ServiceOne - Stopping");
   }
   public void destroy()
   {
      System.out.println("ServiceOne - Destroying");
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
package org.jboss.tutorial.service.client;
import org.jboss.tutorial.service.bean.ServiceOneRemote;
import org.jboss.jmx.adaptor.rmi.RMIAdaptor;
import javax.naming.InitialContext;
import javax.management.Attribute;
import javax.management.ObjectName;
public class Client
{
   public static void main(String[] args) throws Exception
   {
      InitialContext ctx = new InitialContext();
      //Get hold of the MBean server invoker
      RMIAdaptor server = (RMIAdaptor)ctx.lookup("jmx/invoker/RMIAdaptor");
      //Set attribute on singleton ServiceOne via remote interface
      ServiceOneRemote serviceOne = (ServiceOneRemote) ctx.lookup("ServiceOne/remote");
      serviceOne.setAttribute(100);
      //Create object name for ServiceOne
      ObjectName service1 = new ObjectName("jboss.j2ee:jar=tutorial.jar,service=EJB3,name=ServiceOne,type=ManagementInterface");
      //Get attribute of singleton ServiceOne via JMX
      int attr1 = (Integer)server.getAttribute(service1, "Attribute");
      System.out.println("attribute value for singleton obtained via JMX is what we set via remote i/f: " + attr1);
      //Create object name for ServiceThree
      ObjectName service3 = new ObjectName("jboss.j2ee:jar=tutorial.jar,service=EJB3,name=ServiceThree,type=ManagementInterface");
      //Call serviceOneHello() and serviceTwoHello() on ServiceThree
      Object[] noArgs = new Object[0];//No arguments
      String[] noSig = new String[0];//No parameters in signature
      String service1Hello = (String)server.invoke(service3, "serviceOneHello", noArgs, noSig);
      System.out.println(service1Hello);
      String service2Hello = (String)server.invoke(service3, "serviceTwoHello", noArgs, noSig);
      System.out.println(service2Hello);
   }
}
```

jboss-EJB-3.0_RC9_Patch_1.zip( 10,289 k)
