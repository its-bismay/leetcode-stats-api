# 📊 LeetCode Stats API

A fast, async REST API built with **FastAPI** that fetches and serves LeetCode user statistics — problems solved, contest ratings, and topic coverage — by querying LeetCode's internal GraphQL API.

---

## ✨ Features

- 🔢 **Problems Solved** — Total, Easy, Medium, Hard counts
- 🏆 **Global Rank** — Overall site ranking
- 🥊 **Contest Stats** — Rating, global ranking, top percentage, contests attended
- 🧠 **Topics Covered** — All solved tags sorted by count
- ⚡ **Parallel Fetching** — Both GraphQL queries fire simultaneously via `asyncio.gather`
- 📖 **Auto Swagger Docs** — Interactive API docs at `/docs`

---

## 🗂️ Project Structure

```
leetcode-stats-api/
├── app/
│   ├── __init__.py
│   ├── config.py                  # Settings via pydantic-settings
│   ├── api/
│   │   ├── __init__.py
│   │   └── v1/
│   │       ├── __init__.py
│   │       ├── router.py          # Aggregates all v1 routers
│   │       └── endpoints/
│   │           ├── __init__.py
│   │           └── leetcode.py    # Route handlers
│   ├── core/
│   │   ├── __init__.py
│   │   └── exceptions.py          # Custom HTTP exceptions
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── problems.py            # BasicResponse, ProblemCount
│   │   ├── contest.py             # ContestResponse
│   │   ├── topics.py              # TopicsResponse, TopicStat
│   │   └── combined.py            # AllStatsResponse
│   └── services/
│       ├── __init__.py
│       ├── leetcode_client.py     # Fires GraphQL queries to LeetCode
│       └── stats_parser.py        # Parses and shapes raw responses
├── tests/
│   └── conftest.py
├── server.py                      # FastAPI app entry point
├── .env                           # Environment variables
├── .env.example
└── pyproject.toml
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.11+
- [uv](https://github.com/astral-sh/uv) package manager

### Installation

**1. Clone the repository**
```bash
git clone https://github.com/your-username/leetcode-stats-api.git
cd leetcode-stats-api
```

**2. Install dependencies**
```bash
uv add fastapi
uv add "uvicorn[standard]"
uv add httpx
uv add pydantic-settings
```

**3. Set up environment variables**
```bash
cp .env.example .env
```

`.env` file:
```env
LEETCODE_GRAPHQL_URL=https://leetcode.com/graphql
DEBUG=True
```

**4. Run the server**
```bash
uv run uvicorn server:app --reload
```

The API will be live at `http://localhost:8000`

---

## 📡 API Endpoints

Base URL: `/api/v1/leetcode/{username}`

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/v1/leetcode/{username}/all` | All stats in one response |
| `GET` | `/api/v1/leetcode/{username}/basic` | Global rank + problems solved |
| `GET` | `/api/v1/leetcode/{username}/contest` | Contest rating and ranking |
| `GET` | `/api/v1/leetcode/{username}/topics` | Topics sorted by problems solved |

---

## 📦 Response Examples

### `GET /api/v1/leetcode/{username}/basic`

```json
{
  "username": "bibhabasu_11",
  "global_rank": 123456,
  "problems": {
    "total": 280,
    "easy": 100,
    "medium": 140,
    "hard": 40
  }
}
```

### `GET /api/v1/leetcode/{username}/contest`

```json
{
  "username": "bibhabasu_11",
  "available": true,
  "rating": 1654,
  "global_ranking": 45000,
  "total_participants": 700000,
  "top_percentage": 6.43,
  "contests_attended": 12
}
```

> If the user has never attended a contest, `available` will be `false` and all other fields will be `null`.

### `GET /api/v1/leetcode/{username}/topics`

```json
{
  "username": "bibhabasu_11",
  "topics": [
    { "name": "Array", "problems_solved": 85 },
    { "name": "Dynamic Programming", "problems_solved": 60 },
    { "name": "Hash Table", "problems_solved": 55 }
  ]
}
```

### `GET /api/v1/leetcode/{username}/all`

```json
{
  "username": "bibhabasu_11",
  "global_rank": 123456,
  "problems": {
    "total": 280,
    "easy": 100,
    "medium": 140,
    "hard": 40
  },
  "contest": {
    "username": "bibhabasu_11",
    "available": true,
    "rating": 1654,
    "global_ranking": 45000,
    "total_participants": 700000,
    "top_percentage": 6.43,
    "contests_attended": 12
  },
  "topics": [
    { "name": "Array", "problems_solved": 85 },
    { "name": "Dynamic Programming", "problems_solved": 60 }
  ]
}
```

---

## ⚠️ Error Responses

| Status Code | Reason |
|-------------|--------|
| `404 Not Found` | LeetCode username does not exist |
| `502 Bad Gateway` | Failed to reach LeetCode's GraphQL API |

**Example 404:**
```json
{
  "detail": "LeetCode user 'unknown_user' not found."
}
```

**Example 502:**
```json
{
  "detail": "Failed to reach LeetCode GraphQL API. Try again later."
}
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| [FastAPI](https://fastapi.tiangolo.com/) | Web framework |
| [Uvicorn](https://www.uvicorn.org/) | ASGI server |
| [httpx](https://www.python-httpx.org/) | Async HTTP client |
| [Pydantic v2](https://docs.pydantic.dev/) | Data validation and schemas |
| [pydantic-settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/) | Environment config |
| [uv](https://github.com/astral-sh/uv) | Package management |

---

## 📖 Interactive Docs

Once the server is running, visit:

- **Swagger UI** → `http://localhost:8000/docs`
- **ReDoc** → `http://localhost:8000/redoc`

---

## 🔧 Development

### Running in debug mode
```bash
uv run uvicorn server:app --reload --port 8000
```

### Running tests
```bash
uv run pytest
```

---

## 📄 License

MIT License — feel free to use and modify.

---

## 🙌 Acknowledgements

- [LeetCode](https://leetcode.com) for their GraphQL API
- [FastAPI](https://fastapi.tiangolo.com/) for making async APIs a joy to build