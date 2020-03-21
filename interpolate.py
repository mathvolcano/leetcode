#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 15:18:06 2020

@author: mathvolcano
"""

def interpolate(n, instances, price):
    # Note: instances are sorted, but price need not be monotonic
    from decimal import Decimal, ROUND_HALF_UP

    # 0. Create a hash table of instances to price
    instance_price_pairs = list(zip(instances, price))
    # Price quotes lapse: disregard 0 or negative unit prices
    instance_price_pairs = [x for x in instance_price_pairs if x[1] > 0]
    n_prior_instances = len(instance_price_pairs)

    # 1. if the DB has 1 quantity that is the price per unit
    if n_prior_instances == 1:
        return str(round(instance_price_pairs[0][1], 2))

    # Macros
    instance_to_price = dict(instance_price_pairs)
    n_historical_instances = len(instance_price_pairs)
    smallest_instance = instance_price_pairs[0][0]
    largest_instance = instance_price_pairs[-1][0]

    def eval_line_from_point_pair(p0, p1, eval_x):
        """Use point-slope form to evaluate at new x. p0 = (x0, y0)."""
        slope = (p1[1] - p0[1]) / (p1[0] - p0[0])
        y = slope * (eval_x - p0[0]) + p0[1]
        return y


    # 1. if n instances is exactly the same as prior return prior price
    if n in instance_to_price:
#        print('is in')
        val = instance_to_price[n]
    # 2. if n is smaller than priors then linearly extrapolate
    elif n < smallest_instance:
#        print('smallest')
        n_smallest_2 = instance_price_pairs[:2]
        val = eval_line_from_point_pair(n_smallest_2[0], n_smallest_2[1], n)
    # 3. if n is between a small & large number then linearly interpolate
    elif n > largest_instance:
#        print('largest')
        n_largest_2 = instance_price_pairs[-2:]
        val = eval_line_from_point_pair(n_largest_2[0], n_largest_2[1], n)
    elif (n > smallest_instance) and (n < largest_instance):
#        print('between')
        for i in range(n_prior_instances):
            if instances[i] > n:
                smaller = (instances[i-1], price[i-1])
                larger = (instances[i], price[i])
                break
        val = eval_line_from_point_pair(smaller, larger, n)
#    else:
#        print('error case')

    # Return result rounded to 2 decimal places as a str
    val = Decimal(val)
    rounded_val = val.quantize(Decimal('.01'), rounding=ROUND_HALF_UP)
    output_str = str(rounded_val)
    if len(output_str) >= 3:
        if (output_str[-1] == '0') and (output_str[-3] == '.'):
            output_str = output_str[:-1]
    return output_str

n = 2000
instances = [10, 25, 50, 100, 500]
price = [27.32, 23.13, 21.25, 18.00, 15.5]

n = 40
instances = [10, 25, 50, 100, 500]
price = [17.0, 18.0, 20.0, 22.0, 29.15]

