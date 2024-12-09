from sml_core import sml_core
from sml import sml_globals

a = sml_core()
a.get('a.b')

a.set('a.b.c','Hello, world!')
print(a.get('a.b.c'))

a.get('q.w.e')
a.get('q.w.r')
a.set('q.w.a', (1,2,3))
a.ls('q.w')



func = sml_globals.get('**')
print(func)
print(func(12,2))
