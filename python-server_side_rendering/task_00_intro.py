def generate_invitations(template, attendees):
    # Step 1: Check input types
    if not isinstance(template, str):
        print("Error: Template must be a string")
        return
    
    if not isinstance(attendees, list):
        print("Error: Attendees must be a list")
        return
    
    # Check if attendees is a list of dictionaries
    for attendee in attendees:
        if not isinstance(attendee, dict):
            print("Error: Each attendee must be a dictionary")
            return
    
    print("Types validation passed!")
    
    # Step 2: Check if empty (to be filled next)
    print("Checking if empty...")

# Test with different types
if __name__ == "__main__":
    print("=== Test 1: Valid inputs ===")
    generate_invitations("Hello {name}", [{"name": "Alice"}])
    
    print("\n=== Test 2: Invalid template ===")
    generate_invitations(123, [{"name": "Alice"}])
    
    print("\n=== Test 3: Invalid attendees ===")
    generate_invitations("Hello {name}", "not a list")
