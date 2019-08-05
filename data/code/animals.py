import wikipedia
import wptools
import pandas as pd
import requests
import re
import time
from xml.dom.minidom import parse
from xml.dom.minidom import getDOMImplementation
from bs4 import BeautifulSoup

# please don't judge my regex
# this can be more optimized
def clean_common(df):
    clean = df.str.replace(';? ?(<|<)br ?/?(>|>)', ', ')
    clean = clean.str.replace('((\{\{)?(\|)?(\&)?ndash;?(\|)?(/}/})?)|(\|to\|)|(\| ?(-|–) ? ?\|)|(–)|(–)','-')
    clean = clean.str.replace('\&nbsp;', ' ')
    clean = clean.str.replace(' ?;$', '')
    clean = clean.str.replace('(\')|(\")', '')
    
    return clean

def clean_origin(df):
    clean = clean_common(df)
    clean = clean.str.replace('\[\[', '')
    clean = clean.str.replace('\]\]', '')
    clean = clean.str.replace('</?small>', '')
    clean = clean.str.replace('unbulleted list( \|)?', '')
    clean = clean.str.replace('\{\{Plainlist\|\\n\*', '')
    clean = clean.str.replace('\\n', ', ')
    clean = clean.str.replace('\{\{flag(icon)?\|.*\}\}', '')
    clean = clean.str.replace('\{\{', '')
    clean = clean.str.replace('\}\}', '')
    clean = clean.str.replace('(\|)|(;)|(,, )', ', ')
    clean = clean.str.replace('\*', '')
    clean = clean.str.replace('\(Breed.*\)', '')
    clean = clean.str.replace('^,', '')
    clean = clean.str.replace('^ ', '')
    clean = clean.str.replace(',,', ',')

    return clean

def clean_other_names(df):
    clean = clean_common(df)
    clean = clean.str.replace(' ?(\()?(\')*\[\[Breed standard\|(s|S)tandardised breed\]\]:?(\))?;?(\')', '')
    clean = clean.str.replace('(\{\{)?hlist ?(\|)?(\\n\*)?(\|)?,? ?', '')
    clean = clean.str.replace('(\{\{)?flat ?list ?(\|)?(\\n\*)?(\|)?,? ?', '')
    clean = clean.str.replace('(\{\{)?plain ?list ?(\|)?(\\n\*)?(\|)?,? ?', '')
    clean = clean.str.replace('(\{\{)?unbulleted list ?\|', '')
    clean = clean.str.replace('(\{\{)?ubl,', '')
    clean = clean.str.replace('\\n(\*)?', ', ')
    clean = clean.str.replace('\(original \[\[landrace\]\]\)', '')
    clean = clean.str.replace('\[\[Manx \(cat\)\|Manx\]\]', '')
    clean = clean.str.replace(',  \{\{lang\|zh\-Latn\|Lí hua māo\}\} \( \{\{lang\|zh\|貍花貓\}\} \)', '')
    clean = clean.str.replace('\( \{\{zh\|t\|=\|.*\|labels\|=\|no\}\} \)', '')
    clean = clean.str.replace('(\{\{)|<small>?((\|.*\)\}\})|(.*</small>))', '')
    clean = clean.str.replace('\{\{ubl\|', '')
    clean = clean.str.replace('\|(n|N)ickname:.*', '')
    clean = clean.str.replace('\[\[(l|L)andrace\]\].*', '')
    clean = clean.str.replace('(\{\{)?(\|)?transl(\|)?(\|)?(-)?..\|', '')
    clean = clean.str.replace('(\{\{)?(\|)?lang(\|)?(\|)?(-)?..\|', '')
    clean = clean.str.replace('\|Citation.*', '')
    clean = clean.str.replace('\|ref\|.*(\|ref\|.*\|)|\%$', '')
    clean = clean.str.replace('<.*>', '')
    clean = clean.str.replace('\{\{', '')
    clean = clean.str.replace('\}\}', '')
    clean = clean.str.replace('(\[)*', '')
    clean = clean.str.replace('(\])*', '')
    clean = clean.str.replace('\|' ,', ')
    clean = clean.str.replace('^,', '')
    clean = clean.str.replace('^ ', '')
    clean = clean.str.replace(' *, *,', ',')
    
    return clean

