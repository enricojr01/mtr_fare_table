# ABOUT THIS PROJECT
I created this project as a portfolio piece and to demonstrate my ability to make a simple full-stack web application.

It's a simple fare calculator for the Hong Kong MTR. It takes, as source and destination input, any MTR station within Hong Kong and returns the price of a trip between those two stations, in HKD.

Data was taken from `data.gov.hk`, and was in turn provided by the MTR Corporation. It is up-to-date at time of writing (20 Jan 2025).

# STACK
- Python 3.11.9
- FastAPI 0.115.6

# DESIGN GOALS AND CONSIDERATIONS
I wanted the whole thing to fit inside a single Docker image, so that you'd only have one thing to deploy.

I didn't bother loading the fare table into a database because I didn't think it would be worth my time given the simple use case. To normalize, clean and prep the data for loading into a DB, would take me longer than it took me to code this whole thing up. Maybe even longer if I were to use a "proper" db like Postgres. It was way easier to just load the CSV into memory and use a list comprehension to get the data.

If the fare table ever changes I'll just download a new .csv and load that instead. It's not like they're adding/removing MTR Stations all the time.
