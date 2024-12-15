#!/usr/bin/env python3
import os

def generate_invitations(template, attendees):

    try:
        if not isinstance(template, str):
            raise ValueError("Template must be a string.")
        if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
            raise ValueError("Attendees must be a list of dictionaries.")
        if not template:
            raise ValueError("Template is empty, no output files generated.")
        if not attendees:
            raise ValueError("No data provided, no output files generated.")
    
        for index, attendee in enumerate(attendees, start=1):
            name = attendee.get("name", "N/A")
            title = attendee.get("event_title", "N/A")
            date = attendee.get("event_date", "N/A") if attendee.get("event_date") is not None else "N/A"
            location = attendee.get("event_location", "N/A")

            result = template.format(name=name, event_title=title, event_date=date, event_location=location)
            if os.path.exists(f'output_{index}.txt') is False:
                with open(f'output_{index}.txt', 'w') as file:
                    file.write(result)
            else:
                raise Exception("Output file already exists.")
    except Exception as e:
        print(e)