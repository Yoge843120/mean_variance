import numpy as np

def calfo(mat):
    mean = list(mat.mean(axis=0)), list(mat.mean(axis=1)), mat.mean()
    var = list(mat.var(axis=0)), list(mat.var(axis=1)), mat.var()
    std = list(mat.std(axis=0)), list(mat.std(axis=1)), mat.std()
    maxi = list(mat.max(axis=0)), list(mat.max(axis=1)), mat.max()
    mini = list(mat.min(axis=0)), list(mat.min(axis=1)), mat.min()
    sums = list(mat.sum(axis=0)), list(mat.sum(axis=1)), mat.sum()
    mean = list(mean)
    var = list(var)
    std = list(std)
    maxi = list(maxi)
    mini = list(mini)
    sums = list(sums)
    print(f'mean :{mean}\nvariance :{var}\nstandard deviation :{std}\nmax :{maxi}\nmin :{mini}\nsum :{sums}')
def calculate(mat):
    try:
        mat = np.array(mat).reshape(3,3)
        print(f'The matrix is\n {mat}')
        output = calfo(mat)
    except ValueError:
        print('List must contain 9 numbers')
lists = []
for element in range(9):
    num = int(input('Enter the elements of 3x3 matrix: '))
    lists.append(num)
print("call the function of 3x3 by Typing 'calculate'")
user_input = input('call the function ')
if user_input == 'calculate':
    calculate(lists)

    
