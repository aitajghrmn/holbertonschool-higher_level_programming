#!/usr/bin/python3
"""Simple templating program for generating invitations."""


def generate_invitations(template, attendees):
    """Generate personalized invitation files from a template."""

    if not isinstance(template, str):
        print("Invalid input: template must be a string.")
        return

    if not isinstance(attendees, list):
        print("Invalid input: attendees must be a list.")
        return

    if not all(isinstance(attendee, dict) for attendee in attendees):
        print("Invalid input: attendees must be a list of dictionaries.")
        return

    if template == "":
        print("Template is empty, no output files generated.")
        return

    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    placeholders = ["name", "event_title", "event_date", "event_location"]

    for index, attendee in enumerate(attendees, start=1):
        invitation = template

        for key in placeholders:
            value = attendee.get(key)

            if value is None:
                value = "N/A"

            invitation = invitation.replace("{" + key + "}", str(value))

        filename = f"output_{index}.txt"

        try:
            with open(filename, "w") as file:
                file.write(invitation)
        except Exception as e:
            print(f"Error writing file {filename}: {e}")
