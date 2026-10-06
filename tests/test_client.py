import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))
from service_manager.manager import ServiceManager
from unittest.mock import patch

manager = ServiceManager()

def test_manager_add_client():
    
    with patch(
        "builtins.input",
        side_effect=[
            "Sava",
            "+380953701387",
            "sava@gmail.com"
        ]
        ):
        with patch(
            "service_manager.manager.bd_add_client",
            return_value=1
            ) as mock_add_client:
            client = manager.add_client()
            mock_add_client.assert_called_once_with(
                "Sava",
                "+380953701387",
                "sava@gmail.com"
            )

            assert client == 1


def test_manager_add_client_empty_name():

    with patch(
        "builtins.input",
        side_effect=[
            "",
            "+380953701387",
            "sava@gmail.com"
        ]
        ):
        with patch(
            "service_manager.manager.bd_add_client",
            return_value=1
            ):
            client = manager.add_client()
            assert client is None

    