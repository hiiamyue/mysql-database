import csv
import re

def create_genres(source,dest):
    with open(dest,'w',newline='') as file:
        writer =csv.writer(file)
        with open(source) as f:
            reader = csv.reader(f,delimiter=',')
            for r in reader:
                genres = r[2].split('|')
                for genre in genres:
                    writer.writerow([r[0], genre])


def add_index(source,dest):
     with open(dest,'w',newline='') as file:
        writer =csv.writer(file)
        with open(source) as f:
            reader = csv.reader(f,delimiter=',')
            row1 = next(reader)
            row1.append('index')
            writer.writerow(row1)
            index =0
            for r in reader:
                writer.writerow(r+[index])
                index +=1

# def fix_genres(source, dest):
#     with open(dest, 'w', newline='') as file:
#         writer = csv.writer(file)
#         with open(source) as f:
#             reader = csv.reader(f, delimiter=',')
#             for r in reader:
#                 genres = r[1].split('|')
#                 for genre in genres:
#                     writer.writerow([r[0], genre])


def modified_movies(source,dest):
    with open(source) as f:
        with open(dest,'w',newline='') as d:
            writer = csv.writer(d)
            reader = csv.reader(f, delimiter=',')
            row1 = next(reader)#dont need first line
            row1.append('release_date')
            writer.writerow(row1)
            for l in reader:
                date = re.findall(r'\(.*?\)', l[1])
                if len(date)>1:
                    d =date[-1].strip("(,)")
                    new=l[1].replace(date[-1],'').rstrip().strip('"')
                    l[1]=new
                    writer.writerow(l+[d])
                else:
                    if date:
                        d = date[0].strip("(,)")
                        new =l[1].replace(date[0],'').rstrip().strip('"')
                        l[1]=new
                        writer.writerow(l+[d])
                    else:
                        new=l[1].strip('"')
                        l[1]=[new]
                        writer.writerow(l+[0])
                        # null value represented as 0
                    

if __name__=="__main__":
    create_genres('ml-latest-small/movies.csv','Normalised/genres.csv')
    add_index('Normalised/genres.csv','Normalised/new_genres.csv')
    add_index('ml-latest-small/tags.csv','Normalised/new_tags.csv')
    #fix_genres('Normalised/genres.csv','Normalised/new_genres.csv' )
    modified_movies('ml-latest-small/movies.csv','Normalised/new_movies.csv')

 
