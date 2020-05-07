from pysword.modules import SwordModules
modules = SwordModules()
found_modules = modules.parse_modules()
print(found_modules)
bible = modules.get_bible_from_module(u'KJV')
output = bible.get(books=[u'john'], chapters=[3], verses=[16])
print(output)