def clean_nicknames(df):
    clean = clean_common(df)
    clean = clean.str.replace('\{\{flat ?list\|(\\n\*),? ?', '')
    clean = clean.str.replace('\\n\*',', ')
    clean = clean.str.replace('\}\}','')
    clean = clean.str.replace('\{\{hlist\|','')
    clean = clean.str.replace('\{\{unbulleted list ?(\|)?', '')
    clean = clean.str.replace('\[\[', '')
    clean = clean.str.replace('\|..?.?\]\]', '')
    clean = clean.str.replace('\|', ', ')
    clean = clean.str.replace('^,', '')
    clean = clean.str.replace('^ ', '')
    clean = clean.str.replace(',,', ',')
    
    return clean

def clean_weight(df):
    clean = clean_common(df)
    clean = clean.str.replace('(\|kg)(\|lb)?(\|0)?(\|abbr\|=\|on)?(\}\})?', ' kg')
    clean = clean.str.replace('(\|lb)( kg)?(\|kg)?(\|0)?(\|abbr\|=\|on)?(\}\})?', ' lb')
    clean = clean.str.replace('(\|1)?\|((abbr)|(sigfig)|(round))\|=\|((on)|(out)|(..?))\}\}', '')
    clean = clean.str.replace('\|-1\}\}', '')
    clean = clean.str.replace('\|order\|=\|flip\}\}', '')
    clean = clean.str.replace('\{\{nowrap\|convert\|', '')
    clean = clean.str.replace('\{\{(((c|C)onvert)|(cvt)) ?\|', '')
    clean = clean.str.replace('\|lb' , ' lb')
    clean = clean.str.replace('\|kg' , ' kg')
    clean = clean.str.replace('^,', '')
    clean = clean.str.replace('^ ', '')

    return clean

def clean_height(df):
    clean = clean_common(df)
    clean = clean.str.replace('(\|in)(\|cm)?(\|0)?(\|abbr\|=\|on)?(\}\})?', ' in')
    clean = clean.str.replace('(\|cm)( in)?(\|in)?(\|0)?(\|abbr\|=\|on)?(\}\})?', ' cm')
    clean = clean.str.replace('\|((order)|(abbr))\|=\|((flip)|(out)|(on))(\|abbr\|=\|on)?\}\}', '')
    clean = clean.str.replace('\{\{rp?\|...\}\}', '')
    clean = clean.str.replace('\{\{(((c|C)onvert)|(cvt)) ?\|', '')    
    clean = clean.str.replace('\{\{nowrap\|convert\|', '')
    clean = clean.str.replace('\{\{(c|C)onvert\|', '')
    clean = clean.str.replace('at the \[\[withers\]\]', '')
    clean = clean.str.replace('^,', '')
    clean = clean.str.replace('^ ', '')

    return clean

def clean_coat(df):
    clean = clean_common(df)
    clean = clean.str.replace('see below', '')
    clean = clean.str.replace('(See )?\[\[.*\]\]( section below)?', '')
    clean = clean.str.replace('\{\{(c|C)onvert\|', '')
    clean = clean.str.replace('\|cm\|in\}\}', ' cm')
    clean = clean.str.replace('\|in\|cm\}\}', ' in')    
    clean = clean.str.replace(';', ',')
    clean = clean.str.replace('^,', '')
    clean = clean.str.replace('^ ', '')

    return clean

def clean_color(df):
    clean = clean_common(df)
    clean = clean.str.replace('\[\[', '')
    clean = clean.str.replace('\]\]', '')
    clean = clean.str.replace('\{\{hlist\|', '')
    clean = clean.str.replace('\{\{plain ?list\|\\n\*', '')
    clean = clean.str.replace('\\n\*', ', ')
    clean = clean.str.replace('\}\}', '')
    clean = clean.str.replace('\|', ',')
    clean = clean.str.replace('\\n', ' ')
    clean = clean.str.replace('^,', '')
    clean = clean.str.replace('^ ', '')

    return clean

def clean_lifespan(df):
    clean = clean_common(df)
    clean = clean.str.replace('\}\} ', '')
    clean = clean.str.replace('[.*]', '')
    clean = clean.str.replace('\\n', '')
    clean = clean.str.replace('^,', '')
    clean = clean.str.replace('^ ', '')

    return clean

