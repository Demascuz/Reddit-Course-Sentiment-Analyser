# Reddit-Course-Sentiment-Analyser

Reddit course sentiment analyser for UBC students (for now).


**GOAL:** 
    
To analyse the sentiment of a given course in UBC. Done by analysing the top level comments on reddit posts regarding the specific course.

**METHOD:** 
   
* Made a Reddit bot to retrieve and store the comment data of given course. User can change the course searching and number of posts to be scanned parameters to their need. 

* Filtered the posts by discarding the ones with the "Humour" flair, due to it messing up the final average sentiment analysis rating. 

* Filtered out comments by length aswell, must be less than 150 characters and more than 10. These are just arbitrary numbers, since BERT doesn't work    well with short or long writings. Used only top level comments due to the lack of context to work with when BERT individually assesses each comment.

* Performed sentiment analysis on the given individual comments (seperatly) using BERT pre-trained language model developed by Google. Orginally used VADER sentiment analysis tool, switched to BERT as VADER wasn't very good.

**RESULTS (purely observed by me):**
    
BERT works well with simple writings with a singular topic. Not so much with longer and more complex sentences or paragraph. However, for the tested courses it does match the overall sentiment to a good extent.

**HOW TO INTERPRET DATA:**
    
For the BERT analysis and the final average,
* 1.0 - 2.4 means BAD
* 2.5 - 3.9 means NEUTRAL or OKAY
* 4.0 - 5.0 means GOOD
