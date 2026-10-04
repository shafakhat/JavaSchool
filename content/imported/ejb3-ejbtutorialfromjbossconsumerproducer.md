---
title: EJB Tutorial from JBoss
nav: EJB Tutorial from JBoss
description: * Copyright 2006, Red Hat Middleware LLC, and individual contributors
section: Imported - java2s Archive
order: 1015
source: https://web.archive.org/web/20081202025818/http://www.java2s.com:80/Code/Java/EJB3/EJBTutorialfromJBossConsumerproducer.htm
---
EJB Tutorial from JBoss: Consumer producer

```java title=Example.java
File: ExampleProducer.java
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
package org.jboss.tutorial.consumer.bean;
import org.jboss.annotation.ejb.MessageProperties;
import org.jboss.annotation.ejb.DeliveryMode;
import org.jboss.annotation.ejb.DeliveryMode;
import org.jboss.annotation.ejb.MessageProperties;
import java.util.Map;
/**
 * comment
 *
 * @author <a href="mailto:bill@jboss.org">Bill Burke</a>
 */
public interface ExampleProducer
{
   void method1(String msg, int val);
   @MessageProperties(delivery=DeliveryMode.NON_PERSISTENT)
   void method2(String msg, Map<String, String> map);
}
File: ExampleProducerLocal.java
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
package org.jboss.tutorial.consumer.bean;
import org.jboss.annotation.ejb.Producer;
import org.jboss.annotation.ejb.Local;
import org.jboss.annotation.ejb.Producer;
/**
 * comment
 *
 * @author <a href="mailto:bill@jboss.org">Bill Burke</a>
 */
@Local @Producer
public interface ExampleProducerLocal extends ExampleProducer
{
}
File: ExampleProducerRemote.java
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
package org.jboss.tutorial.consumer.bean;
import org.jboss.annotation.ejb.Producer;
/**
 * comment
 *
 * @author <a href="mailto:bill@jboss.org">Bill Burke</a>
 */
@Producer
public interface ExampleProducerRemote extends ExampleProducer
{
}
File: ExampleProducerXA.java
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
package org.jboss.tutorial.consumer.bean;
import java.util.Map;
import org.jboss.annotation.ejb.DeliveryMode;
import org.jboss.annotation.ejb.MessageProperties;
import org.jboss.annotation.ejb.Producer;
import org.jboss.annotation.ejb.Local;
/**
 * comment
 *
 * @author <a href="mailto:bill@jboss.org">Bill Burke</a>
 */
@Local @Producer(connectionFactory="java:/JmsXA")
public interface ExampleProducerXA extends ExampleProducer
{
   @MessageProperties(delivery=DeliveryMode.PERSISTENT, priority=4)
   void method2(String msg, Map<String, String> map);
}
File: Tester.java
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
package org.jboss.tutorial.consumer.bean;
/**
 * Comment
 *
 * @author <a href="mailto:bill@jboss.org">Bill Burke</a>
 * @version $Revision: 57207 $
 */
public interface Tester
{
   void testXA() throws Exception;
   void testLocal() throws Exception;
}
File: TesterBean.java
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
package org.jboss.tutorial.consumer.bean;
import java.util.HashMap;
import java.util.Map;
import org.jboss.annotation.JndiInject;
import javax.ejb.Remote;
import javax.ejb.Stateless;
import javax.ejb.TransactionAttribute;
import javax.ejb.TransactionAttributeType;
import org.jboss.ejb3.mdb.ProducerManager;
import org.jboss.ejb3.mdb.ProducerObject;
/**
 * Show injecting in producers
 * Show how to interact with local producers
 *
 * @author <a href="mailto:bill@jboss.org">Bill Burke</a>
 * @version $Revision: 57207 $
 */
@Stateless
@Remote(Tester.class)
public class TesterBean implements Tester
{
   private ExampleProducerXA xa;
   private ProducerManager xaManager;
   @JndiInject(jndiName="org.jboss.tutorial.consumer.bean.ExampleProducerXA")
   public void setXa(ExampleProducerXA xa)
   {
      this.xa = xa;
      this.xaManager = ((ProducerObject)xa).getProducerManager();
   }
   private ExampleProducer local;
   private ProducerManager localManager;
   @JndiInject(jndiName="org.jboss.tutorial.consumer.bean.ExampleProducerLocal")
   public void setLocal(ExampleProducer local)
   {
      this.local = local;
      this.localManager = ((ProducerObject)local).getProducerManager();
   }
   @TransactionAttribute(TransactionAttributeType.REQUIRED)
   public void testXA() throws Exception
   {
      xaManager.connect();
      xa.method1("testXA", 1);
      Map<String, String> map = new HashMap<String, String>();
      map.put("hello", "world");
      map.put("great", "ejb3");
      xa.method2("testXA2", map);
      System.out.println("end TESTXA **");
      xaManager.close();
   }
   public void testLocal() throws Exception
   {
      localManager.connect();
      local.method1("testLocal", 1);
      Map<String, String> map = new HashMap<String, String>();
      map.put("hello", "world");
      map.put("great", "ejb3");
      local.method2("testLocal2", map);
      localManager.close();
   }
}
File: ExampleConsumerBean.java
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
package org.jboss.tutorial.consumer.bean;
import java.util.Map;
import javax.ejb.ActivationConfigProperty;
import javax.jms.Message;
import org.jboss.annotation.ejb.Consumer;
import org.jboss.annotation.ejb.CurrentMessage;
@Consumer(activationConfig = {
        @ActivationConfigProperty(propertyName="destinationType", propertyValue="javax.jms.Queue"),
        @ActivationConfigProperty(propertyName="destination", propertyValue="queue/tutorial/example")
})
public class ExampleConsumerBean implements ExampleProducerRemote, ExampleProducerLocal, ExampleProducerXA
{
   // you can have container inject the current JMS message so that you can manipulate it, like for instance
   // to get a reply-to destination.
   @CurrentMessage private Message currentMessage;
   public void method1(String msg, int val)
   {
      System.out.println("method1(" + msg + ", " + val + ")");
   }
   public void method2(String msg, Map<String, String> map)
   {
      System.out.println("method2: " + msg);
      for (String key : map.keySet())
      {
         System.out.println("method2 key/val: " + key + ":" + map.get(key));
      }
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
package org.jboss.tutorial.consumer.client;
import java.util.HashMap;
import java.util.Map;
import javax.naming.InitialContext;
import org.jboss.ejb3.mdb.ProducerManager;
import org.jboss.ejb3.mdb.ProducerObject;
import org.jboss.ejb3.mdb.ProducerConfig;
import org.jboss.tutorial.consumer.bean.ExampleProducerRemote;
import org.jboss.tutorial.consumer.bean.Tester;
public class Client
{
   public static void main(String[] args) throws Exception
   {
      InitialContext ctx = new InitialContext();
      ExampleProducerRemote remote = (ExampleProducerRemote) ctx.lookup(ExampleProducerRemote.class.getName());
      // you can typecast the returned proxy to obtain a ProducerManager interface that allows you to manage
      // interaction with JMS.
      ProducerManager manager = ((ProducerObject) remote).getProducerManager();
      // connect
      manager.connect();
      try
      {
         // Call method1
         remote.method1("Remote method1 called", 1);
         // Call method2
         Map<String, String> map = new HashMap<String, String>();
         map.put("hello", "world");
         map.put("great", "ejb3");
         remote.method2("Remote method2 called", map);
      }
      finally
      {
         // instead of typecasting, you can use a helper class that does everything for you.
         ProducerConfig.close(remote);
      }
      // Try out local producers by interfacing with Session bean
      Tester tester = (Tester) ctx.lookup("TesterBean/remote");
      tester.testLocal();
      tester.testXA();
   }
}
```

jboss-EJB-3.0_RC9_Patch_1.zip( 10,289 k)
1.  EJB Tutorial from JBoss: Message driven bean
2.  EJB Tutorial from JBoss: demo for message driven bean
3.  EJB Tutorial from JBoss: message driven bean deployment descriptor
