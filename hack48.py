import operator

def person_lister(f):
    def inner(people):
        # complete the function
        data = sorted(people, key=lambda person: int(person[2]))
        sorted_people = []
        for person in data:
            sorted_people.append(f(person))
        return sorted_people

    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')