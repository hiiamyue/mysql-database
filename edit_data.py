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
            row1.append('idx')
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
            row1 = next(reader)[:2]#dont need first line
            row1.append('release_date')
            writer.writerow(row1)
            for l in reader:
                date = re.findall(r'\(.*?\)', l[1])
                if len(date)>1:
                    d =date[-1].strip("(,)")
                    new=l[1].replace(date[-1],'').rstrip().strip('"')
                    l[1]=new
                    writer.writerow(l[:2]+[d])
                else:
                    if date:
                        d = date[0].strip("(,)")
                        new =l[1].replace(date[0],'').rstrip().strip('"')
                        l[1]=new
                        writer.writerow(l[:2]+[d])
                    else:
                        new=l[1].strip('"')
                        l[1]=new
                        writer.writerow(l[:2]+[0])
                        # null value represented as 0
def new_movies(source1,source2,dest):
     with open(dest, 'w', newline='') as file:
        writer = csv.writer(file)
        with open(source1) as f,open(source2)as mv:
            reader1 = csv.reader(f, delimiter=',')
            reader2 = csv.reader(mv,delimiter=',')
            for l , l2 in zip(reader1,reader2):
                writer.writerow(l2+l[1:])
                

if __name__=="__main__":
    #new_movies()
    create_genres('ml-latest-small/movies.csv','Normalised/genres.csv')
    add_index('Normalised/genres.csv','Normalised/new_genres.csv')
    add_index('ml-latest-small/tags.csv','Normalised/new_tags.csv')
    #fix_genres('Normalised/genres.csv','Normalised/new_genres.csv' )
    modified_movies('ml-latest-small/movies.csv','Normalised/movies.csv')
    new_movies('ml-latest-small/links.csv','Normalised/movies.csv','Normalised/new_movies.csv')

 
