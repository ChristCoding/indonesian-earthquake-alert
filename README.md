# Indonesia Earthquake Alert
Package to retrieve latest Indonesia earthquake alert from https://www.bmkg.go.id/

# How it work?
Package will scrape the latest Indonesia earthquake alert from [BMKG](https://www.bmkg.go.id/) website.
The data will be shown with this format:<br/>
Latest Earthquake News in Indonesia<br/>
Date: ________<br/>
Time: ________ WIB<br/>
Magnitude: ________<br/>
Location: LS: ________ BT: ________<br/>
Center: ________<br/>
Impact Scale: ________<br/>

Package will use BeautifulSoup4 and requests to retrieve and parse the website data.

# Example of usage
---import command---<br/>
import earthquakealert_ID<br/>
---function for scraping data from https://www.bmkg.go.id/---<br/>
result=earthquakealert_ID.getdata()<br/>
---function for display the scraped data---<br/>
earthquakealert_ID.displaydata(result)