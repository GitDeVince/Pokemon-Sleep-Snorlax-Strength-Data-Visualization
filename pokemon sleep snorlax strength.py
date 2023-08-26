import numpy as np
import matplotlib.pyplot as plt

#data from https://www.serebii.net/pokemonsleep/snorlaxratings.shtml

N = 15
width = 0.25

#datapoints of snorlax strength requirement from basic 1 to ultra 5 ranks in Greengrass Isle, Cyan Beach, Taupe Hollow, and Snowdrop Tundra
GI_ss = [0,3118,7171,11693,17149,23385,31492,41314,53006,65634,79197,93540,109130,125032,156121]
CB_ss = [0,4882,11090,18082,26520,36164,48700,63889,81971,101499,122474,144654,168763,195283,224455]
TH_ss = [0,6885,15835,25817,37865,51635,69534,91221,117038,144921,174869,206538,240961,278826,320478]
ST_ss = [0,10486,24118,39323,57673,78645,105909,138940,178262,220730,266344,314580,367010,424683,488123]

#datapoints of snorlax strength requirement from master 1 to master 20 ranks in Greengrass Isle, Cyan Beach, Taupe Hollow, and Snowdrop Tundra
GI_ss_masters = [0.19,0.22,0.25,0.29,0.32,0.36,0.39,0.43,0.47,0.53,0.60,0.74,0.89,1.03,1.20,1.49,1.80,2.17,2.60,3.25]
CB_ss_masters = [0.26,0.29,0.33,0.37,0.42,0.47,0.53,0.59,0.66,0.74,0.82,0.91,1.02,1.18,1.38,1.71,2.06,2.49,2.99,3.73]
TH_ss_masters = [0.37,0.42,0.47,0.53,0.60,0.67,0.76,0.84,0.94,1.05,1.17,1.30,1.44,1.60,1.78,1.97,2.33,2.82,3.39,4.22]
ST_ss_masters = [0.56,0.63,0.72,0.81,0.91,1.03,1.15,1.29,1.44,1.60,1.78,1.98,2.20,2.44,2.71,3.00,3.32,3.67,4.06,4.71]

# turning these into functions as practice but also to make it organized. Also I wanted for Cyan Beach to be light blue not blue but matplolib doesn't accept that?
def basic_ultra():

    plt.style.use('seaborn')

    fig, ax = plt.subplots()

    basic_to_ultra = ['Basic 1', 'Basic 2', 'Basic 3', 'Basic 4', 'Basic 5', 'Great 1', 'Great 2', 'Great 3', 'Great 4','Great 5', 'Ultra 1', 'Ultra 2', 'Ultra 3', 'Ultra 4', 'Ultra 5']

    ax.plot(basic_to_ultra, GI_ss, linewidth = 3, c ='green', label = "Greengrass Isle" )
    ax.plot(basic_to_ultra, CB_ss, linewidth = 3, c ='blue', label = "Cyan Beach")
    ax.plot(basic_to_ultra, TH_ss, linewidth = 3, c ='brown', label = "Taupe Hollow")
    ax.plot(basic_to_ultra, ST_ss, linewidth = 3, c ='purple', label = "Snowdrop Tundra")

    ax.set_title("Basic 1 to Ultra 5 Snorlax Strength Requirement", fontsize = 24)
    ax.set_xlabel("Ranks", fontsize = 14)
    ax.set_ylabel("Snorlax Strength Number", fontsize = 14)
    leg = ax.legend(loc ="upper left")
    plt.show()

def masters():

    plt.style.use('seaborn')

    fig, ax = plt.subplots()
   

    master_rank = ['Master 1', 'Master 2', 'Master 3', 'Master 4', 'Master 5', 'Master 6', 'Master 7', 'Master 8', 'Master 9', 'Master 10', 'Master 11', 'Master 12', 'Master 13', 'Master 14', 'Master 15', 'Master 16', 'Master 17', 'Master 18', 'Master 19', 'Master 20']
    ax.plot(master_rank, GI_ss_masters, linewidth = 3, c ='green', label = "Greengrass Isle" )
    ax.plot(master_rank, CB_ss_masters, linewidth = 3, c ='blue', label = "Cyan Beach")
    ax.plot(master_rank, TH_ss_masters, linewidth = 3, c ='brown', label = "Taupe Hollow")
    ax.plot(master_rank, ST_ss_masters, linewidth = 3, c ='purple', label = "Snowdrop Tundra")

    ax.set_title("Master 1 to Master 20 Snorlax Strength Requirement (in millions)", fontsize = 24)
    ax.set_xlabel("Ranks", fontsize = 14)
    ax.set_ylabel("Snorlax Strength Number", fontsize = 14)
    leg = ax.legend(loc ="upper left")
    plt.show()

while True:
    decision = input("Please choose the letter before the option: '(a) Basic 1 to Ultra 5', '(b) Master 1 to Master 20', or (c) Exit' ")
    decision = decision.capitalize()

    #Earlier, I was thinking of doing like "if decision == 'A' or 'A.'" but its not working. So I workaround that problem by changing the question and the condition.
    if decision == "A":
       basic_ultra()

    elif decision == "B":
        masters()

    elif decision == "C":
        print("Goodbye")
        break

    else:
        print("Please only choose the given options.")

