import os
import random
import time
import requests



STATIC_VARS = {
	'android_uuid':'ddce1643-1136-4ade-963d-c69f23706881',
	'api_level':30,
	'app_token':'yc4m07bvj37k',
	'app_version':	'1.0.11',
	'attribution_deeplink':	1,
	'connectivity_type':	1,
	'country'	:'IN',
	'cpu_type'	:'arm64-v8a',
	'created_at':"2022-11-21T04:33:44.700Z-0800", #time.strftime("%Y-%m-%dT04%H:%M:%S"),
	'device_manufacturer':	'OnePlus',
	'device_name'	:'GM1911',
	'device_type':	'phone',
	'display_height':	2910,
	'display_width':	1440,
	'environment':'production',
	'event_buffering_enabled':	0,
	'gps_adid'	:'98ab3f97-c21e-4d02-bd3d-dc70ea0872b0',
	'gps_adid_attempt':	1, 
	'gps_adid_src':	'service',
	'hardware_name':	'GM1911_21_220617',
	"installed_at": "2022-11-21T04:30:51.049Z-0800",
	'language'	:'en',
	'mcc':	405,
	'mnc':	872,
	'needs_response_details'	:1,
	'os_build':	'RKQ1.201022.002',
	'os_name':	'android',
	'os_version':	11,
	'gps_adid_attempt':	1,
	"package_name": "vn.gamate.tuyetthekiemvuong.ttkv",
	'screen_density'	:'high',
	'screen_format'	:'long',
	'screen_size':	'normal',
	'sent_at'	:"2022-11-21T04:33:44.728Z-0800", # time.strftime("%Y-%m-%dT04%H:%M:%S"),
	'tracking_enabled'	:1,
	'updated_at': '2022-11-21T04:30:51.049Z-0800',

}


def probability():
	return random.randint(1,100)

def timedelay(lb,ub):
	time.sleep(random.uniform(lb, ub))

def connectlocalhost():
	os.environ['http_proxy'] = "http://localhost:8888"
	os.environ['https_proxy'] = "http://localhost:8888"

def adjust_session():
	url = "https://app.adjust.com/session"
	headers = {
		'Accept-Encoding': 'gzip',
		'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 11; GM1911 Build/RKQ1.201022.002)',
		'Content-Type': 'application/x-www-form-urlencoded',
		'Host':'app.adjust.com',
		'Connection': 'Keep-Alive',
		'Client-SDK': 'android4.28.2'
	}
	
	params = {}
	data = STATIC_VARS
	
	requests.post(url, headers=headers, params=params, data=data, verify=False)
	
def adjust_event(eventName):
	url = "https://app.adjust.com/event"
	headers = {
		'Accept-Encoding': 'gzip',
		'Content-Type': 'application/x-www-form-urlencoded',
		'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 11; GM1911 Build/RKQ1.201022.002)',
		'Host':'app.adjust.com',
		'Connection': 'Keep-Alive',
		'Client-SDK': 'android4.28.2'
	}
	params = {}
	data = STATIC_VARS
	data["event_token"] = eventName
	requests.post(url, headers=headers, params=params, data=data, verify=False)

def main():
	connectlocalhost()
	adjust_session()
	if probability() > 50:
		adjust_event("810197")
		timedelay(1, 2)
		if probability() > 50:
			adjust_event("4947d3")
			timedelay(1, 2)
		if probability() > 70:
			adjust_event("xsh5qn")
			timedelay(1, 2)
		if probability() > 90:
			adjust_event("9etg6f")

if __name__ == '__main__':
	main()



static_var ={
	"VIEW_ITEM":[{
  "name": "VIEW_ITEM",
  "custom_data": {
    "identity": ""
  },
  "event_data": {
    "currency": "INR"
  },
  "content_items": [
    {
      "$content_schema": "COMMERCE_PRODUCT",
      "$price": 475,
      "$currency": "INR",
      "$sku": "FSP472",
      "$product_name": " Menstrual Cup with Pouch -  Small & Medium (Duo)",
      "$product_brand": "Sirona",
      "$product_variant": "Small-Medium",
      "content_id": "FSP472",
      "$publicly_indexable": True,
      "$locally_indexable": True,
      "$creation_timestamp": 1710482170147
    }
  ],
  "user_data": {
    "android_id": "d479f7e0-4fe5-4f6f-ac6a-9fbbb82a4d29",
    "brand": "Realme",
    "model": "RMX1827",
    "screen_dpi": 320,
    "screen_height": 1378,
    "screen_width": 720,
    "ui_mode": "UI_MODE_TYPE_NORMAL",
    "os": "Android",
    "os_version": 29,
    "cpu_type": "aarch64",
    "build": "RMX1827_11_C.22",
    "locale": "en_",
    "connection_type": "wifi",
    "os_version_android": "10",
    "language": "en",
    "local_ip": "192.168.29.145",
    "randomized_device_token": "1296767506362549881",
    "app_store": "PlayStore",
    "app_version": "2.53.0",
    "sdk": "android",
    "sdk_version": "5.3.0",
    "user_agent": "Mozilla/5.0 (Linux; Android 10; RMX1827 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.99 Mobile Safari/537.36",
    "environment": "FULL_APP",
    "developer_identity": "bnc_no_value",
    "limit_ad_tracking": 0,
    "aaid": "1dde4fb9-eac2-459e-b20d-33f4c7660e5b"
  },
  "debug": False,
  "partner_data": {},
  "metadata": {},
  "advertising_ids": {
    "aaid": "1dde4fb9-eac2-459e-b20d-33f4c7660e5b"
  },
  "hardware_id": "d479f7e0-4fe5-4f6f-ac6a-9fbbb82a4d29",
  "is_hardware_id_real": False,
  "instrumentation": {
    "v2/event/standard-qwt": "0",
    "v1/install-brtt": "1125"
  },
  "branch_key": "key_live_mf6tWo3CcJ7BbpUfL0CZGjohxEnDG7F7",
  "retryNumber": 0
}]
}