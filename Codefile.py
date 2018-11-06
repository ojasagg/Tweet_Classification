import pymongo
import time
import json
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
from sklearn import cluster
from pymongo import MongoClient
from twython import Twython,TwythonError,TwythonRateLimitError

api_key = '27v2GVACm3JXGdQmwlOZNuCCs'
api_secret = '5MOMThMZa98tsqpoXasH1bzdB6LctsEBmCDgYLV7lps5GFpIpI'
access_token = '2598233010-LALsN4O8oWCeImm9QYgzGQprRKpkDfGJPr1c9CW'
access_token_secret = '9Z0AVLWMstRmlz6tLtdGSGQ7HDkZmPjvqgDIe2shWPH5W'

twitter= Twython(api_key,api_secret,access_token,access_token_secret)

client = MongoClient()
db = client.ojasdb
addr_ask_db=db.addr_ask
contact_ask_db=db.contact_ask
email_ask_db=db.email_ask
addr_give_db=db.addr_give
contact_give_db=db.contact_give
email_give_db=db.email_give
all_give_db=db.all_give
all_ask_db=db.all_ask
all_db=db.all
#Variables declared



'''
#Now collecting tweets providing address details
tweets = twitter.search(q = "meet me -filter:retweets", lang = 'en' , count = "100" , result_type = "mixed",include_entities='True')
for tweet in tweets['statuses']:
	twt_id=tweet['id']
	arr.append(twt_id)
	addr_give.append(twt_id)	
	addr_give_db.insert(tweet)
tweets = twitter.search( q = "address is -filter:retweets", lang = 'en' , count = "100" , result_type = "mixed", include_entities='True')
for tweet in tweets['statuses']:
	twt_id=tweet['id']
	arr.append(twt_id)
	addr_give.append(twt_id)				
	addr_give_db.insert(tweet)
#Tweets giving address done
time.sleep(5)

#Now collecting tweets providing contact details
tweets = twitter.search(q = "contact me -filter:retweets", lang = 'en' , count = "100" , result_type = "mixed",include_entities='True')
for tweet in tweets['statuses']:
	twt_id=tweet['id']
	arr.append(twt_id)
	contact_give.append(twt_id)				
	contact_give_db.insert(tweet)
tweets = twitter.search( q = "contact is -filter:retweets", lang = 'en' , count = "100" , result_type = "mixed",include_entities='True')
for tweet in tweets['statuses']:
	twt_id=tweet['id']
	arr.append(twt_id)	
	contact_give.append(twt_id)				
	contact_give_db.insert(tweet)
tweets = twitter.search( q = "number is -filter:retweets", lang = 'en' , count = "100" , result_type = "mixed",include_entities='True')
for tweet in tweets['statuses']:
	twt_id=tweet['id']
	arr.append(twt_id)	
	contact_give.append(twt_id)				
	contact_give_db.insert(tweet)
tweets = twitter.search( q = "call me -filter:retweets", lang = 'en' , count = "100" , result_type = "mixed", include_entities='True')
for tweet in tweets['statuses']:
	twt_id=tweet['id']
	arr.append(twt_id)	
	contact_give.append(twt_id)		
	contact_give_db.insert(tweet)
tweets = twitter.search( q = "contact at -filter:retweets", lang = 'en' , count = "100" , result_type = "mixed",include_entities='True')
for tweet in tweets['statuses']:
	twt_id=tweet['id']
	arr.append(twt_id)	
	contact_give.append(twt_id)		
	contact_give_db.insert(tweet)
tweets = twitter.search( q = "call at -filter:retweets", lang = 'en' , count = "100" , result_type = "mixed", include_entities='True')
for tweet in tweets['statuses']:
	twt_id=tweet['id']
	arr.append(twt_id)	
	contact_give.append(twt_id)		
	contact_give_db.insert(tweet)	
#Tweets giving contact done
time.sleep(5)

#Now collecting tweets providing email details
tweets = twitter.search( q = "mail me -filter:retweets", lang = 'en' , count = "100" , result_type = "mixed",include_entities='True')
for tweet in tweets['statuses']:
	twt_id=tweet['id']
	arr.append(twt_id)
	email_give.append(twt_id)		
	email_give_db.insert(tweet)	
tweets = twitter.search( q = "email me -filter:retweets", lang = 'en' , count = "100" , result_type = "mixed", include_entities='True')
for tweet in tweets['statuses']:
	twt_id=tweet['id']
	arr.append(twt_id)
	email_give.append(twt_id)		
	email_give_db.insert(tweet)	
tweets = twitter.search( q = "email is -filter:retweets", lang = 'en' , count = "100" , result_type = "mixed", include_entities='True')
for tweet in tweets['statuses']:
	twt_id=tweet['id']
	arr.append(twt_id)
	email_give.append(twt_id)		
	email_give_db.insert(tweet)
#Tweets giving email done
time.sleep(5)


#Now collecting tweets asking address details
tweets = twitter.search( q = "share your address -filter:retweets", lang = 'en' , count = "100" , result_type = "mixed",include_entities='True')
for tweet in tweets['statuses']:
	twt_id=tweet['id']
	arr.append(twt_id)
	addr_ask.append(twt_id)		
	addr_ask_db.insert(tweet)	
#Tweets asking address done
time.sleep(5)

#Now collecting tweets asking contact details
tweets = twitter.search( q = "share your contact -filter:retweets", lang = 'en' , count = "100" , result_type = "mixed",include_entities='True')
for tweet in tweets['statuses']:
	twt_id=tweet['id']
	arr.append(twt_id)
	contact_ask.append(twt_id)		
	contact_ask_db.insert(tweet)	
#Tweets asking contact done
time.sleep(5)

#Now collecting tweets asking email details
tweets = twitter.search( q = "share your email -filter:retweets", lang = 'en' , count = "100" , result_type = "mixed",include_entities='True')
for tweet in tweets['statuses']:
	twt_id=tweet['id']
	arr.append(twt_id)
	email_ask.append(twt_id)		
	contact_ask_db.insert(tweet)	
#Tweets asking email done
time.sleep(5)

#Adding data to db's named 'all'

e=addr_ask_db.find()
for oj in e:
	all_db.insert(oj)
	all_ask_db.insert(oj)
e=contact_ask_db.find()
for oj in e:
	all_db.insert(oj)
	all_ask_db.insert(oj)
e=addr_give_db.find()
for oj in e:
	all_db.insert(oj)
	all_give_db.insert(oj)
e=contact_give_db.find()
for oj in e:
	all_db.insert(oj)
	all_give_db.insert(oj)
e=email_give_db.find()
for oj in e:
	all_db.insert(oj)
	all_give_db.insert(oj)
'''
#Data collection done till now





