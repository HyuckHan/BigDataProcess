import numpy as np
import time

def loadDataSet(filename):
    xList = []; yList = []
    with open(filename) as f:
        for line in f:
            if line.startswith("Price"):
                continue
            instance = str.strip(line).split('\t')
            xList.append(float(instance[1]))
            yList.append(float(instance[0]))
    return np.array(xList), np.array(yList)

def compute_error_for_line_given_points(b, m, points):
    totalError = 0 	#sum of square error formula
    for i in range (0, len(points[0])):
        x = points[0][i]
        y = points[1][i]
        totalError += (y - (m * x + b)) ** 2
    return totalError/ float(len(points))

def step_gradient(b_current, m_current, points, learning_rate):
    #gradient descent
    b_gradient = 0
    m_gradient = 0
    N = float(len(points[0]))
    for i in range(0, len(points[0])):
        x = points[0][i]
        y = points[1][i]
        b_gradient += - (2 / N) * (y - (m_current * x + b_current))
        m_gradient += - (2 / N) * x * (y - (m_current * x + b_current))
    new_b = b_current - (learning_rate * b_gradient)
    new_m = m_current - (learning_rate * m_gradient) 
    return [new_b, new_m]

def step_stochastic_gradient(b_current, m_current, points, learning_rate):
    #stochastic_gradient descent
    b_gradient = 0
    m_gradient = 0
    N = 10
    order = np.random.permutation(len(points[0]))
    for i in range(N):
        x = points[0][order[i]]
        y = points[1][order[i]]
        b_gradient += - (2 / N) * (y - (m_current * x + b_current))
        m_gradient += - (2 / N) * x * (y - (m_current * x + b_current))
    new_b = b_current - (learning_rate * b_gradient)
    new_m = m_current - (learning_rate * m_gradient)
    return [new_b, new_m]

def gradient_descent_runner(points, starting_b, starting_m, learning_rate, num_iteartions):
    b = starting_b
    m = starting_m
    for i in range(num_iteartions):
        b,m = step_gradient(b, m, np.array(points), learning_rate)
    return [b, m]

def stochastic_gradient_descent_runner(points, starting_b, starting_m, learning_rate, num_iteartions):
    b = starting_b
    m = starting_m
    for i in range(num_iteartions):
        b,m = step_stochastic_gradient(b, m, np.array(points), learning_rate)
    return [b, m]

def run_gd(points):
    learning_rate = 0.01 
    initial_b = 0 
    initial_m = 0 
    num_iteration = 10000
    print("Starting gradient descent at b = {0}, m = {1}, error = {2}".format(initial_b, initial_m, compute_error_for_line_given_points(initial_b, initial_m, points)))
    print("Running...")
    [b, m] = gradient_descent_runner(points, initial_b, initial_m, learning_rate, num_iteration)
    print("b = {0}, m = {1}, error = {2}".format(b, m, compute_error_for_line_given_points(b, m, points)))

def run_sgd(points):
    learning_rate = 0.01 #how fast the data converge
    initial_b = 0 
    initial_m = 0 
    num_iteration = 10000
    print("Starting gradient descent at b = {0}, m = {1}, error = {2}".format(initial_b, initial_m, compute_error_for_line_given_points(initial_b, initial_m, points)))
    print("Running...")
    [b, m] = stochastic_gradient_descent_runner(points, initial_b, initial_m, learning_rate, num_iteration)
    print("b = {0}, m = {1}, error = {2}".format(b, m, compute_error_for_line_given_points(b, m, points)))

# main function
if __name__ == "__main__":
    points = loadDataSet('diamonds.txt')

    print('--- gd ---')
    start_time = float(time.time())
    run_gd(points)
    end_time = float(time.time())
    print("Execution time : %fms" % (end_time - start_time))
    
    print('--- sgd ---')
    start_time = float(time.time())
    run_sgd(points)
    end_time = float(time.time())
    print("Execution time : %fms" % (end_time - start_time))
