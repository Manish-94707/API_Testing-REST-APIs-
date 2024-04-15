import requests
import os
import random
import time
import json


STATIC_VARS = {
	"COMMERCE_PRODUCT":[{
		"name" :"COMMERCE_PRODUCT",
    "advertising_ids": {
        "aaid": "1dde4fb9-eac2-459e-b20d-33f4c7660e5b"
    },
    "branch_key": "key_live_mf6tWo3CcJ7BbpUfL0CZGjohxEnDG7F7",
    "content_items": [
        {
            "$content_schema": "COMMERCE_PRODUCT",
            "$creation_timestamp": 1710482170147,
            "$currency": "INR",
            "$locally_indexable": True,
            "$price": 475,
            "$product_brand": "Sirona",
            "$product_name": " Menstrual Cup with Pouch -  Small & Medium (Duo)",
            "$product_variant": "Small-Medium",
            "$publicly_indexable": True,
            "$sku": "FSP472",
            "content_id": "FSP472"
        }
    ],
    "custom_data": {
        "identity": ""
    },
    "debug": False,
    "event_data": {
        "currency": "INR"
    },
    "hardware_id": "d479f7e0-4fe5-4f6f-ac6a-9fbbb82a4d29",
    "instrumentation": {
        "v1/install-brtt": "1125",
        "v2/event/standard-qwt": "0"
    },
    "is_hardware_id_real": False,
    "metadata": {
    },
    "name": "VIEW_ITEM",
    "partner_data": {
    },
    "retryNumber": 0,
    "user_data": {
        "aaid": "1dde4fb9-eac2-459e-b20d-33f4c7660e5b",
        "android_id": "d479f7e0-4fe5-4f6f-ac6a-9fbbb82a4d29",
        "app_store": "PlayStore",
        "app_version": "2.53.0",
        "brand": "Realme",
        "build": "RMX1827_11_C.22",
        "connection_type": "wifi",
        "cpu_type": "aarch64",
        "developer_identity": "bnc_no_value",
        "environment": "FULL_APP",
        "language": "en",
        "limit_ad_tracking": 0,
        "local_ip": "192.168.29.145",
        "locale": "en_",
        "model": "RMX1827",
        "os": "Android",
        "os_version": 29,
        "os_version_android": "10",
        "randomized_device_token": "1296767506362549881",
        "screen_dpi": 320,
        "screen_height": 1378,
        "screen_width": 720,
        "sdk": "android",
        "sdk_version": "5.3.0",
        "ui_mode": "UI_MODE_TYPE_NORMAL",
        "user_agent": "Mozilla/5.0 (Linux; Android 10; RMX1827 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.99 Mobile Safari/537.36"
    }}],
	"VIEW_ITEM" :[
		{"name":"VIEW_ITEM","custom_data":{"identity":""},"event_data":{"currency":"INR"},"content_items":[{"$content_schema":"COMMERCE_PRODUCT","$price":475,"$currency":"INR","$sku":"FSP472","$product_name":" Menstrual Cup with Pouch -  Small & Medium (Duo)","$product_brand":"Sirona","$product_variant":"Small-Medium","content_id":"FSP472","$publicly_indexable":True,"$locally_indexable":True,"$creation_timestamp":1710482170147}],"user_data":{"android_id":"d479f7e0-4fe5-4f6f-ac6a-9fbbb82a4d29","brand":"Realme","model":"RMX1827","screen_dpi":320,"screen_height":1378,"screen_width":720,"ui_mode":"UI_MODE_TYPE_NORMAL","os":"Android","os_version":29,"cpu_type":"aarch64","build":"RMX1827_11_C.22","locale":"en_","connection_type":"wifi","os_version_android":"10","language":"en","local_ip":"192.168.29.145","randomized_device_token":"1296767506362549881","app_store":"PlayStore","app_version":"2.53.0","sdk":"android","sdk_version":"5.3.0","user_agent":"Mozilla\/5.0 (Linux; Android 10; RMX1827 Build\/QP1A.190711.020; wv) AppleWebKit\/537.36 (KHTML, like Gecko) Version\/4.0 Chrome\/80.0.3987.99 Mobile Safari\/537.36","environment":"FULL_APP","developer_identity":"bnc_no_value","limit_ad_tracking":0,"aaid":"1dde4fb9-eac2-459e-b20d-33f4c7660e5b"},"debug":False,"partner_data":{},"metadata":{},"advertising_ids":{"aaid":"1dde4fb9-eac2-459e-b20d-33f4c7660e5b"},"hardware_id":"d479f7e0-4fe5-4f6f-ac6a-9fbbb82a4d29","is_hardware_id_real":False,"instrumentation":{"v2\/event\/standard-qwt":"0","v1\/install-brtt":"1125"},"branch_key":"key_live_mf6tWo3CcJ7BbpUfL0CZGjohxEnDG7F7","retryNumber":1}
	],

	"ADD_TO_CART":[{"name":"ADD_TO_CART","custom_data":{"identity":""},"event_data":{"currency":"INR","revenue":475},"content_items":[{"$content_schema":"COMMERCE_PRODUCT","$quantity":1,"$price":475,"$currency":"INR","$sku":"FSP472","$product_name":" Menstrual Cup with Pouch -  Small & Medium (Duo)","$product_brand":"Sirona","$product_variant":"Small-Medium","original_price":"798.0","content_category":"Period Kits and Combos","content_id":"FSP472","offer_price":"475.0","$publicly_indexable":True,"$locally_indexable":True,"$creation_timestamp":1710482181207}],"user_data":{"android_id":"d479f7e0-4fe5-4f6f-ac6a-9fbbb82a4d29","brand":"Realme","model":"RMX1827","screen_dpi":320,"screen_height":1378,"screen_width":720,"ui_mode":"UI_MODE_TYPE_NORMAL","os":"Android","os_version":29,"cpu_type":"aarch64","build":"RMX1827_11_C.22","locale":"en_","connection_type":"wifi","os_version_android":"10","language":"en","local_ip":"192.168.29.145","randomized_device_token":"1296767506362549881","app_store":"PlayStore","app_version":"2.53.0","sdk":"android","sdk_version":"5.3.0","user_agent":"Mozilla\/5.0 (Linux; Android 10; RMX1827 Build\/QP1A.190711.020; wv) AppleWebKit\/537.36 (KHTML, like Gecko) Version\/4.0 Chrome\/80.0.3987.99 Mobile Safari\/537.36","environment":"FULL_APP","developer_identity":"bnc_no_value","limit_ad_tracking":0,"aaid":"1dde4fb9-eac2-459e-b20d-33f4c7660e5b"},"debug":False,"partner_data":{},"metadata":{},"advertising_ids":{"aaid":"1dde4fb9-eac2-459e-b20d-33f4c7660e5b"},"hardware_id":"d479f7e0-4fe5-4f6f-ac6a-9fbbb82a4d29","is_hardware_id_real":False,"instrumentation":{"v2\/event\/standard-brtt":"10441","v2\/event\/standard-qwt":"1"},"branch_key":"key_live_mf6tWo3CcJ7BbpUfL0CZGjohxEnDG7F7","retryNumber":0}]
,
	"ADD_PAYMENT_INFO" : [{"name":"ADD_PAYMENT_INFO","custom_data":{"identity":"65f3e329fa6e7c0014c0c8c1","content_ids":"FSP472"},"event_data":{"currency":"INR","revenue":475},"content_items":[{"$content_schema":"COMMERCE_PRODUCT","$quantity":1,"$price":475,"$currency":"INR","$sku":"FSP472","$publicly_indexable":True,"$locally_indexable":True,"$creation_timestamp":1710482284058}],"user_data":{"android_id":"d479f7e0-4fe5-4f6f-ac6a-9fbbb82a4d29","brand":"Realme","model":"RMX1827","screen_dpi":320,"screen_height":1378,"screen_width":720,"ui_mode":"UI_MODE_TYPE_NORMAL","os":"Android","os_version":29,"cpu_type":"aarch64","build":"RMX1827_11_C.22","locale":"en_","connection_type":"wifi","os_version_android":"10","language":"en","local_ip":"192.168.29.145","randomized_device_token":"1296767506362549881","developer_identity":"65f3e329fa6e7c0014c0c8c1","app_store":"PlayStore","app_version":"2.53.0","sdk":"android","sdk_version":"5.3.0","user_agent":"Mozilla\/5.0 (Linux; Android 10; RMX1827 Build\/QP1A.190711.020; wv) AppleWebKit\/537.36 (KHTML, like Gecko) Version\/4.0 Chrome\/80.0.3987.99 Mobile Safari\/537.36","environment":"FULL_APP","limit_ad_tracking":0,"aaid":"1dde4fb9-eac2-459e-b20d-33f4c7660e5b"},"debug":False,"partner_data":{},"metadata":{},"advertising_ids":{"aaid":"1dde4fb9-eac2-459e-b20d-33f4c7660e5b"},"hardware_id":"d479f7e0-4fe5-4f6f-ac6a-9fbbb82a4d29","is_hardware_id_real":False,"instrumentation":{"v1\/profile-brtt":"319","v2\/event\/standard-qwt":"0"},"branch_key":"key_live_mf6tWo3CcJ7BbpUfL0CZGjohxEnDG7F7","retryNumber":0}]
,
"ADD_TO_WISHLIST":[{"name":"ADD_TO_WISHLIST","custom_data":{"identity":"65f3e329fa6e7c0014c0c8c1"},"event_data":{"currency":"INR","revenue":99},"content_items":[{"$content_schema":"COMMERCE_PRODUCT","$quantity":1,"$price":99,"$currency":"INR","$sku":"FSP831","$product_name":"Sirona White Sanitary Pads - (XL) Pack of 4","$product_brand":"Sirona","original_price":"99.0","content_category":"Period Care","content_id":"FSP831","offer_price":"99.0","$publicly_indexable":True,"$locally_indexable":True,"$creation_timestamp":1710482601508}],"user_data":{"android_id":"d479f7e0-4fe5-4f6f-ac6a-9fbbb82a4d29","brand":"Realme","model":"RMX1827","screen_dpi":320,"screen_height":1378,"screen_width":720,"ui_mode":"UI_MODE_TYPE_NORMAL","os":"Android","os_version":29,"cpu_type":"aarch64","build":"RMX1827_11_C.22","locale":"en_","connection_type":"wifi","os_version_android":"10","language":"en","local_ip":"192.168.29.145","randomized_device_token":"1296767506362549881","developer_identity":"65f3e329fa6e7c0014c0c8c1","app_store":"PlayStore","app_version":"2.53.0","sdk":"android","sdk_version":"5.3.0","user_agent":"Mozilla\/5.0 (Linux; Android 10; RMX1827 Build\/QP1A.190711.020; wv) AppleWebKit\/537.36 (KHTML, like Gecko) Version\/4.0 Chrome\/80.0.3987.99 Mobile Safari\/537.36","environment":"FULL_APP","limit_ad_tracking":0,"aaid":"1dde4fb9-eac2-459e-b20d-33f4c7660e5b"},"debug":False,"partner_data":{},"metadata":{"$marketing_cloud_visitor_id":"56375354168875614366073360288467180136"},"advertising_ids":{"aaid":"1dde4fb9-eac2-459e-b20d-33f4c7660e5b"},"hardware_id":"d479f7e0-4fe5-4f6f-ac6a-9fbbb82a4d29","is_hardware_id_real":False,"instrumentation":{"v2\/event\/standard-brtt":"283","v2\/event\/standard-qwt":"1"},"branch_key":"key_live_mf6tWo3CcJ7BbpUfL0CZGjohxEnDG7F7","retryNumber":0}]

}



