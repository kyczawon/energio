arr = ['com.lo.py','com.lo_init.py','com.lo.py','com.lo_init.py']
arr2 = filter(lambda x: '_init' not in x, arr)
for lol in arr2:
    print(lol)