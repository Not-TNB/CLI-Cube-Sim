from colorama import *
import random
import time
import os
from itertools import groupby, chain
from collections import Counter
init() # colorama

vis2 = '''

          /-------/-------/|
         /aaaaaaa/bbbbbbb/j|
        /-------/-------/|j|
       /ccccccc/ddddddd/i|j|
      /-------/-------/ii|j|
      |eeeeeee|fffffff|ii|/|
      |eeeeeee|fffffff|ii|l|
      |eeeeeee|fffffff|i/|l|
      |-------|-------|/k|l/
      |ggggggg|hhhhhhh|kk|/
      |ggggggg|hhhhhhh|kk/
      |ggggggg|hhhhhhh|k/
      |-------|-------|/


'''

vis3 = '''

          /--------/--------/--------/|
         /aaaaaaaa/bbbbbbbb/cccccccc/u|
        /--------/--------/--------/|u|
       /dddddddd/eeeeeeee/ffffffff/t|u|
      /--------/--------/--------/|t|u|
     /gggggggg/hhhhhhhh/iiiiiiii/s|t|/|
    /--------/--------/--------/ss|t|x|
    |jjjjjjjj|kkkkkkkk|llllllll|ss|/|x|
    |jjjjjjjj|kkkkkkkk|llllllll|ss|w|x|
    |jjjjjjjj|kkkkkkkk|llllllll|s/|w|/|
    |--------|--------|--------|/v|w|.|
    |mmmmmmmm|nnnnnnnn|oooooooo|vv|/|.|
    |mmmmmmmm|nnnnnnnn|oooooooo|vv|z|./
    |mmmmmmmm|nnnnnnnn|oooooooo|v/|z|/
    |--------|--------|--------|/y|z/
    |pppppppp|qqqqqqqq|rrrrrrrr|yy|/
    |pppppppp|qqqqqqqq|rrrrrrrr|yy/
    |pppppppp|qqqqqqqq|rrrrrrrr|y/
    |--------|--------|--------|/


'''

vis4 = '''

            /--------/--------/--------/--------/|
           /aaaaaaaa/bbbbbbbb/cccccccc/dddddddd/J|
          /--------/--------/--------/--------/|J|
         /eeeeeeee/ffffffff/gggggggg/hhhhhhhh/I|J|
        /--------/--------/--------/--------/|I|J|
       /iiiiiiii/jjjjjjjj/kkkkkkkk/llllllll/H|I|/|
      /--------/--------/--------/--------/|H|I|N|
     /mmmmmmmm/nnnnnnnn/oooooooo/pppppppp/G|H|/|N|
    /--------/--------/--------/--------/GG|H|M|N|
    |qqqqqqqq|rrrrrrrr|ssssssss|tttttttt|GG|/|M|/|
    |qqqqqqqq|rrrrrrrr|ssssssss|tttttttt|GG|L|M|R|
    |qqqqqqqq|rrrrrrrr|ssssssss|tttttttt|G/|L|/|R|
    |--------|--------|--------|--------|/K|L|Q|R|
    |uuuuuuuu|vvvvvvvv|wwwwwwww|xxxxxxxx|KK|/|Q|/|
    |uuuuuuuu|vvvvvvvv|wwwwwwww|xxxxxxxx|KK|P|Q|V|
    |uuuuuuuu|vvvvvvvv|wwwwwwww|xxxxxxxx|K/|P|/|V|
    |--------|--------|--------|--------|/O|P|U|V/
    |yyyyyyyy|zzzzzzzz|AAAAAAAA|BBBBBBBB|OO|/|U|/
    |yyyyyyyy|zzzzzzzz|AAAAAAAA|BBBBBBBB|OO|T|U/
    |yyyyyyyy|zzzzzzzz|AAAAAAAA|BBBBBBBB|O/|T|/
    |--------|--------|--------|--------|/S|T/
    |CCCCCCCC|DDDDDDDD|EEEEEEEE|FFFFFFFF|SS|/
    |CCCCCCCC|DDDDDDDD|EEEEEEEE|FFFFFFFF|SS/
    |CCCCCCCC|DDDDDDDD|EEEEEEEE|FFFFFFFF|S/
    |--------|--------|--------|--------|/


'''

vis5 = '''

              /-------/-------/-------/-------/-------/|
             /aaaaaaa/bbbbbbb/ccccccc/ddddddd/eeeeeee/2|
            /-------/-------/-------/-------/-------/|2|
           /fffffff/ggggggg/hhhhhhh/iiiiiii/jjjjjjj/1|2|
          /-------/-------/-------/-------/-------/|1|/|
         /kkkkkkk/lllllll/mmmmmmm/nnnnnnn/ooooooo/0|1|7|
        /-------/-------/-------/-------/-------/|0|/|7|
       /ppppppp/qqqqqqq/rrrrrrr/sssssss/ttttttt/Z|0|6|/|
      /-------/-------/-------/-------/-------/|Z|/|6|!|
     /uuuuuuu/vvvvvvv/wwwwwww/xxxxxxx/yyyyyyy/Y|Z|5|/|!|
    /-------/-------/-------/-------/-------/YY|/|5|,|/|
    |zzzzzzz|AAAAAAA|BBBBBBB|CCCCCCC|DDDDDDD|YY|4|/|,|>|
    |zzzzzzz|AAAAAAA|BBBBBBB|CCCCCCC|DDDDDDD|Y/|4|.|/|>|
    |-------|-------|-------|-------|-------|/3|/|.|<|/|
    |EEEEEEE|FFFFFFF|GGGGGGG|HHHHHHH|IIIIIII|33|9|/|<|=|
    |EEEEEEE|FFFFFFF|GGGGGGG|HHHHHHH|IIIIIII|3/|9|;|/|=/
    |-------|-------|-------|-------|-------|/8|/|;|}|/
    |JJJJJJJ|KKKKKKK|LLLLLLL|MMMMMMM|NNNNNNN|88|:|/|}/
    |JJJJJJJ|KKKKKKK|LLLLLLL|MMMMMMM|NNNNNNN|8/|:|{|/
    |-------|-------|-------|-------|-------|/?|/|{/
    |OOOOOOO|PPPPPPP|QQQQQQQ|RRRRRRR|SSSSSSS|??|)|/
    |OOOOOOO|PPPPPPP|QQQQQQQ|RRRRRRR|SSSSSSS|?/|)/
    |-------|-------|-------|-------|-------|/(|/
    |TTTTTTT|UUUUUUU|VVVVVVV|WWWWWWW|XXXXXXX|((/
    |TTTTTTT|UUUUUUU|VVVVVVV|WWWWWWW|XXXXXXX|(/
    |-------|-------|-------|-------|-------|/


'''


