import unittest
import yaml, os

from src import load_from_yaml

from unittest.mock import mock_open, patch

class TestImports(unittest.TestCase):

    filename_in_function = os.path.join(os.path.dirname(load_from_yaml.__file__), "commands_list.yaml")
 
    @patch("src.load_from_yaml.yaml.load", return_value={"key": "value"})
    @patch("builtins.open", new_callable=mock_open, read_data="key: value")
    def test_successful_yaml_load(self, mock_file, mock_yaml_load):
        result = load_from_yaml.import_data_from_yaml_file()
        self.assertEqual(result, {"key": "value"})
        # fix: path used in the function
        filename_in_function = os.path.join(os.path.dirname(load_from_yaml.__file__), "commands_list.yaml")
        mock_file.assert_called_once_with(filename_in_function, "r")
        mock_yaml_load.assert_called_once()

    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_file_not_found(self, mock_file):
        with patch("builtins.print") as mock_print:
            result = load_from_yaml.import_data_from_yaml_file()
            filename_in_function = os.path.join(os.path.dirname(load_from_yaml.__file__), "commands_list.yaml")
            mock_print.assert_called_once_with(
                f"Error: {filename_in_function} not found. Please ensure file exists."
            )
            self.assertIsNone(result)

    @patch("src.load_from_yaml.yaml.load", side_effect=yaml.YAMLError("parse error"))
    @patch("builtins.open", new_callable=mock_open, read_data=": invalid")
    def test_yaml_parse_error(self, mock_file, mock_yaml_load):
        with patch("builtins.print") as mock_print:
            result = load_from_yaml.import_data_from_yaml_file()
            mock_print.assert_called_once()
            self.assertIsNone(result) 



if __name__ == "__main__":
    unittest.main()
        