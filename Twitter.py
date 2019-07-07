#!/usr/bin/env python
# -- coding: utf-8 --

from TwitterScrapperRoHec import query_tweets

if __name__ == '__main__':
    #Or save the retrieved tweets to file:
    file = open('output.txt', 'w')
    for tweet in query_tweets("(incendio OR inundación OR temblor OR sismo) AND (CDMX OR Veracruz OR Potosí OR Oaxaca OR Tamaulipas OR Guerrero OR Nayarit OR Chihuahua OR Chiapas OR Jalisco OR Michoacan OR Quintana)", 50):
        try:
            file.write(tweet.text + "\n")
        except:
            continue
    file.close()