def probability():
	return random.randint(1,100)


def timedelay(lb,ub):
	time.sleep(random.uniform(lb, ub))


def connectlocalhost():
	os.environ['http_proxy'] = "http://localhost:8888"
	os.environ['https_proxy'] = "http://localhost:8888"


def install():
	url = "http://api2.branch.io/v1/install"
	headers = {
		'Accept': 'application/json',
		'Accept-Encoding': 'gzip',
		'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 10; RMX1827 Build/QP1A.190711.020)',
		'Content-Type': 'application/json',
		'Connection': 'Keep-Alive',
		'Host': 'api2.branch.io'
		}
	params = {}
	data = {"hardware_id": "d479f7e0-4fe5-4f6f-ac6a-9fbbb82a4d29",
		  "is_hardware_id_real": False,
		  "brand": "Realme",
		   "model": "RMX1827",
 		"screen_dpi": 320,
 		"screen_height": 1378,
 		"screen_width": 720,
 		"wifi": True,
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
		"debug": False,
 		"partner_data": {},
 		"app_version": "2.53.0",
 		"initial_referrer": "android-app://com.oppo.launcher",
 		"facebook_app_link_checked": False,
		 "update": 0,
 		"latest_install_time":"1710422989084",
 		"latest_update_time":"1710422989084",
 		"first_install_time": "1710422989084",
 		"previous_update_time": 0,
		"environment": "FULL_APP",
 		"install_begin_ts": "1710422937",
		 "metadata": {},
 		"install_referrer_extras": "utm_source=google-play&utm_medium=organic",
 		"app_store": "PlayStore",
 		"advertising_ids": {
  		"aaid": "1dde4fb9-eac2-459e-b20d-33f4c7660e5b"
 		},
		 "lat_val": 0,
 		"google_advertising_id": "1dde4fb9-eac2-459e-b20d-33f4c7660e5b",
		 "instrumentation": {
 		 "v1/install-qwt": "0"
 		},
 		"sdk": "android5.3.0",
 		"branch_key": "key_live_mf6tWo3CcJ7BbpUfL0CZGjohxEnDG7F7",
 		"retryNumber": 0
 		}
	data_json = json.dumps(data)
	requests.post(url, headers=headers, params=params, data=data_json, verify=False)

