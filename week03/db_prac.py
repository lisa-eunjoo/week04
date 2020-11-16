from pymongo import MongoClient #파이몽고 쓰겠다
client = MongoClient('localhost', 27017) #파이몽고 접근하라
db = client.dbsparta #dbsparta이름의 db에 접근

#crud
movie = db.movies.find_one({'title':'매트릭스'})
#print(movie['star'])

target_movie = db.movies.find_one({'title':'매트릭스'})
target_star = target_movie['star']

movies = list(db.movies.find({'star':target_star}))

for movie in movies:
    print(movie['title'])

db.movies.update_one({'title':'매트릭스'},{'$set':{'star':0}})

# 코딩 시작
# # 저장 - 예시
# doc = {'name':'bobby','age':21}
# db.users.insert_one(doc)
#
# # 한 개 찾기 - 예시
# user = db.users.find_one({'name':'bobby'})
#
# # 여러개 찾기 - 예시 ( _id 값은 제외하고 출력)
# same_ages = list(db.users.find({'age':21},{'_id':False}))
#
# # 바꾸기 - 예시
# db.users.update_one({'name':'bobby'},{'$set':{'age':19}})
#
# # 지우기 - 예시
# db.users.delete_one({'name':'bobby'})