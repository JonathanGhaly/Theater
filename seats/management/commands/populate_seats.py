# your_app/management/commands/populate_seats.py
from django.core.management.base import BaseCommand
from seats.models import Seat  # Update this with the actual model import

uppercase_chars = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
num1 = [9, 7, 5, 3, 1, 2, 3, 4, 5, 6, 8]
num2 = [7, 5, 3, 1, 2, 3, 4, 5, 6, 8]
num3 = [i for i in range(1, 35) if i % 2 == 0]


class Command(BaseCommand):
    help = 'Populate the database with seat data'

    def handle(self, *args, **options):
        # Add your code to populate the database with seat data
        middle_seats = []
        for i in range(8):
            if i % 2 == 0:
                for j in num1:
                    middle_seats.append(
                        {"row": uppercase_chars[i], 'col': '2', 'number': j, "status": "available"})
            else:
                for j in num2:
                    middle_seats.append(
                        {"row": uppercase_chars[i], 'col': '2', 'number': j, "status": "available"})
        for i in range(8, 17):
            for j in num1:
                middle_seats.append(
                    {"row": uppercase_chars[i], 'col': '2', 'number': j, "status": "available"})
        for i in range(18, 21):
            for j in num2[:-1]:
                middle_seats.append(
                    {"row": uppercase_chars[i], 'col': '2', 'number': j, "status": "available"})

        for seat_info in middle_seats:
            seat, created = Seat.objects.get_or_create(
                row=seat_info['row'],
                number=seat_info['number'],
                COL=seat_info['col'],
                defaults={'status': seat_info['status']}
            )
            # Left seats
            left_seats = []
            seats_num = [i for i in range(9, 22) if i % 2 != 0]
            seats_num.reverse()
            for i in range(2):
                if i == 1:
                    for j in seats_num:
                        left_seats.append(
                            {"row": uppercase_chars[i], 'col': '1', 'number': j, "status": "available"})
                else:
                    for j in seats_num[:-1]:
                        left_seats.append(
                            {"row": uppercase_chars[i], 'col': '1', 'number': j, "status": "available"})
            seats_num = [i for i in range(9, 25) if i % 2 != 0]
            seats_num.reverse()
            for i in range(2, 4):
                if i == 3:
                    for j in seats_num:
                        left_seats.append(
                            {"row": uppercase_chars[i], 'col': '1', 'number': j, "status": "available"})
                else:
                    for j in seats_num[:-1]:
                        left_seats.append(
                            {"row": uppercase_chars[i], 'col': '1', 'number': j, "status": "available"})

            seats_num = [i for i in range(9, 27) if i % 2 != 0]
            seats_num.reverse()
            for i in range(4, 6):
                if i == 5:
                    for j in seats_num:
                        left_seats.append(
                            {"row": uppercase_chars[i], 'col': '1', 'number': j, "status": "available"})
                else:
                    for j in seats_num[:-1]:
                        left_seats.append(
                            {"row": uppercase_chars[i], 'col': '1', 'number': j, "status": "available"})
            for j in seats_num:
                left_seats.append(
                    {"row": uppercase_chars[7], 'col': '1', 'number': j, "status": "available"})
            seats_num = [i for i in range(9, 28) if i % 2 != 0]
            seats_num.reverse()
            for j in seats_num:
                left_seats.append(
                    {"row": uppercase_chars[6], 'col': '1', 'number': j, "status": "available"})
            seats_num = [i for i in range(11, 32) if i % 2 != 0]
            seats_num.reverse()
            for i in range(8, 17):
                if i == 8:
                    for j in seats_num[:-2]:
                        left_seats.append(
                            {"row": uppercase_chars[i], 'col': '1', 'number': j, "status": "available"})
                elif 8 < i < 13:
                    for j in seats_num[:-1]:
                        left_seats.append(
                            {"row": uppercase_chars[i], 'col': '1', 'number': j, "status": "available"})
                else:
                    for j in seats_num:
                        left_seats.append(
                            {"row": uppercase_chars[i], 'col': '1', 'number': j, "status": "available"})
            seats_num = [i for i in range(0, 14) if i % 2 != 0]
            seats_num.reverse()
            for j in seats_num:
                left_seats.append(
                    {"row": uppercase_chars[17], 'col': '1', 'number': j, "status": "available"})
            seats_num = [i for i in range(9, 36) if i % 2 != 0]
            seats_num.reverse()
            for i in range(18, 21):
                for j in seats_num:
                    left_seats.append(
                        {"row": uppercase_chars[i], 'col': '1', 'number': j, "status": "available"})
            seats_num = [i for i in range(1, 32) if i % 2 != 0]
            seats_num.reverse()
            for i in range(21, 26):
                if i < 24:
                    for j in seats_num[:-1]:
                        left_seats.append(
                            {"row": uppercase_chars[i], 'col': '1', 'number': j, "status": "available"})
                else:
                    for j in seats_num:
                        left_seats.append(
                            {"row": uppercase_chars[i], 'col': '1', 'number': j, "status": "available"})
            for seat_info in left_seats:
                seat, created = Seat.objects.get_or_create(
                    row=seat_info['row'],
                    number=seat_info['number'],
                    COL=seat_info['col'],
                    defaults={'status': seat_info['status']}
                )
            # Right seats
            right_seats = []
            seats_num = [i for i in range(10, 31) if i % 2 == 0]
            for i in range(17):
                if i == 0:
                    for j in seats_num[:-5]:
                        right_seats.append(
                            {"row": uppercase_chars[i], 'col': '3', 'number': j, "status": "available"})
                elif i < 3:
                    for j in seats_num[:-4]:
                        right_seats.append(
                            {"row": uppercase_chars[i], 'col': '3', 'number': j, "status": "available"})
                elif i < 5:
                    for j in seats_num[:-3]:
                        right_seats.append(
                            {"row": uppercase_chars[i], 'col': '3', 'number': j, "status": "available"})
                elif i < 9:
                    for j in seats_num[:-2]:
                        right_seats.append(
                            {"row": uppercase_chars[i], 'col': '3', 'number': j, "status": "available"})
                elif i < 13:
                    for j in seats_num[:-1]:
                        right_seats.append(
                            {"row": uppercase_chars[i], 'col': '3', 'number': j, "status": "available"})
                else:
                    for j in seats_num:
                        right_seats.append(
                            {"row": uppercase_chars[i], 'col': '3', 'number': j, "status": "available"})
            seats_num = [i for i in range(2, 15) if i % 2 == 0]
            for j in seats_num:
                right_seats.append(
                    {"row": uppercase_chars[17], 'col': '3', 'number': j, "status": "available"})
            seats_num = [i for i in range(8, 35) if i % 2 == 0]
            for i in range(18, 21):
                for j in seats_num:
                    right_seats.append(
                        {"row": uppercase_chars[i], 'col': '3', 'number': j, "status": "available"})
            seats_num = [i for i in range(1, 33) if i % 2 == 0]
            for i in range(21, 26):
                if i < 24:
                    for j in seats_num[:-1]:
                        right_seats.append(
                            {"row": uppercase_chars[i], 'col': '3', 'number': j, "status": "available"})
                else:
                    for j in seats_num:
                        right_seats.append(
                            {"row": uppercase_chars[i], 'col': '3', 'number': j, "status": "available"})
            for seat_info in right_seats:
                seat, created = Seat.objects.get_or_create(
                    row=seat_info['row'],
                    number=seat_info['number'],
                    COL=seat_info['col'],
                    defaults={'status': seat_info['status']}
                )
        self.stdout.write(self.style.SUCCESS('Seat data population complete.'))