tweet_id=[]
tweet_text=[]
reviewer_id=[]
reviewer_follower_count=[]
reviewer_tweet_count=[]
reviewer_name=[]
reviewer_following_count=[]
follower_following=[]
reputation=[]
verified=[]
data=all_db.find()
vrfd=0
for oj in data:
	tweet_id.append(int(oj['id']))
	reviewer_id.append(int(oj['user']['id']))
	reviewer_follower_count.append(int(oj['user']['followers_count']))
	reviewer_following_count.append(int(oj['user']['friends_count']))
	reviewer_tweet_count.append(int(oj['user']['statuses_count']))
	reviewer_name.append(oj['user']['screen_name'])
	tweet_text.append(oj['text'])
	if(oj['user']['verified']):
		vrfd+=1
		verified.append(1)
	else:
		verified.append(0)
#Data extraction from tweets done till now




'''
print "Address sharing tweet count = "+str(addr_give_db.count())
print "Contact sharing tweet count = "+str(contact_give_db.count())
print "Email sharing tweet count = "+str(email_give_db.count())
print "Address asking tweet count = "+str(addr_ask_db.count())
print "Contact asking tweet count = "+str(contact_ask_db.count())
print "Email asking tweet count = "+str(email_ask_db.count())
print "Total tweet count for this experiment = "+str(all_db.count())
'''

						#Feature Set Generation


#1. Follower following count

for i in range(len(tweet_id)):
	follower_following.append(float(reviewer_follower_count[i])/(float(reviewer_following_count[i])+1))


#2. Tweet count computed above


#3. Reputation count
for i in range(len(tweet_id)):
	reputation.append(float(reviewer_follower_count[i])/(float(reviewer_following_count[i])+1+float(reviewer_follower_count[i])))

#4. Verified computed above




						#Applying K Means Unsupervised Learning


x=[]	#input for kmeans
tmp=[]	#input for x


#Dataset generation for K means
for i in range(len(tweet_id)):
	tmp.append(follower_following[i])
	tmp.append(reputation[i])
	tmp.append(reviewer_tweet_count[i])
	tmp.append(verified[i])
	x.append(tmp)
	tmp = []


#Applying K means

k_means=cluster.KMeans(n_clusters=2)
spammers=k_means.fit_predict(x)

#Plotting graph of spam and non spam tweets

graph = TSNE(n_components=2).fit_transform(x)
gr_x=graph[:,0]
gr_y=graph[:,1]
plt.scatter(gr_x,gr_y,c=spammers)
plt.show()


#Output analysis and comparison with native method spam detection



count=0
for i in range(len(spammers)):
	if(spammers[i]==1):
		count+=1
print 'Number of spam users as per K Means is = '+ str(count)

ff=0
rep=0
twt_cnt=0
for i in range(len(tweet_id)):
	if(reviewer_following_count[i]>0):
		ratio=float(reviewer_follower_count[i])/float(reviewer_following_count[i])
		ratio1=float(reviewer_follower_count[i])/(float(reviewer_following_count[i])+float(reviewer_follower_count[i]))
		if(ratio<.5):
			ff+=1
		if(ratio1<.1):
			rep+=1
		if(reviewer_tweet_count[i]<50):
			twt_cnt+=1

print 'Number of spam users as per (follower/following ratio <.5 is) is = '+ str(ff)
print 'Number of spam users as per (reputation <.1 is) is = '+ str(rep)
print 'Number of spam users as per (tweet count <500 is) is = '+ str(twt_cnt)
print 'Number of spam users as per verified or not is = '+ str(vrfd)

