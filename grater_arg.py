def big( x, y ):
    if x > y:
        return x
    return y
def maximum( x, y, z ):
    return big( x, big( y, z ) )
print(maximum(3, 6, -5))
