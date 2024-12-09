from sml_core import sml_core

sml_globals = sml_core()
sml_globals.set('**', lambda x, y: x ** y)
