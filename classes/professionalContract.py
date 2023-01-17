self.end_date = date(self.date_start.year + self.duration -1 ,6,30) if date(self.date_start.year,6,30) > self.date_start else date(self.date_start.year+ self.duration, 6,30)
