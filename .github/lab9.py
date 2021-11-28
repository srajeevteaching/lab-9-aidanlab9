# Programmers: Aidan, Nicol
# Course: CS151, Dr. Rajeev
# Date: 11/18/2021
# Lab Number: 9
# Program Inputs: [What information do you request from the user?]
# Program Outputs: [What information do you display for the user?]

# (release, date, title, budget box office, gross) Write a program which, given the name of a file respecting this
# format and the name of an output file, writes all movie information from the input file to the output file, but also
# adds a new column with the movie's profit (computed as the difference between box office gross and budget).
# Additionally, the program should determine which movies had the highest and lowest profits and output to the console
# all information related to those two movies.

# Function decomposition Your program should have a function for each of the following tasks. Practice iterative
# development: implement each item according to the instructions section below and then test that your code still works
# before proceeding onto the next item.

# A function load_movie_data which, given the name of a file respecting the csv format outlined above, loads the data
# into a list of lists. Declare column index constants at the top of your program for each of the movie fields (release
# date, title, etc.) Cast each field to the appropriate type. Use try/except so that your program exits normally if the
# file does not exist or if a numerical value in the input file fails to cast.

# A function add_profit_column which, given a movie dataset as a list of lists, adds a profit column to the data
# computed as the difference between each movie's gross and its budget.

# A function print_min_and_max_profit which, given a movie dataset as a list of lists, searches the dataset and prints
# all available info on the movies with the highest and lowest profits.

# A function save_movie_data which, given a movie dataset as a list of lists and a filename, saves the dataset to a
# comma-separated values file of the given name.

# A main function to drive the program

date = 0
title = 1
budget = 2
boxGross = 3
profit = 4

def read_file(filename):
    data_list = []
    try:
        file = open(filename, "r")
        count = 0
        for line in file:
            try:
                count += 1
                sep = line.split(",")
                sep[date] = str(sep[date].strip())
                sep[title] = str(sep[title].strip())
                sep[budget] = float(sep[budget])
                sep[boxGross] = float(sep[boxGross])
                data_list.append(sep)
            except ValueError:
                print(count, "Invalid line and skipped to continue")
        file.close()
    except FileNotFoundError:
        print("Invalid file")
        exit()
    return data_list

def add_column(dataset):
    for i in range(len(dataset)):
        gross = dataset[i][boxGross]
        movieBudget = dataset[i][budget]
        profits = gross - movieBudget
        dataset[i].append(profits)
    return dataset

def profits(dataset):
    profit_list = []
    for i in range(len(dataset)):
        profit_list.append(dataset[i][profit])
    max_val = max(profit_list)
    min_val = min(profit_list)
    max_index = profit_list.index(max_val)
    min_index = profit_list.index(min_val)
    print("Highest Profit Movie: ", dataset[max_index])
    print("Total Profit: ", max_val)
    print()
    print("Lowest Profit Movie:", dataset[min_index])
    print("Total Profit for Lowest: ", min_val)

def save_file(filename):
    def save_file(filename, data_list):
        with open(filename, "w") as file:
            for line in file:
                for line in data_list:
                    for element in line:
                        file.write(str(element) + ",")
                    file.write("\n")

def main():
    movie_list = read_file("movies.csv")
    movie_list_profits = add_column(movie_list)
    profits(movie_list_profits)
    choice = input("What's the name of the first file? ")
    created_file_name = input("What's the name of the second file? ")
    movie_list = read_file(choice)
    movie_profit_list = add_column(movie_list)
    profits(movie_profit_list)
    save_file(created_file_name, movie_profit_list)

main()