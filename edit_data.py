import csv

def fix_genres(source, dest):
    with open(dest, 'w', newline='') as file:
        writer = csv.writer(file)
        with open(source) as f:
            reader = csv.reader(f, delimiter=',')
            for r in reader:
                genres = r[1].split('|')
                for genre in genres:
                    writer.writerow([r[0], genre])


if __name__=="__main__":
    fix_genres('Normalised/genres.csv','Normalised/new_genres.csv' )
