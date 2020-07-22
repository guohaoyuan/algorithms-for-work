class A:
    pass

class B(A):
    pass

print(isinstance(B(), A))
print(isinstance(A(), B))
print(type(B()) == A)