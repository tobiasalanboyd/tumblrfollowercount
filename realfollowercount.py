client = pytumblr2.TumblrRestClient(     
'<consumer_key>',     
'<consumer_secret>',     
'<oauth_token>',     
'<oauth_secret>', )  
client.info()
blogname="lonelytuatara"

info = client.blog_info(blog_name)
followers = info['blog']['followers']
print(followers)