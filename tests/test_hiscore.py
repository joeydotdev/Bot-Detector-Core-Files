import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from api import app
from api.Config import token
from fastapi.testclient import TestClient

client = TestClient(app.app)

@pytest.mark.filterwarnings('ignore::DeprecationWarning')
def test_hiscore():
    response = client.get(f"/v1/hiscore/?player_id=1&token={token}")
    assert response.status_code == 200, f'invalid response {response.status_code }'
    assert isinstance(response.json(), list), f'invalid response return type: {type(response.json())}'


if __name__ == "__main__":
  test_hiscore()
