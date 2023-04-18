import pandas as pd

class NJCleaner():
    def __init__(self, csv_path) -> None:
        self.data = pd.read_csv(csv_path)
    
    def order_by_scheduled_time(self) -> pd.DataFrame:
        order = self.data.sort_values(by = ['scheduled_time'])
        return order
    
    def drop_columns_and_nan(self) -> pd.DataFrame:
        self.data = self.data.dropna()
        self.data = self.data.drop(['from', 'to'], axis = 1)
        return self.data
        
    def convert_date_to_day(self) -> pd.DataFrame:
        self.data['day'] = pd.to_datetime(self.data['date']).dt.day_name()
        self.data = self.data.drop(['date'], axis = 1)
        return self.data
    
    def convert_scheduled_time_to_part_of_the_day(self):
        bins = [0, 4, 8, 12, 16, 20, 24]
        labels = ['late_night', 'early_morning', 'morning', 'afternoon', 'evening', 'night']
        self.data['part_of_the_day'] = pd.cut(pd.to_datetime(self.data['scheduled_time']).dt.hour, bins = bins, labels = labels, right = False)
        self.data = self.data.drop(['scheduled_time'], axis = 1)
        return self.data
    
    def convert_delay(self):
        self.data['delay'] = self.data['delay_minutes'].apply(lambda x: 1 if x >= 5 else 0)
        return self.data
    
    def drop_unnecessary_columns(self):
        self.data = self.data.drop(['train_id', 'actual_time', 'delay_minutes'], axis = 1)
        return self.data
    
    def save_first_60k(self, path) -> None:
        self.data.iloc[:60000].to_csv(path, index = False)
        
    def prep_df(self, path) -> None:
        self.data = self.order_by_scheduled_time()
        self.data.to_csv(path)
        self.drop_columns_and_nan()
        self.convert_date_to_day()
        self.convert_scheduled_time_to_part_of_the_day()
        self.convert_delay()
        self.drop_unnecessary_columns()
        self.save_first_60k(path)
        