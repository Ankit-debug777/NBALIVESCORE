# NBALIVESCORE
## Get live NBA scores. (It can also be used for other professional basketball leagues)
This program accesses the xml data using urllib.request. </br>
The xml data looks like this: https://www.scorespro.com/rss2/live-basketball.xml </br>
Then we read the xml data using ET.fromstring. </br>
The details of the match are present in the item tags. </br>
We use regular expressions to group various types of data present in the item tag (re.compile). </br>
And then we search them (regex.search) and match them with their property, for example: team name, score etc. </br>
time.sleep(30) pauses the program for 30 secs. </br>
The clear_screen function clears the terminal before displaying the scores again.</br>
The while loop ensures the program keeps running.</br>
 The scores are computed every 30 seconds.
 #### Note: For mac os and linux replace 'cls' with 'clear' in clear_screen function
