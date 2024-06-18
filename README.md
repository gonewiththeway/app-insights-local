
## Installation

### Prerequisites
- Docker
- Git

### Steps

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/insights-app.git
    cd insights-app
    ```

2. Build the Docker image:
    ```sh
    docker build -t insights-app .
    ```

3. Run the Docker container:
    ```sh
    docker run -it -p 8000:8000 insights-app
    ```

4. Access the API documentation:
    Open your browser and go to `http://localhost:8000/docs` to see the automatically generated Swagger UI.

## Endpoints

### Get Repositories
**GET** `/repositories`

#### Query Parameters
- `userid` (string): The ID of the user.

#### Response
A list of repositories for the given user.

### Get Insights
**GET** `/insights`

#### Query Parameters
- `userid` (string): The ID of the user.
- `repo` (string): The name of the repository.

#### Response
A dictionary containing insights about the specified repository.

## Example Usage

### Get Repositories
```sh
curl -X 'GET' \
  'http://localhost:8000/repositories?userid=user1' \
  -H 'accept: application/json'


https://app-insights-local.onrender.com/docs