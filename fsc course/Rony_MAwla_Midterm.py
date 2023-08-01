import datetime #with the help of w3schools

# Initialize counter
counter = 0

# Read tickets from the text file and create the ticketing system list
ticketing_system = []
filename = "file.txt"


def display_statistics(ticketing_system):
  event_counts = {}
  total_tickets = len(ticketing_system)
  total_priority = 0

  max_event_id = None
  max_tickets_count = 0

  for ticket in ticketing_system:
    event_id = ticket[1]
    if event_id in event_counts:
      event_counts[event_id] += 1
    else:
      event_counts[event_id] = 1

    total_priority += ticket[4]

    # Update max_tickets_count and max_event_id if necessary
    if event_counts[event_id] > max_tickets_count:
      max_tickets_count = event_counts[event_id]
      max_event_id = event_id

  if not event_counts:
    print("No tickets found.")
  else:
    avg_priority = total_priority / total_tickets

    print(
        "Event ID with the highest number of tickets: {}".format(max_event_id))#with the help of google

#with the help of w3schools
with open(filename, "r") as file:
  for line in file:
    ticket_id, event_id, username, timestamp, priority_integer = line.strip(
    ).split(", ")
    priority_integer = int(priority_integer)
    ticketing_system.append(
        [ticket_id, event_id, username, timestamp, priority_integer])

# Display welcome message and login form
print("Welcome to the Ticketing System!")

# Loop for login attempts
while counter < 5:
  # Display login form
  print("Welcome to the System")
  username = input("Enter your username (user/admin): ")
  password = input("Enter your password (leave empty for User): ")

  # Check user type and creentials
  if username.lower() == "user" and password == "":
    print("Login Successful! Welcome user.")
    break
  elif username.lower() == "admin" and password == "admin123123":
    print("Login Successful! Welcome Admin.")
    break
  else:
    # Incorrect credentials, increment counter
    counter += 1
    print("Incorrect Username and/or Password. Attempts remaining: {}".format(
        5 - counter))

# Max attempts reched, display error message
if counter == 5:
  print("Maximum number of attempts reached. Please try again later.")

# Admin Menu
if username == "admin":
  while True:
    print("""
        1. Display Statistics
        2. Book a Ticket
        3. Display all Tickets
        4. Change Ticket’s Priority
        5. Disable Ticket
        6. Run Events
        7. Exit
        """)

    choice = input("What do you want to do? ")
    if choice == "1":
      # if user chose 1, a function to display statistics goes here
      display_statistics(ticketing_system)
    elif choice == "2":
      # if user chose 2, a function to book a new ticket goes here
      ticket_id = str(len(ticketing_system) + 1).zfill(3)
      event_id = input("Enter the event ID: ")
      username = input("Enter your username: ")
      priority = int(input("Enter the priority of the ticket: "))
      timestamp = datetime.datetime.now().strftime("%Y%m%d")
      ticketing_system.append(
          [ticket_id, event_id, username, timestamp, priority])
      print("Ticket booked successfully!")
    elif choice == "3":
      # if user chose 3, a function to display all tickets goes here
      # Sort the ticketing_system based on date and event_id
      sorted_tickets = sorted(ticketing_system, key=lambda x: (x[3], x[1]))
      today_date = datetime.datetime.now().strftime("%Y%m%d")
      for ticket in sorted_tickets:
        if ticket[3] >= today_date:
          print(
              "Ticket ID: {}, Event ID: {}, Username: {}, Timestamp: {}, Priority: {}"
              .format(ticket[0], ticket[1], ticket[2], ticket[3], ticket[4]))
    elif choice == "4":
      # if user chose 4, a function to change ticket's priority goes here
      ticket_id = input(
          "Enter the ID of the ticket you want to change its priority: ")
      priority_ticket = int(
          input("Enter the current priority of the ticket: "))
      new_priority = int(input("Enter the new priority: "))

      ticket_found = False
      for ticket in ticketing_system:
        if ticket[0] == ticket_id and ticket[4] == priority_ticket:
          ticket[4] = new_priority
          ticket_found = True
          print("Priority updated successfully!")
          break
      if not ticket_found:
        print("Ticket not found.")

    elif choice == "5":
      # Fif user chose 5, a function to disable a ticket goes here
      ticket_id = input("Enter the ID of the ticket you want to disable: ")

      ticket_found = False
      for ticket in ticketing_system:
        if ticket[0] == ticket_id:
          ticketing_system.remove(ticket)
          ticket_found = True
          print("Ticket disabled successfully!")
          break
      if not ticket_found:
        print("Ticket not found.")

    elif choice == "6":
      # if user chose 6, a function to run events goes here
      print("Function to run events")

    elif choice == "7":
      # if user chose 7,  f Save the updated ticketing_system to the file and exit the program
      with open(filename, "w") as file:
        for ticket in ticketing_system:
          file.write("{}, {}, {}, {}, {}\n".format(ticket[0], ticket[1],
                                                   ticket[2], ticket[3],
                                                   ticket[4]))
      print("Inventory information has been updated and saved to the file.")
      print("Exiting the program...")
      break
    else:
      print("Invalid Choice! Please enter a number between 1 & 7.")

# Normal User Menu
elif username == "user":
  while True:
    print("""
        1. Book a Ticket
        2. Exit
        """)

    choice = input("What do you want to do? ")
    if choice == "1":
      # if user chose 1, a function to book a new ticket for the user goes here
      ticket_id = str(len(ticketing_system) + 1).zfill(3)
      event_id = input("Enter the event ID: ")
      priority = 0
      timestamp = datetime.datetime.now().strftime("%Y%m%d")
      ticketing_system.append(
          [ticket_id, event_id, username, timestamp, priority])
      print("Ticket booked successfully!")
    elif choice == "2":
      # if user chose 2, Save the updated ticketing_system to the file and exit the program
      with open(filename, "w") as file:
        for ticket in ticketing_system:
          file.write("{}, {}, {}, {}, {}\n".format(ticket[0], ticket[1],
                                                   ticket[2], ticket[3],
                                                   ticket[4]))
      print("Inventory information has been updated and saved to the file.")
      print("Exiting the program...")
      break
    else:
      print("Invalid Choice! Please enter a number between 1 & 2.")
else:
  print("Invalid user type.")
