import sys
sys.stdin = open('in.asm', 'r')
lines = []
for line in sys.stdin:
  append_value = line.split(" ")
  if len(append_value) > 1: append_value[-1] = append_value[-1][:-1]
  lines.append(append_value)
sys.stdin = sys.__stdin__
ACC = []
varlocs = {}
branchlocs = {}
OPCODES = ['LOAD','STORE','ADD','SUB','MULT','DIV','BG','BE','BL','BU','READ','PRINT','DC','END']
for i in range(len(lines)):
  if lines[i][0] not in OPCODES and lines[i][1] != "DC":
    branchlocs[lines[i][0]] = lines.index(lines[i])-1
    lines[i].pop(0)
done = False
i = 0
while not done:
  line = lines[i]
  if len(line) == 2:
    OPCODE = line[0]
    LOC = line[-1]
    immediate = False
    if LOC[0] == "=": LOC = LOC[1:]; immediate = True
    if OPCODE == "LOAD":
      ACC.append(varlocs[LOC]) if not immediate else ACC.append(int(LOC))
    elif OPCODE == "STORE":
      varlocs[LOC] = ACC[-1]
    elif OPCODE == "ADD":
      ACC.append(ACC[-1] + varlocs[LOC]) if not immediate else ACC.append(ACC[-1] + int(LOC))
    elif OPCODE == "SUB":
      ACC.append(ACC[-1] - varlocs[LOC]) if not immediate else ACC.append(ACC[-1] - int(LOC))
    elif OPCODE == "MULT":
      ACC.append(ACC[-1] * varlocs[LOC]) if not immediate else ACC.append(ACC[-1] * int(LOC))
    elif OPCODE == "DIV":
      ACC.append(ACC[-1] / varlocs[LOC]) if not immediate else ACC.append(ACC[-1] / int(LOC))
    elif OPCODE == "BG":
      if ACC[-1] > 0: i = branchlocs[LOC]
    elif OPCODE == "BE":
      if ACC[-1] == 0: i = branchlocs[LOC]
    elif OPCODE == "BL":
      if ACC[-1] < 0: i = branchlocs[LOC]
    elif OPCODE == "BU":
      i = branchlocs[LOC]
    elif OPCODE == "READ":
      varlocs[LOC] = int(input("READ: "))
    elif OPCODE == "PRINT":
      print("PRINT:", varlocs[LOC]) if not immediate else print("PRINT:", LOC)
    else:
      done = True
  elif len(line) == 3:
    LABEL = line[0]
    OPCODE = line[1]
    LOC = line[-1]
    if OPCODE == "DC":
      varlocs[LABEL] = int(LOC)
    else:
      done = True
  else:
    done = True
  i += 1
for i in varlocs.keys():
  print(i + ":", varlocs[i])
print("ACC:", ACC)
