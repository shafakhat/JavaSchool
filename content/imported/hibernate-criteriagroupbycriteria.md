---
title: Criteria
nav: Criteria
description: Criteria: Group By Criteria : Java examples (example source code) » Hibernate » Criteria Group
section: Imported - java2s Archive
order: 1022
source: https://web.archive.org/web/20060513081028/http://www.java2s.com/Code/Java/Hibernate/CriteriaGroupByCriteria.htm
---
Criteria: Group By Criteria : Java examples (example source code) » Hibernate » Criteria Group

Criteria: Group By Criteria

```java title=Example.java
/////////////////////////////////////////////////////////////////////////
import java.util.*;
import java.sql.*;
import org.hibernate.*;
import org.hibernate.criterion.*;
public class Main {
  public static void main(String[] args) {
    HibernateUtil.setup("create table Supplier ( id int, name VARCHAR);");
    HibernateUtil.setup("create table Product ( id int, name VARCHAR, description VARCHAR, price double,supplierId int);");
    prepareData();
    Session session = HibernateUtil.currentSession();
        Criteria crit = session.createCriteria(Product.class);
        ProjectionList projList = Projections.projectionList();
        projList.add(Projections.property("name"));
        projList.add(Projections.groupProperty("name"));
        crit.setProjection(projList);
        List results = crit.list();
        displayObjectsList(results);
        HibernateUtil.checkData("select * from Supplier");
        HibernateUtil.checkData("select * from Product");
  }
    static public void displayObjectsList(List list)
    {
        Iterator iter = list.iterator();
        if (!iter.hasNext())
        {
            System.out.println("No objects to display.");
            return;
        }
        while (iter.hasNext())
        {
            System.out.println("New object");
            Object[] obj = (Object[]) iter.next();
            for (int i=0;i<obj.length;i++)
            {
                System.out.println(obj[i]);
            }
        }
    }
  private static void prepareData(){
        Session session = HibernateUtil.currentSession();
        Supplier supplier1 = new Supplier();
        supplier1.setName("Supplier Name 1");
        session.save(supplier1);
        Supplier supplier2 = new Supplier();
        supplier2.setName("Supplier Name 2");
        session.save(supplier2);
        Product product1 = new Product("Product 1","Name for Product 1", 2.0);
        product1.setSupplier(supplier1);
        supplier1.getProducts().add(product1);
        session.save(product1);
        Product product12 = new Product("Product 2","Name for Product 2", 22.0);
        product12.setSupplier(supplier1);
        supplier1.getProducts().add(product12);
        session.save(product12);
        Product product2 = new Product("Product 3", "Name for Product 3", 30.0);
        product2.setSupplier(supplier2);
        supplier2.getProducts().add(product2);
        session.save(product2);
        session.flush();
        HibernateUtil.closeSession();
  }
}
/////////////////////////////////////////////////////////////////////////
public class Product
{
    private int id;
    private Supplier supplier;
    private String name;
    private String description;
    private double price;
    public Product()
    {
        super();
    }
    public Product(String name, String description, double price)
    {
        super();
        this.name = name;
        this.description = description;
        this.price = price;
    }
    public String getDescription()
    {
        return description;
    }
    public void setDescription(String description)
    {
        this.description = description;
    }
    public int getId()
    {
        return id;
    }
    public void setId(int id)
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
    public Supplier getSupplier()
    {
        return supplier;
    }
    public void setSupplier(Supplier supplier)
    {
        this.supplier = supplier;
    }
    public double getPrice()
    {
        return price;
    }
    public void setPrice(double price)
    {
        this.price = price;
    }
}
/////////////////////////////////////////////////////////////////////////
<?xml version='1.0' encoding='utf-8'?>
<!DOCTYPE hibernate-mapping
   PUBLIC "-//Hibernate/Hibernate Mapping DTD//EN"
   "http://hibernate.sourceforge.net/hibernate-mapping-3.0.dtd">
<hibernate-mapping>
   <class name="Supplier">
      <id name="id" type="int">
         <generator class="increment"/>
      </id>
      <property name="name" type="string"/>
      <bag name="products" inverse="true" cascade="all,delete-orphan">
        <key column="supplierId"/>
        <one-to-many class="Product"/>
      </bag>
   </class>
</hibernate-mapping>
/////////////////////////////////////////////////////////////////////////
import java.util.ArrayList;
import java.util.List;
public class Supplier
{
    private int id;
    private String name;
    private List products = new ArrayList();
    public int getId()
    {
        return id;
    }
    public void setId(int id)
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
    public List getProducts()
    {
        return products;
    }
    public void setProducts(List products)
    {
        this.products = products;
    }
}
/////////////////////////////////////////////////////////////////////////
```

Download: HibernateCriteriaGroupByCriteria.zip (3692 K)
Related examples in the same category
