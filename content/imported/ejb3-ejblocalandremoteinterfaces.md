---
title: Ejb Local And Remote Interfaces
nav: Ejb Local And Remote Inter...
description: public class HelloServiceBean implements HelloServiceLocal, HelloServiceRemote {
section: Imported - java2s Archive
order: 1008
source: https://web.archive.org/web/20081229030734/http://www.java2s.com:80/Code/Java/EJB3/EjbLocalAndRemoteInterfaces.htm
---
```java title=Example.java
File: HelloServiceBean.java
import javax.ejb.Stateless;
@Stateless
public class HelloServiceBean implements HelloServiceLocal, HelloServiceRemote {
    public String sayHello(String name) {
        return "Hello1, "  + name;
    }
}
File: HelloServiceLocal.java
import javax.ejb.Local;
@Local
public interface HelloServiceLocal {
    public String sayHello(String name);
}
File: HelloServiceRemote.java
import javax.ejb.Remote;
@Remote
public interface HelloServiceRemote{
    public String sayHello(String name);
}
File: jndi.properties
java.naming.factory.initial=org.jnp.interfaces.NamingContextFactory
java.naming.factory.url.pkgs=org.jboss.naming:org.jnp.interfaces
java.naming.provider.url=localhost:1099
File: Main.java
import java.util.*;
import javax.naming.*;
public class Main{
   public static void main(String[] a) throws Exception{
        String name = "java2s";
        HelloServiceRemote service = null;
        //Context compEnv = (Context) new InitialContext().lookup("java:comp/env");
        //service = (HelloService)new InitialContext().lookup("java:comp/env/ejb/HelloService");
        service = (HelloServiceRemote)new InitialContext().lookup("HelloServiceBean/remote");
        System.out.println(service.sayHello(name));
   }
}
```

EJB-EjbLocalAndRemote.zip( 4,485 k)
1.  Local Interface Without Marking
