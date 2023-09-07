# Create your views here.
# seats/views.py
from collections import defaultdict

from django.shortcuts import render, redirect
from .models import Seat
from django.contrib import messages


def seating_chart(request):
    seats = Seat.objects.all().order_by('row', 'COL')  # Order seats by row and col
    # Create a defaultdict to group seats by row
    grouped_seats = defaultdict(list)
    # Group seats by row
    for seat in seats:
        grouped_seats[seat.row].append(seat)
    # Calculate the total available seats and available seats in each row
    # total_available_seats = 0
    # available_seats_in_each_row = {}
    #
    # for row, seats_in_row in grouped_seats.items():
    #     available_seats_count = sum(1 for seat in seats_in_row if seat.status == 'available')
    #     available_seats_in_each_row[row] = available_seats_count
    #     total_available_seats += available_seats_count
    available_seats_in_each_row = {}
    total_available_seats = 0

    # Create a list of rows for easier iteration in the template
    rows = [{'row': row, 'seats': seats} for row, seats in grouped_seats.items()]
    for row in rows:
        available_count = sum(1 for seat in row['seats'] if seat.status == 'available')
        available_seats_in_each_row[row['row']] = available_count
        total_available_seats += available_count
    return render(request, 'seats/seating_chart.html', {'rows': rows, 'total_available_seats': total_available_seats,
                                                        'available_seats_in_each_row': available_seats_in_each_row})


def submit_reservation(request):
    if request.method == 'POST':
        # Get the list of selected seat IDs from the form
        selected_seat_ids = request.POST.getlist('selected_seats')

        if not selected_seat_ids:
            messages.error(request, 'No seats selected for reservation.')
            return redirect('seating_chart')

        try:
            seats_ids = [int(num) for num in selected_seat_ids[0].split(',')]

            # Fetch the selected seats
            selected_seats = Seat.objects.filter(id__in=seats_ids)

            # Toggle the status of selected seats between 'reserved' and 'available'
            for seat in selected_seats:
                if seat.status == 'available':
                    seat.status = 'reserved'
                elif seat.status == 'reserved':
                    seat.status = 'available'
                seat.save()

            messages.success(request, 'Seats successfully updated!')

        except Exception as e:
            messages.error(request, f'An error occurred while updating seats: {str(e)}')

        return redirect('seating_chart')
    else:
        # Handle GET requests to the submit_reservation URL if needed
        # You can redirect or render a specific template for GET requests
        pass