vis6 = r'''

                /-------/-------/-------/-------/-------/-------/|
               /aaaaaaa/bbbbbbb/ccccccc/ddddddd/eeeeeee/fffffff/[|
              /-------/-------/-------/-------/-------/-------/|[|
             /ggggggg/hhhhhhh/iiiiiii/jjjjjjj/kkkkkkk/lllllll/"|[|
            /-------/-------/-------/-------/-------/-------/|"|/|
           /mmmmmmm/nnnnnnn/ooooooo/ppppppp/qqqqqqq/rrrrrrr/'|"|^|
          /-------/-------/-------/-------/-------/-------/|'|/|^|
         /sssssss/ttttttt/uuuuuuu/vvvvvvv/wwwwwww/xxxxxxx/=|'|%|/|
        /-------/-------/-------/-------/-------/-------/|=|/|%|`|
       /yyyyyyy/zzzzzzz/AAAAAAA/BBBBBBB/CCCCCCC/DDDDDDD/}|=|$|/|`|
      /-------/-------/-------/-------/-------/-------/|}|/|$|~|/|
     /EEEEEEE/FFFFFFF/GGGGGGG/HHHHHHH/IIIIIII/JJJJJJJ/{|}|#|/|~|₄|
    /-------/-------/-------/-------/-------/-------/{{|/|#|+|/|₄|
    |KKKKKKK|LLLLLLL|MMMMMMM|NNNNNNN|OOOOOOO|PPPPPPP|{{|@|/|+|₃|/|
    |KKKKKKK|LLLLLLL|MMMMMMM|NNNNNNN|OOOOOOO|PPPPPPP|{/|@|_|/|₃|₊|
    |-------|-------|-------|-------|-------|-------|/]|/|_|₂|/|₊|
    |QQQQQQQ|RRRRRRR|SSSSSSS|TTTTTTT|UUUUUUU|VVVVVVV|]]|*|/|₂|₉|/|
    |QQQQQQQ|RRRRRRR|SSSSSSS|TTTTTTT|UUUUUUU|VVVVVVV|]/|*|₁|/|₉|↓|
    |-------|-------|-------|-------|-------|-------|/&|/|₁|₈|/|↓|
    |WWWWWWW|XXXXXXX|YYYYYYY|ZZZZZZZ|0000000|1111111|&&|₀|/|₈|↑|/
    |WWWWWWW|XXXXXXX|YYYYYYY|ZZZZZZZ|0000000|1111111|&/|₀|₇|/|↑/
    |-------|-------|-------|-------|-------|-------|/\|/|₇|₎|/
    |2222222|3333333|4444444|5555555|6666666|7777777|\\|₆|/|₎/
    |2222222|3333333|4444444|5555555|6666666|7777777|\/|₆|₍|/
    |-------|-------|-------|-------|-------|-------|/₅|/|₍/
    |8888888|9999999|.......|,,,,,,,|!!!!!!!|???????|₅₅|₌|/
    |8888888|9999999|.......|,,,,,,,|!!!!!!!|???????|₅/|₌/
    |-------|-------|-------|-------|-------|-------|/₋|/
    |:::::::|;;;;;;;|<<<<<<<|>>>>>>>|(((((((|)))))))|₋₋/
    |:::::::|;;;;;;;|<<<<<<<|>>>>>>>|(((((((|)))))))|₋/
    |-------|-------|-------|-------|-------|-------|/
'''


