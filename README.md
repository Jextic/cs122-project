**GPU Price Tracker**

**Authors:**
- Johnny Huynh (Role #1)
- An Pham (Role #2)

**Project Description:**

Our project will track and analyze pricing trends for various GPUs from online business websites. The data would be gathered from businesses like Micro Center, BestBuy, Newegg, and more. In our interface, users would be able to select their preferred GPU and view the change in price over the months. Users would also be able to apply filters to the data such as showing prices from only the past 6 months or exclude certain businesses from appearing in the data. Using our interface, users will be able to determine the best places and the best times to purchase their GPUS.

**Project Plan:**
- **Interface Plan:**\
  Our interface would include a large selection of recordable GPUs. Clicking on a GPU will open a popup window displaying a line plot graph of recorded prices over time for that specific GPU. There will be multiple line plots indicating which businesses those prices were recorded from. There would be buttons for users to select their preferred GPU, filter data, change the appearance of the data, and more.
- **Data Collection and Storage Plan:**\
  Importing Python's requests and BeautifulSoup libraries would help fetch the GPU names and prices from online websites. Some businesses like BestBuy also have a developer API that can be used to fetch data as well. Most likely, the raw data would be stored and organized in an Excel file.
- **Data Analysis and Visualization Plan:**\
  Analyzes the prices on different days and checks the trend of when the price is at the lowest to see when is the best place and best time to buy. We will use a time series graph to track the pricing on different websites and plot the time and date.
