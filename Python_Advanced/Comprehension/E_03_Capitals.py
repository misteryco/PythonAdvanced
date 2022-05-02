# countries = input().split(", ")
# capitals = input().split(", ")
#
# dict_data = {tuples[0]: tuples[1] for tuples in zip(countries, capitals)}
# for country, capital in dict_data.items():
#     print(f"{country} -> {capital}")
# ==============================================================================================================
# [print(f"{country} -> {capital}") for country, capital in {tuples[0]: tuples[1]
#                                                            for tuples in zip(countries, capitals)}.items()]
# ==============================================================================================================

[print(f"{country} -> {capital}")
 for country, capital in {tuples[0]: tuples[1]
                          for tuples in zip(input().split(", "), input().split(", "))}.items()]

# ==============================================================================================================
#  extremely stupid use of comprehension - first example is much better
