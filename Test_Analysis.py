# importing the data
import pandas as pd

data = pd.read_csv(
    "https://media.githubusercontent.com/media/nickeubank/MIDS_Data/master/World_Development_Indicators/wdi_small_tidy_2015.csv"
)


data.head()


# pulling out columns
data2 = data[
    [
        "Mortality rate, infant (per 1,000 live births)",
        "GDP per capita (constant 2010 US$)",
        "Country Name",
    ]
]

data2.head()


# plotting data
import matplotlib.pyplot as plt

plt.plot(
    "Mortality rate, infant (per 1,000 live births)",
    "GDP per capita (constant 2010 US$)",
    data=data2,
)
