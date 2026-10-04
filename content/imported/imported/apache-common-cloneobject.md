---
title: Clone Object
nav: Clone Object
description: // Movie newMovieBean = (Movie)BeanUtils.cloneBean(movieBean);
section: Imported - java2s Archive
order: 1012
source: https://web.archive.org/web/20070110030518/http://www.java2s.com:80/Code/Java/Apache-Common/CloneObject.htm
---
```java title=Example.java
import org.apache.commons.beanutils.BeanUtils;
import java.util.Map;
import java.util.Date;
import java.util.List;
import java.util.HashMap;
import java.util.ArrayList;
import java.util.GregorianCalendar;
public class BeanUtilsExampleV2 {
  public static void main(String args[]) throws Exception {
    BeanUtilsExampleV2 diff = new BeanUtilsExampleV2();
    Movie movieBean = diff.prepareData();
    // create a new Movie with the same properties
    Movie newMovieBean = new Movie();
    BeanUtils.copyProperties(newMovieBean, movieBean);
    // Movie newMovieBean = (Movie)BeanUtils.cloneBean(movieBean);
    // change its title
    BeanUtils.setProperty(newMovieBean, "title", "Quills");
    // and date
    BeanUtils.setProperty(
      newMovieBean,
      "dateOfRelease",
      new GregorianCalendar(2000, 0, 1).getTime());
    // and director name
    BeanUtils.setProperty(newMovieBean, "director.name", "Philip Kaufman");
    // and director's home number
    BeanUtils.setProperty(
      newMovieBean,
      "director.contactNumber(Home)",
      "3349084333");
    System.err.println(BeanUtils.getProperty(movieBean, "title"));
    System.err.println(BeanUtils.getProperty(movieBean, "director.name"));
    System.err.println(BeanUtils.getProperty(
      newMovieBean,
      "director.contactNumber(Home)"));
  }
  private Movie prepareData() {
    Movie movie = new Movie();
    movie.setTitle("The Italian Job");
    movie.setDateOfRelease(new GregorianCalendar(1969, 0, 1).getTime());
    // sets the genre
    Map genre_map = new HashMap();
    genre_map.put("THR", "Thriller");
    genre_map.put("ACT", "Action");
    movie.setGenre(genre_map);
    // creates the Director
    Person director = new Person();
    director.setName("Peter Collinson");
    director.setGender(1);
    Map director_contacts = new HashMap();
    director_contacts.put("Home", "99922233");
    director_contacts.put("Mobile", "0343343433");
    director.setContactNumber(director_contacts);
    movie.setDirector(director);
    // create the actors
    Actor actor1 = new Actor();
    actor1.setName("Michael Caine");
    actor1.setGender(1);
    actor1.setWorth(10000000);
    List actor1_movies = new ArrayList();
    Movie movie2 = new Movie();
    movie2.setTitle("The Fourth Protocol");
    Movie movie3 = new Movie();
    movie3.setTitle("Shiner");
    actor1_movies.add(movie2);
    actor1_movies.add(movie3);
    actor1.setMovieCredits(actor1_movies);
    Actor actor2 = new Actor();
    actor2.setName("Margaret Blye");
    actor2.setGender(2);
    actor2.setWorth(20000000);
    List actors = new ArrayList();
    actors.add(actor1);
    actors.add(actor2);
    movie.setActors(actors);
    return movie;
  }
}
----------------------------------------------------------------------------
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
----------------------------------------------------------------------------
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
----------------------------------------------------------------------------
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
```

Download: BeanUtilsExampleV2.zip ( 880 K )
---
Related examples in the same category
1. Map ResultSet to Object
