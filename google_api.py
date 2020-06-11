import googlemaps
import pprint
#pprint讓你看起來比較舒服一樣但其實就是print
API_KEY = "AIzaSyAADZ81sf1zROTCOZeLkohcXNxCeNVzSzc"
#這是放你的key的地方你要把它改掉
gmaps = googlemaps.Client(key=API_KEY)
#創建一個地圖物件

#Search
#第一種搜尋方法:關鍵字搜尋
fields = ['name','formatted_address','place_id']
result = gmaps.find_place(input="淘客美式漢堡 公館店",input_type="textquery",fields=fields)
#input放你的關鍵字，可以是電話搜尋也可以是文字搜尋
#input_type 選擇你要電話搜尋還是文字,"phonenumber","textquery"
#他會回傳一切的candidate
#fields 是在指定你要回傳的細節，我這裡選名字跟地址還有他的ID
#如果不指定的話只會回傳ID
pprint.pprint(result)

#第二種搜尋方法：使用附近搜尋
location = "24.121531,120.653043"
radius = 5000
results = gmaps.places_nearby(location=location,radius=100,keyword='餐廳咖啡廳')
#指定一個地點，找尋方圓半境內的商家，可以用keyword指定商家類型
#會回傳前20個項目，回傳json檔，如果覺得還是太亂可以這樣取出來
pprint.pprint(results)

for result in results['results'][:3]:
    my_place_id = result['place_id']
	#把每個地點的ID取出來使用第三種方法：找特定地點
    my_fields = ['name','formatted_phone_number','formatted_address','business_status','price_level','rating']
    detials = gmaps.place(place_id=my_place_id,fields=my_fields,language="zh-TW")
    #language可以指定回傳的語言
    pprint.pprint(detials)

#也可以這樣找
place = gmaps.places("restaurants+淘客美式漢堡+公館店",language='zh-TW')
#把他想像成在google搜尋打的結果就好，跑出來跟上面near_by一樣
pprint.pprint(place)