def find_bird(request):
    html = requests.get(request)
    b = BeautifulSoup(html.text, 'lxml')

    m = 0

    for i in b.find_all(name='table', class_='infobox biota'):
        for j in i.find_all(name='tr'):
            for k in j.find_all(name='td', style=False, colspan=False):
                if m == 1:
                    kingdom = k.text
                if m == 3:
                    phylum = k.text
                if m == 7:
                    order = k.text
                if m == 9:
                    family = k.text
                m = m + 1   

    return kingdom, phylum, order, family

#birds
bird_df = pd.DataFrame(columns=['breed', 'summary', 'image', 'conservation_status', 'kingdom', 'phylum',
                               'order', 'family', 'binomial_name'])

html = requests.get('https://en.wikipedia.org/wiki/List_of_birds_of_Canada')

#turn the HTML into a beautiful soup text object
b = BeautifulSoup(html.text, 'lxml')

done = False

for i in b.find_all(name='ul'):
    for j in i.find_all(name='li'):        
        #get the summary of each breed
        # loop = True
        for link in j.find_all(name='a', href=True, title=True):
            # while loop:
            try:
                breed = link['title']
                if breed == 'Portal:Birds':
                    done = True
                    break
                page = wptools.page(breed)
                parse = page.get_parse()

                try:
                    if (parse.data['infobox']['status'] == 'LC'):
                        conservation_status = 'Least Concern'
                        
                    if (parse.data['infobox']['status'] == 'NT'):
                        conservation_status = 'Near Threatened'
                        
                    if (parse.data['infobox']['status'] == 'VU'):
                        conservation_status = 'Vulnerable'
                        
                    if (parse.data['infobox']['status'] == 'EN'):
                        conservation_status = 'Endangered'
                        
                    if (parse.data['infobox']['status'] == 'CR'):
                        conservation_status = 'Critically Endangered'
                        
                    if (parse.data['infobox']['status'] == 'EW'):
                        conservation_status = 'Extinct In The Wild'
                        
                    if (parse.data['infobox']['status'] == 'EX'):
                        conservation_status = 'Extinct'

                except:
                    conservation_status = None
                
                restbase = page.get_restbase('/page/summary/')
                url = restbase.data['url']
                
                kingdom, phylum, order, family = find_bird(url)
                
                try:
                    genus = parse.data['infobox']['genus']
                except:
                    genus = None
                
                try:
                    species = parse.data['infobox']['species']
                except: 
                    species = None
                
                try: 
                    binomial_name = genus + ' ' + species
                except:
                    try:
                        binomial_name = parse.data['infobox']['taxon']
                    except:
                        binomial_name = None
                
                try:
                    image = parse.data['image'][0]['url']
                except:
                    image = 'https://user-images.githubusercontent.com/24848110/33519396-7e56363c-d79d-11e7-969b-09782f5ccbab.png'
                summary = wikipedia.WikipediaPage(breed).summary

                bird_df = bird_df.append({'breed':breed, 'summary': summary, 'image': image,
                                         'conservation_status': conservation_status, 'kingdom': kingdom,
                                          'phylum': phylum, 'order': order, 'family': family, 
                                          'binomial_name': binomial_name},
                                         ignore_index = True)
                # loop = False

            except:
                print('Sleeping until reconnect')
                time.sleep(5)

        if(done):
            break
    if(done):
        break

bird_df = bird_df.drop_duplicates(subset = 'breed')
bird_df.to_csv('birds.csv',index = False, header = True)

#cat
cat_df = pd.DataFrame(columns=['breed', 'summary', 'image', 'other_names', 'nicknames', 'origin'])

html = requests.get('https://en.wikipedia.org/wiki/List_of_cat_breeds')

#turn the HTML into a beautiful soup text object
b = BeautifulSoup(html.text, 'lxml')

