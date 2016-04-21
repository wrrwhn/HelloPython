from qiniu import Auth, put_file, etag, urlsafe_base64_encode
import qiniu.config
import uuid
from os import path

#Access Key /Secret Key/ import zoom name
access_key = 'DraImie8qSbwoPoyrHV38lfTnVr9aj8S487egGsC'
secret_key = '62PYqPKVBwFIHvObxdrzeRcqB7Ep_ufpqTXLZ_8b'
def_host= 'http://7xsy59.com1.z0.glb.clouddn.com/'
bucket_name = 'image'


def upload(localfile, fileName=None):
	'''localfile = local file path'''

	# auth
	q = Auth(access_key, secret_key)

	# init
	file_basename, file_extension= path.splitext(localfile)

	# save name
	if not fileName:
		key = str(uuid.uuid1())+ file_extension
	else:
		tmp_basename, tmp_extension= path.splitext(fileName)
		print tmp_basename, tmp_extension
		key = tmp_basename+ file_extension

	token = q.upload_token(bucket_name, key, 3600)

	ret, info = put_file(token, key, localfile)
	return def_host+ key
