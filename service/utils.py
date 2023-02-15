from datetime import datetime, date, timedelta

def remaining_days(d:date):
    if d.month < 6:
        return (date(d.year,6,30) - d).days
    else :
        return (date(d.year + 1, 6,30) - d).days

def get_days_periods(date_start, date_end):
    periods = []
    start_year = date_start.year
    end_year = date_end.year
    if date_start.month < 7:
        start_year -= 1
    if date_end.month < 7 or (date_end.month == 7 and date_end.day < 2):
        end_year -= 1
    for year in range(start_year, end_year + 1):
        start_date = date(year, 7, 1)
        end_date = date(year + 1, 7, 1) - timedelta(days=1)
        if start_date < date_start:
            start_date = date_start
        if end_date > date_end:
            end_date = date_end
        periods.append((end_date - start_date).days + 1)
    
    while len(periods)<3 :
        periods = [0] + periods
    return periods

def new_total_salary(date_start, date_end,actual_salary_grid,new_salary_grid):
    init_duration = get_days_periods(date_start,date_end)
    print(init_duration)

    remaning_duration = get_days_periods(datetime.now().date(),date_end)
    print(remaning_duration)
    past_duration = [init_duration[i] - remaning_duration[i] for i in range(len(init_duration))]
    print(past_duration)
    new_total_salary = sum([actual_salary_grid[i]*past_duration[i] + new_salary_grid[i]*remaning_duration[i] for i in range(len(init_duration)) ])
    return(new_total_salary)

def in_progress(date_end) :
    return date_end > datetime.now()

