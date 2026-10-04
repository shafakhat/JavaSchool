---
title: Java IO Tutorial - Java File Owner Permissions
nav: Java IO Tutorial - Java Fi...
description: We need to work with UserPrincipal and GroupPrincipal interfaces to manage the owner of a file.
section: Imported - java2s Archive
order: 50236
source: https://www.java2s.com/Tutorials/Java/Java_io/1030__Java_nio_File_Owner_Permissions.html
---
There are three ways to manage the owner of a file:

- Using Files.getOwner()and Files.setOwner() methods.
- Using Files.getAttribute() and Files.setAttribute() methods using "owner" as the attribute name.
- Using the FileOwnerAttributeView.

We need to work with UserPrincipal and GroupPrincipal interfaces to manage the owner of a file.

The owner of a file could be a user or a group.

A UserPrincipal represents a user. A GroupPrincipal represents a group.

When we read the owner of a file, we get an instance of UserPrincipal. Call the getName() method on the UserPrincipal object to get the name of the user.

To set the owner of a file, get an object of the UserPrincipal from a user name.

To get a UserPrincipal from the file system, use an instance of the UserPrincipalLookupService class, which we can get using the getUserPrincipalLookupService() method of the FileSystem class.

The following code gets a UserPrincipal object for a user whose user id is myName:

```java title=Example.java
FileSystem fs  = FileSystems.getDefault();
UserPrincipalLookupService upls  = fs.getUserPrincipalLookupService();
UserPrincipal user = upls.lookupPrincipalByName("myName");
System.out.format("User principal name is %s%n", user.getName());
```

The following code shows how to change the Owner of a File Using the FileOwnerAttributeView.

```java title=Example.java
import java.io.IOException;
import java.nio.file.FileSystem;
import java.nio.file.FileSystems;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.attribute.FileOwnerAttributeView;
import java.nio.file.attribute.UserPrincipal;
import java.nio.file.attribute.UserPrincipalLookupService;
publicclass Main {
  publicstaticvoid main(String[] args) throws Exception {
      Path path = Paths.get("C:\\Java_Dev\\test1.txt");
      FileOwnerAttributeView foav = Files.getFileAttributeView(path,
          FileOwnerAttributeView.class);
      UserPrincipal owner = foav.getOwner();
      System.out.format("Original owner  of  %s  is %s%n", path,
          owner.getName());
      FileSystem fs = FileSystems.getDefault();
      UserPrincipalLookupService upls = fs.getUserPrincipalLookupService();
      UserPrincipal newOwner = upls.lookupPrincipalByName("brice");
      foav.setOwner(newOwner);
      UserPrincipal changedOwner = foav.getOwner();
      System.out.format("New owner  of  %s  is %s%n", path,
          changedOwner.getName());
  }
}
```

The following code uses the Files.setOwner() method to update the owner of a file identified with the path C:\Java_Dev\test1.txt on Windows:

```java title=Example.java
UserPrincipal owner  = get   the   owner;
Path  path   = Paths.get("C:\\Java_Dev\\test1.txt");
Files.setOwner(path,  owner);
```

## ACL File Permissions

ACL type file attributes are supported on Microsoft Windows.

An ACL consists of an ordered list of access control entries. Each entry consists of a UserPrincipal, the type of access, and the level of the access to an object.

AclEntry class represents an entry in an ACL.

To get and set a List of AclEntry for a file using the getAcl() and setAcl() methods of the AclFileAttributeView.

The following code gets the List of ACL entries for a file called C:\Java_Dev\test1.txt:

```java title=Example.java
Path  path   = Paths.get("C:\\Java_Dev\\test1.txt");
AclFileAttributeView view  = Files.getFileAttributeView(path,  AclFileAttributeView.class);
List<AclEntry> aclEntries = view.getAcl();
```

AclEntry class can read various properties of an ACL entry. Its principal() method returns the UserPrincipal to identify the user or the group.

permissions() from AclEntry returns a set of AclEntryPermission objects to identify the permissions.

type() method from AclEntry returns an enum constant of the type AclEntryType such as ALARM, ALLOW, AUDIT, and DENY that indicates the type of the access.

flags() method from AclEntry returns a Set of AclEntryFlag enum constants, which contains the inheritance flags of the ACL entry.

The following code shows how to read ACL entries for file C:\Java_Dev\test1.txt.

```java title=Example.java
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.attribute.AclEntry;
import java.nio.file.attribute.AclEntryPermission;
import java.nio.file.attribute.AclFileAttributeView;
import java.util.List;
import java.util.Set;
publicclass Main {
  publicstaticvoid main(String[] args) throws Exception {
    Path path = Paths.get("C:\\Java_Dev\\test1.txt");
    AclFileAttributeView aclView = Files.getFileAttributeView(path,
        AclFileAttributeView.class);
    if (aclView == null) {
      System.out.format("ACL view  is not  supported.%n");
      return;
    }
    List<AclEntry> aclEntries = aclView.getAcl();
    for (AclEntry entry : aclEntries) {
      System.out.format("Principal: %s%n", entry.principal());
      System.out.format("Type: %s%n", entry.type());
      System.out.format("Permissions are:%n");
      Set<AclEntryPermission> permissions = entry.permissions();
      for (AclEntryPermission p : permissions) {
        System.out.format("%s %n", p);
      }
    }
  }
}
```

## Example

The following code shows how to add a new ACL entry for a user named brice. It adds DATA_READ and DATA_ WRITE permissions for the user on the C:\Java_Dev\test1.txt file.

