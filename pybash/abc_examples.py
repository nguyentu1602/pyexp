"""
WHY USE ABSTRACT BASE CLASSES?

    Abstract base classes are a form of interface checking more strict than individual hasattr() checks 
    for particular methods. By defining an abstract base class, a common API can be established for
    a set of subclasses. This capability is especially useful in situations where someone less familiar 
    with the source for an application is going to provide plug-in extensions, but can also help when
    working on a large team or with a large code-base where keeping track of all of the classes at the
    same time is difficult or not possible.

HOW DOES ABCs WORK?
    - abc works by marking methods of the base class as abstract, and then registering concrete classes
        as implementations of the abstract base. 
    - If an application or library requires a particular API, issubclass() or isinstance() can be used to
        check an object against the abstract class.


"""

import abc
from sys import implementation
# define and abstract base class to represent the API of a set of plug-ins for saving and loading data
# set metaclass for the new base class to ABCMeta, and use decorators to establish public API for it
class PluginBase(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def load(self, input):
        """retrieve data from the input source and return an object
        
        Args:
            input (_type_): _description_
        """
    @abc.abstractmethod
    def save(self, output, data):
        """save the data object to the output

        Args:
            output (_type_): _description_
            data (_type_): _description_
        """


# There are two ways to indicate that a concrete class implements an abstract API: 
# 1. explicitly register the class
#    Use the register() class method as a decorator on a concrete class to add it explicitly when the
#    class provides the required API, but is not part of the inheritance tree of the abstract base class.
# 2. create a new subclass directly from the abstract base. 
 

        
class LocalBaseClass:
    pass


@PluginBase.register
class RegisteredImplementation(LocalBaseClass):
    def load(self, input):
        return input.read()
    
    def save(self, output, data):
        return output.write(data)

    
if __name__ == '__main__':
    print(f"RegisteredImplementation: Subclass: {issubclass(RegisteredImplementation,  PluginBase)}")
    print(f"RegisteredImplementation: Instance: {isinstance(RegisteredImplementation(), PluginBase)}")
    
# Subclass directly from the base avoids the need to register the class explicitly:

class SubclassImplementation(PluginBase):

    def load(self, input):
        return input.read()

    def save(self, output, data):
        return output.write(data)


if __name__ == '__main__':
    print('SubclassImplementation: Subclass:', issubclass(SubclassImplementation, PluginBase))
    print('SubclassImplementation: Instance:', isinstance(SubclassImplementation(), PluginBase))
# Here, normal Python class management features are used to recognize  SubclassImplementation as 
# implementing the abstract PluginBase.

# We can find all of the implementations of a plugin by asking the base class for the list of 
# known classes derived from it.
for sc in PluginBase.__subclasses__():
    print(f"All implementations of PlugingBase: {sc.__name__}")

# Even though RegisteredImplementation is in the scope, it is not among the list of subclasses 
# because it is not actually derived from the base.


####################
## HELPER base class
####################
# Forgetting to set the metaclass properly means the concrete implementations do not have their APIs enforced.
# To make it easier to set up the abstract class properly, a base class is provided that sets the metaclass 
# automatically.

class PluginBaseDirect(abc.ABC):
    @abc.abstractmethod
    def load(self, input):
        """Retrieve data from the input source
        and return an object.
        """

    @abc.abstractmethod
    def save(self, output, data):
        """Save the data object to the output."""


class SubclassImplementation1(PluginBaseDirect):

    def load(self, input):
        return input.read()

    def save(self, output, data):
        return output.write(data)

if __name__ == '__main__':
    print('SubclassImplementation1 Subclass:', issubclass(SubclassImplementation1, PluginBaseDirect))
    print('SubclassImplementation1 Instance:', isinstance(SubclassImplementation1(), PluginBaseDirect))
    
##################################
## Incomplete implementations:
# ################################
# Another benefit of subclassing directly from the abstract base class is that the subclass cannot be 
# instantiated unless it fully implements the abstract portion of the API.
# This feature keeps incomplete implementations from triggering unexpected errors at runtime
################################

@PluginBase.register
class IncompleteImplementation(PluginBase):

    def save(self, output, data):
        return output.write(data)


if __name__ == '__main__':
    print('Subclass:', issubclass(IncompleteImplementation,  PluginBase))
    try: 
        print('Instance:', isinstance(IncompleteImplementation(),PluginBase))  # cant's instantiate
    except Exception as ex:
        print(f"ex: {ex}")
        
    
####################################################################################################

#########################################
## Concrete Methods in ABCs
#########################################
# Although a concrete class must provide implementations of all abstract methods, the abstract base class
# can also provide implementations that can be invoked via super(). This allows common logic to be reused
# by placing it in the base class, but forces subclasses to provide an overriding method with (potentially) 
# custom logic.
#########################################
import io

class ABCWithConcreteImplementation(abc.ABC):

    @abc.abstractmethod
    def retrieve_values(self, input):
        print('base class reading data') # common logic can be put here
        return input.read()
    
    
class ConcreteOverride(ABCWithConcreteImplementation):
    
    def retrieve_values(self, input):
        base_data = super(ConcreteOverride, self).retrieve_values(input)  # calling same name method in base class
        print('subclass sorting data')
        response = sorted(base_data.splitlines())
        return response
    
input = io.StringIO("""line one
line two
line three
""")

reader = ConcreteOverride()
print(reader.retrieve_values(input))
print()


######################################
## Abstract Properties
######################################
# if an API specification includes attributes in addition to methods, it can require the attributes in
# concrete classes by combining abstractmethod() with property().

class Base(abc.ABC):
    """Cannot be instanstiated because it has only an abtract version of the property getter methods 
        for value and constant.
    """
    @property
    @abc.abstractmethod
    def value(self):
        return 'should never reach here'
    
    @property
    @abc.abstractmethod
    def constant(self):
        return 'Should never reach here'
    
    
class Implementation(Base):
    @property
    def value(self):
        return 'concrete property'
    
    constant = 'set by a class attribute'
    
try:
    b = Base()
    print('Base.value', b.value)
except Exception as err:
    print(f'ERROR: {str(err)}')
    
i = Implementation()
print(f'Implementation.value:   \t {i.value}')    
print(f'Implementation.constant:\t {i.constant}')    

##############################
## Abstract read-write properties
# 
#   To use the decorator syntax with read-write abstract properties, the methods to get and set the value
#   must be named the same.
##############################
class BaseRW(abc.ABC):
    @property
    @abc.abstractmethod
    def value(self):
        return 'Should never reach here'

    @value.setter
    @abc.abstractmethod
    def value(self, new_value):
        return
    
    
class PartialImplementation(BaseRW):
    """The concrete property must be defined the same way as the abstract property, as either read-write
        or read-only. 
        Overriding a read-write property in PartialImplementation with one that is read-only leaves the property
        read-only - the property's setter method from the base class is NOT reused.
    """
    @property
    def value(self):
        return 'Read only'
    

class FullImplementation(BaseRW):
    _value = 'Default value'
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_value):
        self._value = new_value

    
