#I think that i will need only nx and json
import networkx as nx
import json

#A prototype for a url parser (from URL get domain)
#this will considered the source
def domainretrieve(link):
    pass

filename='semantic-entities.json'

fh = open('semantic-entities.json')

##From here parse the JSON to get for each source the topics
#Ie consider to loop on each entity |-> check for errors? TODO

#PASS to retrieve domain to get the URL -> this considered the SOURCE
#Cycle through the annotations, retrieve the title -> add the to the graph

#In the above cycle and edge property will be the timestamp here comes the only
#hard part : if teh edge is still present; then the new timestamp must be appended to a list
#OK i will check it with has_edge
#From the 




#Open the DOT file (possibly above the fh)

#Write the graph on the DOT file

#Close both files
