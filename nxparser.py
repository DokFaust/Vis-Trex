#I think that i will need only nx and json
import networkx as nx
import json
import unicodedata

from urlparse import urlparse
from random import random as rnd

#Substitute non-ascii characters from unicode string
def normalize(unistr):
    try:
        normstr = unicodedata.normalize('NFKD', unistr).encode('ascii', 'ignore')
        return normstr
    except TypeError:
        return unistr

#A prototype for a url parser (from URL get domain)
#this will considered the source
def domainretrieve(link):
    parsed_uri = urlparse(link)
    domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
    return normalize(domain)

filename='semantic-entities.json'

fh = open('semantic-entities.json')

fc = open('graph.dot','w')

data = json.load(fh)

##Initialize NX graph
G = nx.MultiGraph()



##From here parse the JSON to get for each source the topics
#Ie consider to loop on each entity |-> check for errors? TODO

#Cycle for each entity

for (idx,entity) in enumerate(data):

    try:
        if(data[idx]["error"]):
            continue
    except KeyError:
        pass
#Consider only the 20 percent of the entries of our 
    if(rnd() > 0.05):
        continue        

    source = domainretrieve((data[idx]["url"]))

    if source not in G.nodes():
        G.add_node(source)

    #Select the timestamp
    ts = data[idx]["timestamp"]["$date"]

    #For each topic add aNEW edge with the property timestamp
    for (jdx, topic_properties) in enumerate(data[idx]["annotations"]):

            topic = normalize(topic_properties["label"])

            #Create and edge

            G.add_edge(source,topic,timestamp=ts)

                ##Fr thos not present create a list of timestamps, set as property of the edge
            
            #Append to the edge's list the timestamp
    

#Write in DOT formt the graph
nx.drawing.nx_pydot.write_dot(G,fc)

fh.close()
fc.close()
