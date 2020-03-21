#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 16:15:35 2020

@author: mathvolcano
"""

## Employee info
#class Employee:
#    def __init__(self, id: int, importance: int, subordinates: List[int]):
#        # It's the unique id of each node.
#        # unique id of this employee
#        self.id = id
#        # the importance value of this employee
#        self.importance = importance
#        # the id of direct subordinates
#        self.subordinates = subordinates

def getImportance(employees, idx):
    """Slow."""
    imprt = [x.importance for x in employees if x.id == id][0]
    subs = [x.subordinates for x in employees if x.id == id][0]
    while subs:
        sub_emp = subs.pop(0)
        sub_imprt = [x.importance for x in employees if x.id == sub_emp][0]
        sub_subs = [x.subordinates for x in employees if x.id == sub_emp][0]
        imprt += sub_imprt
        subs = subs + sub_subs
    return imprt


def getImportance(employees, id):
    employee_dict = {employee.id : employee for employee in employees}
    
    def dfs(id):
        return employee_dict[id].importance + sum(dfs(id) for id in employee_dict[id].subordinates)
    
    return dfs(id)
