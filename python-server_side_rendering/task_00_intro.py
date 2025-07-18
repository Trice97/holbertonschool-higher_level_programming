def generate_invitations(template, attendees):
    # Step 1: Check input types
    if not isinstance(template, str):
        print("Error: Template must be a string")
        return
    
    if not isinstance(attendees, list):
        print("Error: Attendees must be a list")
        return
    
    for attendee in attendees:
        if not isinstance(attendee, dict):
            print("Error: Each attendee must be a dictionary")
            return
    
    # Step 2: Check if empty
    if not template:
        print("Template is empty, no output files generated.")
        return
    
    if not attendees:
        print("No data provided, no output files generated.")
        return
    
    # Step 3 & 4: Process and create files
    for index, attendee in enumerate(attendees, start=1):
        invitation = template
        
        # Get values with default "N/A"
        name = attendee.get('name', 'N/A')
        event_title = attendee.get('event_title', 'N/A') 
        event_date = attendee.get('event_date', 'N/A')
        event_location = attendee.get('event_location', 'N/A')
        
        # Handle None values
        if name is None:
            name = 'N/A'
        if event_title is None:
            event_title = 'N/A'
        if event_date is None:
            event_date = 'N/A'
        if event_location is None:
            event_location = 'N/A'
        
        # Replace placeholders
        invitation = invitation.replace('{name}', str(name))
        invitation = invitation.replace('{event_title}', str(event_title))
        invitation = invitation.replace('{event_date}', str(event_date))
        invitation = invitation.replace('{event_location}', str(event_location))
        
        # Create file
        filename = f"output_{index}.txt"
        with open(filename, 'w') as file:
            file.write(invitation)