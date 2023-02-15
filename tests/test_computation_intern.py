from unittest import TestCase
from typing import List
from datetime import datetime,date
from service.computation_intern_strategy import ComputationInternStrategy
class TestComputationIntern(TestCase) :
    def test_compute_salary(self) :
        #given
        league_internal_salary_grid = [15,25,40]
        date_start = date(2021,4,15)
        date_end = date(2023,6,30)
        compute = ComputationInternStrategy()

        #when
        salary = compute.compute_salary(None,league_internal_salary_grid,date_start,date_end,None)

        #then
        self.assertEqual(salary,24865)








