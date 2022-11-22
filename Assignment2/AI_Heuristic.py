# import pygame library
import tracemalloc
from tracemalloc import start
import pygame
import time

# initialise the pygame font
pygame.font.init()

# Total window
screen = pygame.display.set_mode((700, 700))

# Title and Icon
pygame.display.set_caption("SUDOKU SOLVER USING BACKTRACKING")
img = pygame.image.load('android.svg')
pygame.display.set_icon(img)

x = 0
y = 0
dif = 500 / 9
val = 0
# Default Sudoku Board.
grid =[
		[7, 8, 0, 4, 0, 0, 1, 2, 0],
		[6, 0, 0, 0, 7, 5, 0, 0, 9],
		[0, 0, 0, 6, 0, 1, 0, 7, 8],
		[0, 0, 7, 0, 4, 0, 2, 6, 0],
		[0, 0, 1, 0, 5, 0, 9, 3, 0],
		[9, 0, 4, 0, 6, 0, 0, 0, 5],
		[0, 7, 0, 3, 0, 0, 0, 1, 2],
		[1, 2, 0, 0, 0, 7, 4, 0, 0],
		[0, 4, 9, 2, 0, 6, 0, 0, 7]
	]

# Load test fonts for future use
font1 = pygame.font.SysFont("comicsans", 30)
font2 = pygame.font.SysFont("comicsans", 10)
def get_cord(pos):
	global x
	x = pos[0]//dif
	global y
	y = pos[1]//dif

# Highlight the cell selected
def draw_box():
	for i in range(2):
		pygame.draw.line(screen, (255, 0, 0), (x * dif-3, (y + i)*dif), (x * dif + dif + 3, (y + i)*dif), 7)
		pygame.draw.line(screen, (255, 0, 0), ( (x + i)* dif, y * dif ), ((x + i) * dif, y * dif + dif), 7)

# Function to draw required lines for making Sudoku grid		
def draw():
	# Draw the lines
		
	for i in range (9):
		for j in range (9):
			if grid[i][j]!= 0:

				# Fill blue color in already numbered grid
				pygame.draw.rect(screen, (0, 153, 153), (i * dif, j * dif, dif + 1, dif + 1))

				# Fill grid with default numbers specified
				text1 = font1.render(str(grid[i][j]), 1, (0, 0, 0))
				screen.blit(text1, (i * dif+17, j * dif+5))
	# Draw lines horizontally and verticallyto form grid		
	for i in range(10):
		if i % 3 == 0 :
			thick = 7
		else:
			thick = 1
		pygame.draw.line(screen, (0, 0, 0), (0, i * dif), (500, i * dif), thick)
		pygame.draw.line(screen, (0, 0, 0), (i * dif, 0), (i * dif, 500), thick)	

# Fill value entered in cell	
def draw_val(val):
	text1 = font1.render(str(val), 1, (0, 0, 0))
	screen.blit(text1, (x * dif + 15, y * dif + 15))

# Raise error when wrong value entered
def raise_error1():
	text1 = font1.render("WRONG !!!", 1, (0, 0, 0))
	screen.blit(text1, (20, 570))
def raise_error2():
	text1 = font1.render("Wrong !!! Not a valid Key", 1, (0, 0, 0))
	screen.blit(text1, (20, 570))

# Check if the value entered in board is valid
def valid(m, i, j, val):
	for it in range(9):
		if m[i][it]== val:#check column
			return False
		if m[it][j]== val:#check row
			return False
	#check square
	it = i//3
	jt = j//3
	for i in range(it * 3, it * 3 + 3):
		for j in range (jt * 3, jt * 3 + 3):
			if m[i][j]== val:
				return False
	return True


# Solves the sudoku board using depth first search
def solve(grid, i, j):
	#print(grid)
	#สร้างตัวแปร save ขึ้นมาเพื่อเก็บค่าที่เป็นไปได้แต่ละช่อง
	save = [
				[[], [], [], [], [], [], [], [], []],
				[[], [], [], [], [], [], [], [], []],
				[[], [], [], [], [], [], [], [], []],
				[[], [], [], [], [], [], [], [], []],
				[[], [], [], [], [], [], [], [], []],
				[[], [], [], [], [], [], [], [], []],
				[[], [], [], [], [], [], [], [], []],
				[[], [], [], [], [], [], [], [], []],
				[[], [], [], [], [], [], [], [], []]
				]
	# สร้างตัวแปรในการทำ loop ตรวจสอบแต่ละ squre
	i_ref = 0
	j_ref = 0
	count = 0
	while i <= 8 and j <= 8 :
		if grid[i][j] == 0 :
			# print("Empty")
			for it in range(1,10) :   #หาค่าที่เป็นไปได้ในช่องนั้นๆ แล้วเก็บเข้า save
				if valid(grid,i,j,it) == True :
					#print(i,j,"= ",it)
					save[i][j].append(it)      
			if len(save[i][j]) == 1 :   #ถ้าค่าที่เป็นไปได้มีแค่ค่าเดียวให้ใส่ลงช่อง แล้วเอาค่านั้นออกจากต save
				grid[i][j] = save[i][j][0]
				save[i][j].pop()
			pygame.event.pump()
			screen.fill((255, 255, 255))
			draw()
			draw_box()
			pygame.display.update()
			pygame.time.delay(80)
		# else :
		# 	print(grid[i][j])
		if i - i_ref < 2 : 
			i+=1
		else :
			if j - j_ref < 2 :
				i = i_ref
				j += 1
			else :
				#print(save)
				i_ref += 3
				i = i_ref
				j = j_ref
				count += 1
				if (count)%3 == 0 and count != 0:
					# print("New squre")
					j_ref += 3
					j = j_ref
					i_ref = 0
					i = i_ref
	#print(save)				
	for i_check in range(8) :    #เช็ค save ว่ายังมีค่าที่เป็นไปได้เหลือป่าว ถ้าเหลือก็ recursive ถ้าไม่เหลือก็เสร็จ
		for j_check in range(8) :
			if save[i_check][j_check] != [] :
				#print(save[i_check][j_check])
				solve(grid,0,0)
				break
	#save.sort()
	
	# print(save[0][2])
	#print(grid)
