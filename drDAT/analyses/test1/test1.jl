using Statistics
using PyPlot
using CSV

rd = CSV.read("C:\\Users\\Dwight\\Documents\\Projects\\data\\data1.csv")
#print(rd.Time)
plot(rd.Time, rd.Value);
savefig("C:/Users/Dwight/Documents/Projects/Dat/Dev2/images/fig3.png",format="png")