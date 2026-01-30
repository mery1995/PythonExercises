ROWS = 5
SEATS = 10


def main():
    seat_layout = [["O" for _ in range(SEATS)] for _ in range(ROWS)]

    while True:
        print_menu_options()
        choice = input("Wybierz opcję (1-5): ")

        if choice == '1':
            show_seating(seat_layout)

        elif choice == '2':
            book_seat(seat_layout)

        elif choice == '3':
            cancel_reservation(seat_layout)

        elif choice == '4':
            show_statistics(seat_layout)

        elif choice == '5':
            print("Koniec programu.")
            break

        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")


def print_menu_options():
    print("1. Pokaż salę")
    print("2. Zarezerwuj miejsce")
    print("3. Anuluj rezerwację")
    print("4. Statystyki")
    print("5. Zakończ")


def show_seating(seat_layout):
    print("        " + " ".join(str(i) for i in range(1, SEATS + 1)))
    for row in range(len(seat_layout)):
        print(
            f"Rząd {row + 1}: {' '.join(str(seat) for seat in seat_layout[row])}")


def book_seat(seat_layout):
    row, seat = input_row_seat()
    if row is None or seat is None:
        print("Anulowano rezerwację.")
        return
    if seat_layout[row][seat] == "O":
        seat_layout[row][seat] = "X"
        print("Miejsce zarezerwowane pomyślnie.")
    else:
        print("Miejsce jest już zajęte.")


def cancel_reservation(seat_layout):
    row, seat = input_row_seat()
    if row is None or seat is None:
        print("Anulowano operację.")
        return
    if seat_layout[row][seat] == "X":
        seat_layout[row][seat] = "O"
        print("Rezerwacja anulowana pomyślnie.")
    else:
        print("Miejsce nie jest zarezerwowane.")


def show_statistics(seat_layout):
    total_seats = len(seat_layout) * len(seat_layout[0])
    booked_seats = sum(seat == "X" for row in seat_layout for seat in row)
    available_seats = total_seats - booked_seats
    percentage_booked = (booked_seats / total_seats) * 100
    print(f"Liczba zarezerwowanych miejsc: {booked_seats}")
    print(f"Liczba dostępnych miejsc: {available_seats}")
    print(f"Procent zarezerwowanych miejsc: {percentage_booked:.2f}%")


def input_row_seat():
    while True:
        row_input = input(
            "Podaj numer rzędu (1-5) lub wpisz 'anuluj' aby wyjść: ")
        if row_input.lower() == 'anuluj':
            return None, None
        if not row_input.isdigit() or not (1 <= int(row_input) <= ROWS):
            print(f"Błędny numer rzędu. Podaj liczbę od 1 do {ROWS}.")
            continue
        row = int(row_input) - 1
        break
    while True:
        seat_input = input(
            "Podaj numer miejsca (1-10) lub wpisz 'anuluj' aby wyjść: ")
        if seat_input.lower() == 'anuluj':
            return None, None
        if not seat_input.isdigit() or not (1 <= int(seat_input) <= SEATS):
            print(f"Błędny numer miejsca. Podaj liczbę od 1 do {SEATS}.")
            continue
        seat = int(seat_input) - 1
        break
    return row, seat


if __name__ == "__main__":
    main()
