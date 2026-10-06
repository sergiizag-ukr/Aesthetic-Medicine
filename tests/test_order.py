import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from unittest.mock import patch
from service_manager.manager import ServiceManager

manager = ServiceManager()


def test_add_order():

    with patch(
        "service_manager.manager.get_all_clients",
        return_value=[
            {
                "id": 1,
                "name": "Sava",
                "phone": "+380953701387"
            }
        ]
    ):
        with patch(
            "service_manager.manager.get_all_services",
            return_value=[
                {
                    "id": 1,
                    "name": "Massage",
                    "duration": 60,
                    "price": 1200
                }
            ]
        ):
            with patch(
                "builtins.input",
                side_effect=["1", "1"]
            ):
                with patch(
                    "service_manager.manager.bd_add_order",
                    return_value=1
                ) as mock_add_order:
                    manager.add_order()
                    mock_add_order.assert_called_once_with(
                        1,
                        1
                    )

def test_add_order_no_clients():

    with patch(
        "service_manager.manager.get_all_clients",
        return_value=[]
    ):
        with patch(
            "service_manager.manager.bd_add_order"
        ) as mock_add_order:

            result = manager.add_order()

            mock_add_order.assert_not_called()

            assert result is None