class Cube:
  def __init__(self, size=3):
    self.turnTime = 0.1
    self.size = size
    self.area = self.size**2

    self.pos = self.solved = [
      ['w']*self.area, ['o']*self.area, ['g']*self.area,
      ['r']*self.area, ['b']*self.area, ['y']*self.area
    ]    

    # Came up with my own face rotation mapping algorithm instead of the usual transpose+reverse
    # (This is due to the data structure of each face of the club being a 1D list instead of a square matrix, making
    # the usual method more complicated to implement)
    self.Cmap = []*self.area
    self.ACmap = []*self.area

    p1 = (self.area) - self.size
    p2 = self.size - 1

    n = self.area-self.size+1
    for _ in range(self.area):
      self.Cmap.append(int(p1))
      self.ACmap.append(int(p2))

      if (q1 := p1-self.size) >= 0: p1 = q1
      else: p1 += n
      if (q2 := p2+self.size) < self.area: p2 = q2
      else: p2 -= n

  def pieces(self):
    u, l, f, r, b, d = self.pos
    return [
      # CORNERS
      Counter([u[0], b[2], l[0]]), # 0 top back left
      Counter([u[2], b[0], r[2]]), # 1 top back right
      Counter([u[6], f[0], l[2]]), # 2 top front left
      Counter([u[8], f[2], r[0]]), # 3 top front right

      Counter([d[6], b[8], l[6]]), # 4 bottom back left
      Counter([d[8], b[6], r[8]]), # 5 bottom back right
      Counter([d[0], f[6], l[8]]), # 6 bottom front left
      Counter([d[2], f[8], r[6]]), # 7 bottom front right

      # EDGES
      Counter([u[1], b[1]]), # 8  top back
      Counter([u[3], l[1]]), # 9  top left
      Counter([u[5], r[1]]), # 10 top right
      Counter([u[7], f[1]]), # 11 top front

      Counter([b[5], l[3]]), # 12 middle back left
      Counter([b[3], r[5]]), # 13 middle back right
      Counter([f[3], l[5]]), # 14 middle front left
      Counter([f[5], r[3]]), # 15 middle front right

      Counter([d[7], b[7]]), # 16 bottom back
      Counter([d[3], l[7]]), # 17 bottom left
      Counter([d[5], r[7]]), # 18 bottom right
      Counter([d[1], f[7]]), # 19 bottom front

      # CENTERS
      Counter([u[4]]), # 20 U
      Counter([l[4]]), # 21 L
      Counter([f[4]]), # 22 F
      Counter([r[4]]), # 23 R
      Counter([b[4]]), # 24 B
      Counter([d[4]]), # 25 D
    ]

  def isSolved(self):
    def completeFace(f):
      grp = groupby(f)
      return next(grp, True) and not next(grp, False)
    return all(completeFace(f) for f in self.pos)

  def clockwise(self, face):
    return [face[i] for i in self.Cmap]

  def anticlockwise(self, face):
    return [face[i] for i in self.ACmap]

  def uTurn(self):
    u, l, f, r, b, d = self.pos
    self.pos = [
      self.clockwise(u),  
      f[:self.size] + l[self.size:],
      r[:self.size] + f[self.size:],
      b[:self.size] + r[self.size:],
      l[:self.size] + b[self.size:],
      d
    ]

  def xRot(self):
    u, l, f, r, b, d = self.pos
    return [
      f,     
      self.anticlockwise(l),     
      d,     
      self.clockwise(r), 
      u[::-1],     
      b[::-1]
    ]

  def yRot(self):
    u, l, f, r, b, d = self.pos
    return [
      self.clockwise(u), # rotating U face C
      f, r, b, l,
      self.anticlockwise(d)  # rotating D face AC
    ]

  def zRot(self):
    u, l, f, r, b, d = self.pos
    return [
      self.clockwise(l),
      self.clockwise(d),
      self.clockwise(f),
      self.clockwise(u),                  
      self.anticlockwise(b),
      self.clockwise(r)
    ] 

  def turn(self, move):
    # should handle: U, L, F, R, B, D, M, E, S
    # THEIR PRIMES ('), DOUBLES (2) AND WIDE MOVES (NO WIDE MOVES FOR M, E, S)
    # rotations: x, y, z, THEIR PRIMES (') AND DOUBLES (2)
    if move[-1] == '\'': 
      for i in range(3): self.turn(move[:-1])
      return
    if move[-1] == '2': 
      for i in range(2): self.turn(move[:-1])
      return

    match move:
      case 'x': self.pos = self.xRot()
      case 'y': self.pos = self.yRot()
      case 'z': self.pos = self.zRot()      
      case 'U': self.uTurn()
      case 'D': self.algo('x2 U x2')
      case 'L': self.algo('z U z\'')      
      case 'R': self.algo('z\' U z')
      case 'F': self.algo('x U x\'')
      case 'B': self.algo('x\' U x')

      case 'u': self.algo('y D')
      case 'd': self.algo('y\' U')
      case 'l': self.algo('x\' R')
      case 'r': self.algo('x L')
      case 'f': self.algo('z B')
      case 'b': self.algo('z\' F')
      case 'M': self.algo('L\' R x\'')
      case 'E': self.algo('U D\' y\'')
      case 'S': self.algo('F\' B z')

  def algo(self, moves):
    if moves:
      for m in moves.replace('(', '').replace(')', '').split(' '):
        self.turn(m)

  def colorize(self, x):
    return x.replace('o', Fore.MAGENTA+'o'+Fore.WHITE
            ).replace('g', Fore.GREEN+'g'+Fore.WHITE
            ).replace('r', Fore.RED+'r'+Fore.WHITE
            ).replace('b', Fore.BLUE+'b'+Fore.WHITE
            ).replace('y', Fore.YELLOW+'y'+Fore.WHITE)

  def __str__(self, faces=None, template=vis3):
    u, l, f, r, b, d = self.pos
    if faces == None:
      faces = str.maketrans('abcdefghijklmnopqrstuvwxyz.', ''.join(u+f+r))
    return self.colorize(template.translate(faces))

  def reset(self):
    self.pos = self.solved

  def scramble(self, moveNo=None, moves=['U', 'D', 'R', 'L', 'F', 'B']):
    if moveNo == None: moveNo = random.randint(15, 25)
    s = time.process_time()
    alg = []
    for i in range(moveNo):
      while True:
        move = random.choice(moves)
        match random.randint(0, 2):
          case 1: move += '\''
          case 2: move += '2'    
        # balls
        if move[0] != (['balls']+alg)[-1][0]: break

      clear()
      self.turn(move)
      print(self)
      alg.append(move)
      time.sleep(self.turnTime)  
    return alg, time.process_time()-s

  def solve(self):
    alg1 = ''
    clear()

    pt1 = '\n\n--- STEP 1: CROSS ---\n\n'

    match [f[4] for f in self.pos].index('w'):
      case 1: alg1 += 'z'
      case 2: alg1 += 'x'
      case 3: alg1 += 'z\''
      case 4: alg1 += 'x\''
      case 5: alg1 += 'x2'

    if alg1: self.algo(alg1)

    alg2 = ''
    match [f[4] for f in self.pos].index('g'):
      case 1: alg2 += ' y\''
      case 3: alg2 += ' y'
      case 4: alg2 += ' y2'

    if alg2: self.algo(alg2.removeprefix(' '))

    if (alg:=alg1+alg2) != '':
      pt1 += f'Position white top green front: {alg}\n{self}'

    alg = ''

    def flip():
      if self.pos[0][7] != 'w':
        self.algo('F U\' R U')
        return ' (flip: F U\' R U)'
      return ''

    def insertCross(name, hasY):
      alg = ''
      if hasY:
        alg += 'y '
        self.turn('y')

      match self.pieces().index(Counter(['w', name[0]])):
        case 8: alg += 'B\' R2 F\''
        case 9: alg += 'U\''
        case 10: alg += 'R\' F\''
        case 11: alg += ''
        case 12: alg += 'U L U\''
        case 13: alg += 'U\' R\' U'
        case 14: alg += 'F'
        case 15: alg += 'F\''
        case 16: alg += 'D2 F2'
        case 17: alg += 'D F2'
        case 18: alg += 'D\' F2'
        case 19: alg += 'F2'

      self.algo(alg.removeprefix('y '))
      alg += flip()
      return f'Place {name} edge: {alg}\n{self}' if alg != '' else ''

    if (wgResult:=insertCross('green', False)) != '':
      pt1 += wgResult

    pt1 += insertCross('red', True)
    pt1 += insertCross('blue', True)
    pt1 += insertCross('orange', True)

    self.turn('z2')
    pt1 += f'Rotate by z2 to place cross on bottom: {self}'

    def sexyMoves(pc):
      sm = 0
      while pc not in [[self.pos[5][2], self.pos[2][8], self.pos[3][6]], [self.pos[5][2], self.pos[3][6], self.pos[2][8]]]:
        sm += 1
        self.algo('R U R\' U\'')
      if sm == 0: return ''
      elif sm == 1: return '(R U R\' U\')'
      else: return f'(R U R\' U\'){sm}' 

    pt2 = '\n\n--- STEP 2: FIRST LAYER ---\n\n'

    def insertCorner(pc, name, hasY):
      alg = ''
      if hasY:
        alg += 'y '
        self.turn('y')

      match self.pieces().index(Counter(pc)):
        case 0: alg += 'U2'
        case 1: alg += 'U'
        case 2: alg += 'U\''
        case 3 | 7: alg += ''
        case 4: alg += 'L U L\' U'
        case 5: alg += 'R\' U R U'
        case 6: alg += 'L\' U\' L'

      self.algo(alg.removeprefix('y '))
      if alg != '': alg += ' '
      alg += sexyMoves(pc)
      return f'Place {name} corner with R U R\' U\': {alg}\n{self}'

    if (wobResult:=insertCorner(['w', 'o', 'b'], 'white-blue-orange', False)) != '': 
      pt2 += wobResult

    pt2 += insertCorner(['w', 'r', 'b'], 'white-blue-red', True)
    pt2 += insertCorner(['w', 'r', 'g'], 'white-red-green', True)
    pt2 += insertCorner(['w', 'o', 'g'], 'white-orange-green', True)

    pt3 = '\n\n--- STEP 3: SECOND LAYER ---\n\n'

    leftEdge = '(U R U\' R\' U\' F\' U F)'
    rightEdge = '(U\' F\' U F U R U\' R\')'

    def insertEdge(pc, name, hasY):
      alg = ''
      alg2 = ''
      if hasY:
        alg += 'y '
        self.turn('y')

      rightCenter = self.pos[3][4]

      match self.pieces().index(Counter(pc)):
        case 8: 
          if self.pos[0][1] == rightCenter: alg += f'U2 {leftEdge}'
          else: alg += f'U {rightEdge}'
        case 9:
          if self.pos[0][3] == rightCenter: alg += f'U\' {leftEdge}'
          else: alg += f'U2 {rightEdge}'
        case 10:
          if self.pos[0][5] == rightCenter: alg += f'U {leftEdge}'
          else: alg += rightEdge
        case 11:
          if self.pos[0][7] == rightCenter: alg += leftEdge
          else: alg += f'U\' {rightEdge}'

        case 12:
          alg2 = f'(y2 {leftEdge} y2) '
          self.algo(alg2[:-1])
          alg += alg2
          if self.pos[0][7] == rightCenter: alg += leftEdge
          else: alg += f'U\' {rightEdge}'

        case 13:
          alg2 = f'(y {leftEdge} y\') '
          self.algo(alg2[:-1])
          alg += alg2
          if self.pos[0][3] == rightCenter: alg += f'U\' {leftEdge}'
          else: alg += f'U2 {rightEdge}'   

        case 14:
          alg2 = f'(y\' {leftEdge} y) '  
          self.algo(alg2[:-1])
          alg += alg2
          if self.pos[0][5] == rightCenter: alg += f'U {leftEdge}'
          else: alg += rightEdge

        case 15:
          if self.pos[3][3] == rightCenter: alg += ''
          else: alg += f'{leftEdge} U2 {leftEdge}'         

      self.algo(alg.removeprefix('y ').replace(alg2, ''))
      return f'Place {name} edge: {alg}\n{self}'

    if (ogResult:=insertEdge(['o', 'g'], 'green-orange', False)) != '': 
      pt3 += ogResult

    pt3 += insertEdge(['o', 'b'], 'blue-orange', True)
    pt3 += insertEdge(['r', 'b'], 'blue-red', True)
    pt3 += insertEdge(['r', 'g'], 'green-red', True)

    pt4 = '\n\n--- STEP 4: ORIENTATING LAST LAYER (OLL) ---\n\n'

    def interpretU(u):
      match u:
        case 0: return ''
        case 1: return '(U)'
        case 2: return '(U2)'
        case 3: return '(U\')'      

    cross = ''.join(['T' if self.pos[0][x]=='y' else 'F' for x in [1, 3, 5, 7]])
    solved = cross == 'TTTT'
    alg = ''
    uTurns = 0

    if not solved:
      while True:
        cross = ''.join(['T' if self.pos[0][x]=='y' else 'F' for x in [1, 3, 5, 7]])
        match cross:
          case 'FTTF': alg = ['Line', 'F (R U R\' U\') F\'']; break
          case 'FFTT': alg = ['L-shape', 'f (R U R\' U\') f\'']; break
          case 'FFFF': alg = ['Dot', 'F (R U R\' U\') S (R U R\' U\') f\'']; break

        uTurns += 1
        self.turn('U')

      uTurns = interpretU(uTurns)

      if uTurns != '': pt4 += f'Recognized case: {alg[0]}\nAlgorithm: {uTurns} {alg[1]}'
      else: pt4 += f'Recognized case: {alg[0]}\nAlgorithm: {alg[1]}'

      self.algo(f'{alg[1]}')
      pt4 += str(self)
    else: pt4 += '(CROSS STEP SKIPPED - YELLOW CROSS ALREADY SOLVED)\n\n'

    solved = self.pos[0] == ['y']*9
    alg = ''
    uTurns = 0

    if not solved:
      while True:
        corners = ''.join(['T' if x=='y' else 'F' for x in list(chain.from_iterable([self.pos[i][j] for i in range(1, 5) for j in [0, 2]]))])
        match corners:
          case 'FFTTFFTT': 
            alg = ['H', 'R U2 R\' U\' (R U R\' U\') R U\' R\'']; break
          case 'TTFTFFTF':
            alg = ['Pi', 'R U2 R2 U\' R2 U\' R2 U2 R']; break
          case 'TFTFTFFF':
            alg = ['Antisune', 'R U2 R\' U\' R U\' R\'']; break
          case 'FFFTFTFT':
            alg = ['Sune', 'R U R\' U R U2 R\'']; break
          case 'FFTFFTFF':
            alg = ['L', '(F R\' F\' r) (U R U\' r\')']; break
          case 'FFTFFFFT':
            alg = ['T', '(r U R\' U\') (r\' F R F\')']; break
          case 'FFFFFFTT':
            alg = ['U', 'R2 D\' (R U2 R\') D (R U2 R)']; break

        uTurns += 1
        self.turn('U')

      uTurns = interpretU(uTurns)

      if uTurns != '': pt4 += f'Recognized case: {alg[0]}\nAlgorithm: {uTurns} {alg[1]}'
      else: pt4 += f'Recognized case: {alg[0]}\nAlgorithm: {alg[1]}'

      self.algo(f'{alg[1]}')
      pt4 += str(self)
    else: pt4 += '(CORNER STEP SKIPPED - YELLOW FACE ALREADY SOLVED)\n\n'

    pt5 = '\n\n--- STEP 4: PERMUTING LAST LAYER (PLL) ---\n\n'

    def isOpp(col1, col2):
      return (l:=['w', 'g', 'r', 'o', 'b', 'y']).index(col1) + l.index(col2) == 5

    alg = ''
    uTurns = 0

    a = self.pos[1][0]
    b = self.pos[1][2]
    c = self.pos[3][0]
    d = self.pos[3][2]

    if a == b and c == d:
      pt5 += '(CORNER STEP SKIPPED - CORNERS ALREADY SOLVED)\n\n'
    else:
      if isOpp(a, b) and isOpp(c, d):
        alg = ['Y-Perm', 'F (R U\' R\' U\') (R U R\') F\' (R U R\' U\') (R\' F R F\')']
      else:
        alg = ['T-Perm', '(R U R\' U\') R\' F (R2 U\' R\' U\') (R U R\') F\'']
        while not isOpp(self.pos[3][0], self.pos[3][2]):
          uTurns += 1
          self.turn('U')

      uTurns = interpretU(uTurns)

      if uTurns != '': pt5 += f'Recognized case: {alg[0]}\nAlgorithm: {uTurns} {alg[1]}'
      else: pt5 += f'Recognized case: {alg[0]}\nAlgorithm: {alg[1]}'

      self.algo(f'{alg[1]}')
      pt5 += str(self)

    solved = len(set(self.pos[1][:3])) + len(set(self.pos[2][:3])) == 2
    alg = ''
    uTurns = 0

    if solved:
      pt5 += '(EDGE STEP SKIPPED - EDGES ALREADY SOLVED)'
    else:
      # H PERM OR Z PERM
      if isOpp(self.pos[1][1], self.pos[3][1]) and isOpp(self.pos[2][1], self.pos[4][1]):
        if isOpp(self.pos[1][1], self.pos[1][2]):
          alg = ['H-Perm', 'M2 U M2 U2 M2 U M2']
        else:
          while self.pos[1][1] != self.pos[2][0]:
            uTurns += 1
            self.turn('U')
          alg = ['Z-Perm','M\' U (M2 U M2 U) M\' U2 M2']
      # Ua OR Ub PERM
      else:
        while self.pos[4][0] != self.pos[4][1]:
          uTurns += 1
          self.turn('U')
        if isOpp(self.pos[2][1], self.pos[3][1]):
          alg = ['Ua-Perm', 'R U\' (R U R U) (R U\' R\' U\') R2']
        else:
          alg = ['Ub-Perm', 'R2 U (R U R\' U\') (R\' U\' R\' U) R\'']

      uTurns = interpretU(uTurns)

      if uTurns != '': pt5 += f'Recognized case: {alg[0]}\nAlgorithm: {uTurns} {alg[1]}'
      else: pt5 += f'Recognized case: {alg[0]}\nAlgorithm: {alg[1]}'

      self.algo(f'{alg[1]}')
      pt5 += str(self)

    # AUF
    if not self.isSolved():
      uTurns = 0
      while len(set(self.pos[1])) != 1:
        uTurns += 1
        self.turn('U')

      uTurns = interpretU(uTurns)  

      pt5 += f'Adjusting U Face (AUF): {uTurns}'
      pt5 += str(self) 

    print(pt1, pt2, pt3, pt4, pt5, sep='')
    input('\nCube has been solved! > ')


