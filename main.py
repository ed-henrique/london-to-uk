import pandas as pd

# Read customer data
#
customers = pd.read_csv("data/data.csv")
# print(customers)

# Investigate missing values
#
# print(customers.isnull().sum())

# Drop missing values
# We could also map missing addresses to 'Other', if needed
#
customers.dropna(subset=["address"], inplace=True)

# Check for negative values is "total_spend"
#
# print(customers["total_spend"].describe())

# Sample addresses
# From here, we learn that:
# - Address is divided by rows
# - Number of rows is variable
# - Addresses end with the postcode
# - All rows but the last one end with ','
# - There are no specific rows for the city
# - Searching for 'LONDON' may find 'LONDON ROAD' in some city other than
# 'London'
# - Searching for 'LONDON,' (notice the comma) may find the best results
#
# for address in customers["address"].head():
#     print(address, "\n")

# Ensure that all addreses are uppercase
#
customers["address_clean"] = customers["address"].str.upper()

# Check if there are differences between search for 'LONDON' and 'LONDON,'
#
# print(len(customers[customers["address_clean"].str.contains("LONDON")]))
# print(len(customers[customers["address_clean"].str.contains("LONDON,")]))

# Check if there are patterns for adresses with the same address lines amount
# Long story short, no reliable pattern could be found
#
customers["address_lines"] = (
    customers["address_clean"]
    .str.split(",\n")
    .apply(len)
)
# print(customers["address_lines"].value_counts().sort_index())
# print(customers.loc[customers["address_lines"] == 1, "address_clean"])
# print((
#     customers[customers["address_lines"] == 2]
#     .sample(5, random_state=42)
#     ["address_clean"])
# )

# Read cities data
#
cities = pd.read_csv("data/cities.csv", header=None, names=["city"])
# print(cities.head())

# Clean cities data
#
countries_to_remove = ["England", "Scotland", "Wales", "Northern Ireland"]
# print(len(cities))
cities_to_remove = cities[cities["city"].isin(countries_to_remove)].index
cities = cities.drop(index=cities_to_remove)
# print(len(cities))
cities["city"] = cities["city"].str.replace("*", "", regex=False)
cities["city"] = cities["city"].str.upper()
# print(cities.head())

# Create 'city' column
#
for city in cities["city"].values:
    customers.loc[customers["address_clean"].str.contains(f"\n{city},"),
    "city"] = city

customers["city"] = customers["city"].fillna("OTHER")
# print(customers.head())

# Explore the new city column
#
# print(customers["city"].value_counts().head(20))

# Explore the address for 'city' equal to 'OTHER'
# We can see that there are addresses that refer to regions inside London, as in
# Twickenham. This may be added in a future iteration
#
# sample_other = customers[customers["city"] == "OTHER"].sample(5,
# random_state=42)
# for address in sample_other["address_clean"].values:
#     print(address, "\n")

# Check if there are any cities without representation
# We can see that there are no customers in 'KINGSTON-UPON-HULL', but this might
# be because the city is often abbreviated to 'HULL', which is domain specific
# knowledge
#
# print(set(cities["city"]) - set(customers["city"]))

# Check if 'KINGSTON-UPON-HULL' appears as 'HULL'
# There are multiple instances where this occurs
#
# print(customers[customers["address_clean"].str.contains("\nHULL,")])

# Fixing 'KINGSTON-UPON-HULL'
#
customers.loc[customers["address_clean"].str.contains("\nHULL,"),
"city"] = "HULL"

# Analyze spend by city
# from matplotlib.ticker import FuncFormatter
# import matplotlib.pyplot as plt
# 
# def millions(x, pos):
#     return '£%1.1fM' % (x * 1e-6)
# 
# formatter = FuncFormatter(millions)
# 
# fig, axis = plt.subplots()
# 
# top_20_spend = (
#     customers
#     .groupby("city")
#     ["total_spend"].sum()
#     .sort_values(ascending=False)
#     .head(20)
#     .sort_values(ascending=True)
# )
# 
# top_20_spend.plot.barh(ax=axis)
# 
# axis.xaxis.set_major_formatter(formatter)
# axis.set(
#     title="Total customer spend by city",
#     xlabel="Total spend"
# )
# 
# plt.show()

# Answering the problem questions
print("Total spend for London customers:")
print(customers.loc[customers["city"] == "LONDON", "total_spend"].sum())

print("Total spend outside London:")
print(customers.loc[customers["city"] != "LONDON", "total_spend"].sum())

print("Total spend outside London (excluding OTHER):")
print(customers.loc[~customers["city"].isin(["LONDON", "OTHER"]), "total_spend"]
.sum())
