from django.shortcuts import render
from django.http import HttpResponse
from .media_class import Media
import csv
from itertools import islice
import os
from django.conf import settings
import random


csv_file_name = 'imdb_top_1000.csv'
csv_file_name2 = 'tv_shows_new.csv'
csv_file_path = os.path.join(settings.BASE_DIR, 'movie_manager', 'data', csv_file_name)
csv_file_path2 = os.path.join(settings.BASE_DIR, 'movie_manager', 'data', csv_file_name2)
# Create your views here.

content = []


with open (csv_file_path) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in islice(reader, 60):
        newMedia = Media(row['Series_Title'], row['Released_Year'], 'movie', False, row['Overview'], False, row['Poster_Link'], row['Genre'].replace(" ", "").split(","), False, row['IMDB_Rating'])
        content.append(newMedia)

with open (csv_file_path2) as csvfile2:
    reader = csv.DictReader(csvfile2)
    for row in islice(reader, 60):
        genre = row['genre'].strip("[]").replace("u'", "").replace("'", "").replace(" ", "").split(",")
        year = row['year'].replace(" TV Series", "").replace("(", "").replace(")", "")
        newMedia = Media(row['title'], year, 'show', False, row['text'], False, row['image url'], genre, False, row['rating'])
        content.append(newMedia)
       

dramaMovies = []
dramaShows = []
index = 0
while((len(dramaMovies) < 5 or len(dramaShows) < 5) and index < len(content)):
    if("Drama" in content[index].genre and content[index].type == "movie" and len(dramaMovies) < 5):
        dramaMovies.append(content[index])
    if("Drama" in content[index].genre and content[index].type == "show" and len(dramaShows) < 5):
        dramaShows.append(content[index])
    index+=1

thrillerMovies = []
thrillerShows = []
index = 0
while((len(thrillerMovies) < 5 or len(thrillerShows) < 5) and index < len(content)):
    if("Thriller" in content[index].genre and content[index].type == "movie" and len(thrillerMovies) < 5):
        thrillerMovies.append(content[index])
    if("Thriller" in content[index].genre and content[index].type == "show" and len(thrillerShows) < 5):
        thrillerShows.append(content[index])
    index+=1

crimeMovies = []
crimeShows = []
index = 0
while((len(crimeMovies) < 5 or len(crimeShows) < 5) and index < len(content)):
    if("Crime" in content[index].genre and content[index].type == "movie" and len(crimeMovies) < 5):
        crimeMovies.append(content[index])
    if("Crime" in content[index].genre and content[index].type == "show" and len(crimeShows) < 5):
        crimeShows.append(content[index])
    index+=1

adventureMovies = []
adventureShows = []
index = 0
while((len(adventureMovies) < 5 or len(adventureShows) < 5) and index < len(content)):
    if("Adventure" in content[index].genre and content[index].type == "movie" and len(adventureMovies) < 5):
        adventureMovies.append(content[index])
    if("Adventure" in content[index].genre and content[index].type == "show" and len(adventureShows) < 5):
        adventureShows.append(content[index])
    index+=1

romanceMovies = []
romanceShows = []
index = 0
while((len(romanceMovies) < 5 or len(romanceShows) < 5) and index < len(content)):
    if("Romance" in content[index].genre and content[index].type == "movie" and len(romanceMovies) < 5):
        romanceMovies.append(content[index])
    if("Romance" in content[index].genre and content[index].type == "show" and len(romanceShows) < 5):
        romanceShows.append(content[index])
    index+=1

scifiMovies = []
scifiShows = []
index = 0
while((len(scifiMovies) < 5 or len(scifiShows) < 5) and index < len(content)):
    if("Sci-Fi" in content[index].genre and content[index].type == "movie" and len(scifiMovies) < 5):
        scifiMovies.append(content[index])
    if("Sci-Fi" in content[index].genre and content[index].type == "show" and len(scifiShows) < 5):
        scifiShows.append(content[index])
    index+=1

mysteryMovies = []
mysteryShows = []
index = 0
while((len(mysteryMovies) < 5 or len(mysteryShows) < 5) and index < len(content)):
    if("Mystery" in content[index].genre and content[index].type == "movie" and len(mysteryMovies) < 5):
        mysteryMovies.append(content[index])
    if("Mystery" in content[index].genre and content[index].type == "show" and len(mysteryShows) < 5):
        mysteryShows.append(content[index])
    index+=1

comedyMovies = []
comedyShows = []
index = 0
while((len(comedyMovies) < 5 or len(comedyShows) < 5) and index < len(content)):
    if("Comedy" in content[index].genre and content[index].type == "movie" and len(comedyMovies) < 5):
        comedyMovies.append(content[index])
    if("Comedy" in content[index].genre and content[index].type == "show" and len(comedyShows) < 5):
        comedyShows.append(content[index])
    index+=1

fantasyMovies = []
fantasyShows = []
index = 0
while((len(fantasyMovies) < 5 or len(fantasyShows) < 5) and index < len(content)):
    if("Fantasy" in content[index].genre and content[index].type == "movie" and len(fantasyMovies) < 5):
        fantasyMovies.append(content[index])
    if("Fantasy" in content[index].genre and content[index].type == "show" and len(fantasyShows) < 5):
        fantasyShows.append(content[index])
    index+=1



