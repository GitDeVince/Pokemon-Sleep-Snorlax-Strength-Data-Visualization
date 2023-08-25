import numpy as np
import matplotlib.pyplot as plt

#data from https://www.serebii.net/pokemonsleep/snorlaxratings.shtml

N = 15
width = 0.25

GI_ss = [0,3118,7171,11693,17149,23385,31492,41314,53006,65634,79197,93540,109130,125032,156121]
CB_ss = [0,4882,11090,18082,26520,36164,48700,63889,81971,101499,122474,144654,168763,195283,224455]
TH_ss = [0,6885,15835,25817,37865,51635,69534,91221,117038,144921,174869,206538,240961,278826,320478]
ST_ss = [0,10486,24118,39323,57673,78645,105909,138940,178262,220730,266344,314580,367010,424683,488123]

GI_ss_masters = [187832,220177,253169,286821,321146,356158,391870,428296,465451,532707,601308,742056,885619,1029700,1199506,1486800,1795052,2165541,2604280,3245795]
CB_ss_masters = [256544,291842,330670,373381,420363,472043,528891,591424,660210,735875,819107,910682,1018462,1184155,1379432,1709820,2064310,2490372,2994922,3732664]
TH_ss_masters = [366295,416694,472133,533116,600197,673986,755154,844439,942653,1050688,1169527,1300250,1444045,1602220,1776213,1967605,2333568,2815203,3385564,4219534]
ST_ss_masters = [557907,634669,719107,811989,914159,1026546,1150172,1286161,1435749,1600296,1781298,1980400,2199412,2440325,2705329,2996833,3317487,3670206,4058197,4706403]

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
    ax.yaxis.get_major_formatter().set_scientific(False)
    ax.yaxis.get_major_formatter().set_useOffset(False)

    master_rank = ['Master 1', 'Master 2', 'Master 3', 'Master 4', 'Master 5', 'Master 6', 'Master 7', 'Master 8', 'Master 9', 'Master 10', 'Master 11', 'Master 12', 'Master 13', 'Master 14', 'Master 15', 'Master 16', 'Master 17', 'Master 18', 'Master 19', 'Master 20']
    ax.plot(master_rank, GI_ss_masters, linewidth = 3, c ='green')
    ax.plot(master_rank, CB_ss_masters, linewidth = 3, c ='blue')
    ax.plot(master_rank, TH_ss_masters, linewidth = 3, c ='brown')
    ax.plot(master_rank, ST_ss_masters, linewidth = 3, c ='purple')

    ax.set_title("Master 1 to Master 20 Snorlax Strength Requirement", fontsize = 24)
    ax.set_xlabel("Ranks", fontsize = 14)
    ax.set_ylabel("Snorlax Strength Number", fontsize = 14)
    plt.legend( (GI_ss_masters, CB_ss_masters, TH_ss_masters, ST_ss_masters), ("Greengrass Isle", "Cyan Beach", "Taupe Hollow", "Snowdrop Tundra"))
    plt.show()

while True:
    decision = input("Please choose the letter before the option: '(a) Basic 1 to Ultra 5', '(b) Master 1 to Master 20', or (c) Exit' ")
    decision = decision.capitalize()

    if decision == "A":
       basic_ultra()

    elif decision == "B":
        masters()

    elif decision == "C":
        print("Goodbye")
        break

    else:
        print("Please only choose the given options.")

