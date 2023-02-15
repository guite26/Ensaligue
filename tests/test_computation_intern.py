from unittest import TestCase
from typing import List
from datetime import datetime,date
from service.computation_intern_strategy import ComputationInternStrategy
from service.utils import get_days_periods
class TestComputationIntern(TestCase) :
    def test_get_days_period(self):
        #GIVEN
        date_start = date(2021,4,15)
        date_end = date(2023,6,30)
        #WHEN
        l = get_days_periods(date_start,date_end)
        #THEN
        self.assertEqual(l,[77,365,365])


    def test_compute_salary(self) :
        #given
        league_internal_salary_grid = [15,25,40]
        date_start = date(2021,4,15)
        date_end = date(2023,6,30)
        compute = ComputationInternStrategy()

        #when
        salary = compute.compute_salary(None,league_internal_salary_grid,date_start,date_end,None)

        #then
        self.assertEqual(salary,24880)


    def test_update_salary(self) :
        #given
        league_internal_salary_grid = [15,25,40]
        new_league_internal_salary_grid = [20,30,45]
        date_start = date(2021,4,15)
        date_end = date(2023,6,30)
        compute = ComputationInternStrategy()

        #when
        salary = compute.update_salary(None,new_league_internal_salary_grid,date_start,date_end,None,league_internal_salary_grid)

        #then
        self.assertEqual(salary,25560)