# get to the table on the page
for i in b.find_all(name='table', class_='wikitable sortable'):
    for j in i.find_all(name='tr'):
        #get the summary of each breed
        for k in j.find_all(name='th'):
            
            # get within that cell to just get the words
            for link in k.find_all('a', href=True):
                # loop = True
                # while loop:
                try:
                    if(re.match('^#', link['href'])):
                        continue
                    else:
                        breed = j.find('a')['title']
                        page = wptools.page(breed)
                        parse = page.get_parse()
                        
                        try:
                            other_names = parse.data['infobox']['altname']
                        except:
                            other_names = None
                            
                        try:
                            nicknames = parse.data['infobox']['nickname']
                        except:
                            nicknames = None
                        
                        try:
                            origin = parse.data['infobox']['country']
                        except:
                            origin = None
                            
                        try:
                            image = parse.data['image'][0]['url']
                        except:
                            image = 'https://user-images.githubusercontent.com/24848110/33519396-7e56363c-d79d-11e7-969b-09782f5ccbab.png'
                        
                        summary = wikipedia.WikipediaPage(breed).summary

                        cat_df = cat_df.append({'breed':breed, 'summary': summary, 'image':image,
                                               'other_names': other_names, 'nicknames': nicknames,
                                                'origin': origin}, ignore_index = True)
                        # loop = False
                    
                except:
                    print('Sleeping until reconnect')
                    time.sleep(5)

cat_df['origin'] = clean_origin(cat_df['origin'])
cat_df['nicknames'] = clean_nicknames(cat_df['nicknames'])
cat_df['other_names'] = clean_other_names(cat_df['other_names'])

cat_df = cat_df.drop_duplicates(subset='breed')
cat_df.to_csv('cats.csv', index = False, header = True)

#dog
dog_df = pd.DataFrame(columns=['breed', 'summary', 'image','other_names','nicknames','origin','weight','height',
                              'coat','color','lifespan'])

html = requests.get('https://en.wikipedia.org/wiki/List_of_dog_breeds')

#turn the HTML into a beautiful soup text object
b = BeautifulSoup(html.text, 'lxml')

# get to the table on the page
for i in b.find_all(name='table', class_='wikitable sortable'):
    
    for j in i.find_all(name='tr'):
        # loop = True
        # while loop:
        try:    
            if(j.find('a') == None):
                continue
            else:
                breed = j.find('a')['title']
                page = wptools.page(breed)
                parse = page.get_parse()
                
                try:
                    other_names = parse.data['infobox']['altname']
                except:
                    other_names = None
                
                try:
                    nicknames = parse.data['infobox']['nickname']
                except:
                    nicknames = None
                
                try:
                    origin = parse.data['infobox']['country']
                except:
                    origin = None
                    
                #some have male and/or female weight/height
                #because we only have a single column for weight, I'm only going 
                #to take the male weight if offered
                try:
                    weight = parse.data['infobox']['weight']
                except:
                    try:
                        weight = parse.data['infobox']['maleweight']
                    except:
                        weight = None
                
                try:
                    height = parse.data['infobox']['height']
                except:
                    try:
                        height = parse.data['infobox']['maleheight']
                    except:
                        height = None
                try:
                    coat = parse.data['infobox']['coat']
                except:
                    coat = None
                
                try:
                    color = parse.data['infobox']['color']
                except:
                    color = None
                
                try:
                    lifespan = parse.data['infobox']['life_span']
                except:
                    lifespan = None
                
                try:
                    image = parse.data['image'][0]['url']
                except:
                    image = 'https://user-images.githubusercontent.com/24848110/33519396-7e56363c-d79d-11e7-969b-09782f5ccbab.png'
                
                summary = wikipedia.WikipediaPage(breed).summary
                
                dog_df = dog_df.append({'breed':breed, 'summary': summary, 'image': image, 'other_names':other_names,
                                        'nicknames': nicknames, 'origin': origin, 'weight': weight,
                                        'height': height, 'coat': coat, 'color': color, 'lifespan': lifespan},
                                       ignore_index = True)
                # loop = False

        except:
            print('Sleeping until reconnect')
            time.sleep(5)

dog_df['origin'] = clean_origin(dog_df['origin'])
dog_df['nicknames'] = clean_nicknames(dog_df['nicknames'])
dog_df['other_names'] = clean_other_names(dog_df['other_names'])
dog_df['height'] = clean_height(dog_df['height'])
dog_df['weight'] = clean_weight(dog_df['weight'])
dog_df['coat'] = clean_coat(dog_df['coat'])
dog_df['color'] = clean_coat(dog_df['color'])
dog_df['lifespan'] = clean_lifespan(dog_df['lifespan'])

dog_df = dog_df.drop_duplicates(subset = 'breed').drop([0])
dog_df.to_csv('dogs.csv', index = False, header = True)