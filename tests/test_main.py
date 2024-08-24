import unittest
from unittest.mock import patch, MagicMock
from cowchat.main import get_chatgpt_response, display_with_cowpy


class TestCowChat(unittest.TestCase):

    @patch("cowchat.main.openai.ChatCompletion.create")
    def test_get_chatgpt_response(self, mock_openai_create):
        # Mock the API response
        mock_openai_create.return_value = iter(
            [
                {"choices": [{"delta": {"content": "Hello"}}]},
                {"choices": [{"delta": {"content": " world"}}]},
            ]
        )

        prompt = "Hello?"
        model = "gpt-3.5-turbo"
        max_tokens = 50
        temperature = 0.5

        result = "".join(get_chatgpt_response(prompt, model, max_tokens, temperature))

        self.assertEqual(result, "Hello world")
        mock_openai_create.assert_called_once_with(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ],
            max_tokens=max_tokens,
            temperature=temperature,
            stream=True,
        )

    @patch("builtins.print")
    def test_display_with_cowpy(self, mock_print):
        message = "Hello, world!"

        # Test with default cow
        display_with_cowpy(message)
        expected_output = """
 ______________
< Hello, world! >
 --------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\\
                ||----w |
                ||     ||
"""
        mock_print.assert_called_with(expected_output.strip())

        # Test with a custom cow
        display_with_cowpy(message, cowfile="tux")
        expected_tux_output = """
 _________
< Hello, world! >
 ---------
   \
    \
       .--.
      |o_o |
      |:_/ |
     //   \ \\
    (|     | )
   /'\_   _/`\\
   \___)=(___/
"""
        mock_print.assert_called_with(expected_tux_output.strip())

    @patch("cowchat.main.openai.ChatCompletion.create")
    @patch("builtins.print")
    def test_main(self, mock_print, mock_openai_create):
        # Mock the API response
        mock_openai_create.return_value = iter(
            [
                {"choices": [{"delta": {"content": "Hello"}}]},
                {"choices": [{"delta": {"content": " world"}}]},
            ]
        )

        with patch("cowchat.main.sys.argv", ["cowchat", "Hello?"]):
            with patch("cowchat.main.os.getenv", return_value="fake_api_key"):
                from cowchat.main import main

                main()
                expected_response = "Hello world"
                expected_output = """
 ______________
< Hello world >
 --------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\\
                ||----w |
                ||     ||
"""
                mock_print.assert_any_call(expected_response, end="", flush=True)
                mock_print.assert_any_call("\n\nCowpy Output:\n")
                mock_print.assert_any_call(expected_output.strip())
