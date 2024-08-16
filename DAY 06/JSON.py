import json
xyz = '{"Name": "Tanvir Rahman Tonoy", "Age": 21, "City": "Dhaka"}'
print(type(xyz))

a = json.loads(xyz)
print(type(a))
print(a)
print(a["Name"])
z = json.dumps(a, indent=4)
print(type(z))
print(z)