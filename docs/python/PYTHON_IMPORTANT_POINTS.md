# Python Important Points

> Publication note: reformatted from private study notes. Employer-specific personal details and confidential context have been removed or generalized.

Interview Question #1

## Why is a list mutable but a tuple immutable?

Answer

Lists are designed for dynamic modification.

Tuples are designed for fixed collections that should not change.

Because tuples are immutable:

* Safer
* Faster in some situations
* Hashable (sometimes)
* Can be used as dictionary keys

## Why can a tuple be used as a dictionary key but a list cannot?
Dictionary keys must be hashable. A list is mutable and its value can change. Even if tuple contains a mutable object, it still going to
throw out the error as everything inside must also be hashable.

Python passes object references.
For mutable objects, modifications can affect the original object. For immutable objects, operations usually create new objects.

Python variables hold references to objects. Mutable objects can be modified in place,
causing changes to be visible through all references. Immutable objects cannot be modified, so operations create new objects instead.

Mutates Original Object:
Changes are visible outside the function.
append()
extend()
remove()
pop()
sort()
update()
add()

Original object remains unchanged:
+
sorted()
replace()
upper()
lower()

## What is a shallow copy?
A shallow copy creates a new outer object but keeps references to nested objects.

## What is a deep copy?
A deep copy recursively copies all nested objects, creating a completely independent structure.

Interview Cheatsheet:

Operation           Copy Type

b = a               No copy

b = a.copy()        Shallow

b = a[:]            Shallow

b = list(a)         Shallow

copy.copy(a)        Shallow

copy.deepcopy(a)    Deep

## Is Python pass-by-reference?
Python passes object references. The behavior depends on whether the object is mutated or reassigned.
Mutable objects can be modified inside a function and those changes are visible outside.
Reassigning a parameter only changes the local reference.

Error                                             Meaning

AttributeError                                    Object doesn't have method/property

NoneType Error                                    Trying to use None like an object

KeyError                                          Missing dictionary key

IndexError                                        List index out of range

TypeError                                         Wrong type operation

ValueError                                        Invalid value

NameError                                         Variable not defined

ModuleNotFoundError                               Package missing

ImportError                                       Import target missing

FileNotFoundError                                 File/path missing

PermissionError                                   Access denied

MemoryError                                       Out of memory

ZeroDivisionError                                 Divide by zero