class Cube2(Cube):
  def __init__(self, size=2):
    super().__init__(size)

  def pieces(self):
    u, l, f, r, b, d = self.pos
    return [
      Counter([u[0], b[1], l[0]]), # top back left
      Counter([u[1], b[0], r[1]]), # top back right
      Counter([u[2], f[0], l[1]]), # top front left
      Counter([u[3], f[1], r[0]]), # top front right

      Counter([d[2], b[3], l[2]]), # bottom back left
      Counter([d[3], b[2], r[3]]), # bottom back right
      Counter([d[0], f[2], l[3]]), # bottom front left
      Counter([d[1], f[3], r[2]]), # bottom front right
    ]

  def turn(self, move):
    # should handle: U, L, F, R, B, D
    # THEIR PRIMES ('), DOUBLES (2) (NO WIDE MOVES FOR POCKET CUBE)
    # rotations: x, y, z, THEIR PRIMES (') AND DOUBLES (2)
    if move[-1] == '\'': 
      for i in range(3): self.turn(move[:-1])
      return
    if move[-1] == '2': 
      for i in range(2): self.turn(move[:-1])
      return

    match move:
      case 'x': self.pos = self.xRot()
      case 'y': self.pos = self.yRot()
      case 'z': self.pos = self.zRot()      
      case 'U': self.uTurn()
      case 'D': self.algo('x2 U x2')
      case 'L': self.algo('z U z\'')      
      case 'R': self.algo('z\' U z')
      case 'F': self.algo('x U x\'')
      case 'B': self.algo('x\' U x')

  def __str__(self, faces=None, template=vis2):
    u, l, f, r, b, d = self.pos
    if faces == None: faces = str.maketrans('abcdefghijkl', ''.join(u+f+r))
    return super().__str__(faces, template)

  def scramble(self, moveNo=None):
    moves = ['U', 'R', 'F']
    if moveNo == None: moveNo = random.randint(10, 15)
    return super().scramble(moveNo, moves)

  def solve(self):
    alg = ''

    clear()
    print('######## SOLVING ########\n--- STEP 1: FIRST LAYER ---\n')

    wrbPiece = Counter(['w', 'b', 'r'])
    match self.pieces().index(wrbPiece):
      case 0: alg = 'y2'
      case 1: alg = 'y'
      case 2: alg = 'y\''
      case 3: alg = ''
      case 4: alg = 'x2 y\''
      case 5: alg = 'x2'
      case 6: alg = 'z2'
      case 7: alg = 'z2 y\''
    self.algo(alg)
    if alg != '':
      print(f'Locate and place white-blue-red piece: {alg}')
      print(self)

    match ([self.pos[0][3], self.pos[2][1], self.pos[3][0]]).index('w'):
      case 0: alg = ''
      case 1: alg = 'x y'
      case 2: alg = 'z\' y\''
    self.algo(alg)
    if alg != '':
      print(f'Make white-blue-red piece upright: {alg}')
      print(self)

    print('Rotate by z2 to place white-blue-red on bottom front left place:')
    self.turn('z2')
    print(self)

    def sexyMoves(pc):
      sm = 0
      while pc not in [[self.pos[5][1], self.pos[2][3], self.pos[3][2]], [self.pos[5][1], self.pos[3][2], self.pos[2][3]]]:
        sm += 1
        self.algo('R U R\' U\'')
      if sm == 0: return None
      elif sm == 1: alg = 'R U R\' U\''
      else: alg = f'(R U R\' U\'){sm}'
      print(f'Use R U R\' U\' to place: {alg}')       
      print(self)   

    # locating and placing white-green-red piece
    wrgPiece = ['w', 'r', 'g']
    match self.pieces().index(Counter(wrgPiece)):
      case 0: alg = 'U2'
      case 1: alg = 'U'
      case 2: alg = 'U\''
      case 3 | 7: alg = ''
      case 4: alg = 'B\' U2'
      case 5: alg = 'R'
    self.algo(alg)
    if alg != '':
      print(f'Position white-green-red piece: {alg}')
      print(self)
    sexyMoves(wrgPiece)

    self.turn('y')

    # locating and placing white-green-orange piece
    wogPiece = ['w', 'o', 'g']
    match self.pieces().index(Counter(wogPiece)):
      case 0: alg = 'U2'
      case 1: alg = 'U'
      case 2: alg = 'U\''
      case 3 | 7: alg = ''
      case 5: alg = 'R'
    self.algo(alg)
    print(f'Position white-green-orange piece: y {alg}')
    print(self)
    sexyMoves(wogPiece)

    self.turn('y')

    # locating and placing white-green-orange piece
    wobPiece = ['w', 'o', 'b']
    match self.pieces().index(Counter(wobPiece)):
      case 0: alg = 'U2'
      case 1: alg = 'U'
      case 2: alg = 'U\''
      case 3 | 7: alg = ''
    self.algo(alg)
    print(f'Position white-blue-orange piece: y {alg}')
    print(self)
    sexyMoves(wobPiece)  

    print('--- STEP 2: TOP FACE (OLL) ---')

    recognized = True if self.pos[0] == ['y']*4 else False
    alg = ''
    uTurns = 0

    if not recognized:
      while not recognized:
        yellow = ''.join(['T' if x=='y' else 'F' for x in list(chain.from_iterable([self.pos[i][:2] for i in range(1, 5)]))])
        match yellow:
          case 'FFTTFFTT': 
            alg = ['H', 'R2 U2 R U2 R2']; recognized = True
          case 'TTFTFFTF':
            alg = ['Pi', 'R U2 R2 U\' R2 U\' R2 U2 R']; recognized = True
          case 'TFTFTFFF':
            alg = ['Antisune', 'R U2 R\' U\' R U\' R\'']; recognized = True
          case 'FFFTFTFT':
            alg = ['Sune', 'R U R\' U R U2 R\'']; recognized = True
          case 'FFTFFTFF':
            alg = ['L', '(F R\' F\' R) (U R U\' R\')']; recognized = True
          case 'FFTFFFFT':
            alg = ['T', '(R U R\' U\') (R\' F R F\')']; recognized = True
          case 'TTFFFFFF':
            alg = ['U', 'F (R U R\' U\') F\'']; recognized = True

        uTurns += 1
        self.turn('U')

      uTurns -= 1
      self.turn('U\'')
      match uTurns:
        case 0: uTurns = ''
        case 1: uTurns = '(U)'
        case 2: uTurns = '(U2)'
        case 3: uTurns = '(U\')'

      if uTurns != '': print(f'Recognized OLL case: {alg[0]}\nAlgorithm: {uTurns} {alg[1]}')
      else: print(f'Recognized OLL case: {alg[0]}\nAlgorithm: {alg[1]}')

      self.algo(f'{alg[1]}')
      print(self)
    else: print('(STEP SKIPPED - TOP FACE ALREADY SOLVED)\n')

    print('--- STEP 3: TOP LAYER (PLL) ---')

    def isOpp(cols):
      return (l:=['w', 'g', 'r', 'o', 'b', 'y']).index(cols[0]) + l.index(cols[1]) == 5

    uTurns = 0
    alg = ''
    if self.pos[1][0] == self.pos[1][1] and self.pos[3][0] == self.pos[3][1]: # solved case
      print('(STEP SKIPPED - TOP LAYER ALREADY SOLVED)\n')
    else:
      if isOpp(self.pos[1]) and isOpp(self.pos[2]): # y-perm
        alg = ['Y-Perm', 'F (R U\' R\' U\') (R U R\') F\' (R U R\' U\') (R\' F R F\')']
      else: # t-perm
        alg = ['T-Perm', '(R U R\' U\') R\' F (R2 U\' R\' U\') (R U R\') F\'']
        while not isOpp(self.pos[3]):
          uTurns += 1
          self.turn('U')

      match uTurns:
        case 0: uTurns = ''
        case 1: uTurns = '(U)'
        case 2: uTurns = '(U2)'
        case 3: uTurns = '(U\')'

      if uTurns != '': print(f'Recognized PLL case: {alg[0]}\nAlgorithm: {uTurns} {alg[1]}')
      else: print(f'Recognized PLL case: {alg[0]}\nAlgorithm: {alg[1]}')

      self.algo(f'{alg[1]}')
      print(self)

    # AUF
    if not self.isSolved():
      uTurns = 0
      while len(set(self.pos[1])) != 1:
        uTurns += 1
        self.turn('U')

      match uTurns:
        case 1: uTurns = 'U'
        case 2: uTurns = 'U2'
        case 3: uTurns = 'U\''     

      print(f'Adjusting U Face (AUF): {uTurns}')
      print(self)   

    input('Cube has been solved! > ')