try:
    b = BaseRW()
    print(f'BaseRW.value: {b.value}')   
except Exception as err:
    print(f'ERROR: {str(err)}')

p = PartialImplementation()
print(f'PartialImplementation.value: {p.value}')

try:
    p.value = 'Alteration'
    print(f'PartialImplementation.value: {p.value}')
except Exception as err:
    print(f'Error: {str(err)}')
    
i = FullImplementation()
print(f'FullImplementation.value: {i.value}')

i.value = 'New Value'
print(f'FullImplementation changed value: {i.value}')


#########################################################
## Abstract class and static methods
#########################################################
# class and static methods can also be marked as abstract
#
# In the below example, Although the class method is invoked on the class rather than an instance,
# it still prevents the class from being instantiated if it is not defined.
 

class BaseStatic(abc.ABC):
    @classmethod
    @abc.abstractmethod
    def factory(cls, *args):
        return cls()
    
    @staticmethod
    @abc.abstractmethod
    def const_behavior():
        return 'should never reach here'
    
class ImplementationStatic(BaseStatic):
    def do_something(self):
        pass
    
    @classmethod
    def factory(cls, *args):
        obj = cls(*args)
        obj.do_something()
        return obj
    
    @staticmethod
    def const_behavior():
        return 'static behavior differs'
    
    
try:
    o = BaseStatic.factory()
    print(f'BaseStatic.value: {o.const_behavior()}')
except Exception as err:
    print(f'ERROR: {str(err)}')

i = ImplementationStatic.factory()
print(f'ImplementationStatic.const_behavior {i.const_behavior()}')