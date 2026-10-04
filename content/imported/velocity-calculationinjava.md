---
title: Calculation In Java
nav: Calculation In Java
description: Calculation In Java : Java examples (example source code) » Velocity » Calculation
section: Imported - java2s Archive
order: 1017
source: https://web.archive.org/web/20060411085924/http://www.java2s.com:80/Code/Java/Velocity/CalculationInJava.htm
---
Calculation In Java : Java examples (example source code) » Velocity » Calculation

```java title=Example.java
import java.io.StringWriter;
import java.io.Writer;
import java.util.ArrayList;
import java.util.Collection;
import java.util.Iterator;
import org.apache.velocity.Template;
import org.apache.velocity.VelocityContext;
import org.apache.velocity.app.Velocity;
public class ProductList {
  public static void main(String[] args) throws Exception {
    Velocity.init();
    Template t = Velocity.getTemplate("./src/calculation.vm");
    VelocityContext ctx = new VelocityContext();
    Collection products = new ArrayList();
    products.add(new Product("Product 1", 12.99));
    products.add(new Product("Product 2", 13.99));
    products.add(new Product("Product 3", 11.99));
    ctx.put("productList", products);
    // calculate total
    Iterator itr = products.iterator();
    double total = 0.00;
    while (itr.hasNext()) {
      Product p = (Product) itr.next();
      total += p.getPrice();
    }
    ctx.put("totalPrice", new Double(total));
    Writer writer = new StringWriter();
    t.merge(ctx, writer);
    System.out.println(writer);
  }
}
-------------------------------------------------------------------------------------
public class Product {
    private String name;
    private double price;
    public Product(String aName, double aPrice) {
        name = aName;
        price = aPrice;
    }
    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
    public double getPrice() {
        return price;
    }
    public void setPrice(double price) {
        this.price = price;
    }
}
-------------------------------------------------------------------------------------
#foreach($product in $productList)
$product.Name    $$product.Price
#end
Total Price: $$totalPrice
```

Download: velocity-CalculationInJava.zip (876 K)
---
Related examples in the same category
1. Calculation Based on Model
