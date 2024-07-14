from faker import Faker

def get_mock_user():
    # Initialize Faker
    fake = Faker()
    
    # Generate user details
    name = fake.name()
    email = fake.email()
    phone_number = fake.phone_number()
    address = fake.address().replace('\n', ', ')
    city = fake.city()
    state = fake.state()
    zip_code = fake.zipcode()
    
    # Create a dictionary to hold all user details
    mock_user = {
        "name": name,
        "email": email,
        "phone_number": phone_number,
        "address": address,
        "city": city,
        "state": state,
        "zip_code": zip_code
    }
    
    return mock_user

# mock_user = get_mock_user()