class Cube4(Cube):
  def __init__(self, size=4):
    super().__init__(size)

  def pieces(self): pass

  def deepU(self):
    u, l, f, r, b, d = self.pos
    x = self.size * 2
    self.pos = [
      self.clockwise(u),  
      f[:x] + l[x:],
      r[:x] + f[x:],
      b[:x] + r[x:],
      l[:x] + b[x:],
      d
    ]    

  def turn(self, move):
    # should handle: U, L, F, R, B, D
    # THEIR PRIMES ('), DOUBLES (2) (NO WIDE MOVES FOR POCKET CUBE)
    # rotations: x, y, z, THEIR PRIMES (') AND DOUBLES (2)
    if move[-1] == '\'': 
      for i in range(3): self.turn(move[:-1])
      return
    if move[-1] == '2': 
      for i in range(2): self.turn(move[:-1])
      return

    match move:
      # before drugs
      case 'x': self.pos = self.xRot()
      case 'y': self.pos = self.yRot()
      case 'z': self.pos = self.zRot()      
      case 'U': self.uTurn()
      case 'D': self.algo('x2 U x2')
      case 'L': self.algo('z U z\'')      
      case 'R': self.algo('z\' U z')
      case 'F': self.algo('x U x\'')
      case 'B': self.algo('x\' U x')

      # during drugs
      case 'u': self.algo('y D')
      case 'd': self.algo('y\' U')
      case 'l': self.algo('x\' R')
      case 'r': self.algo('x L')
      case 'f': self.algo('z B')
      case 'b': self.algo('z\' F')
      case 'M': self.algo('L\' R x\'')
      case 'E': self.algo('U D\' y\'')
      case 'S': self.algo('F\' B z')

      # after drugs
      case 'Uw': self.deepU()
      case 'Dw': self.algo('x2 Uw x2')
      case 'Lw': self.algo('z Uw z\'')
      case 'Rw': self.algo('z\' Uw z')
      case 'Fw': self.algo('x Uw x\'')
      case 'Bw': self.algo('x\' Uw x')

  def __str__(self, faces=None, template=vis4):
    u, l, f, r, b, d = self.pos
    if faces == None:
      faces = str.maketrans('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUV', ''.join(u+f+r))
    return super().__str__(faces, template)

  def scramble(self, moveNo=None, moves=None):
    if moves == None:
      basic = ['U', 'F', 'R', 'L', 'D', 'B']
      moves = basic + [x+'w' for x in basic[:3]]
    if moveNo == None: moveNo = random.randint(35, 45)
    return super().scramble(moveNo, moves)


