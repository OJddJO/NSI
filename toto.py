x = 1037.123456789
print('{:g}'.format(x))
print('{:.3f}'.format(x))
print('{:.3e}'.format(x))
print('{0:20.3f}'.format(x))
print('{0:>20.3f}'.format(x))
print('{0:<20.3f}'.format(x))
print('{0:^20.3f}'.format(x))
print('{0:.3f}; {1:.3f}'.format(x, -x))
print('{0:+.3f}; {1:+.3f}'.format(x, -x))
print('{0: .3f}; {1: .3f}'.format(x, -x))
