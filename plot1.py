
import matplotlib.pyplot as plt 

# x axis values 
x = [260,250,240,230,220,210,200,190,180,170,160,150,140,130,120,110,100,90] 
# corresponding y axis values 
y = [4.28,4.18,4.12,4.05,3.96,3.88,3.82,3.74,3.64,3.57,3.49,3.41,3.32,3.25,3.17,3.10,3.04,2.95] 

# 2 pontos quaisquer
xf = 'x'
yf = 'y'

x1 = x[0] 
y1 = y[0]
x2 = x[1] 
y2 = y[1] 

result1 = int((xf*y1)) + int((x1*y2)) - int((yf*x1)) - int((y1*x2) 
print(result1)
deltax = (x[0] - x[17]) 
deltay = (y[0] - y[17]) 

# plotting the points  
plt.plot(x, y) 
# naming the x axis 
plt.xlabel('Nível') 
# naming the y axis 
plt.ylabel('Tensão Bomba') 
# giving a title to my graph 
plt.title(' Gráfico (Nível - Tensão Bomba)') 
# function to show the plot 
plt.show() 