def open():
	url = "http://api2.branch.io/v1/open"
	headers = {'Accept': 'application/json',
		'Accept-Encoding': 'gzip',
		'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 12; Realme 7 Pro Build/SP2A.220405.004)',
		'Content-Type': 'application/json',
		'Connection': 'Keep-Alive',
		'Host': 'api2.branch.io'
		}
	params = {}
	data = {
  "randomized_device_token": "1296767506362549881",
  "randomized_bundle_token": "1296815359264993183",
  "hardware_id": "6eb416711c8b0b96",
  "is_hardware_id_real": True,
  "brand": "Realme",
  "model": "RMX1827",
  "screen_dpi": 320,
  "screen_height": 1378,
  "screen_width": 720,
  "wifi": True,
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
  "debug": False,
  "partner_data": {},
  "app_version": "2.53.0",
  "initial_referrer": "android-app://com.android.vending",
  "facebook_app_link_checked": False,
  "update": 1,
  "latest_install_time": 1710422989084,
  "latest_update_time": 1710422989084,
  "first_install_time": 1710422989084,
  "previous_update_time": 1710422989084,
  "environment": "FULL_APP",
  "metadata": {},
  "app_store": "PlayStore",
  "lat_val": 0,
  "instrumentation": {
    "v1/open-qwt": "0"
  },
  "sdk": "android5.3.0",
  "branch_key": "key_live_mf6tWo3CcJ7BbpUfL0CZGjohxEnDG7F7",
  "retryNumber": 0
}
	data_json = json.dumps(data)
	requests.post(url, headers=headers, params=params, data=data_json, verify=False)

