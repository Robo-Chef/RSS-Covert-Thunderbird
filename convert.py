print("hello world")

#class (blueprint for your custom types)
class RssFeedLine(): #RssFeedLine() or RssFeedLine
    """
    """
    def __init__(self, line): #__init__ intitialise the method, or constructor, self refers to the new object(instance) being created
        line = line.strip('\n') #return a COPY of the line string, stripped of '\n' (new line delimiter)
        self.title, self.url = line.split(',') # this will produce 'ACS Earth,http://feeds.feedburner' into ['ACS Earth', 'Http://etc']

    def capitalize_title(self):
        return self.title.upper()

    

# we need to read in the rss-feed-list file
# use the python builtin `open` function, to read in the file.
with open('rss-feed-list.csv', 'r') as rss_feed_file: # load the file in read mode into the rss_feed_file variable
    # rss_feed_file == ['ACS Earth and Space,http://feeds.feedburner', 'ACS Energy Letter,http://feeds']

    count = 1
    rss_feed_list = [] # an empty list, a list being defined by = [a, 'b', True, 1]
    for line in rss_feed_file:
        rss_feed_list.append(RssFeedLine(line))
    

for line in rss_feed_list:
    print(line.title)
    print(line.url)
    print(line.capitalize_title())


print('Test')


#python primitive/basic types
#string = 'a,b,c,d'
#Boolean = True or False
#integer = 112334




# class Car():
#     def __init__(self, engine, steering_wheel, accelerator):
#         self.engine = engine
#         self.steering_wheel = steering_wheel
#         self.accelerator = 'a'

# mitsubishi_car = Car(engine='Super engine', steering_wheel="amazing steering wheel", accelerator="awesome accelerator")
# lionels_car = Car(engine="shit engine", steering_wheel="shit steering wheel", accelerator="shit accelerator")
# print(mitsubishi_car.accelerator)
# print(lionels_car.accelerator)

# x = RssFeedLine() # x is an instance of type 'RssFeedLine'
# y = RssFeedLine()

# print(x.title)
# print(x.url)

# x = "hello" # defining a variable of type string
# y = False # defining a variable of type boolean
# a, b = "Hello", True
# x, y, a, b= "hello", False, "Hello", True

