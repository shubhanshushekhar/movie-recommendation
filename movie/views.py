from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd
import math


def login(request):
    return render(request,'login.html')

def pages(request):
    return render(request,'pages.html')

def homepage(request):
    return render(request,'home.html')



def suggest(request):

    text = request.GET['fulltext']
    dictionary = {}
    dictionary[text] = 1
    columns_name = ["user_id", "item_id", "rating", "timestamp"]
    # csvfile = request.FILES['u.data']
    df = pd.read_csv('movie/u.data', sep='\t', names = columns_name)
    # csvfile = request.FILES['u.item']
    movie_titles = pd.read_csv('movie/u.item', sep="\|", header=None)
    n = len(df)
    movie_titles = movie_titles[[0,1]]
    movie_titles.columns = ['item_id', 'title']
    df = pd.merge(df, movie_titles, on="item_id")
    ratings = pd.DataFrame(df.groupby('title').mean()['rating'])
    ratings['num of ratings'] = pd.DataFrame(df.groupby('title').count()['rating'])
    moviemat = df.pivot_table(index="user_id", columns="title", values = "rating")
    movie_user_ratings = moviemat[text]
    def fitness(population, rating, U):
        fitness_value=0
        for i in range(rating.len()):
            fitness_value = fitness_value + abs(population[i] - rating[i])
        fitness_value = fitness_value*(1/U)
        
        return fitness_value
        
    def mutation( array ):
        for i in range(array.len()/2):
            array[i] = array[i]^0
            
    def crossover( array ):
        k = random.randint(0,array.len()-1)
        array[k] = array[k]^1
        
    def similarity_function( rating, users_rating, population, m, M ):
        value=0.000
        for i in range(n):
            value = abs(rating[i]-users_rating[i])
        value = math.sin(value)
        
        
    def genetic( rating, users_rating ):
        population = np.random.rand(n,m)*10
        ra = np.random.rand(n,m)*10
        for i in range(n):
            for j in range(m):
                V12[i][j] = users_rating[i][j]
            
    
    similar_to_movie = moviemat.corrwith(movie_user_ratings)
    corr_movie = pd.DataFrame(similar_to_movie, columns=['Correlation'])
    corr_movie.dropna(inplace = True)
    corr_movie = corr_movie.join(ratings['num of ratings'])
    predictions = corr_movie[corr_movie['num of ratings']>100].sort_values('Correlation', ascending=False)
    # print(predictions)
    # arr = list(predictions.itertuples(index=False, name=None))
    # print(type(predictions))
    # var mydic = (predictions.iloc[1,1], predictions.iloc[2,1], predictions.iloc[3,1], predictions.iloc[,1])
    return render(request,'suggest.html',{'fulltext': predictions.iloc[1:5,1]} )
