def add_time(start, duration, day=None):
    # Convert start time to 24-hour format
    start_hour, start_minutes = map(int, start[:-2].split(':'))
    am_pm = start[-2:]

    # Convert duration to hours and minutes
    dur_hour, dur_minutes = map(int, duration.split(':'))

    # Convert start time to 24-hour format
    if am_pm == 'PM' and start_hour != 12:
        start_hour += 12
    elif am_pm == 'AM' and start_hour == 12:
        start_hour = 0

    # Calculate the new time
    total_hours = start_hour + dur_hour
    total_minutes = start_minutes + dur_minutes

    # Handle minutes overflow
    while total_minutes >= 60:
        total_minutes -= 60
        total_hours += 1

    # Handle hours overflow and calculate days later
    days_later = total_hours // 24
    total_hours = total_hours % 24

    # Convert back to 12-hour format
    if total_hours >= 12:
        if total_hours > 12:
            total_hours -= 12
        am_pm = 'PM'
    else:
        if total_hours == 0:
            total_hours = 12
        am_pm = 'AM'

    new_time = "{:02}:{:02} {}".format(total_hours, total_minutes, am_pm)

    # Handle days of the week
    if day:
        days_of_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        day = day.capitalize()  # Ensure the first letter is capitalized
        if day not in days_of_week:
            raise ValueError(f"Day '{day}' is not valid. Expected one of {days_of_week}.")
        day_index = days_of_week.index(day)
        final_day = days_of_week[(day_index + days_later) % 7]
        
        if days_later == 0:
            new_time += f", {final_day}"
        elif days_later == 1:
            new_time += f", {final_day} (next day)"
        else:
            new_time += f", {final_day} ({days_later} days later)"
    
    return new_time


def add_time11111111111(start, duration, day_of_week=None):
    # Define days of the week
    days_of_the_week_index = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3, 'Friday': 4, 'Saturday': 5, 'Sunday': 6}
    days_of_the_week_array = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    # Parse start time
    start_time, am_pm = start.split()
    start_hours, start_minutes = map(int, start_time.split(':'))
    
    # Convert 12-hour format to 24-hour format
    if am_pm == 'PM' and start_hours != 12:
        start_hours += 12
    elif am_pm == 'AM' and start_hours == 12:
        start_hours = 0
    
    # Parse duration
    duration_hours, duration_minutes = map(int, duration.split(':'))
    
    # Convert start time to minutes
    start_total_minutes = start_hours * 60 + start_minutes
    
    # Calculate end time in minutes
    duration_total_minutes = duration_hours * 60 + duration_minutes
    end_total_minutes = start_total_minutes + duration_total_minutes
    
    # Calculate days passed and adjust minutes
    days_passed = end_total_minutes // (24 * 60)
    end_total_minutes %= (24 * 60)
    
    # Convert back to hours and minutes
    end_hours = end_total_minutes // 60
    end_minutes = end_total_minutes % 60
    
    # Determine AM/PM for the end time
    if end_hours >= 12:
        end_am_pm = 'PM'
        if end_hours > 12:
            end_hours -= 12
    else:
        end_am_pm = 'AM'
        if end_hours == 0:
            end_hours = 12
    
    # Format minutes to always be two digits
    end_minutes = f'{end_minutes:02}'
    
    # Build return time
    return_time = f'{end_hours}:{end_minutes} {end_am_pm}'
    
    if day_of_week:
        day_of_week = day_of_week.capitalize()  # Normalize case
        if day_of_week in days_of_the_week_index:
            index = (days_of_the_week_index[day_of_week] + days_passed) % 7
            new_day = days_of_the_week_array[index]
            return_time += f', {new_day}'
            
            if days_passed == 1:
                return return_time + ' (next day)'
            elif days_passed > 1:
                return return_time + f' ({days_passed} days later)'
    
    return return_time


# Running tests
print(add_time('3:30 PM', '2:12'))  # Should return '5:42 PM'
print(add_time('11:55 AM', '3:12'))  # Should return '3:07 PM'
print(add_time('2:59 AM', '24:00'))  # Should return '2:59 AM (next day)'
print(add_time('11:59 PM', '24:05'))  # Should return '12:04 AM (2 days later)'
print(add_time('8:16 PM', '466:02'))  # Should return '6:18 AM (20 days later)'
print(add_time('3:30 PM', '2:12', 'Monday'))  # Should return '5:42 PM, Monday'
print(add_time('2:59 AM', '24:00', 'saturDay'))  # Should return '2:59 AM, Sunday (next day)'
print(add_time('8:16 PM', '866:02', 'tuesday'))  # Should return '6:18 AM, Monday (20 days later)'
