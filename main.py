import sys
sys.stdout = open('out.py', 'w')
print('ACC = []')
inlines = []
N = int(input())
for i in range(N):
  inlines.append(input().split(" "))
def init(prelines, loop):
  loops = loop
  indent = ' ' * loops
  lines = [i for i in prelines]
  for i in lines:
    if 'END' in i:
      if len(i) == 1:
        print('exit()')
      else:
        LABEL = i[0]
        print(indent + 'def ' + LABEL + '():')
        print(indent + ' ' + 'exit()')
        print(indent + 'exit()')
    elif len(i) == 2:
      OPCODE = i[0]
      LOC = i[1]
      if OPCODE == 'LOAD':
        if LOC[0] == '=':
          LOC = LOC[1:]
        print(indent + 'ACC.append(' + LOC + ')')
      elif OPCODE == 'STORE':
        print(indent + LOC + ' = ACC[-1]')
      elif OPCODE == 'ADD':
        if LOC[0] == '=':
          LOC = LOC[1:]
        print(indent + 'ACC.append(ACC[-1] + ' + LOC + ')')
      elif OPCODE == 'SUB':
        if LOC[0] == '=':
          LOC = LOC[1:]
        print(indent + 'ACC.append(ACC[-1] - ' + LOC + ')')
      elif OPCODE == 'MULT':
        if LOC[0] == '=':
          LOC = LOC[1:]
        print(indent + 'ACC.append(ACC[-1] *' + LOC + ')')
      elif OPCODE == 'DIV':
        if LOC[0] == '=':
          LOC = LOC[1:]
        print(indent + 'ACC.append(ACC[-1] /' + LOC + ')')
      elif OPCODE == 'READ':
        print(indent + LOC + ' = int(input())')
      elif OPCODE == 'PRINT':
        print(indent + 'print(' + LOC + ')')
      elif OPCODE == 'BG':
        print(indent + 'if ACC[-1] > 0:')
        print(indent + ' ' + LOC + '()')
      elif OPCODE == 'BE':
        print(indent + 'if ACC[-1] == 0:')
        print(indent + ' ' + LOC + '()')
      elif OPCODE == 'BL':
        print(indent + 'if ACC[-1] < 0:')
        print(indent + ' ' + LOC + '()')
      elif OPCODE == 'BU':
        print(indent + LOC + '()')
    elif len(i) == 3:
      LABEL = i[0]
      OPCODE = i[1]
      LOC = i[2]
      if OPCODE == 'DC':
        print(indent + LABEL + ' = ' + LOC)
      elif OPCODE == 'LOAD':
        print(indent + 'def ' + LABEL + '():')
        print(indent + ' ' + 'ACC.append(' + LOC + ')')
        xlines = [i for i in lines]
        lines = lines[lines.index(i)+1:]
        loop += 1
        init(lines, loops+1)
        print(indent + 'ACC.append(' + LOC + ')')
        linex = [i for i in xlines]
        loop -= 1
      elif OPCODE == 'STORE':
        print(indent + 'def ' + LABEL + '():')
        print(indent + ' ' + LOC + ' = ACC[-1]')
        xlines = [i for i in lines]
        lines = lines[lines.index(i)+1:]
        loop += 1
        init(lines, loops+1)
        print(indent + LOC + ' = ACC[-1]')
        linex = [i for i in xlines]
        loop -= 1
      elif OPCODE == 'ADD':
        print(indent + 'def ' + LABEL + '():')
        if LOC[0] == '=':
          LOC = LOC[1:]
        print(indent + ' ' + 'ACC.append(ACC[-1] + ' + LOC + ')')
        xlines = [i for i in lines]
        lines = lines[lines.index(i)+1:]
        loop += 1
        init(lines, loops+1)
        if LOC[0] == '=':
          LOC = LOC[1:]
        print(indent + 'ACC.append(ACC[-1] + ' + LOC + ')')
        linex = [i for i in xlines]
        loop -= 1
      elif OPCODE == 'SUB':
        print(indent + 'def ' + LABEL + '():')
        if LOC[0] == '=':
          LOC = LOC[1:]
        print(indent + ' ' + 'ACC.append(ACC[-1] - ' + LOC + ')')
        xlines = [i for i in lines]
        lines = lines[lines.index(i)+1:]
        loop += 1
        init(lines, loops+1)
        if LOC[0] == '=':
          LOC = LOC[1:]
        print(indent + 'ACC.append(ACC[-1] - ' + LOC + ')')
        linex = [i for i in xlines]
        loop -= 1
      elif OPCODE == 'MULT':
        print(indent + 'def ' + LABEL + '():')
        if LOC[0] == '=':
          LOC = LOC[1:]
        print(indent + ' ' + 'ACC.append(ACC[-1] * ' + LOC + ')')
        xlines = [i for i in lines]
        lines = lines[lines.index(i)+1:]
        loop += 1
        init(lines, loops+1)
        if LOC[0] == '=':
          LOC = LOC[1:]
        print(indent + 'ACC.append(ACC[-1] * ' + LOC + ')')
        linex = [i for i in xlines]
        loop -= 1
      elif OPCODE == 'DIV':
        print(indent + 'def ' + LABEL + '():')
        if LOC[0] == '=':
          LOC = LOC[1:]
        print(indent + 'ACC.append(ACC[-1] / ' + LOC + ')')
        xlines = [i for i in lines]
        lines = lines[lines.index(i)+1:]
        loop += 1
        init(lines, loops+1)
        if LOC[0] == '=':
          LOC = LOC[1:]
        print(indent + 'ACC.append(ACC[-1] / ' + LOC + ')')
        linex = [i for i in xlines]
        loop -= 1
      elif OPCODE == 'READ':
        print(indent + 'def ' + LABEL + '():')
        print(indent + ' ' + LOC + ' = int(input())')
        xlines = [i for i in lines]
        lines = lines[lines.index(i)+1:]
        loop += 1
        init(lines, loops+1)
        print(indent + LOC + ' = int(input())')
        linex = [i for i in xlines]
        loop -= 1
      elif OPCODE == 'PRINT':
        print(indent + 'def ' + LABEL + '():')
        print(indent + ' ' + 'print(' + LOC + ')')
        xlines = [i for i in lines]
        lines = lines[lines.index(i)+1:]
        loop += 1
        init(lines, loops+1)
        print(indent + 'print(' + LOC + ')')
        linex = [i for i in xlines]
        loop -= 1
      else:
        print('print("ERROR: OPCODE DOES NOT SUPPORT LABELS")')
    else:
      print('print("ERROR: LABEL OPCODE LOC FORMAT NOT FOLLOWED")')
init(inlines, 0)
print('print("ACC:", ACC)')