class Cube5(Cube4):
  def __init__(self, size=5):
    super().__init__(size)

  def __str__(self):
    u, l, f, r, b, d = self.pos
    faces = str.maketrans('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,!?:;<>(){}=', ''.join(u+f+r))
    return super().__str__(faces, vis5)

  def scramble(self, moveNo=None):
    basic = ['U', 'F', 'R', 'L', 'D', 'B']
    moves = basic + [x+'w' for x in basic]
    if moveNo == None: moveNo = random.randint(55, 65)
    return super().scramble(moveNo, moves)


class Cube6(Cube4):
  def __init__(self, size=6):
    super().__init__(size)

  def __str__(self):
    u, l, f, r, b, d = self.pos
    faces = str.maketrans('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,!?:;<>(){}=\'\"[]@#$%^&*_+~`\\₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎↑↓', ''.join(u+f+r))
    return super().__str__(faces, vis6)

  def U3slice(self):
    u, l, f, r, b, d = self.pos
    x = self.size * 3
    self.pos = [
      self.clockwise(u),  
      f[:x] + l[x:],
      r[:x] + f[x:],
      b[:x] + r[x:],
      l[:x] + b[x:],
      d
    ]    

  def turn(self, move):
    # should handle: U, L, F, R, B, D
    # THEIR PRIMES ('), DOUBLES (2) (NO WIDE MOVES FOR POCKET CUBE)
    # rotations: x, y, z, THEIR PRIMES (') AND DOUBLES (2)
    if move[-1] == '\'': 
      for i in range(3): self.turn(move[:-1])
      return
    if move[-1] == '2': 
      for i in range(2): self.turn(move[:-1])
      return

    match move:
      # outer slice (1st/6th)
      case 'x': self.pos = self.xRot()
      case 'y': self.pos = self.yRot()
      case 'z': self.pos = self.zRot()      
      case 'U': self.uTurn()
      case 'D': self.algo('x2 U x2')
      case 'L': self.algo('z U z\'')      
      case 'R': self.algo('z\' U z')
      case 'F': self.algo('x U x\'')
      case 'B': self.algo('x\' U x')

      # wide moves
      case 'u': self.algo('y D')
      case 'd': self.algo('y\' U')
      case 'l': self.algo('x\' R')
      case 'r': self.algo('x L')
      case 'f': self.algo('z B')
      case 'b': self.algo('z\' F')
      case 'M': self.algo('L\' R x\'')
      case 'E': self.algo('U D\' y\'')
      case 'S': self.algo('F\' B z')

      # 2-slice
      case 'Uw': self.deepU()
      case 'Dw': self.algo('x2 Uw x2')
      case 'Lw': self.algo('z Uw z\'')
      case 'Rw': self.algo('z\' Uw z')
      case 'Fw': self.algo('x Uw x\'')
      case 'Bw': self.algo('x\' Uw x')

      # 3-slice (WIP)
      case '3Uw': self.U3slice()
      case '3Dw': self.algo('x2 3Uw x2')
      case '3Lw': self.algo('z 3Uw z\'')
      case '3Rw': self.algo('z\' 3Uw z')
      case '3Fw': self.algo('x 3Uw x\'')
      case '3Bw': self.algo('x\' 3Uw x')

  def scramble(self, moveNo=None):
    basic = ['U', 'F', 'R', 'L', 'D', 'B']
    moves = basic + [x+'w' for x in basic] + ['3'+x+'w' for x in basic]
    if moveNo == None: moveNo = random.randint(85, 95)
    return super().scramble(moveNo, moves)  


