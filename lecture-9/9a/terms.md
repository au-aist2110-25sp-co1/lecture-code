# NEW TERMS!!!

## _A quick primer on "Object-Oriented" or "Object-Based" Code_

  - "class"
    
    *Mostly* just another word for "data type". A class "defines" the attributes
    of values of a certain data type, as well as the operations that can be
    performed on those values. Classes can describe simple types (like a number
    or a string) or complex types (like a person or account).

  - "object" or "instance"

    An actual value, usually buy not necessarily stored in a variable. "Paul"
    and 42 are both objects. One is an instance of a string class and the other
    an instance of in integer class. Complex objects like a person would contain
    many simple values (like first_name, last_name, date_of_birth, etc.).

  - "method"

    A special kind of function that is defined within a class. Generally a
    method performs some operation on or using an object's value(s).

  - "constructor"

    A special method that creates a new instance of a class (i.e., an object).
    This is usually just the name of the class (e.g., `str()` or `float()` or
    `int()`). Yes, we've secretly been calling a constructors for strings,
    floats, and ints since VERY early in the course.
  
  - "inheritance"

    The process of defining classes hierarchically, with a "base class" defining
    attributes and operations for a very generic data type and "sub classes"
    that define more specialized forms of the base class. This is  analogous to
    animal classification (kingdom > phylum > class, etc.).
