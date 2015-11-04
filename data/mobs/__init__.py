maxlevel=2
__all__=["level%i"%(i+1) for i in range(maxlevel)]
for i in __all__: exec("import %s"%i)
