---
title: Convert Utils Demo
nav: Convert Utils Demo
description: convertUtilsBean.register(new MyStringConverter(), String.class);
section: Imported - java2s Archive
order: 1024
source: https://web.archive.org/web/20070403123432/http://www.java2s.com:80/Code/Java/Apache-Common/ConvertUtilsDemo.htm
---
Convert Utils Demo

```java title=Example.java
import org.apache.commons.beanutils.Converter;
import org.apache.commons.beanutils.PropertyUtils;
import org.apache.commons.beanutils.BeanUtilsBean;
import org.apache.commons.beanutils.ConvertUtilsBean;
import org.apache.commons.beanutils.PropertyUtilsBean;
import org.apache.commons.beanutils.ConversionException;
import java.util.Map;
public class BeanUtilsExampleV4 {
  public static void main(String args[]) throws Exception {
    BeanUtilsExampleV4 diff = new BeanUtilsExampleV4();
    Actor actor = diff.prepareData();
    ConvertUtilsBean convertUtilsBean = new ConvertUtilsBean();
    convertUtilsBean.deregister(String.class);
    convertUtilsBean.register(new MyStringConverter(), String.class);
    convertUtilsBean.deregister(Long.class);
    convertUtilsBean.register(new MyLongConverter(), Long.class);
    convertUtilsBean.register(new MyLongConverter(), Long.TYPE);
    BeanUtilsBean beanUtilsBean =
      new BeanUtilsBean(convertUtilsBean, new PropertyUtilsBean());
    System.err.println("==== Values before calling describe ==== ");
    System.err.println("By PropertyUtils: " +
      PropertyUtils.getProperty(actor, "name"));
    System.err.println("By BeanUtils: " +
      beanUtilsBean.getProperty(actor, "name"));
    System.err.println(beanUtilsBean.getProperty(actor, "worth"));
    Map describedData = beanUtilsBean.describe(actor);
    // check the map
    System.err.println("==== Values in Map ==== ");
    System.err.println(describedData.get("name"));
    System.err.println(describedData.get("worth"));
    // create a new Actor Bean
    Actor newActor = new Actor();
    beanUtilsBean.populate(newActor, describedData);
    System.err.println("==== Values after calling populate ==== ");
    System.err.println(beanUtilsBean.getProperty(newActor, "name"));
    System.err.println(beanUtilsBean.getProperty(newActor, "worth"));
  }
  private Actor prepareData() {
    Actor actor = new Actor();
    actor.setName("Michael Caine");
    actor.setGender(1);
    actor.setWorth(10000000);
    return actor;
  }
}
class MyStringConverter implements Converter {
  public Object convert(Class type, Object value) {
    if(value == null) {
      return (String)null;
    } else {
      return (value.toString().replaceAll("\\s", ""));
    }
  }
}
class MyLongConverter implements Converter {
  private Object defaultValue;
  private boolean useDefault;
  public MyLongConverter() {
    this(true, new Long(0));
  }
  public MyLongConverter(boolean useDefault, Object defaultValue) {
    this.useDefault = useDefault;
    this.defaultValue = defaultValue;
  }
  public Object convert(Class type, Object value) {
    if(value == null) {
      if(useDefault) {
        return defaultValue;
      } else {
        throw new ConversionException("No default value specified");
      }
    }
    if(value instanceof Long) {
      return new Long(((Long)value).longValue() + 1000);
    } else {
      try {
        return new Long(new Long(value.toString()).longValue() + 1000);
      } catch (Exception e) {
        System.err.println(e);
        if(useDefault) {
          return defaultValue;
        } else {
          throw new ConversionException(e);
        }
      }
    }
  }
}
------------------------------------------------------------------------
import java.util.Map;
import java.util.List;
import java.util.Date;
public class Movie {
  public Movie() {
  }
  public Date getDateOfRelease() { return this.dateOfRelease; }
  public void setDateOfRelease(Date dateOfRelease) {
    this.dateOfRelease = dateOfRelease;
  }
  public String getTitle() { return this.title; }
  public void setTitle(String title) {this.title = title; }
  public Person getDirector() { return this.director; }
  public void setDirector(Person director) { this.director = director; }
  public List getActors() { return this.actors; }
  public void setActors(List actors) { this.actors= actors; }
  public String[] getKeywords() { return this.keywords; }
  public void setKeyWords(String[] keywords) { this.keywords = keywords; }
  public Map getGenre() { return this.genre; }
  public void setGenre(Map genre) { this.genre = genre; }
  private Date dateOfRelease;
  private String title;
  private Person director;
  private List actors;
  private String[] keywords;
  private Map genre;
}
------------------------------------------------------------------------
import java.util.Map;
import org.apache.commons.lang.builder.EqualsBuilder;
import org.apache.commons.lang.builder.HashCodeBuilder;
import org.apache.commons.lang.builder.ToStringBuilder;
public class Person {
  public Person() {
  }
  public String getName() {
    return this.name == null ? "NoName" : this.name; }
  public void setName(String name) { this.name = name; }
  public int getGender() { return this.gender; }
  public void setGender(int gender) {  // 0 - Indeterminate, 1 - Male, 2 - Female
    this.gender = (gender > 2 || gender < 0) ? 0 : gender; }
  public Map getContactNumber() { return this.contactNumber; }
  public void setContactNumber(Map contactNumber) {
    this.contactNumber = contactNumber;
  }
  /**public boolean equals(Object o) {
    if(o == this) return true;
    if(!(o instanceof Person)) return false;
    Person otherPerson = (Person)o;
    if(otherPerson.getName().equals(this.name) &&
       otherPerson.getGender() == this.gender) return true;
    return false;
  }*/
  public boolean equals(Object o) {
    if(!(o instanceof Person)) return false;
    Person otherPerson = (Person)o;
    return new EqualsBuilder()
               .append(name, otherPerson.getName())
               .append(gender, otherPerson.getGender())
               .isEquals();
  }
  public int hashCode() {
    return new HashCodeBuilder(7, 51)
               .append(name)
               .append(gender)
               .append(contactNumber)
               .toHashCode();
  }
  public String toString() {
    return new ToStringBuilder(this)
               .append("Name", name)
               .append("Gender", gender)
               .append("Contact Details", contactNumber)
               .toString();
  }
  private String name;
  private int gender;
  private Map contactNumber;
}
------------------------------------------------------------------------
import java.util.List;
public class Actor extends Person {
  public Actor() {
  }
  public List getMovieCredits() { return this.movieCredits; }
  public void setMovieCredits(List movieCredits) {
    this.movieCredits = movieCredits;
  }
  public long getWorth() { return this.worth; }
  public void setWorth(long worth) { this.worth = worth; }
  private List movieCredits;
  private long worth;
}
```

Download: BeanUtilsExampleV4.zip ( 881 K )
Related examples in the same category
