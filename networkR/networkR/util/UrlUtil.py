

def get_domain(url):
	if 'http://' in url:
		url = url[7:]

	if 'https://' in url:
		url = url[8:]

	if '/' in url:
		index = url.index('/')
		url = url[0:index]

	return url



def handle_url(url = None):
    if url is None:
        return url

    if 'http://' in url:
        url = url[7:]

    if 'https://' in url:
        url = url[8:]
    
    if '?' in url:
        index = url.index('?')
        url = url[0:index]

    return url


