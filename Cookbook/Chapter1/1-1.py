p = (4,5)
x,y = p
print('x =', x, 'y =',y)

data = ['Vu ngoc Long',9,(2000,3,30)]
name,point,(yy,m,d) = data

print('Name :', name,'\nPoint :',point, '\nDOB :{}/{}/{}'.format(yy,m,d))