from xml.sax.xmlreader import InputSource


def greater(a,b):
    if a>b:
        return(a,'is greater')
    else: 
        return(b,'is greater')
print(greater(a=int(input()),b= int(input())))     