class User:
  def __init__(self, fname, lname, role, age):
    self.fname = fname
    self.lname = lname
    self.role = role
    self.age = age

adminFilePath = "Datnes/admin.txt"
viesisFilePath = "Datnes/viesis.txt"
allUsers = []

with open(adminFilePath) as f:
  [
    allUsers.append(
      User(line.split(",")[0], line.split(",")[1], line.split(",")[2], line.split(",")[3])
    ) for line in f.readlines()
  ]

with open(viesisFilePath) as f:
  [
    allUsers.append(
      User(line.split(",")[0], line.split(",")[1], line.split(",")[2], line.split(",")[3])
    ) for line in f.readlines()
  ]
  
adminuserAges = []
adminCount = 0;
viesisCount = 0;
print("visi lietotaji:")
for user in allUsers:
  if user.role == "admin":
    adminCount += 1
    adminuserAges.append(int(user.age))
  if user.role == "viesis":
    viesisCount += 1

  print(user.fname + " " + user.lname)

print("\nadmin vecumi:")
print("videjais vecums - " + str(sum(adminuserAges)/len(adminuserAges)))
print("jaunākais - " + str(min(adminuserAges)))
print("vecākais - " + str(max(adminuserAges)))

print("\nLietotaju daudzums:")
print("admin - " + str(adminCount))
print("viesis - " + str(viesisCount))