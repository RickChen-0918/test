import plotly.express as px
import pandas as pd 
import omdb

with open('data project/movies.tsv') as f:
    lines = f.readlines()
    movies = []
for line in lines: 
  x = line.strip().split('\t')
  flag = 0
  for n in x:
    if n == '':
      flag = 1
  if flag == 0:
    movies.append(x)

df = pd.DataFrame(movies, columns =['Year','Length','Title','Subject','Actor','Actress','Director','Popularity','Awards','Image'])
df['Year'] = df['Year'].astype(int) 
df['Length'] = df['Length'].astype(int)
df['Popularity'] = df['Popularity'].astype(int)

def number_of_each_catagory():
  subjects = []
  for i in df['Subject']:
    subjects.append(i)

  catagories = []
  for i in subjects:
    if not(i in catagories):
      catagories.append(i)
  
  number = []
  for i in catagories:
    number.append(subjects.count(i))

  fig = px.bar(x = catagories, y = number)  
  fig.show()

def average_runtime_by_catagory():
  subjects = []
  for i in df['Subject']:
    subjects.append(i)
  
  runtimes = []
  for n in df['Length']:
    runtimes.append(n)

  catagories = []
  for i in subjects:
    if not(i in catagories):
      catagories.append(i)

  avg_times = []
  for i in catagories:
    total = 0
    count = 0
    for k in range(len(subjects)):
      if subjects[k] == i:
        total += runtimes[k]
        count += 1
    avg = total/count
    avg_times.append(avg)
  
  data = []
  for i in range(len(catagories)):
    x = [catagories[i],avg_times[i]]
    data.append(x)

  frame = pd.DataFrame(data,columns =['Catagories','Average runtime'])
  fig = px.bar(frame, x='Catagories', y='Average runtime', title='Average runtime by catagory')
  fig.show()

def year_vs_popularity():
  fig = px.scatter(df, x="Year", y="Popularity")
  fig.show()

def highest_popularity_in_1973():
  years = []
  for i in df['Year']:
    years.append(i)

  popularities = []
  for i in df['Popularity']:
    popularities.append(i)

  index = []
  for i in range(len(years)):
    if years[i] == 1973:
      index.append(i)

  max = 0
  for i in index:
    if popularities[i] > max:
      max = popularities[i]
  
  return df.iloc[max]
  
def verifying():
  omdb.set_default('apikey','84fcc539')
  sample = []
  for i in range(100):
    sample.append(df['Title'][i])

  ratings = []
  for i in range(100):
    ratings.append(df['Popularity'][i])
  
  good = 0
  bad = 0
  total = 0
  for i in range(len(sample)):
    movie = omdb.get(title = sample[i])
    try:
      if abs(int(movie['metascore']) - int(ratings[i])) < 20:
        good += 1
        total += 1
      else:
        bad += 1
        total += 1
    except:
      pass

  return good, bad, total
  




if __name__ == '__main__':
  average_runtime_by_catagory()
  year_vs_popularity()
  print(verifying())
