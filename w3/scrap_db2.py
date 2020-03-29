from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

#'어벤져스: 엔드게임'의 평점을 가져오기
target_movie = db.movies.find_one({'title':'어벤져스: 엔드게임'})
print (target_movie['star'])

print()

#'어벤져스: 엔드게임'의 평점과 같은 평점의 영화 제목들을 가져오기
same_stars = list(db.movies.find({'star':target_movie['star']}))
for same_star in same_stars:      # 반복문을 돌며 모든 결과값을 보기
    print(same_star['title'])

print()

#'어벤져스: 엔드게임'의 평점과 같은 평점의 영화 제목들의 평점을 0으로 만들기
target_movie = db.movies.find_one({'title':'어벤져스: 엔드게임'})
target_star = target_movie['star']

db.movies.update_many({'star':target_star},{'$set':{'star':0}})

stars_zero = list(db.movies.find({'star':0}))
print(stars_zero)