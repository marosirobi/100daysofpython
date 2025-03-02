# travel_log = {
#     "France" : ["Paris","Lille","Dijon"],
#     "Germany" : ["Stuttgart","Berlin"]
# }
#
# print(travel_log["France"][1])

nested_list = ["a","b",["c","d"]]
print(nested_list[2][1])

travel_log = {
    "France" : {
        "num_times_visited": 8,
        "cities_visited" : ["Paris","Lille","Dijon"]
    },
    "Germany" : {
        "num_times_visited": 8,
        "cities_visited" : ["Stuttgart","Berlin","Hamburg"]
    }
}

print(travel_log["Germany"]["cities_visited"][0])