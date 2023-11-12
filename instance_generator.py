"""
This script is used to generate random instances of an EOSCSP problem given : 
n_Satelite : Number of sattelites 
n_UserEX : Number of exclusive users
n_Task : Number of tasks 

An EOSCSP problem is defined by a tuple : <S, U, R, O>
S : Set of Satellites
U : Set of users
R : Set of requests
O : set of observations to schedule to fulfill requests in R

PyDcop file formats : https://pydcop.readthedocs.io/en/latest/usage/fileformat_ref.html
example : "dcop_format.yml" 

"""

def generate_instance(n_Satelite, n_UserEX, n_Task): 
    print("loul")

if __name__ == "__main__":
    n_Satelite = 3
    n_UserEX = 2
    n_Task = 6

    instance = generate_instance(n_Satelite, n_UserEX, n_Task)
    print(instance)