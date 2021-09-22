from flask import render_template,request,redirect,url_for
from .main import main
from .request import get_sources,get_article
from .models import Source,Articles


@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    #Getting Technology related sources

   
    business_sources = get_sources('business')
    sports_sources = get_sources('sports')
    tech_sources = get_sources('technology')

    print(tech_sources)
    title = 'NEWS BING BNN'
    
    return render_template('index.html', title = title, technology = tech_sources, business = business_sources, sports = sports_sources)

@main.route('/source/<id>')
def articles(id):
    '''
    view articles function that returns a list of articles on the articles
    '''

    articles = get_article(id)
    title = f'Headline {id}'    

    return render_template('article.html',title = title, articles = articles)