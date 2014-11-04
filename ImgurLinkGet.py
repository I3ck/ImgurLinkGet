import urllib
import json
import urlparse

class ImgurLinkGet:
	def __init__(self):
		self.data = []

	def load_data(self, url):
		self.data = [] # reset data (todo make another mode to append data or create a reset method)
		parsed = urlparse.urlparse(url)
		if parsed.netloc != "imgur.com":
			print "no imgur url" #todo just for debugging, remove later
			return False
		if parsed.path.startswith("/gallery"):
			response = urllib.urlopen("http://imgur.com" + parsed.path + ".json")
			jsn = json.loads(response.read())
			images =  jsn['data']['image']['album_images']['images']
			for image in images:
				date = {'hash' : image['hash'], 'ext' : image['ext']}
				self.data.append(date)
			print "is a gallery" #todo just for debugging, remove later
			# do gallery stuff
		elif parsed.path.startswith("/user"):
			print "is a user" #todo just for debugging, remove later
			return False
		else:
			date = {'hash' : parsed.path[1:], 'ext' : '.jpg'} #todo get correct filetype
			self.data.append(date)
		return True

	def _get_any(self,suffix):
		links = []
		for date in self.data:
			links.append("http://i.imgur.com/" + date['hash'] + suffix + date['ext'])
		return links

	def get_small_squares(self):
		return self._get_any("s")

	def get_big_squares(self):
		return self._get_any("b")

	def get_small_thumbnails(self):
		return self._get_any("t")

	def get_medium_thumbnails(self):
		return self._get_any("m")

	def get_large_thumbnails(self):
		return self._get_any("l")

	def get_huge_thumbnails(self):
		return self._get_any("h")

	def get_originals(self):
		return self._get_any("")


if __name__ == '__main__':
	"""this is meant as a basic usage example"""
	imgurLinkGet = ImgurLinkGet()

	if imgurLinkGet.load_data("http://imgur.com/gallery/qMEJb"):
		print imgurLinkGet.get_small_squares()
		print imgurLinkGet.get_big_squares()
		print imgurLinkGet.get_small_thumbnails()
		print imgurLinkGet.get_medium_thumbnails()
		print imgurLinkGet.get_large_thumbnails()
		print imgurLinkGet.get_huge_thumbnails()
		print imgurLinkGet.get_originals()

	if imgurLinkGet.load_data("http://imgur.com/lqH3gJq"):
		print imgurLinkGet.get_small_squares()
		print imgurLinkGet.get_big_squares()
		print imgurLinkGet.get_small_thumbnails()
		print imgurLinkGet.get_medium_thumbnails()
		print imgurLinkGet.get_large_thumbnails()
		print imgurLinkGet.get_huge_thumbnails()
		print imgurLinkGet.get_originals()
