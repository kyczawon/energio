import os, subprocess
app = "com.android.chrome"
res = subprocess.check_output(["adb","shell","pm","clear",app])

for line in res.splitlines():
    text = line.decode()
    if (text == 'Success'):
        print('Sucesfully cleared cache of '+app)
    else:
        print(line.decode())