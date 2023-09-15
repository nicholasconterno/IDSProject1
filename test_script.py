import unittest
import os
import subprocess

class TestScriptExecution(unittest.TestCase):
    
    def test_script_runs_without_errors(self):
        # This will raise an error if the script has an error
        result = subprocess.run(["python", "main.py"], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)

    def test_markdown_file_generation(self):
        # Assuming running the script generates the markdown file
        self.assertTrue(os.path.exists('generated_markdown.md'))

    def test_markdown_file_content(self):
        with open('generated_markdown.md', 'r') as file:
            content = file.read()
            self.assertTrue(len(content) > 0)

    def test_histogram_image_generation(self):
        # Assuming the script generates an image named histogram.png
        self.assertTrue(os.path.exists('histogram.png'))


if __name__ == '__main__':
    unittest.main()