```java title=Example.java
importstatic java.nio.file.attribute.AclEntryPermission.READ_DATA;
importstatic java.nio.file.attribute.AclEntryPermission.WRITE_DATA;
import java.io.IOException;
import java.nio.file.FileSystems;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.attribute.AclEntry;
import java.nio.file.attribute.AclEntryPermission;
import java.nio.file.attribute.AclEntryType;
import java.nio.file.attribute.AclFileAttributeView;
import java.nio.file.attribute.UserPrincipal;
import java.util.EnumSet;
import java.util.List;
import java.util.Set;
publicclass Main {
  publicstaticvoid main(String[] args) throws Exception {
    Path path = Paths.get("C:\\Java_Dev\\test1.txt");
    AclFileAttributeView aclView = Files.getFileAttributeView(path,
        AclFileAttributeView.class);
    if (aclView == null) {
      System.out.format("ACL view  is not  supported.%n");
      return;
    }
    UserPrincipal bRiceUser = FileSystems.getDefault()
        .getUserPrincipalLookupService().lookupPrincipalByName("brice");
    Set<AclEntryPermission> permissions = EnumSet.of(READ_DATA, WRITE_DATA);
    AclEntry.Builder builder = AclEntry.newBuilder();
    builder.setPrincipal(bRiceUser);
    builder.setType(AclEntryType.ALLOW);
    builder.setPermissions(permissions);
    AclEntry newEntry = builder.build();
    List<AclEntry> aclEntries = aclView.getAcl();
    aclEntries.add(newEntry);
    aclView.setAcl(aclEntries);
  }
}
```

## POSIX File Permissions

UNIX supports POSIX standard file attributes. POSIX file permissions consist of nine components:

- three for the owner
- three for the group
- three for others

The three types of permissions are read, write, and execute.

A typical POSIX file permission in a string form looks like "rw-rw----", which has read and write permissions for the owner and the group.

The PosixFilePermission enum type defines nine constants, one for each permission component.

The nine constants are named as X_Y, where X is OWNER, GROUP, and OTHERS, and Y is READ, WRITE, and EXECUTE.

PosixFilePermissions is a utility class that has methods to convert the POSIX permissions of a file from one form to another.

Its toString() method converts a Set of PosixFilePermission enum constants into a string of the rwxrwxrwx form.

Its fromString() method converts the POSIX file permissions in a string of the rwxrwxrwx form to a Set of PosixFilePermission enum constants.

Its asFileAttribute() method converts a Set of PosixFilePermission enum constants into a FileAttribute object.

The following code reads and prints POSIX file permissions in the rwxrwxrwx form for a file named test in the default directory:

```java title=Example.java
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.attribute.PosixFileAttributeView;
import java.nio.file.attribute.PosixFileAttributes;
import java.nio.file.attribute.PosixFilePermission;
import java.nio.file.attribute.PosixFilePermissions;
import java.util.Set;
publicclass Main {
  publicstatic void main(String[] argv)throws Exception {
    Path path = Paths.get("test");
    PosixFileAttributeView posixView = Files.getFileAttributeView(path,
        PosixFileAttributeView.class);
    PosixFileAttributes attribs = posixView.readAttributes();
    Set<PosixFilePermission> permissions = attribs.permissions();
    // Convert the file permissions into the rwxrwxrwx string form
    String rwxFormPermissions = PosixFilePermissions.toString(permissions);
    // Print the permissions
    System.out.println(rwxFormPermissions);
  }
}
```

To update the POSIX file permissions, call the setPermissions() method of PosixFileAttributeView, passing the Set of the PosixFilePermission enum constants as an argument.

The following code shows how to set the POSIX file permissions:

```java title=Example.java
String rwxFormPermissions = "rw-r-----";
Set<PosixFilePermission> permissions = PosixFilePermissions.fromString(rwxFormPermissions);
posixView.setPermissions(permissions);
```

The following code creates a Set of PosixFilePermission enum constants directly and set it as the file permissions.

```java title=Example.java
Set<PosixFilePermission> permissions = EnumSet.of(OWNER_READ,  OWNER_WRITE, GROUP_READ);
posixView.setPermissions(permissions);
```

The following code demonstrates how to read and update POSIX file permissions for a file named test on UNIX-like platforms.

```java title=Example.java
importstatic java.nio.file.attribute.PosixFilePermission.GROUP_READ;
importstatic java.nio.file.attribute.PosixFilePermission.OWNER_READ;
importstatic java.nio.file.attribute.PosixFilePermission.OWNER_WRITE;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.attribute.PosixFileAttributeView;
import java.nio.file.attribute.PosixFileAttributes;
import java.nio.file.attribute.PosixFilePermission;
import java.nio.file.attribute.PosixFilePermissions;
import java.util.EnumSet;
import java.util.Set;
publicclass Main {
  publicstaticvoid main(String[] args) throws Exception {
    Path path = Paths.get("test");
    PosixFileAttributeView posixView = Files.getFileAttributeView(path,
        PosixFileAttributeView.class);
    if (posixView == null) {
      System.out.format("POSIX attribute view  is not  supported%n.");
      return;
    }
    readPermissions(posixView);
    updatePermissions(posixView);
  }
  publicstaticvoid readPermissions(PosixFileAttributeView posixView)
      throws Exception {
    PosixFileAttributes attribs;
    attribs = posixView.readAttributes();
    Set<PosixFilePermission> permissions = attribs.permissions();
    // Convert the set of posix file permissions into rwxrwxrwx form
    String rwxFormPermissions = PosixFilePermissions.toString(permissions);
    System.out.println(rwxFormPermissions);
  }
  publicstaticvoid updatePermissions(PosixFileAttributeView posixView)
      throws Exception {
    Set<PosixFilePermission> permissions = EnumSet.of(OWNER_READ, OWNER_WRITE,
        GROUP_READ);
    posixView.setPermissions(permissions);
    System.out.println("Permissions set successfully.");
  }
}
```

The code above generates the following result.

- « Previous
