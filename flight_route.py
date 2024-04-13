#Task 1

our_routes = {"LAX", "JFK", "CDG", "DXB", "ORD", "SBN"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK", "MDW"}

both_dest = our_routes.intersection(competitor_routes)
print("These are the destinations that we share with our competitor:", both_dest)

our_unique = our_routes.difference(competitor_routes)
print("These destinations are unique to our airline:", our_unique)

unique_both = our_routes.symmetric_difference(competitor_routes)
print("These destinations are unqiue amongst both airlines:", unique_both)