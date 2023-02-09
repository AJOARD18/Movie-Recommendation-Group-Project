from xgboost import XGBRanker
from website.retrieval import retrieval
from website.recommend import recommend
from website.recommend import description

# 18035            Batman: Year One
# 44977    Batman Beyond: The Movie
# 585                        Batman
# 1328               Batman Returns
# 10122               Batman Begins
# 18252       The Dark Knight Rises

# model = XGBRanker()
# model.load_model('ranking_model_sklearn.txt')
# model.predict('Toy Story')

movies = recommend('The Dark Knight', 6)



print(description(movies))