cube2 = Cube2()
cube3 = Cube()
cube4 = Cube4()
cube5 = Cube5()
cube6 = Cube6()

cubeList = '''####### CUBE OPTIONS #######

cube2: 2x2 cube
cube3: 3x3 cube
cube4: 4x4 cube
cube5: 5x5 cube
cube6: 6x6 cube'''

def cubeChange():
  clear()
  choice = ''
  while True:
    clear()
    print(cubeList)
    choice = input('\nWhich cube would you like to use? > ')

    match choice:
      case 'cube2': return cube2
      case 'cube3': return cube3
      case 'cube4': return cube4
      case 'cube5': return cube5
      case 'cube6': return cube6
      case _: input('ERROR: requested puzzle not recognized > ')
  
def clear():
  os.system('cls' if os.name == 'nt' else 'clear')
  print("\033c\033[3J")

def main():
  cube = cubeChange()

  while True:
    clear()
    print(cube)

    if cube.isSolved():
      print('--- Cube is in a solved state ---')

    cmd = input('Input a command (type ? for help) > ').split(' ')

    match cmd[0]:
      case '?' | 'help':
        input('''
        ####### LIST OF COMMANDS #######

        [command (aliases) {parameters}: what it does]

        ? (help): shows this message
        scramble (scr) {move}: scrambles the cube randomly with {move}>0 moves. {move} is 10 to 20 moves by default
        {turns}: turns the cube according to the move/algorithm specified
        solve: shows how to solve the current scramble with the beginner's method
        reset (rst): resets the cube to a solved state, with white on the top and green on the front
        turnTime {ms}: sets how long each move takes to {ms} milliseconds when scrambling
        change: changes the cube being used to a puzzle of your choice
        exit (end): exits the program

        FORMATTING TURNS/ALGORITHMS
        - Turns may only contain ' or 2 (R2, x', y2, etc.)
        - Each turn in your typed algorithm must be seperated by a space
        - For now, brackets will be ignored and triggers are not implemented

                WRONG                        CORRECT
                          R3 --> R2 R
                     R2xFU'B --> R2 x F U' B
                (R U R' U')2 --> R U R' U' R U R' U'

        - If the move(s) entered are incorrectly formatted, they will be ignored and the cube will undergo NO change
        - For 3x3, wide moves should be denoted with lowercase (u, d, f, etc.)
        - For 4x4 and 5x5, deep turns should be denoted with -w (Uw, Rw, Fw, etc.)

        Click enter to continue > ''')

      case 'scramble' | 'scr':
        if len(cmd) == 1: output = cube.scramble()
        else:
          try:
            moveNo = int(cmd[1])
            if moveNo < 1:
              input('ERROR: Should be at least 1 move long > ')
              continue
            output = cube.scramble(moveNo)
          except:
            input('ERROR: Scramble length must be a positive integer > ')
            continue

        clear()
        print(cube)

        input(f'SCRAMBLE ALGORITHM: {" ".join(output[0])}\nExecution time for scramble: {output[1]}s\n> ')

      case 'solve':
        if cube not in [cube2, cube3]:
          input('Sorry, haven\'t figured this out yet! > ')
          continue
        cube.solve()

      case 'reset' | 'rst': cube.reset()

      case 'turnTime':
        try:
          t = float(cmd[1])
          if t < 0:
            input('ERROR: time between moves must be 0 or more ms > ')
            continue
          cube.turnTime = t/1000
        except:
          input('ERROR: time between moves must be a number > ')
          continue

      case 'change':
        cube = cubeChange()

      case 'exit' | 'end':
        print('Exiting program...')
        exit(0)

      case _: # move
        try:
          cube.algo(' '.join(cmd))      
        except:
          continue

if __name__ == '__main__':
  main()
