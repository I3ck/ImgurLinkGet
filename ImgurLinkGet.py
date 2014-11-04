import urllib
import json
import urlparse

class ImgurLinkGet:
	def __init__(self):
		self.data = []

	def load_data(self, url):
		self.data = [] # reset data
		parsed = urlparse.urlparse(url)
		if parsed.netloc != "imgur.com":
			print "no imgur url" #todo just for debugging, remove later
			return False
		if parsed.path.startswith("/gallery"):
			response = urllib.urlopen("http://imgur.com" + parsed.path + ".json")
			jsn = json.loads(response.read())
			images =  jsn['data']['image']['album_images']['images']
			for image in images:
				self.data.append(image['hash'] + image['ext'])
			print "is a gallery" #todo just for debugging, remove later
			print self.data
			# do gallery stuff
		elif parsed.path.startswith("/user"):
			print "is a user" #todo just for debugging, remove later
			return False
		else:
			self.data = ["http://i.imgur.com" + parsed.path + ".jpg", ] #todo get correct filetype
			print self.data #todo just for debugging, remove later
		#response = urllib.urlopen(url)
		#print response.read()
		return True

	def get_small_squares():
		pass

	def get_big_squares():
		pass

	def get_small_thumbnails():
		pass

	def get_medium_thumbnails():
		pass

	def get_large_thumbnails():
		pass

	def get_huge_thumbnails():
		pass

	def get_originals():
		pass


if __name__ == '__main__':
	imgurLinkGet = ImgurLinkGet()
	imgurLinkGet.load_data("http://imgur.com/gallery/qMEJb")