def home(request):
    if(request.method == "POST"):
        title = list(request.POST)[1].split(",")
        print(title[1])
        if(title[1] == "watch-list"):
            for media in content:
                if(media.title == title[0]):
                    media.is_watch_list = True
        elif(title[1] == "no-watch-list"):
            for media in content:
                if(media.title == title[0]):
                    media.is_watch_list = False
        elif(title[1] == "add-alr-wat"):
            for media in content:
                if(media.title == title[0]):
                    media.alr_wat = True
        elif(title[1] == "rem-alr-wat"):
            for media in content:
                if(media.title == title[0]):
                    media.alr_wat = False
        elif(title[1] == "add-curr-wat"):
            for media in content:
                if(media.title == title[0]):
                    media.is_curr_wat = True
        else:
            for media in content:
                if(media.title == title[0]):
                    media.is_curr_wat = False
    
    watchlist = []
    index = 0
    while(len(watchlist) < 5 and index < len(content)):
        if(content[index].is_watch_list):
            watchlist.append(content[index])
        index+=1
    
    alrWatched = []
    index = 0
    while(len(alrWatched) < 5 and index < len(content)):
        if(content[index].alr_wat):
            alrWatched.append(content[index])
        index+=1
    
    currWatched = []
    index = 0
    while(len(currWatched) < 5 and index < len(content)):
        if(content[index].is_curr_wat):
            currWatched.append(content[index])
        index+=1
    obj = {
        'medias': content, 
        'watchlist': watchlist, 
        'curr_wat': currWatched, 
        'alr_watch': alrWatched
    }
    return render(request, 'home.html', obj)

def movies(request):
    watchlistMovies = []
    index = 0
    while(len(watchlistMovies) < 5 and index < len(content)):
        if(content[index].is_watch_list and content[index].type == "movie"):
            watchlistMovies.append(content[index])
        index+=1
    
    alrWatchedMovies = []
    index = 0
    while(len(alrWatchedMovies) < 5 and index < len(content)):
        if(content[index].alr_wat and content[index].type == "movie"):
            alrWatchedMovies.append(content[index])
        index+=1

    currWatchedMovies = []
    index = 0
    while(len(currWatchedMovies) < 5 and index < len(content)):
        if(content[index].is_curr_wat and content[index].type == "movie"):
            currWatchedMovies.append(content[index])
        index+=1
    
    obj = {
        'medias': content,
        'drama_movies': dramaMovies,
        'thriller_movies': thrillerMovies,
        'crime_movies': crimeMovies,
        'adventure_movies': adventureMovies,
        'romance_movies': romanceMovies,
        'scifi_movies': scifiMovies,
        'mystery_movies': mysteryMovies,
        'comedy_movies': comedyMovies,
        'fantasy_movies': fantasyMovies,
        'watchlist_movies': watchlistMovies,
        'alr_wat_movies': alrWatchedMovies,
        'curr_wat_movies': currWatchedMovies
    }
    return render(request, 'movies.html', obj)

def shows(request):
    watchlistShows = []
    index = 0
    while(len(watchlistShows) < 5 and index < len(content)):
        if(content[index].is_watch_list and content[index].type == "show"):
            watchlistShows.append(content[index])
        index+=1
    
    alrWatchedShows = []
    index = 0
    while(len(alrWatchedShows) < 5 and index < len(content)):
        if(content[index].alr_wat and content[index].type == "show"):
            alrWatchedShows.append(content[index])
        index+=1

    currWatchedShows = []
    index = 0
    while(len(currWatchedShows) < 5 and index < len(content)):
        if(content[index].is_curr_wat  and content[index].type == "show"):
            currWatchedShows.append(content[index])
        index+=1
    
    
    obj = {
        'medias': content,
        'drama_shows': dramaShows,
        'thriller_shows': thrillerShows,
        'crime_shows': crimeShows,
        'adventure_shows': adventureShows,
        'romance_shows': romanceShows,
        'scifi_shows': scifiShows,
        'mystery_shows': mysteryShows,
        'comedy_shows': comedyShows,
        'fantasy_shows': fantasyShows,
        'watchlist_shows': watchlistShows,
        'alr_wat_shows': alrWatchedShows,
        'curr_wat_shows': currWatchedShows
    }
    return render(request, 'shows.html', obj)

def movie_info(request):
    for media in content:
        if media.title in request.POST:
            return render(request, 'movie-info.html', {'media': media})

    if request.method == 'POST':
        for media in content:
            if media.title.lower() == request.POST.get("movie-title").lower():
                return render(request, 'movie-info.html', {'media': media})
    
    return render(request, 'not-found.html')
        
    

def list_info(request):
    post_list = list(request.POST.keys())
    media_info = post_list[1].split(",")
    return render(request, 'list-info.html', {'medias': content, 'genre': media_info[0], 'type': media_info[1]})

def random_picker(request):
    random_media = random.choice(content)
    return render(request, 'movie-info.html', {'media': random_media})


