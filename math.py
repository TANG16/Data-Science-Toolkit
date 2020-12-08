#Plot sin and cos function
def sin_func(x):
  return np.sin(x)

def cos_func(x):
  return np.cos(x)

x = np.linspace(-10, 10, 100)

plt.figure(figsize=(20, 8))
plt.scatter(x, sin_func(x))
plt.scatter(x, cos_func(x))

#Optimization
# 目的となる関数
def objective(x):
    x1 = x[0]
    x2 = x[1]
    x3 = x[2]
    x4 = x[3]
    return x1*x4*(x1+x2+x3)+x3


# 制約式その1
def constraint1(x):
    return x[0]*x[1]*x[2]*x[3]-25.0

# 制約式その2
def constraint2(x):
    sum_sq = 40
    for i in range(4):
        sum_sq = sum_sq - x[i]**2
    return sum_sq


# 初期値
x0 = [1,5,5,1]
print(objective(x0))

b = (1.0,5.0)
bnds = (b,b,b,b)
con1 = {'type':'ineq','fun':constraint1}
con2 = {'type':'ineq','fun':constraint2}
cons = [con1,con2]

sol = minimize(objective,x0,method='SLSQP',bounds=bnds,constraints=cons)
print(sol)

print('Y:',sol.fun)
print('X:',sol.x)


#Monte Carlo Method
import math

x = np.random.uniform(0, 1, 10000)
y = np.random.uniform(0, 1, 10000)


plt.figure(figsize=(12, 8))
for i, j in zip(x, y):
  norm = math.hypot(i, j)
  if norm<1:
    plt.scatter(i, j,  color="orange")
  else:
    plt.scatter(i, j, color="blue")


#The raw of Large number
# 計算回数
calc_times =1000
# サイコロ
sample_array = np.array([1, 2, 3, 4, 5, 6])
number_cnt = np.arange(1, calc_times + 1)

# 4つのパスを生成
for i in range(10):
    p = np.random.choice(sample_array, calc_times).cumsum()
    plt.plot(p / number_cnt)

#Central Limit Theorem
def function_central_theory(N):
    
    sample_array = np.array([1, 2, 3, 4, 5, 6])
    numaber_cnt = np.arange(1, N + 1) * 1.0
 
    mean_array = np.array([])
 
    for i in range(1000):   
        cum_variables = np.random.choice(sample_array, N).cumsum()*1.0
        mean_array = np.append(mean_array, cum_variables[N-1] / N)
 
    plt.hist(mean_array)