def close():
	url = "http://api2.branch.io/v1/close"
	headers = {}
	params = {}
	data = {}
	requests.post(url, headers=headers, params=params, data=data, verify=False)

def event(eventName):
	url = "http://api2.branch.io/v2/event/standard"
	headers = {
		'Accept-Encoding': 'gzip',
		'Accept': 'application/json',
		'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 10; RMX1827 Build/QP1A.190711.020)',
		'Content-Type': 'application/json',
		'Connection': 'Keep-Alive',
		'Host': 'api2.branch.io'
	}
	params = {}
	#data["name"] = eventName
	#data = STATIC_VARS # Please use the global variable STATIC_VARS for the values which are repeating in adjust_session() and adjust_event(eventName) functions
	#data["name"] = eventName
	""" if data[eventName] =="COMMERCE_PRODUCT":
		return data["COMMERCE_PRODUCT"]
	elif  data[eventName] =="VIEW_ITEM":
		return data["VIEW_ITEM"]                   
	elif  data[eventName] =="VIEW_CART":
		return data["VIEW_CART"]
	elif  data[eventName] =="ADD_PAYMENT_INFO":
		return data["ADD_PAYMENT_INFO"] """
	
	data = STATIC_VARS.get(eventName, [])
	if data:
		data = data[0]  # Select the first element if it exists
		requests.post(url, headers=headers, params=params, json=data, verify=False)


def main():
	connectlocalhost()
	install()
	open()
	if probability()>50:
		event("COMMERCE_PRODUCT")
		timedelay(1, 2)
	if probability()>50:
		event("VIEW_ITEM")
		timedelay(1, 2)
	if probability()>50:
		event("VIEW_CART")
		timedelay(1, 2)
	if probability()>50:
		event("ADD_PAYMENT_INFO")
		timedelay(1, 2)
	if probability()>50:
		event("ADD_TO_CART")
		timedelay(1, 2)
	if probability()>50:
		event("ADD_TO_WISHLIST")
		timedelay(1, 2)
	
	# add session request
	# add event requests as per the probability you decide using the probability() funtion given and "if condition"
	# add time-delays in b/w (if required) using the timedelay() function given
	close()


if __name__ == '__main__':
	main()