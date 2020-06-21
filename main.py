#from src.twitter import Twitter        # Import Class: Twitter
from src.instagram import Instagram     # Import Class: Instagram
from src.classify import classify       # Import Class: classify

if __name__ == '__main__':
    print("Starting Social Media Scrapper...")
    insta_tag = str(input('What hastag would you like to search for: '))
    num_pics  = int(input('Number of pictures you would like to search (int):  '))
    insta = Instagram(insta_tag,num_pics)
    print("Starting Instagram Scrapper")
    insta.Tag_Scrapper()
    print("Starting Classification of Images")
    classify = classify(insta_tag)
    classify.process()
