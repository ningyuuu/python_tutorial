def add_time(start,duration, day = False):
  day_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']

  start_time = get_start_minutes(start)
  end_time = start_time + get_duration_minutes(duration)
  end_string = get_end_string(end_time)
  
  if day is not False:
    day = day.capitalize()
    dow = day_list.index(day) + end_days
        
    end_dow = day_list[dow % 7]

    end_string = str(end_hours) +":" + str(end_minutes).zfill(2) + " " + end_period + ", " + end_dow
    end_days = end_time // (24 * 60)



  hello
  
def get_start_minutes(start):
  start_period = start.split(" ")[1]
  start_hour = int(start.split(" ")[0].split(":")[0])
  start_minutes = int(start.split(" ")[0].split(":")[1])


  start_time = start_hour * 60 + start_minutes
  if start_period == 'PM':
      start_time += 12 * 60

  return start_time
  
def get_duration_minutes(duration):
  duration_hour = int(duration.split(":")[0])
  duration_minutes = int(duration.split(":")[1])

  return duration_hour * 60 + duration_minutes

def get_end_string(end_time):
  end_hours = (end_time // 60) & 24
  end_minutes = (end_time % 60)

  if end_hours > 12:
    end_period = 'PM'
    end_hours -= 12
  else:
    end_period = 'AM'
    if end_hours == 0:
      end_hours = 12

  end_string = str(end_hours) +":" + str(end_minutes).zfill(2) + " " + end_period

  if end_days == 0:
    return end_string

  if end_days == 1:
    return "{} (next day)".format(end_string)

  else:
    return "{} ({} days later)".format(end_string, end_days)