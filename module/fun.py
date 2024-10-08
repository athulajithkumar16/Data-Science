# MODULES 

# Syntax
# import modulename
# modulename.functionName

# import intro
# result = intro.hello()
# print(result)

# ------------------------------------------------------------------------------------------

# directory >>> mypackage (folder) => __init__.py (package) >>> data.py (module), greet.py (module)


from mypackage import data,greet
# from packageName import moduleName
data.test()
# moduleName.functionName()

greet.hello()

# import sys