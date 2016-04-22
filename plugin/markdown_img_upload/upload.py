from qiniu import Auth, put_file, etag, urlsafe_base64_encode
import qiniu.config
import uuid
from os import path, remove

#Access Key /Secret Key/ import zoom name
access_key = 'DraImie8qSbwoPoyrHV38lfTnVr9aj8S487egGsC'
secret_key = '62PYqPKVBwFIHvObxdrzeRcqB7Ep_ufpqTXLZ_8b'
def_host= 'http://7xsy59.com1.z0.glb.clouddn.com/'
bucket_name = 'image'


def upload(local_file_path, upload_file_name=None, is_delete= True):
	'''local_file_path = local file path'''

	# auth
	q = Auth(access_key, secret_key)

	# init
	file_basename, file_extension= path.splitext(local_file_path)

	# save name
	if not upload_file_name:
		key = str(uuid.uuid1())+ file_extension
	else:
		tmp_basename, tmp_extension= path.splitext(upload_file_name)
		print tmp_basename, tmp_extension
		key = tmp_basename+ file_extension

	# upload
	token = q.upload_token(bucket_name, key, 3600)
	ret, info = put_file(token, key, local_file_path)

	# check delete
	if is_delete:
		remove(local_file_path)

	return def_host+ key
