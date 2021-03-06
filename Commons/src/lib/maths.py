'''
Created on Jun 15, 2013

@author: rmaharaj
@summary: This file contains math related functions.
'''
#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#
# Reuse Instructions
# Ensure that project references the Commons project
# add:
#     import lib.maths as maths
#   or
#     from lib import maths as maths
#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#

# imports
import math, decimal
decimal.getcontext().prec = 10

def linear_regression(a):
    # x and y positions in array
    x = 1
    y = 2
    n = len(a)
    sumX = sum_array(a, x, n)
    sumY = sum_array(a, y, n)
    avgX = average_array(a, x, n)
    avgY = average_array(a, y, n) #average_array(list(a[i][y] for i in a))
    sumXY = sum_double_array(a, a, x, y, n)#sum_array(list(a[i][x]*a[i][y] for i in a))
    sumXX = sum_double_array(a, a, x, x, n)#sum_array(list(a[i][x]*2 for i in a))
    sumYY = sum_double_array(a, a, y, y, n)
    beta1 = calc_beta_sub_0(sumXY, sumXX, avgX, avgY, n)
    beta0 = calc_beta_sub_1(beta1, avgX, avgY)
    r = calc_correlation(n, sumXY, sumX, sumY, sumXX, sumYY)
    sig_70 = calc_significance(r, n, 70)
    sig_90 = calc_significance(r, n, 90)
    std_dev = calc_std_dev(n, a, x, y, beta0, beta1)
    X_k = 44.8 #386
    Y_k = beta0 + (beta1 * X_k)
    range_70 = calc_prediction_range(n, 70, a, x, y, beta0, beta1, X_k, avgX)
    range_90 = calc_prediction_range(n, 90, a, x, y, beta0, beta1, X_k, avgX)
    LPI_70 = Y_k - range_70
    UPI_70 = Y_k + range_70
    LPI_90 = Y_k - range_90
    UPI_90 = Y_k + range_90
    print "n:",n
    print "sumX:",sumX
    print "sumY:",sumY
    print "sumXY:",sumXY
    print "sumXX:",sumXX
    print "sumYY:",sumYY
    print "avgX:",avgX
    print "avgY:",avgY
    
    print "Beta1:", beta1, "; Beta0:", beta0
    print "corr:",r
    print "significance @ 70: t = " + str(sig_70[0]) + ";  p = " + str(sig_70[1])
    print "significance @ 90: t = " + str(sig_90[0]) + ";  p = " + str(sig_90[1])
    print "std dev:",std_dev
    print "range_70:",range_70
    print "range_90:",range_90
    
    print "UPI_70:",UPI_70
    print "LPI_70:",LPI_70
    print "UPI_90:",UPI_90
    print "LPI_90:",LPI_90
    

def calc_beta_sub_0(sumXY, sumXX, avgX, avgY, n):
    numerator = sumXY - (n * avgX * avgY)
    denominator = sumXX - (n * avgX**2)
    return float(numerator / denominator)

def calc_beta_sub_1(beta1, avgX, avgY):
    return float(avgY - (beta1 * avgX))

def calc_correlation(n, sumXY, sumX, sumY, sumXX, sumYY):
    numerator = n * sumXY - sumX * sumY
    denominator = math.sqrt(((n*sumXX)-sumXX)*((n*sumYY)-sumYY))
    return float(numerator / denominator)

def calc_significance(r, n, alpha_over_two):
    t = float( ( math.fabs(r) * (math.sqrt(n - 2)) ) / math.sqrt(1 - (r**2) ) )
    prob = calc_t_dist_values(n, alpha_over_two, t_value=t)
    two_tailed_prob = float(2 * ( 1 - prob ) )
    return [t,two_tailed_prob]

def calc_variance(n, a, x, y, beta0, beta1):
    sum = 0
    for i in range(0, n):
        sum += float((float(a[i][y]) - beta0 - (beta1*float(a[i][x])))**2)
    return float(  decimal.Decimal(sum) * ( decimal.Decimal(1) / decimal.Decimal(n-2) )  )

def calc_std_dev(n, a, x, y, beta0, beta1):
    return float(math.sqrt(calc_variance(n, a, x, y, beta0, beta1)))

