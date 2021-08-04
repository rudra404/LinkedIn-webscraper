# LinkedIn-webscraper

This python script scrapes LinkedIn profiles for essential info (using Selenium) and stores the data in the results.csv file

To use it, go to parameters.py and enter your LinkedIn login credentials as well as search terms for the profiles. E.g.: "Software Developer" AND "Hong Kong"
Run scraper.py from your terminal and let the magic begin.

Made as a side-project in September 2020 to learn webscraping.

Credits: https://www.linkedin.com/pulse/how-easy-scraping-data-from-linkedin-profiles-david-craven/

Status on 06-10-2020: Script can open different tabs, login on LinkedIn, search query on google, and print all the profile links on terminal.

To do: Loop clicking on all printed links. Scrape info from each profile link. Print it in the results.csv file.

Additional To do: Make the browsing more "human-like" by adding suitable delays and mimic "scrolling" behaviour. Copy the cookies and use them in scraper.
