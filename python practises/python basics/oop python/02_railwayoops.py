import pandas as pd
pd.DataFrame()
class RailwayForm:
    formType="Railwayform"
    def printdata(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")
hasnainsApplication=RailwayForm()
hasnainsApplication.name="Hasnain"
hasnainsApplication.train="RajdhaniExpress"
hasnainsApplication.printdata()