def calc_prediction_range(n, alpha_over_two, a, x, y, beta0, beta1, X_k, avgX):
    part1 = calc_t_dist_values(n, alpha_over_two)
    part2 = calc_std_dev(n, a, x, y, beta0, beta1)
    outside = float(part1 * part2)
    up = float((X_k - avgX)**2)
    down = 1 # setting to 1 to avoid div by 0 error
    for i in range(0, n):
        down += float((float(a[i][x]) - avgX)**2)
    
    inside = float( (1 + (decimal.Decimal(1)/decimal.Decimal(n) + ((decimal.Decimal(up) / decimal.Decimal(down - 1))))).sqrt())
    return float(outside * inside)

def calc_t_dist_values(n, alpha_over_two, t_value=0):
    # table A2 selected values. dof is first column
    p_values = [.2, .4, .7, .8, .9, .95, .98, .99]
    # a/2 =       20 ,  40,   70,    80,    90,    95,     98,     99
    tdist = [[1,  .325, .727, 1.963, 3.078, 6.314, 12.706, 31.821, 63.657],
             [2,  .289, .617, 1.386, 1.886, 2.920, 4.303,  6.965,  9.925],
             [3,  .277, .584, 1.250, 1.638, 2.353, 3.182,  4.541,  5.841],
             [4,  .271, .569, 1.190, 1.533, 2.132, 2.776,  3.747,  4.604],
             [5,  .267, .559, 1.156, 1.476, 2.015, 2.571,  3.365,  4.032],
             [6,  .265, .553, 1.134, 1.440, 1.943, 2.447,  3.143,  3.707],
             [7,  .263, .549, 1.119, 1.415, 1.895, 2.365,  2.998,  3.499],
             [8,  .262, .546, 1.108, 1.397, 1.860, 2.306,  2.896,  3.355],
             [9,  .261, .543, 1.100, 1.383, 1.833, 2.262,  2.821,  3.250],
             [10, .260, .542, 1.093, 1.372, 1.812, 2.228,  2.764,  3.169],
             [15, .258, .536, 1.074, 1.341, 1.753, 2.131,  2.602,  2.947],
             [20, .257, .533, 1.064, 1.325, 1.725, 2.086,  2.528,  2.845],
             [30, .256, .530, 1.055, 1.310, 1.697, 2.042,  2.457,  2.750],
             [99, .253, .524, 1.036, 1.282, 1.645, 1.960,  2.326,  2.576]]
    dof = n-2
    index = [0, 0]
    if dof == 0:
        print "Size of sample is too small: Degress of Freedom = 0"
    elif dof <= 10 and dof > 0:
        index[0] = dof - 1
    elif dof == 15:
        index[0] = 10
    elif dof == 20:
        index[0] = 11
    elif dof == 30:
        index[0] = 12
    else:
        index[0] = 13
        
    if alpha_over_two == 20:
        index[1] = 1
    elif alpha_over_two == 40:
        index[1] = 2
    elif alpha_over_two == 70:
        index[1] = 3
    elif alpha_over_two == 80:
        index[1] = 4
    elif alpha_over_two == 90:
        index[1] = 5
    elif alpha_over_two == 95:
        index[1] = 6
    elif alpha_over_two == 98:
        index[1] = 7
    elif alpha_over_two == 99:
        index[1] = 8
    else:
        print "Alpha/2 is not valid.  Using value of 99."
        index[1] = 8
    
    if t_value == 0:
        return tdist[index[0]][index[1]]
    else:
        row = tdist[index[0]]
        for i in range(1, len(row)):
            if row[i] > t_value and i != 0:
                prob = p_values[i-1]
                break
            else:
                continue
            if i == len(row)-1:
                prob = p_values[i]
        return prob

def sum_array(a, value, n):
    result = 0.0
    for i in range(0, n):
        result += float(a[i][value])
    return result

def sum_double_array(a, b, value1, value2, n):
    result = 0.0
    for i in range(0, n):
        result += float(a[i][value1]) * float(b[i][value2])
    return result

def average_array(a, value, n):
    return float((sum_array(a, value, n)) / n)

def average_double_array(a, b, value1, value2, n):
    return float((sum_double_array(a, b, value1, value2, n)) / n)



#linear_regression([[1, 75, 80], [2, 63, 60]])
    