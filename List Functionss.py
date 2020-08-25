lucky_numbers = [42, 18, 4, 8, 15, 16, 23]
friends = ["Kevin", "Karen", "Jim", "Jim", "JIM", "Oscar", "Toby"]
friends.extend(lucky_numbers)
friends.append("Creed")
friends.insert(1, "Kelly")
friends.remove("Toby")
lucky_numbers.sort()
print(friends)
friends.clear()
friends.extend(lucky_numbers)
print(friends)

friends = ["Kevin", "Karen", "Jim", "Jim", "JIM", "Oscar", "Toby"]
friends2 = friends.copy()
lucky_numbers.reverse()
friends2.extend(lucky_numbers)
print(friends2)
friends2.pop()
print(friends2)
print(friends2.index("Karen"))
friends2.pop()
print(friends2.count("Jim"))
friends2.clear()