# Display instruction for the game
def instruction():
	text1 = font2.render("PRESS D TO RESET TO DEFAULT / R TO EMPTY", 1, (0, 0, 0))
	text2 = font2.render("ENTER VALUES AND PRESS ENTER TO VISUALIZE", 1, (0, 0, 0))
	screen.blit(text1, (20, 520))	
	screen.blit(text2, (20, 540))

# Display options when solved
def result():
	text1 = font1.render("FINISHED PRESS R or D", 1, (0, 0, 0))
	screen.blit(text1, (20, 570))
run = True
flag1 = 0
flag2 = 0
rs = 0
error = 0

# The loop thats keep the window running
while run:
	
	# White color background
	screen.fill((255, 255, 255))
    
	# Loop through the events stored in event.get()
	for event in pygame.event.get():
		# Quit the game window
		if event.type == pygame.QUIT:
			run = False
		# Get the mouse position to insert number
		if event.type == pygame.MOUSEBUTTONDOWN:
			flag1 = 1
			pos = pygame.mouse.get_pos()
			get_cord(pos)
		# Get the number to be inserted if key pressed
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				x-= 1
				flag1 = 1
			if event.key == pygame.K_RIGHT:
				x+= 1
				flag1 = 1
			if event.key == pygame.K_UP:
				y-= 1
				flag1 = 1
			if event.key == pygame.K_DOWN:
				y+= 1
				flag1 = 1
			if event.key == pygame.K_1:
				val = 1
			if event.key == pygame.K_2:
				val = 2
			if event.key == pygame.K_3:
				val = 3
			if event.key == pygame.K_4:
				val = 4
			if event.key == pygame.K_5:
				val = 5
			if event.key == pygame.K_6:
				val = 6
			if event.key == pygame.K_7:
				val = 7
			if event.key == pygame.K_8:
				val = 8
			if event.key == pygame.K_9:
				val = 9
			if event.key == pygame.K_RETURN:
				flag2 = 1
				
                
			# If R pressed clear the sudoku board
			if event.key == pygame.K_r:
				rs = 0
				error = 0
				flag2 = 0
				grid =[
				[0, 0, 0, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0, 0, 0]
				]
			# If D is pressed reset the board to default
			if event.key == pygame.K_d:
				rs = 0
				error = 0
				flag2 = 0
				grid =[
					[7, 8, 0, 4, 0, 0, 1, 2, 0],
					[6, 0, 0, 0, 7, 5, 0, 0, 9],
					[0, 0, 0, 6, 0, 1, 0, 7, 8],
					[0, 0, 7, 0, 4, 0, 2, 6, 0],
					[0, 0, 1, 0, 5, 0, 9, 3, 0],
					[9, 0, 4, 0, 6, 0, 0, 0, 5],
					[0, 7, 0, 3, 0, 0, 0, 1, 2],
					[1, 2, 0, 0, 0, 7, 4, 0, 0],
					[0, 4, 9, 2, 0, 6, 0, 0, 7]
				]
    
	if flag2 == 1:
		tracemalloc.start()
		start_time = time.time()					
		if solve(grid, 0, 0)== False:
			error = 1
		else:
			rs = 1
		elasped_time = time.time()-start_time
		print("time=",end='')
		print(elasped_time)			
		flag2 = 0
		print(tracemalloc.get_traced_memory())
		tracemalloc.stop()
	if val != 0:		
		draw_val(val)
		# print(x)
		# print(y)
		if valid(grid, int(x), int(y), val)== True:
			grid[int(x)][int(y)]= val
			flag1 = 0
		else:
			grid[int(x)][int(y)]= 0
			raise_error2()
		val = 0
	
	if error == 1:
		raise_error1()
	if rs == 1:
		result()	
	draw()
	if flag1 == 1:
		draw_box()	
	instruction()

	# Update window
	pygame.display.update()

# Quit pygame window
pygame.quit()	
	
