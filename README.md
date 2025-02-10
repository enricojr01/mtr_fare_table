# ABOUT THIS PROJECT
I created this project as a portfolio piece and to demonstrate my ability to make a simple full-stack web application.

It's a simple fare calculator for the Hong Kong MTR. It takes, as source and destination input, any MTR station within Hong Kong and returns the price of a trip between those two stations, in HKD.

Data was taken from `data.gov.hk`, and was in turn provided by the MTR Corporation. It is up-to-date at time of writing (20 Jan 2025).

# STACK
- Python 3.11.9
- FastAPI 0.115.6
- Jinja
- Podman

# DESIGN GOALS AND CONSIDERATIONS
I wanted the whole thing to fit inside a single Docker image, so that you'd only have one thing to deploy. Locally I'm using Podman for development, so I chose to use the more generic name "Containerfile" as opposed to "Dockerfile".

I didn't bother loading the fare table into a database because I didn't think it would be worth my time given the simple use case. To normalize, clean and prep the data for loading into a DB, would take me longer than it took me to code this whole thing up. If the fare table ever changes I'll just download a new .csv and load that instead. It's not like they're adding/removing MTR Stations all the time.

There's only around 9000~ rows in the CSV, and about half are "duplicates", i.e the same route but in reverse. As an example, there is a row for Central Station to Admiralty Station and another row for Admiralty Station to Central.

I went with an old-fashioned server-rendered template using Jinja2 and FastAPI's TemplateResponse because a full SPA with React/Svelte/Vue/Angular is way overkill for what I wanted to do here and would have increased development and build time without adding to the overall experience of the app.

# USAGE
1. Clone the repository.
1. Build the image using `podman build -t <whatever> .` (substitute with `docker build` if you're using Docker, it should work just fine)
1. Run the image with `podman run`, make sure to forward port 8000 from the container to a port on the host.
1. Visit in browser at the appropraite port.
