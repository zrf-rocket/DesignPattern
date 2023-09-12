from singleton import singleton_instance
singleton_instance.do_something()
print(id(singleton_instance))  # 2636891172368

from singleton import singleton_instance
print(id(singleton_instance))  # 2636891172368






