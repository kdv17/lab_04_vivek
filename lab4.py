class Flight_Table:
    def Team_Details(self):
        self.table= [
            {"Location": "Mumbai", "Team 01": "India", "Team 02": "Sri Lanka", "Timing": "DAY"},
            {"Location": "Delhi", "Team 01": "England", "Team 02": "Australia", "Timing": "DAY-NIGHT"},
            {"Location": "Chennai", "Team 01": "India", "Team 02": "South Africa", "Timing": "DAY"},
            {"Location": "Indore", "Team 01": "England", "Team 02": "Sri Lanka", "Timing": "DAY-NIGHT"},
            {"Location": "Mohali", "Team 01": "Australia", "Team 02": "South Africa", "Timing": "DAY-NIGHT"},
            {"Location": "Delhi", "Team 01": "India", "Team 02": "Australia", "Timing": "DAY"}
        ]
    
    def team_search(self, team_name):
        result_match = [match for match in self.table if team_name in (match["Team 01"], match["Team 02"])]
        return result_match
    
    def location_search(self, location):
        result_match = [match for match in self.table if match["Location"] == location]
        return result_match
    
    def timing_search(self, timing):
        result_match = [match for match in self.table if match["Timing"] == timing]
        return result_match

def main():
    flight_table = Flight_Table()
    flight_table.Team_Details()

    print("Choose choice to search:")
    print("1. List of all the matches of a Team")
    print("2. List of Matches on a Location")
    print("3. List of Matches based on timing")
    choice = int(input("Enter your choice (1/2/3): "))
    
    if choice == 1:
        team_name = input("Enter team name: ")
        matches = flight_table.team_search(team_name)
    elif choice == 2:
        location = input("Enter location: ")
        matches = flight_table.location_search(location)
    elif choice == 3:
        timing = input("Enter timing: ")
        matches = flight_table.timing_search(timing)
    else:
        print("Invalid choice!")
        return

    if matches:
        print("Search Results:")
        for match in matches:
            print(match)
    else:
        print("No matches found.")

if __name__ == "__main__":
    main()

