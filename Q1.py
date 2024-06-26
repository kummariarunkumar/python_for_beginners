class FlightTicketGenerator:
    def __init__(self, airline, src, dest, start_number=101):
        self.airline = airline
        self.src = src[:3].upper()
        self.dest = dest[:3].upper()
        self.start_number = start_number
        self.ticket_numbers = []

    def generate_tickets(self, passenger_count):
        for i in range(passenger_count):
            ticket_number = f"{self.airline}:{self.src}:{self.dest}:{self.start_number + i}"
            self.ticket_numbers.append(ticket_number)

    def get_last_five_tickets(self):
        if len(self.ticket_numbers) < 5:
            return self.ticket_numbers
        else:
            return self.ticket_numbers[-5:]

# Example usage:
airline = "AL1"
src_city = "New York"
dest_city = "Los Angeles"
passenger_count = 7  # Example passenger count

ticket_generator = FlightTicketGenerator(airline, src_city, dest_city)
ticket_generator.generate_tickets(passenger_count)
last_five_tickets = ticket_generator.get_last_five_tickets()

print("Last five ticket numbers:", last_five_tickets)
