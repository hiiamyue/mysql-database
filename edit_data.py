import csv
import re

def fix_genres(source, dest):
    with open(dest, 'w', newline='') as file:
        writer = csv.writer(file)
        with open(source) as f:
            reader = csv.reader(f, delimiter=',')
            for r in reader:
                genres = r[1].split('|')
                for genre in genres:
                    writer.writerow([r[0], genre])


def modified_movies(source,dest):
    list =[]
    with open(source) as f:
        with open(dest,'w',newline='') as d:
            writer = csv.writer(d)
            reader = csv.reader(f, delimiter=',')
            row1 = next(reader)#dont need first line
            row1.append('Date')
            writer.writerow(row1)
            for l in reader:
                date = re.findall(r'\(.*?\)', l[1])
                if len(date)>1:
                    d =date[-1].strip("(,)")
                    new=l[1].replace(date[-1],'').replace(" ", "")
                    l[1]=new
                    writer.writerow(l+[d])
                else:
                    if date:
                        d = date[0].strip("(,)")
                        new =l[1].replace(date[0],'').replace(" ", "")
                        l[1]=new
                        writer.writerow(l+[d])
                    else:
                        writer.writerow(l+[0])
                    
    
    

if __name__=="__main__":
    fix_genres('Normalised/genres.csv','Normalised/new_genres.csv' )
    list =modified_movies('Normalised/movies.csv','Normalised/new_movies.csv')
    #print(len(list))
