---
title: Calculation Based on Model
nav: Calculation Based on Model
description: Calculation Based on Model : Java examples (example source code) » Velocity » Calculation
section: Imported - java2s Archive
order: 1016
source: https://web.archive.org/web/20060411091828/http://www.java2s.com:80/Code/Java/Velocity/CalculationBasedonModel.htm
---
Calculation Based on Model : Java examples (example source code) » Velocity » Calculation

Calculation Based on Model

```java title=Example.java
import java.io.StringWriter;
import java.io.Writer;
import java.util.ArrayList;
import java.util.Collection;
import org.apache.velocity.Template;
import org.apache.velocity.VelocityContext;
import org.apache.velocity.app.Velocity;
public class ProductList {
    public static void main(String[] args) throws Exception {
        Velocity.init();
        Template t = Velocity.getTemplate("./src/model.vm");
        VelocityContext ctx = new VelocityContext();
        Collection products = new ArrayList();
        products.add(new Product("Product 1", 142.919));
        products.add(new Product("Product 2", 133.199));
        products.add(new Product("Product 3", 112.991));
        ProductListModel model = new ProductListModel(products);
        ctx.put("model", model);
        Writer writer = new StringWriter();
        t.merge(ctx, writer);
        System.out.println(writer);
    }
}
-------------------------------------------------------------------------------------
import java.util.Collection;
import java.util.Iterator;
public class ProductListModel {
  private Collection productList = null;
  private double totalPrice = Double.MIN_VALUE;
  public ProductListModel(Collection aProductList) {
    productList = aProductList;
  }
  public Collection getProductList() {
    return productList;
  }
  public void setProductList(Collection aProductList) {
    productList = aProductList;
  }
  public double getTotalPrice() {
    if (totalPrice == Double.MIN_VALUE) {
      totalPrice = 0;
      Iterator itr = productList.iterator();
      while (itr.hasNext()) {
        Product p = (Product) itr.next();
        totalPrice += p.getPrice();
      }
    }
    return totalPrice;
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
#foreach($product in $model.productList)
$product.Name    $$product.Price
#end
Total Price: $$model.totalPrice
```

Download: velocity-CalculationBasedonModel.zip (876 K)
---
Related examples in the same category
1. Calculation In Java
